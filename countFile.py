#!/usr/bin/env python
import glob
import os
txtcount=0
ppUrlcount=0
IDPath="/home/johnny/Documents/linkedin/Alice/"
os.chdir(IDPath)

for file in glob.glob("*.txt"):
	txtcount = txtcount +1

for file2 in glob.glob("*_publicProfileUrl.txt"):
	ppUrlcount = ppUrlcount +1

print "Total txt file = ",txtcount
print "Total Non Public Profile URL file = ",(txtcount - ppUrlcount)
print "Total     Public Profile URL file = ",ppUrlcount
