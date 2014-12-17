#!/usr/bin/python
import sys
import os

RTPDUMP_BIN = "/usr/bin/rtpdump" #change this if your path is different
PLAY_BIN = "/usr/bin/play" #change this if your path is different

if len(sys.argv) != 2:
	print "Please supply a valid Livewire channel number (1 - 32767). Correct usage: xplay 32767"
	sys.exit(1)
else:
	multicastAddr = int(sys.argv[1]) + 0xEFC00000 #Axia channel number + base IP (239.192.0.0 [in hex]) 
	os.system(RTPDUMP_BIN + " -F payload " + hex(multicastAddr) + "/5004 | " + PLAY_BIN + " -c 2 -r 48000 -b 24 -e signed-integer  -B -t raw -")
