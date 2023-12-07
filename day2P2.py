import time
import re

def real(arg):
	checks = 0
	#print("real called")

	#stores colors in a list
	colors = []
	lred = 0
	lblue = 0
	lgreen = 0
	ltotal = 0
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
		if colors[i] == 'red' and numlist[i+1] > lred:
			lred = numlist[i+1]
			print("red increased in size")
		if colors[i] == 'green' and numlist[i+1] > lgreen:
			lgreen = numlist[i+1]
			print("green increase")
		if colors[i] == 'blue' and numlist[i+1] > lblue:
			lblue = numlist[i+1]
			print("blue increase")

	ltotal = lblue * lgreen * lred
	print("ltotal is: " + str(ltotal))
	return ltotal

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