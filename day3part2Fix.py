import time
import re

def calcRatio(firstNum, secondNum):
	print(firstNum * secondNum)
	return firstNum * secondNum

def getnum(numlist, row, col):
	number = []
	intnum = 0
	#print("getting number...")
	#check left
	if numlist[int(row)][col-1].isdigit():
		number.insert(0, numlist[int(row)][col-1])
	if numlist[int(row)][col-2].isdigit() and numlist[int(row)][col-1].isdigit():
		number.insert(0, numlist[int(row)][col-2])
	#adds main number
	number.append(numlist[int(row)][col])
	#addnumbers to right
	if numlist[int(row)][col+1].isdigit():
		number.append(numlist[int(row)][col+1])
	if numlist[int(row)][col+2].isdigit() and numlist[int(row)][col+1].isdigit():
		number.append(numlist[int(row)][col+2])
	intnum = int("".join(number))
	#print("number found: " + str(intnum))
	return intnum

"""
This function checks if there is a number by the gear
TODO: Maybe fix to check if two numbers by gear?
"""
def checkForNum(numList, row, i):
	ratio = 0
	j = -1
	gettingNumber = 0
	numOne = 0
	numTwo = 0
	#finds the location of the number
	while j <= 1:
		#print(j)
		if numList[int(row)-1][i+j].isdigit():
			#This basically checks if this is the same as number one and assigns one and two before getting gear ratio
			#This logic is so screwed tbh
			#print("found number in gear above: " + str(j))
			if gettingNumber == 0 and numOne != getnum(numList, int(row) - 1, i + j):
				gettingNumber += 1
				numOne = getnum(numList, int(row) - 1, i + j)
				j = -1 #resets for loop
				print(numOne)
				continue
			elif gettingNumber == 1 and numOne != getnum(numList, int(row) - 1, i + j):
				numTwo = getnum(numList, int(row) - 1, i + j)
				print(numTwo)
				break
		if numList[int(row)+1][i+j].isdigit():
			#print("found number in gear below: " + str(j))
			if gettingNumber == 0 and (numOne != getnum(numList, int(row) + 1, i + j)):
				gettingNumber += 1
				numOne = getnum(numList, int(row) + 1, i + j)
				j = -1
				print(numOne)
				continue
			elif gettingNumber == 1 and numOne != getnum(numList, int(row) + 1, i + j):
				numTwo = getnum(numList, int(row) + 1, i + j)
				print(numTwo)
				break
		if numList[int(row)][i+1].isdigit():
			#print("found number in gear right: " + str(j))
			if gettingNumber == 0 and numOne != getnum(numList, int(row), i + 1):
				gettingNumber += 1
				numOne = getnum(numList, int(row), i + 1)
				j = -1
				print(numOne)
				continue
			elif gettingNumber == 1 and numOne != getnum(numList, int(row), i + 1):
				numTwo = getnum(numList, int(row), i + 1)
				print(numTwo)
				break
		if numList[int(row)][i-1].isdigit():
			#print("found number in gear left: " + str(j))
			if gettingNumber == 0 and numOne != getnum(numList, int(row), i - 1):
				isNumOne = True
				gettingNumber += 1
				numOne = getnum(numList, int(row), i - 1)
				j = -1
				print(numOne)
				continue
			elif gettingNumber == 1 and numOne != getnum(numList, int(row), i - 1):
				isNumTwo = True
				numTwo = getnum(numList, int(row), i - 1)
				print(numTwo)
				break
		j += 1

	if numOne != 0 and numTwo != 0:
		ratio = calcRatio(numOne, numTwo)

	return ratio

def checkForGear(numList, length):
	row = 0
	count = 0
	total = 0
	numAtPos = False

	for row in range(length):
		i = 1	
		while i < length:
			numAtPos = False
			if numList[int(row)][i] == '*':
				total = total + checkForNum(numList, row, i)

			#Finds numbers
			if numAtPos == True:
				total += 1

			i += 1
		row += 1
	
	return total

def main():
	#initializing multidemensional array
	length = 0;
	graph = []
	file1 = open('input.txt', 'r')
	i = 0
	while True:
		
		line = file1.readline()
		if not line:
			break
		letterlist = list(line)
		graph.append(letterlist)
	
		#graph.append([line])

		#print(graph)
		i += 1
	#print(graph)
	length = len(graph)
	length += -1 #fixes length
	#print(length)

	#gets total 
	total = checkForGear(graph, length)
	print("total ratios is: " + str(total))
	#print(graph)
main()
print("program finished")