from __future__ import print_function
import Basics as ba
import math

"""
Mit diesem Programm kann die Greedy Heuristik fuer das Warehouse Location Problem geloest werden.
Eine kleine Anleitung zur Benutzung findet ihr unten. Bei allen Sachen, bei denen 'def' vornedran steht, solltet ihr nichts aendern.
"""

def greedy(varCosts, fixCosts, potentialLocs):
	X = []
	J = shiftDown(potentialLocs)
	l = 1
	ui = [getUi(varCosts,J,l-1)]
	F = getCosts(ui[0])
	Flist = [F]
	deltaJ = [[]]
	omegaJ = [[]]
	while(J != []):
		print('Iteration l = ' + str(l))
		deltaJ.append(deltaJ[l-1])
		omegaJ.append(omegaJ[l-1])
		
		delta = getDelta(varCosts, ui[l-1], J)
		omega = getOmega(delta,J,fixCosts)
		
		deltaJ[l] = delta
		omegaJ[l] = omega
		#print(deltaJ[l])
		#print(omegaJ[l])
		potLoc = getPotentialLocation(omegaJ[l],J)
		print('Groesstes Kostenersparnis mit Standort ' + str(potLoc+1) + ': omega tilde l j =  omega(l = ' + str(l) + ', j = ' + str(potLoc+1) + ').  Kostenersparnis: ' + str(omegaJ[l][potLoc]))
		if(omegaJ[l][potLoc] < 0):
			print('Fuer l = ' + str(l) + ' gilt: Omega tilde l j < 0 fuer alle j in J' + str(l) + ' -> STOPP!')
			printTable(varCosts, ui, deltaJ, omegaJ,fixCosts,Flist)
			return X
		#print('Before:')
		#print(X)
	#	print(J)
		X.append(potLoc)
		J.remove(potLoc)
		F = F - omegaJ[l][potLoc]
		ui.append(getUi(varCosts,X,l))
		Flist.append(F)
		if(J == []):
			print('Da J' + str(l) + '= Leere Menge -> STOPP!')
			printTable(varCosts, ui, deltaJ, omegaJ,fixCosts,Flist)
			return X
		#print('After: ')
		print('X' + str(l) + ' = ' + printSet(X))
		print('J' +str(l) + ' = '+ printSet(J))
		
		
		print('F(X' + str(l) + ') = ' + str(F))
		J = removeSmallerThanZero(omegaJ[l],J)
		
		print('Entferne alle Standorte aus J, fuer die gilt: omega l j < 0: J = ' + printSet(J))
		if(J == []):
			print('Da J' + str(l) + ' = Leere Menge -> STOPP!')
			printTable(varCosts, ui, deltaJ, omegaJ,fixCosts,Flist)
			return X
		
		
		print('')
		l += 1
	
	#printTable(varCosts, ui, deltaJ, omegaJ)
	#return X


def printTable(varCosts,ui,delta,omega,fix,iterationCosts):
	print('')
	print('Tableau:')
	print('')
	print(' '*12*len(varCosts[0]) + '                   ' + 'ui')
	for i in range(0,len(varCosts)):
		print('             ', end='')
		for j in range(0,len(varCosts[i])):
			print(ba.printForTable(varCosts[i][j]), end='')
		print('|      ', end='')
		for x in range(0,len(ui)):
			print(ba.printForTable(ui[x][i]),end='')
		print('')
	print('_'*12*len(varCosts[0])+'_____________|' + '_'*12*len(iterationCosts))
	print('Fixkosten    ', end='')
	for i in fix:
		print(ba.printForTable(i), end='')
	print('|      ',end='')
	for i in iterationCosts:
		print(ba.printForTable(i),end='')
	print('')
	for i in range(1,len(delta)):
		print('_'*12*len(varCosts[0])+'_____________|')
		print('delta        ' , end='')
		for j in range(0,len(delta[i])):
			print(ba.printForTable(delta[i][j]), end='')
		print('|')
		print('omega        ', end='')
		for j in range(0,len(omega[i])):
			print(ba.printForTable(omega[i][j]), end='')
		print('|')

def getUi(varCosts,J,index):
	Ui = []
	if(index==0):
		for i in range(0,len(varCosts)):
			Ui.append(getMax(varCosts[i]))
	else:
		for i in range(0,len(varCosts)):
			Ui.append(getMin(varCosts[i],J))
	return Ui


def getMax(vector):
	result = vector[0]
	for costs in vector:
		if(costs > result):
			result = costs
	return result

