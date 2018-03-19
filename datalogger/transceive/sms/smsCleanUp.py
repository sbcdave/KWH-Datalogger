#!/usr/bin/env python
#from file import function
import subprocess
import string
import sys
# Load environment variables
execfile("/KWH/datalogger/conf/pyvars.py")
DEBUG = int(DEBUG)

#Clean up all the messags after having processed them
#Open the data file and run through the

delFile ="/KWH/datalogger/transceive/sms/smsDel.sh"


for messN in messNum:
        subprocess.Popen([delFile,str(messN)])

#Finally, update to reflect deletions
subprocess.Popen(smsReadFile)
        
