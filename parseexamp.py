# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:07:11 2019

@author: Kyle Odom
"""

import pandas

data=pandas.read_csv("example.txt")
throughput=list(data['throughput'])
throughput.sort()
key=throughput[0]
interface = data.loc[data['throughput'] == key, 'interfaceID']
print(interface[1])
