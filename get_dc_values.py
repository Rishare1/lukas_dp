#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ina219 import INA219, DeviceRangeError
from time import sleep
import sys,getopt


SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)

def read_ina219():
	try:
		print('Napeti: {0:0.2f}V'.format(ina.voltage()))
		print('Proud: {0:0.2f}mA'.format(ina.current()))
		print('Vykon: {0:0.2f}mW'.format(ina.power()))
		print('Ubytek napeti na bocniku: {0:0.2f}mV\n'.format(ina.shunt_voltage()))
	except DeviceRangeError as e:
	        # Current out of device range with specified shunt resister
		print(e)

def main(argv):
	cyklu = -1
	try:
		opts, args = getopt.getopt(argv,"hc:",["cyklu="])
	except getopt.GetoptError:
		print('get_dc_values.py -c <pocet cyklu>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('get_dc_values.py -c <pocet cyklu>')
			sys.exit(0)
		elif opt in ("-c", "--cyklu"):
			cyklu = int(arg)
			#print("Provadim", cyklu,"cyklu.")

	while cyklu != 0:
		read_ina219()
		cyklu = cyklu -1
		if cyklu != 0:
			sleep(1)

if __name__ == '__main__':
	try:
		main(sys.argv[1:])
	except KeyboardInterrupt:
		sys.exit(0)
