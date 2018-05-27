#!/usr/bin/python2.7

# load datalogger environment variables from config
DPATH = "/KWH/datalogger"
execfile(DPATH + "/config/pyvars.py")

# setup string(str) in KP format
str = ADMPW+"#STA:" + STA 
#+ ";TM:"
#with open(DPATH + '/datetime/datetime', 'r') as input:
#    str = str + input.read() + ";C:86;V:0000"

# analog channels
if AD01 == "1":
    with open(DPATH + '/adc/AD01', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD01:" + data
if AD02 == "1":
    with open(DPATH + '/adc/AD02', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD02:" + data
if AD03 == "1":
    with open(DPATH + '/adc/AD03', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD03:" + data
if AD04 == "1":
    with open(DPATH + '/adc/AD04', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD04:" + data
if AD05 == "1":
    with open(DPATH + '/adc/AD05', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD05:" + data
if AD06 == "1":
    with open(DPATH + '/adc/AD06', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD06:" + data
if AD07 == "1":
    with open(DPATH + '/adc/AD07', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD07:" + data
if AD08 == "1":
    with open(DPATH + '/adc/AD08', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";AD08:" + data

# Temp sensors
if TM01 == "1":
    with open(DPATH + '/temperature/' + TEMP1, 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";TM01:" + data
if TM02 == "1":
    with open(DPATH + '/temperature/' + TEMP2, 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";TM02:" + data
if TM03 == "1":
    with open(DPATH + '/temperature/' + TEMP2, 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";TM03:" + data
#Add more temp sensor channels

# Digital channels
if PU01 == "1":
    with open(DPATH + '/pulse/PU01', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU01:" + data
if PU02 == "1":
    with open(DPATH + '/pulse/PU02', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU02:" + data 
if PU03 == "1":
    with open(DPATH + '/pulse/PU03', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU03:" + data 
if PU04 == "1":
    with open(DPATH + '/pulse/PU04', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU04:" + data 
if PU05 == "1":
    with open(DPATH + '/pulse/PU05', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU05:" + data 
if PU06 == "1":
    with open(DPATH + '/pulse/PU06', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU06:" + data 
if PU07 == "1":
    with open(DPATH + '/pulse/PU07', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU07:" + data 
if PU08 == "1":
    with open(DPATH + '/pulse/PU08', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";PU08:" + data 

# ModBus
if M1VOLTAGE == "1":
    with open(DPATH + '/modbus/values/m1Voltage', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1VOL:" + data 

if M1CURRENT == "1":
    with open(DPATH + '/modbus/values/m1Current', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1CUR:" + data 

if M1FREQUENCY == "1":
    with open(DPATH + '/modbus/values/m1Frequency', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1FRQ:" + data 

if M1ACTIVE_POWER == "1":
    with open(DPATH + '/modbus/values/m1ActivePower', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1ACP:" + data 

if M1APPARENT_POWER == "1":
    with open(DPATH + '/modbus/values/m1ApparentPower', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1APP:" + data 

if M1REACTIVE_POWER == "1":
    with open(DPATH + '/modbus/values/m1ReactivePower', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1RCP:" + data 

if M1POWER_FACTOR == "1":
    with open(DPATH + '/modbus/values/m1PowerFactor', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1PFC:" + data

if M1PHASE_ANGLE == "1":
    with open(DPATH + '/modbus/values/m1PhaseAngle', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1ANG:" + data

if M1EXPORT_ACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1ExportActiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1EAE:" + data

if M1EXPORT_REACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1ExportReactiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1ERE:" + data

if M1IMPORT_ACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1ImportActiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1IAE:" + data

if M1IMPORT_REACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1ImportReactiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1IRE:" + data

if M1TOTAL_ACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1TotalActiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1TAE:" + data

if M1TOTAL_REACTIVE_ENERGY == "1":
    with open(DPATH + '/modbus/values/m1TotalReactiveEnergy', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";M1TRE:" + data


# Signal
if SQ == "1":
    with open(DPATH + '/signal/signal', 'a+') as input:
        data = input.read()
        if data <> "":
            str = str + ";SQ:" + data 

# Finish string
str = str + ";#" 

# Write to tstring
with open(DPATH + '/transceive/tcp/tstring', 'w') as tstring:
    tstring.write(str)
