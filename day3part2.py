import time
import re


#check gear ratio
def ratio(numlist, row, col):
	print("checking for gear ratio...")
	ratioNum = 0
	numOne = 0
	numTwo = 1
	#finds number one
	if numlist[int(row-1)][col-1].isdigit():
		numOne = getnum(numlist, row-1, col-1)
	elif numlist[int(row-1)][col].isdigit():
		numOne = getnum(numlist, row-1, col)	
	elif numlist[int(row-1)][col+1].isdigit():
		numOne = getnum(numlist, row-1, col+1)
	elif numlist[int(row)][col-1].isdigit():
		numOne = getnum(numlist, row, col-1)
	elif numlist[int(row)][col+1].isdigit():
		numOne = getnum(numlist, row, col+1)
	elif numlist[int(row+1)][col+1].isdigit():
		numOne = getnum(numlist, row+1, col+1)
	elif numlist[int(row+1)][col].isdigit():
		numOne = getnum(numlist, row+1, col)
	elif numlist[int(row+1)][col-1].isdigit():
		numOne = getnum(numlist, row+1, col-1)
	else:
		print("no number found?")
		return 0
	print("first number in ratio: " + str(numOne))

	#finds number two
	if numlist[int(row+1)][col-1].isdigit():
		numTwo = getnum(numlist, row+1, col-1)
	elif numlist[int(row+1)][col].isdigit():
		numTwo = getnum(numlist, row+1, col)
	elif numlist[int(row+1)][col+1].isdigit():
		numTwo = getnum(numlist, row+1, col+1)
	elif numlist[int(row)][col+1].isdigit():
		numTwo = getnum(numlist, row, col+1)
	elif numlist[int(row)][col-1].isdigit():
		numTwo = getnum(numlist, row, col-1)
	elif numlist[int(row-1)][col+1].isdigit():
		numTwo = getnum(numlist, row-1, col+1)
	elif numlist[int(row-1)][col].isdigit():
		numTwo = getnum(numlist, row-1, col)
	elif numlist[int(row-1)][col-1].isdigit():
		numTwo = getnum(numlist, row-1, col-1)
	else:
		print("no number found?")
		return 0
	print("second number in ratio: " + str(numTwo))

	if numOne == numTwo:
		print("ratio number: 0")
		return 0

	#find num two
	ratioNum = numOne * numTwo
	print("ratio number: " + str(ratioNum))
	return ratioNum

#builds number and adds it together
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

#function checks if number should be included and adds to total
def check(numlist):
	print("checking all nums")
	length = 141
	row = 0
	count = 0
	allNum = 0
	prevRatNum = 0

	for row in range(length):
		temp = 0
		i = 1
		while i < length:
			#print("checking vals")
			ratNum = 0
			if numlist[int(row)][i].isdigit():

				#check for symbols around number
				#check above
				if numlist[int(row-1)][i] != '.' and not numlist[int(row-1)][i].isdigit():
					if numlist[int(row-1)][i] == '*':
						ratNum = ratio(numlist, row-1, i)

						if ratNum == 0:
							#allNum += getnum(numlist, row, i)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
						else:
							if ratNum == prevRatNum:
								print("found past ratio")
								while numlist[int(row)][i].isdigit():
									i += 1
								continue
							allNum += ratNum
							prevRatNum = ratNum
							print(allNum)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
					#print("numvalid: " + str(numlist[int(row)][i]))
					#allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						#print("i before: " + str(i))
						i += 1
						#print("i after: " + str(i))
					continue
				#check above and left
				if numlist[int(row-1)][i-1] != '.' and not numlist[int(row-1)][i-1].isdigit():
					if numlist[int(row-1)][i-1] == '*':
						ratNum = ratio(numlist, row-1, i-1)
						if ratNum == 0:
							#allNum += getnum(numlist, row, i)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
						else:
							if ratNum == prevRatNum:
								print("found past ratio")
								while numlist[int(row)][i].isdigit():
									i += 1
								continue
							allNum += ratNum
							prevRatNum = ratNum
							print(allNum)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
					#print("numvalid: " + str(numlist[int(row)][i]))
					#allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue
				#check above and right
				if numlist[int(row-1)][i+1] != '.' and not numlist[int(row-1)][i+1].isdigit():
					if numlist[int(row-1)][i+1] == '*':
						ratNum = ratio(numlist, row-1, i+1)
						if ratNum == 0:
							#allNum += getnum(numlist, row, i)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
						else:
							if ratNum == prevRatNum:
								print("found past ratio")
								while numlist[int(row)][i].isdigit():
									i += 1
								continue
							allNum += ratNum
							prevRatNum = ratNum
							print(allNum)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
					#print("numvalid: " + str(numlist[int(row)][i]))
					#allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i+= 1
					continue

				#check down left
				if numlist[int(row+1)][i-1] != '.' and not numlist[int(row+1)][i-1].isdigit():
					if numlist[int(row+1)][i-1] == '*':
						ratNum = ratio(numlist, row, i-1)
						if ratNum == 0:
							#allNum += getnum(numlist, row, i)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
						else:
							if ratNum == prevRatNum:
								print("found past ratio")
								while numlist[int(row)][i].isdigit():
									i += 1
								continue
							allNum += ratNum
							prevRatNum = ratNum
							print(allNum)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
					#print("numvalid: " + str(numlist[int(row)][i]))
					#allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue


				#check right
				if numlist[int(row)][i+1] != '.' and not numlist[int(row)][i+1].isdigit():
					if numlist[int(row)][i+1] == '*':
						ratNum = ratio(numlist, row, i+1)
						if ratNum == 0:
							#allNum += getnum(numlist, row, i)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
						else:
							if ratNum == prevRatNum:
								print("found past ratio")
								while numlist[int(row)][i].isdigit():
									i += 1
								continue
							allNum += ratNum
							prevRatNum = ratNum
							print(allNum)
							while numlist[int(row)][i].isdigit():
								i += 1
							continue
					#print("numvalid: " + str(numlist[int(row)][i]))
					#allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue

				#print("number found: " + str(numlist[int(row)][i]))
			i+=1
			#print("i = " + str(i))

		count += 1
		row += 1
		#print("row: " + str(row))
	print(i)
	print(count)
	return allNum



#multidemensional array
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
print(graph)
total = check(graph)
print("total ratios is: " + str(total))
#print(graph)
print("program finished")