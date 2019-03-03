#!/usr/bin/env python
import bitbang

# load datalogger environment variables from config
DPATH = "/KWH/datalogger"
execfile(DPATH + "/config/pyvars.py")

################################################################################
# 1. The RPi GPIO pins for the ADC are hard coded into bitbang.py
################################################################################
# 2. The ADC has 12 bits and upon request from the RPi it responds with numbers 
# from 0 to 4095. If the sensed voltage = the comparison voltage, the ADC will 
# respond with 4095. If the sensed voltage is half the comparison voltage, the 
# ADC will respond with 2048.
# i.e. ADC reported voltage = (x/4096) * comparison voltage, where x is the 
# number the ADC responds with.
################################################################################
# 3. Not every request the pi sends to the ADC gets an accurate response. With a 
# large enough set of respones, the majority are accurate. This logic takes a 
# set of samples and orders them from smallest to largest. Placing the set in 
# numerical order puts the low and high outliers at the beggining and end of the
# array. The logic then looks at the middle of the array and computes a mean 
# average.
# e.g. Logic asks for 7 samples and the chip responds with: 
#      1002, 45, 1007, 4003, 4095, 1008, 2
# These are ordered to: 2, 45, 1002, 1007, 1008, 4003, 4095
# Then logic takes a mean average of the center three: (1002 + 1007 + 1008) / 3
# 1005.666 is then divided by 4095 to see the ratio of the comparison voltage.
# The logic then uses the equation from (2.) to report the voltage...~1.25 V
################################################################################

samples = 31
cmpr_voltage = 5.25
skewing_percentage = 1.0
bias = 0.000

# instantiating needed arrays
value = []
channel = []
config = [AD01, AD02, AD03, AD04, AD05, AD06, AD07, AD08]

# collecting samples in 2-d array: value x channel
for j in range(8):
    if config[j] == '1':
	for i in range(samples):
		# using this because unable to append 1st element
		if i == 0:
			value = [bitbang.readadc(j)]
		else:
			value.append(bitbang.readadc(j))
	# using this because unable to append 1st element
	if j == 0:
		channel = [sorted(value)]
	else:
		channel.append(sorted(value))

# computing responses and storing in values[]
values = [0]*8
for i in range(8):
    if config[i] == '1':
	values[i] = (channel[i][len(channel[i])/2-2] + \
		    channel[i][len(channel[i])/2-1] + \
		    channel[i][len(channel[i])/2] + \
		    channel[i][len(channel[i])/2+1] + \
		    channel[i][len(channel[i])/2+2]) / 5
    else:
	values[i] = 0.0

# write channel values to files
with open(DPATH + '/adc/AD01', 'w') as a1:
	a1.write("%06f" % ((values[0]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD02', 'w') as a2:
	a2.write("%06f" % ((values[1]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD03', 'w') as a3:
	a3.write("%06f" % ((values[2]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD04', 'w') as a4:
	a4.write("%06f" % ((values[3]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD05', 'w') as a5:
	a5.write("%06f" % ((values[4]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD06', 'w') as a6:
	a6.write("%06f" % ((values[5]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD07', 'w') as a7:
	a7.write("%06f" % ((values[6]/4095.0)*cmpr_voltage*skewing_percentage-bias))

with open(DPATH + '/adc/AD08', 'w') as a8:
	a8.write("%06f" % ((values[7]/4095.0)*cmpr_voltage*skewing_percentage-bias))
