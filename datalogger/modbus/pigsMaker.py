#!/usr/bin/env python
import sys
import math

baud = int(sys.argv[1])
string = sys.argv[2]

bitPeriod = 1000000.0/baud

first = True
timeArr = []
bitLast = ""
count = 1

for bit in string:
    if first:
        bitLast = bit
        first = False
    else:
        if bitLast == bit:
            count = count + 1
        else:
            timeArr.append(count*bitPeriod)
            count = 1
    bitLast = bit

timeArr.append(count*bitPeriod)

f = open("/KWH/datalogger/modbus/pigsmade", "w")
f.write("pigs w 22 1 \\\nw 10 1 mics "+str(int(round(45*bitPeriod)))+" \\\n")
high=False
remainder = 0

for time in timeArr:
    if remainder < 0:
        remainder += int(math.ceil(time)) - time
        time = str(int(math.ceil(time)))
        if high:
            f.write("w 10 1 mics "+time+" \\\n")
            high = not high
        else:
            f.write("w 10 0 mics "+time+" \\\n")
            high = not high
    elif remainder > 0:
        remainder += int(math.floor(time)) - time
        time = str(int(math.floor(time)))
        if high:
            f.write("w 10 1 mics "+time+" \\\n")
            high = not high
        else:
            f.write("w 10 0 mics "+time+" \\\n")
            high = not high
    else:
        remainder += int(round(time)) - time
        time = str(int(round(time)))
        if high:
            f.write("w 10 1 mics "+time+" \\\n")
            high = not high
        else:
            f.write("w 10 0 mics "+time+" \\\n")
            high = not high
    if abs(remainder) < 0.3:
        remainder = 0

f.write("w 10 1 mics "+str(int(round(45*bitPeriod)))+" \\\nw 22 0 \\\n")

remainder = 0
for i in range(1,191):
    if remainder < 0:
        remainder += int(math.ceil(bitPeriod)) - bitPeriod
        time = str(int(math.ceil(bitPeriod)))
        f.write("r 5 mics "+time+" \\\n")
    elif remainder > 0:
        remainder += int(math.floor(bitPeriod)) - bitPeriod
        time = str(int(math.floor(bitPeriod)))
        f.write("r 5 mics "+time+" \\\n")
    else:
        remainder += int(round(bitPeriod)) - bitPeriod
        time = str(int(round(bitPeriod)))
        f.write("r 5 mics "+time+" \\\n")
    if abs(remainder) < 0.3:
        remainder = 0

f.write("r 5 mics "+str(int(round(bitPeriod))))
f.close()
