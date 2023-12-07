import time
import re

def real(arg, num):
	possible = False
	#print("real called")
	if arg:
		possible = True
	return num

#opens file input
file1 = open('input.txt', 'r')

#gets line one at a time
total = 0
count = 0

while True:
	line = file1.readline()
	if not line:
		break
	print("{}".format(line))
	total += real(line, count)
	count += 1

print("{}".format(count))

print("end of program")
#pauses for 10s to see ouput
time.sleep(10)