def getMin(vector,J):
	
	result = 1000000
	for index in J:
		if(vector[index] < result):
			result = vector[index]
	
	return result

def getCosts(vector):
	result = 0
	for x in range(0,len(vector)):
		result += vector[x]
	return result

def getDelta(varCosts, ui, J):
	delta = []
	for j in range(0, len(varCosts[0])):
		if(J.count(j) > 0):
			deltaJ = 0
			for i in range(0,len(varCosts)):
				summand = ui[i] - varCosts[i][j]
				if(summand > 0):
					deltaJ += summand
		else:
			deltaJ = '-'
		delta.append(deltaJ)
	return delta

def getOmega(delta,J,fix):
	omega = []
	#print('getOmega')
	#print(delta)
	#print(J)
	#print(fix)
	for j in range(0, len(delta)):
		if(J.count(j) > 0):
			omegaJ = delta[j] - fix[j]
		else:
			omegaJ = '-'
		omega.append(omegaJ)
	return omega

def getPotentialLocation(vector,J):
	result = J[0]
	for j in J:
		if(vector[j] > vector[result]):
			result = j
	return result

def removeSmallerThanZero(omega, J):
	for j in range(0,len(omega)):
		if(J.count(j) > 0):
			if(omega[j] < 0):
				J.remove(j)
	return J

def printSet(set):
	if(len(set)==0):
		return 'Leere Menge'
	result = '{'
	for i in range(0,len(set)-1):
		result += str(set[i]+1) + ', '
	result += str(set[len(set)-1] + 1) + '}'
	return result

def shiftDown(vector):
	result = vector
	for i in range(0,len(result)):
		result[i] = result[i]-1
	return result

def InterchangeCost(a,b,matrix,vector):
	sum = 0
	for row in matrix:
		ca = row[a-1]
		cb = row[b-1]
		if(ca < cb):
			sum += ca
		else:
			sum += cb
	sum += vector[a-1]
	sum += vector[b-1]
	return sum






"""
Ab hier koennt ihr euch austoben :)

Zunaechst muesst ihr die Inputparameter eingeben:
Zur Veranschaulichung gibt es Beispiele unten.

Beachtet, dass das Programm mit Fehler lauft, wenn ihr gar keine Inputdaten eingebt.

"""


"""
Hier die Kostenmatrix eingeben. Zum Beispiel gebt ihr die Matrix

1 2 3
4 5 6
7 8 9

so ein:

[[1,2,3], [4,5,6], [7,8,8]]

"""
Kostenmatrix = [[1,5,8,6],[4,2,3,7],[3,6,4,1],[5,8,2,9],[3,3,5,5],[2,5,1,8]]

"""
Hier die Fixkosten eingeben.
Wenn Standort 1 die Fixkosten 5, Standort 2 die Fixkosten 7 und Standort 3 die Fixkosten 19 hat, sieht das so aus:
[5,7,19]
"""
Fixkosten = [14,6,15,16]

"""
Hier die potentiellen Standorte eingeben. Wenn Beispielweise 
an allen drei Standorten 1,2 und 3 eine Einrichtung eroeffnet werden kann, sieht das so aus:
[1,2,3]
"""
PotentielleStandorte = [1,2,3,4]

#Hier wird die Methode aufgerufen. Hier muesst ihr nichts aendern. Es reicht, oben die Inputdaten einzugeben.
greedy(Kostenmatrix,Fixkosten,PotentielleStandorte)









"""
Hier sind noch die Beispiele aus der Vorlesung und aus der Uebung.
Entfernt einfach die # vor den entsprechenden Zeilen, damit sie ausgefuehrt werden :)
"""
kostenVl = [[8,10,19,13],[7,14,24,21],[18,12,5,12],[16,14,7,13],[15,15,8,18]]
fixVl = [21,17,20,22]
jVl = [1,2,3,4]

#greedy(kostenVl,fixVl,jVl)

kostenuebung = [[0,15,35,50,30,20],[6,0,8,14,12,14],[42,24,0,18,36,48],[40,28,12,0,28,28],[24,24,24,28,0,8],[20,35,40,35,10,0]]
fixuebung = [35,35,35,35,35,35]
juebung = [1,2,3,4,5,6]

#greedy(kostenuebung,fixuebung,juebung)


#print(InterchangeCost(4,5,kostenuebung,fixuebung))

k = [[10,10],[10,5]]
f = [10,10]
j = [1,2]

#greedy(k,f,j)





