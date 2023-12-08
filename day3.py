import time
import re


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
	print("number added: " + str(intnum))
	return intnum

#function checks if number should be included and adds to total
def check(numlist):
	print("checking all nums")
	length = 141
	row = 0
	count = 0
	allNum = 0


	for row in range(length):
		temp = 0
		i = 1
		while i < length:
			#print("checking vals")
			if numlist[int(row)][i].isdigit():

				#check for symbols around number
				#check above
				if numlist[int(row-1)][i] != '.' and not numlist[int(row-1)][i].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						#print("i before: " + str(i))
						i += 1
						#print("i after: " + str(i))
					continue
				#check above and left
				if numlist[int(row-1)][i-1] != '.' and not numlist[int(row-1)][i-1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue
				#check above and right
				if numlist[int(row-1)][i+1] != '.' and not numlist[int(row-1)][i+1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i+= 1
					continue

				#check left
				if numlist[int(row)][i-1] != '.' and not numlist[int(row)][i-1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue

				#check right
				if numlist[int(row)][i+1] != '.' and not numlist[int(row)][i+1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue

				#check below
				if numlist[int(row+1)][i] != '.' and not numlist[int(row+1)][i].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue
				#check below and left
				if numlist[int(row+1)][i-1] != '.' and not numlist[int(row+1)][i-1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue
				#check below and right
				if numlist[int(row+1)][i+1] != '.' and not numlist[int(row+1)][i+1].isdigit():
					print("numvalid: " + str(numlist[int(row)][i]))
					allNum += getnum(numlist, row, i)
					while numlist[int(row)][i].isdigit():
						#print("moving up")
						i += 1
					continue


				#print("number found: " + str(numlist[int(row)][i]))
			i+=1
			#print("i = " + str(i))

		count += 1
		row += 1
		print("row: " + str(row))
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
print("total is: " + str(total))
#print(graph)
print("program finished")
time.sleep(5)