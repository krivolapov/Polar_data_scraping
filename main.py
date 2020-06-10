# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:05:33 2020

@author: Max
"""

import matplotlib.pyplot as plt
from parsehrm import HRMParser

path = 'example_data/19100301.hrm'
test = HRMParser(path)

print(test.time)

#print(test.heartrate)

print(test.get_header(test.get_file_content(path)))

#print(test.heartrate)

plt.plot(test.heartrate)