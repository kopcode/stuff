import os
y ="Y"
start = int(raw_input("Do you want to start? (0=yes/1=no):")
if start==0
	where = raw_input("what directory:")
	os.chroot(where)
	out = os.listdir(where)
	print out
if start==1
I = raw_input ("press enter to end.")
