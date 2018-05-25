#!/usr/bin/env python

import sys
import time
import pigpio

RX = 9
TX = 10
TXRX = 27

MSGLEN = 8
baud = 2048
bits = 8
#runtime=10
#ten_char_time = 100.0 / float(baud)
total_char = 0
#if ten_char_time < 0.1:
#	ten_char_time = 0.1

# Request for voltage
# 01  04  00  00  00  02  71  BC

MASK=(1<<bits)-1
msg = [0] * (MSGLEN)
#for i in range(len(msg)):
#	if i < 10:
#		msg[i] = 0 & MASK
#	else:
#		msg[i] = 170 & MASK
msg[0] = 1 & MASK
msg[1] = 4 & MASK
msg[2] = 0 & MASK
msg[3] = 0 & MASK
msg[4] = 0 & MASK
msg[5] = 2 & MASK
msg[6] = 114 & MASK
msg[7] = 188 & MASK

first = 0
pi = pigpio.pi()
pi.set_mode(TX, pigpio.OUTPUT)
pi.set_mode(TXRX, pigpio.OUTPUT)
pi.write(TXRX, 1)

pigpio.exceptions = False
pi.bb_serial_read_close(RX)
pigpio.exceptions = True

pi.wave_clear()

TEXT = msg[first:first+MSGLEN]

pi.wave_add_serial(TX, baud, TEXT)
wid = pi.wave_create()

pi.bb_serial_read_open(RX, baud, bits)

pi.wave_send_once(wid)
pi.wave_delete(wid)

TXTEXT=TEXT
first += 1
if first >= MSGLEN:
	first = 0

TEXT = msg[first:first+MSGLEN]
pi.wave_add_serial(TX, baud, TEXT, bb_bits=7)

while pi.wave_tx_busy():
	pass

#receive mode
time.sleep((1.0/2048)*80)
pi.write(TXRX, 0)

wid=pi.wave_create()

count = 1
text = ""
lt = 0
total_char += MSGLEN

while count:
	(count, data) = pi.bb_serial_read(RX)
	if count:
		text += data
		lt += count

print "TX: "+str(TXTEXT)
#for byte in text:
#	print bin(byte)
print ''.join('{:02b}'.format(x) for x in text)

pi.wave_delete(wid)
pi.bb_serial_read_close(RX)
pi.stop()
