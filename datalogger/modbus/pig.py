#!/usr/bin/env python

import sys
import time
import pigpio

RX = 9
TX = 10
TXRX = 27

MSGLEN = 256
baud = 2048
bits = 8
char_time = 10 / float(baud)

# Request for voltage
# 01  04  00  00  00  02  71  BC

MASK=(1<<bits)-1
msg = [0] * (MSGLEN)
for i in range(len(msg)):
	if i < 10:
		msg[i] = 0 & MASK
	else:
		msg[i] = 170 & MASK
#msg[0] = 1 & MASK
#msg[1] = 4 & MASK
#msg[2] = 0 & MASK
#msg[3] = 0 & MASK
#msg[4] = 0 & MASK
#msg[5] = 2 & MASK
#msg[6] = 114 & MASK
#msg[7] = 188 & MASK

# Prep library
pi = pigpio.pi()
pi.set_mode(TX, pigpio.OUTPUT)
pi.set_mode(RX, pigpio.INPUT)
pi.set_mode(TXRX, pigpio.OUTPUT)
pi.write(TXRX, 1)
pigpio.exceptions = False
pi.bb_serial_read_close(RX)
pigpio.exceptions = True
pi.wave_clear()

# Build wave to send
msg = sys.argv[1]
#total = pi.wave_add_serial(TX, baud, msg, bb_bits=8, offset=(3.5*char_time), bb_stop=2)
total = pi.wave_add_serial(TX, baud, msg, bb_bits=8, bb_stop=2)
print str(total)+" bits in message...Sending"
#pi.wave_add_serial(TX, baud, msg)
wid = pi.wave_create()

pi.wave_send_once(wid)

while pi.wave_tx_busy():
	pass

# Receive mode
#time.sleep(3.5*char_time)
pi.write(TXRX, 0)

count = 1
text = ""

pi.bb_serial_read_open(RX, baud)

nonsense = 0
while True:
	(count, data) = pi.bb_serial_read(RX)
	if count:
		text += data
	nonsense += 1
	if nonsense > 1000:
		break

print "TX: "+str(msg)
print ''.join('{:02b}'.format(x) for x in text)

pi.wave_delete(wid)
pi.bb_serial_read_close(RX)
pi.stop()
