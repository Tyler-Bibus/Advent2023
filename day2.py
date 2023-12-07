import time
import re

def real(arg):
	possible = True
	checks = 0

	#print("real called")

	#stores colors in a list
	colors = []

	#finds all the numbers
	nums = re.findall(r'\d+', arg)
	numlist = list(map(int, nums))

	#finds order of colors
	#colors = re.findall(r'[rgb]', arg)
	colors = re.findall(r'red|green|blue', arg)
	print(colors)
	print("numbers in list ar: " + str(numlist))

	#finds if possible
	checks = len(colors)
	print("Length of color list: " + str(checks))
	i = 0
	print("checking...")
	for i in range(checks):
		if colors[i] == 'red' and numlist[i+1] > 12:
			possible = False
			print("not possible")
			return 0
		if colors[i] == 'green' and numlist[i+1] > 13:
			possible = False
			print("not possible")
			return 0
		if colors[i] == 'blue' and numlist[i+1] > 14:
			possible = False
			print("not possible")
			return 0

	return numlist[0]

#opens file input
file1 = open('inputFin.txt', 'r')

#gets line one at a time
total = 0
count = 0

while True:
	line = file1.readline()
	if not line:
		break
	print("{}".format(line))
	total += real(line)
	count += 1

print("{}".format(count))
print(total)
print("end of program")
#pauses for 10s to see ouput
time.sleep(2)