from struct import *
import os, time, datetime, string, sys, math, re, shutil, glob, getopt

def read_lc1(lc1_filename):
	filehandler = open(lc1_filename, 'rb')
	sseId = os.path.split(lc1_filename)[1]
	sseId = os.path.splitext(sseId)[0]
	if (sseId[0:2]).lower == 'sh' or (sseId[0:2]).lower == 'sz':
		sseId = sseId[2:]
	data = []
	while 1:
		rawdata = filehandler.read(4 * 8)
		if len(rawdata) <= 0:
			break
		t = unpack('IfffffII', rawdata)
		mins = (t[0] >> 16) & 0xffff
		mds  = t[0] & 0xffff
		#print (mds)
		year = int(mds / 2048) + 2004
		month = int((mds % 2048) / 100)
		day   = int((mds % 2048) % 100)
		hour = int(mins / 60)
		minute = int(mins % 60)
		data.append((sseId,(month,day,hour,minute),t[1],t[2],t[3],t[4],t[5],t[6],t[7]))
		datet = "%d-%d-%d,%02d:%02d" % (year,month,day,hour,minute)
		#print ("%s,%f,%f,%f,%f,%f,%d,%d" % (datet,t[1],t[2],t[3],t[4],t[5],t[6],t[7]))
	filehandler.close()
	return data

def main():
	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv, "ht:", ["help", "type="])
	except getopt.GetoptError:
		sys.exit(0)
	read_lc1(args[0])

if __name__ == "__main__": main()