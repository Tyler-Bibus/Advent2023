import time
import re


"""
This gets the subtotal for each list
"""
def getSubTotal(winInList):
	#print("wins: " + str(winInList))
	i = winInList
	count = 0
	if i >= 1:
		count = pow(2, i - 1)
	#print("points:" + str(count))
	return count

"""
gets the subtotal for all lists in array
"""
def getWin(numList, winningNums):
	subTotal = 0
	winInList = 0
	#print("getting Win")
	for num in numList:
		for win in winningNums:
			#print(num)
			#print(win)
			if int(num) == int(win):
				winInList += 1
	subTotal = getSubTotal(winInList)

	return subTotal

"""
This updates the total and searches each list for wins
"""
def calcWins(haveNums, winNums):
	total = 0
	i = 0
	#searches each array for winning numbers
	while i < len(haveNums):
		#print("card: " + str(i))
		total += getWin(haveNums[i], winNums[i])
		#print("new total: " + str(total))
		i += 1


	return total

"""
This reads input from an input file and sorts into two linked lists
@Param: haveNums
@Param: winNums
"""
def readInput(haveNums, winNums):
	file1 = open('input.txt', 'r')
	tempNums = []
	row = 0
	while True:
		getHave = False
		getWin = False
		line = file1.readline()
		if not line:
			break
		letterlist = line.split(' ')
		#print(line)
		for num in letterlist:
			#print(num)
			if ':' in num:
				#print("switching to getHave")
				getHave = True
				continue
			if '|' in num:
				tempList = list(tempNums)
				haveNums.append(tempNums)
				tempNums = []
				getHave = False
				getWin = True
				continue
			if '\n' in num:
				endValue = num.removesuffix('\n')
				#print(endValue)
				tempNums.append(endValue)
				tempList = list(tempNums)
				winNums.append(tempNums)
				tempNums = []
				getHave = False
				getWin = False
				row += 1
				continue
			if getHave == True and num.isdigit():
				tempNums.append(num)
			if getWin == True and num.isdigit():
				tempNums.append(num)
			



def main():
	total = 0
	#Numbers we have
	haveNums = []
	#Numbers that are winners
	winNums = []
	readInput(haveNums, winNums)
	print(haveNums[0])
	print(winNums[0])
	total = calcWins(haveNums, winNums)
	print(total)



main()
print ("program finished")