# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:05:33 2020

@author: Max
"""

import matplotlib.pyplot as plt
from parsehrm import HRMParser

import numpy as np
import pandas as pd

path = 'example_data/19100301.hrm'
test = HRMParser(path)

#print(test.time)

#print(test.heartrate)

header = test.get_header(test.get_file_content(path))

print(header)

#print(test.heartrate)

#plt.plot(test.heartrate)

plt.plot(test.heartrate)
plt.gcf().autofmt_xdate()
plt.show()

np_arr = np.array([list(map(int,i)) for i in test.data])

test_df = pd.DataFrame(np_arr, columns=['HR','Stride','Cadence','Altitude'])

test_df['Time'] = test.time

HR_stat = test_df['HR'].describe()

mode_df = pd.DataFrame(data = (list(header[1]))).T
mode_df.columns = ['Speed','Cadence','Altitude','Power','Power Balance','Pedal Index','HR/CC','US/EU','Air Press']
Setting_df = pd.DataFrame({'HR_MAX': int(header[5])})

weight = int(header[7])
hr_min = int(header[6])
hr_max = int(header[5])
