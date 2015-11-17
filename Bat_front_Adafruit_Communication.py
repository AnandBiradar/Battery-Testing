# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 12:26:31 2015

@author: Anand Biradar

https://learn.adafruit.com/adafruit-ft232h-breakout/i2c

"""

import binascii

import Adafruit_GPIO.FT232H as FT232H

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()

# Find the first FT232H device.
ft232h = FT232H.FT232H()

# Create an I2C device at address 0x70. >> Address from Bat_front chip 0x08
device = FT232H.I2CDevice(ft232h, 0x08 ) #  for magnetometer 0x1E

#response = device.readU8(0x08)


#print 'Scanning all I2C bus addresses...'
## Enumerate all I2C addresses.
#for address in range(127):
#	# Skip I2C addresses which are reserved.
#	if address <= 7 or address >= 120:
#		continue
#	# Create I2C object.
#	i2c = FT232H.I2CDevice(ft232h, address)
#	# Check if a device responds to this address.
#	if i2c.ping():
#		print 'Found I2C device at address 0x{0:02X}'.format(address)
#print 'Done!'


# Now manually create and send an I2C transaction to write 0x6A, 0xFF, 0x00 on the I2C bus:
device._idle()
device._transaction_start()
device._i2c_start()
device._i2c_write_bytes([0x08, 0xFF, 0x00]) #0x08
device._i2c_stop()
response = device._transaction_end()

# Print out the ACK response bytes.  These should be 0 if there was an ACK and 1 if there wasn't.
print 'ACK response bytes:', binascii.hexlify(response)