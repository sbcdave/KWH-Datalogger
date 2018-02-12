#!/usr/bin/python2.7

# load datalogger environment variables from conf
DPATH = "/KWH/datalogger"
execfile(DPATH + "/conf/pyvars.py")

# setup string(str) in KP format
str = "#STA:" + STA + ";TM:"
with open(DPATH + '/datetime/datetime', 'r') as date:
    str = str + date.read() + ";C:86;V:0000"

# analog channels
if AD01 == "1":
    with open(DPATH + '/adc/AD01', 'a+') as AD01:
	str = str + ";AD01:" + AD01.read()
if AD02 == "1":
    with open(DPATH + '/adc/AD02', 'a+') as AD02:
	str = str + ";AD02:" + AD02.read()
if AD03 == "1":
    with open(DPATH + '/adc/AD03', 'a+') as AD03:
	str = str + ";AD03:" + AD03.read()
if AD04 == "1":
    with open(DPATH + '/adc/AD04', 'a+') as AD04:
	str = str + ";AD04:" + AD04.read()
if AD05 == "1":
    with open(DPATH + '/adc/AD05', 'a+') as AD05:
	str = str + ";AD05:" + AD05.read()
if AD06 == "1":
    with open(DPATH + '/adc/AD06', 'a+') as AD06:
	str = str + ";AD06:" + AD06.read()
if AD07 == "1":
    with open(DPATH + '/adc/AD07', 'a+') as AD07:
	str = str + ";AD07:" + AD07.read()
if AD08 == "1":
    with open(DPATH + '/adc/AD08', 'a+') as AD08:
	str = str + ";AD08:" + AD08.read()
# need to add the rest of the temp sensors here and configure them
# in the conf

if AD11 == "1":
    with open(DPATH + '/temperature/' + TEMP1, 'a+') as AD11:
	str = str + ";AD11:" + AD11.read()

if AD12 == "1":
    with open(DPATH + '/temperature/' + TEMP2, 'a+') as AD12:
	str = str + ";AD12:" + AD12.read()


# digital channels
if PU01 == "1":
    with open(DPATH + '/pulse/PU01', 'a+') as PU01:
	str = str + ";PU01:" + PU01.read() 
if PU02 == "1":
    with open(DPATH + '/pulse/PU02', 'a+') as PU02:
	str = str + ";PU02:" + PU02.read() 
if PU03 == "1":
    with open(DPATH + '/pulse/PU03', 'a+') as PU03:
	str = str + ";PU03:" + PU03.read() 
if PU04 == "1":
    with open(DPATH + '/pulse/PU04', 'a+') as PU04:
	str = str + ";PU04:" + PU04.read() 
if PU05 == "1":
    with open(DPATH + '/pulse/PU05', 'a+') as PU05:
	str = str + ";PU05:" + PU05.read() 
if PU06 == "1":
    with open(DPATH + '/pulse/PU06', 'a+') as PU06:
	str = str + ";PU06:" + PU06.read() 
if PU07 == "1":
    with open(DPATH + '/pulse/PU07', 'a+') as PU07:
	str = str + ";PU07:" + PU07.read() 
if PU08 == "1":
    with open(DPATH + '/pulse/PU08', 'a+') as PU08:
	str = str + ";PU08:" + PU08.read() 

# finish string
str = str + ";DI:333000;DO:0000;#" # need to learn what these are and see if 
# they should be configurable
with open(DPATH + '/transceive/tcp/tstring', 'w') as tstring:
    tstring.write(str)
