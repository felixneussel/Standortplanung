from __future__ import print_function
import math

def lTwoSquared (a,b):
	result = 0.0
	for i in range(0,len(a)):
		result += (a[i]-b[i])**2
	return result

def lTwo(a,b):
	return math.sqrt(lTwoSquared(a,b))

def printForTable(a):
	if(type(a) is str):
		result = a
	
	elif(type(a) is float):
		result = str(round(a,4))
	else:
		result = str(a)
	num = 12 - len(result)
	spaces = ''
	for i in range(0,num):
		spaces += ' '
	result += spaces
	return result


