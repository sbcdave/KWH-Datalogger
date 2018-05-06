#!/usr/bin/python2.7

# load datalogger environment variables from config
DPATH = "/KWH/datalogger"
execfile(DPATH + "/config/pyvars.py")

# setup string(str) in KP format
str = "#STA:" + STA + ";TM:"
with open(DPATH + '/datetime/datetime', 'r') as date:
    str = str + date.read() + ";C:86;V:0000"

# analog channels
if AD01 == "1":
    with open(DPATH + '/adc/AD01', 'a+') as AD01:
        data = AD01.read()
        if data <> "":
            str = str + ";AD01:" + data
if AD02 == "1":
    with open(DPATH + '/adc/AD02', 'a+') as AD02:
        data = AD02.read()
        if data <> "":
            str = str + ";AD02:" + data
if AD03 == "1":
    with open(DPATH + '/adc/AD03', 'a+') as AD03:
        data = AD03.read()
        if data <> "":
            str = str + ";AD03:" + data
if AD04 == "1":
    with open(DPATH + '/adc/AD04', 'a+') as AD04:
        data = AD04.read()
        if data <> "":
            str = str + ";AD04:" + data
if AD05 == "1":
    with open(DPATH + '/adc/AD05', 'a+') as AD05:
        data = AD05.read()
        if data <> "":
            str = str + ";AD05:" + data
if AD06 == "1":
    with open(DPATH + '/adc/AD06', 'a+') as AD06:
        data = AD06.read()
        if data <> "":
            str = str + ";AD06:" + data
if AD07 == "1":
    with open(DPATH + '/adc/AD07', 'a+') as AD07:
        data = AD07.read()
        if data <> "":
            str = str + ";AD07:" + data
if AD08 == "1":
    with open(DPATH + '/adc/AD08', 'a+') as AD08:
        data = AD08.read()
        if data <> "":
            str = str + ";AD08:" + data

# need to switch temp sensors to a new code like TP01
if AD11 == "1":
    with open(DPATH + '/temperature/' + TEMP1, 'a+') as AD11:
        data = AD11.read()
        if data <> "":
            str = str + ";AD11:" + data

if AD12 == "1":
    with open(DPATH + '/temperature/' + TEMP2, 'a+') as AD12:
        data = AD12.read()
        if data <> "":
            str = str + ";AD12:" + data


# digital channels
#Using PU01 temporarily to send signal until we adjust the server side tcpipapp code
if PU01 == "1":
    with open(DPATH + '/signal/signal', 'a+') as PU01:
        data = PU01.read()
        if data <> "":
            str = str + ";PU01:" + data 
#if PU01 == "1":
#    with open(DPATH + '/pulse/PU01', 'a+') as PU01:
#        data = PU02.read()
#        if data <> "":
#            str = str + ";PU01:" + data
if PU02 == "1":
    with open(DPATH + '/pulse/PU02', 'a+') as PU02:
        data = PU02.read()
        if data <> "":
            str = str + ";PU02:" + data 
if PU03 == "1":
    with open(DPATH + '/pulse/PU03', 'a+') as PU03:
        data = PU03.read()
        if data <> "":
            str = str + ";PU03:" + data 
if PU04 == "1":
    with open(DPATH + '/pulse/PU04', 'a+') as PU04:
        data = PU04.read()
        if data <> "":
            str = str + ";PU04:" + data 
if PU05 == "1":
    with open(DPATH + '/pulse/PU05', 'a+') as PU05:
        data = PU05.read()
        if data <> "":
            str = str + ";PU05:" + data 
if PU06 == "1":
    with open(DPATH + '/pulse/PU06', 'a+') as PU06:
        data = PU06.read()
        if data <> "":
            str = str + ";PU06:" + data 
if PU07 == "1":
    with open(DPATH + '/pulse/PU07', 'a+') as PU07:
        data = PU07.read()
        if data <> "":
            str = str + ";PU07:" + data 
if PU08 == "1":
    with open(DPATH + '/pulse/PU08', 'a+') as PU08:
        data = PU08.read()
        if data <> "":
            str = str + ";PU08:" + data 

# finish string
str = str + ";DI:333000;DO:0000;#" # need to learn what these are and see if 
# they should be configurable
with open(DPATH + '/transceive/tcp/tstring', 'w') as tstring:
    tstring.write(str)
