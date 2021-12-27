from __future__ import print_function
import math

demandList = [0,0,6,8,11,8,9,7,5,6,8,10,8,6,0,0]

matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def calcWin(a,b,demand):
	start = a-2
	end = a+3
	win = 0
	for x in range(start,end):
		a_dist = math.fabs(x-a)
		b_dist = math.fabs(x-b)
		if(a_dist < b_dist):
			win += demand[x]
		elif(a_dist == b_dist):
			win += (demand[x]/2.0)
		else:
			win += 0
	return win

def getMax(row):
	maximum = row[0]
	maxIndex = 0
	for x in range(1,len(row)):
		if(row[x]>maximum):
			maximum = row[x]
			maxIndex = x
	output = [maxIndex, maximum]
	return output

print(calcWin(4,3,demandList))

for leader in range (2,14):
	for follower in range (2,14):
		if(leader==follower):
			matrix[leader-2][follower-2] = 0
		else:
			matrix[leader-2][follower-2] = calcWin(follower, leader, demandList)

for x in range(0,12):
	result = getMax(matrix[x])
	table[x][1] = result[0]
	table[x][2] = result[1]

for x in range(0,12):
	result = calcWin(x+2,table[x][1]+2, demandList)
	table[x][0] = x
	table[x][3] = result
		

for x in range (0,12):
	for y in range(0,12):
		print(str(matrix[x][y]) + '   ', end ='')
	print('')

for x in range (0,12):
	for y in range(0,4):
		print(str(table[x][y]) + '   ', end ='')
	print('')

leaderWins = [0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(0,12):
	leaderWins[x]=table[x][3]

leaderPos = getMax(leaderWins)
followerPos = [table[leaderPos[0]][1],table[leaderPos[0]][2]]

print('Leader position: ' + str(leaderPos[0] + 1) + ', Leader revenue: ' + str(leaderPos[1]))
print('Follower position: ' + str(followerPos[0] + 1) + ', Follower revenue: ' + str(followerPos[1]))

print(calcWin(4,8,demandList))

"""
for leader in range (2,14):
	for follower in range (2,14):
		win = 0
		if((leader - follower) == -4):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1] + demand[follower-2]/2
		elif((leader - follower) == -3):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1]
		elif((leader - follower) == -2):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1]/2
		elif((leader - follower) == -1):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2]
		elif((leader - follower) == 0):
			win = 0
		elif((leader - follower) == 1):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2]
		elif((leader - follower) == 2):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]/2
		elif((leader - follower) == 3):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]
		elif((leader - follower) == 4):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1] + demand[follower+2]/2
		else:
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1] + demand[follower+2]
		matrix[leader-2][follower-2] = win
		print(str(win) + '   ', end='')
	print('')
"""

#for x in range(0,11):
	#for y in range(0,11):
		#print(str(matrix[x][y])+'   ', end='')
	#print('')


"""
def calcWin(leader, follower, demand):
	win = 0
		if((leader - follower) == -4):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1] + demand[follower-2]/2
		elif((leader - follower) == -3):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1]
		elif((leader - follower) == -2):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2] + demand[follower-1]/2
		elif((leader - follower) == -1):
			win = demand[follower] + demand[follower + 1] + demand[follower + 2]
		elif((leader - follower) == 0):
			win = 0
		elif((leader - follower) == 1):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2]
		elif((leader - follower) == 2):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]/2
		elif((leader - follower) == 3):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]
		elif((leader - follower) == 4):
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]/2 + demand[follower+2]/2
		else:
			win = demand[follower] + demand[follower - 1] + demand[follower - 2] + demand[follower+1]/2 + demand[follower+2]

"""
