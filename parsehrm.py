from abc import ABCMeta
from datetime import datetime, timedelta


class HRMParser(object):

    def __init__(self, hrm_file):
        content = self.get_file_content(hrm_file)
        if not content is None:
            header = self.get_header(content)
            data = self.get_data(content)

            self.time = Time(data, header[2:5])
            self.heartrate = HeartRate(data, header[4])

    def get_file_content(self, hrm_file):
        if not hrm_file is None:
            if hrm_file.lower().endswith(('.hrm', '.txt')):
                with open(hrm_file, 'r') as f:
                    f = list(map(str.strip, list(f)))
                return f

    def get_header(self, content):
        if not content is None:
            devices = {'36': 'Polar RS400', '38': 'Polar RS800cx'}
            parse_data = False
            data = []
            for line in content:
                if line.lower().startswith('monitor'):
                    try:
                        device = devices[line.split('=')[1]]
                    except KeyError:
                        device = 'Other'
                elif line.lower().startswith('smode'):
                    mode = line.split('=')[1]
                elif line.lower().startswith('date'):
                    date = line.split('=')[1]
                elif line.lower().startswith('starttime'):
                    start_time = line.split('=')[1]
                elif line.lower().startswith('interval'):
                    interval = line.split('=')[1]
            return device, mode, date, start_time, interval

    def get_data(self, content):
        if not content is None:
            parse = False
            data = []
            for line in content:
                if line.lower() == '[hrdata]':
                    parse = True
                    next
                elif parse:
                    data.append(line.split(' '))
            return data


class Measure(metaclass=ABCMeta):

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


class Time(Measure):

    def __init__(self, data, header):
        self.data, abs_time = self.get_data(data, header)
        self.absolute = AbsTime(abs_time)

    def get_data(self, data, header):
        start = datetime.strptime(header[0] + ' ' + header[1],
                                  '%Y%m%d %H:%M:%S.%f')
        interval = header[2]
        raw = []
        if interval == '238':
            for i, val in enumerate(data):
                if i == 0:
                    raw.append(start + timedelta(seconds=float(val[0])/1000))
                else:
                    raw.append(raw[-1] + timedelta(seconds=float(val[0])/1000))
        else:
            for i, val in enumerate(data):
                raw.append(start + timedelta(seconds=i * 5))

        elapsed = [x - raw[0] for x in raw]
        return elapsed, raw

    def __repr__(self):
        return repr([repr(x) for x in self.data])

    def __str__(self):
        return str([str(x) for x in self.data])

    @property
    def duration(self):
        if self.data:
            return self.data[-1]

    @property
    def start(self):
        if self.data:
            return self.absolute[0]

    @property
    def finish(self):
        if self.data:
            return self.absolute[-1]


class AbsTime(Measure):
    def __init__(self, abs_time):
        self.data = abs_time

    def __repr__(self):
        return repr([repr(x) for x in self.data])

    def __str__(self):
        return str([str(x) for x in self.data])


class HeartRate(Measure):

    def __init__(self, data, interval):
        self.data, self.rrinterval = self.get_data(data, interval)

    def get_data(self, data, interval):
        temp = []
        for val in data:
            temp.append(float(val[0]))
        if interval == '238':
            heartrate = [60000 / x for x in temp]
            return heartrate, temp
        else:
            return temp, None


# --------------- TEST ---------------
# =============================================================================
# path = 'example_data/19100301.hrm'
# test = HRMParser(path)
# 
# print(test.heartrate)
# =============================================================================
