import math

#Führt das Dual-Ascent Verfahren aus
def dualAscent(costMatrix,sj,I):
    iterationCounter = 1
    v = []
    J = []
    for row in costMatrix:
        min = row[0]
        for j in row:
            if j < min:
                min = j
        v.append(min)
        J.append(calcJi(row,min))

    print('')
    print('Initialisierung')
    print('sj : ' + str(sj))
    print('v : ' + str(v))
    print('J : ' + str(J))
    print('I : ' + str(I))
    
    while I != []:
        iterationResult = dualAscentIteration(costMatrix,sj,v,J,I)
        sj = iterationResult[0]
        v = iterationResult[1]
        J = iterationResult[2]
        I = iterationResult[3]
        print('')
        print('Iteration ' + str(iterationCounter))
        print('sj : ' + str(sj))
        print('v : ' + str(v))
        print('J : ' + str(J))
        print('I : ' + str(I))
        iterationCounter += 1
    return (sj,v,J)

#Berechnet eine Iteration von Dual Ascent für gegebene Kostenmatrix, sj, vi und Indexmenge I
def dualAscentIteration(costMatrix,sj,v,J,I):
    ToBeRemoved = []
    for i in I:
        #Indexmenge beginnt mit 1, subtrahiere 1 um auf Arrays zuzugreifen.
        i = i - 1
        row = costMatrix[i]
        rowToBeSorted = []
        for x in row:
            rowToBeSorted.append(x)
        deltai = getMin(sj,J[i])
        delta = getMin([deltai,getNext(v[i],rowToBeSorted) - v[i]],[1,2])
        if deltai == 0 or delta == deltai:
           ToBeRemoved.append(i+1)
       
        v[i] += delta
        sj = updateSj(sj,J[i],delta)
        J[i] = calcJi(row,v[i])
    for i in ToBeRemoved:
        I.remove(i)
    return (sj,v,J,I)

#Berechnet kleinsten Wert unter Indexmenge eines Arrays
def getMin(array, indices):
    #Setze Startwert auf Array an der Stelle des ersten Index aus Indexmenge. (-1, weil Ji mit Indizes ab 1 beginnend gefüllt ist.)
    result = array[indices[0]-1]
    for index in indices:
        if array[index-1] < result:
            result = array[index-1]
    return result

#Gibt naechstgroesseres Element nach vi aus
def getNext(vi,array):
    array.sort()
    for k in array:
        if k > vi:
            return k
    return float('inf')

#Berechnet fuer Zeile und gegebenes vi die Menge Ji
def calcJi(array,vi):
    J = []
    for i in range (0,len(array)):
        if array[i] <= vi:
            J.append(i+1)
    return J

#Zieht fuer alle sj, fuer die j element J, delta ab
def updateSj(array,J,d):
    for j in J:
        array[j-1] = array[j-1] - d
    return array


#Klausur
Kostenmatrix = [[1,5,8,6],[4,2,3,7],[3,6,4,1],[5,8,2,9],[3,3,5,5],[2,5,1,8]]
sj = [14,6,15,16]
I = [1,2,3,4,5,6]

dualAscent(Kostenmatrix,sj,I)





"""
kostenmatrix = [[3,5,4],[2,7,10],[11,8,3],[5,9,2],[3,1,5]]
sj = [9,3,1]
v = [4,7,8,5,3]
J = [[1,3],[1,2],[2,3],[1,3],[1,2]]
I = [1,2,3,4,5]
"""
"""
kostenmatrix = [[4,9,5],[8,2,4],[4,10,6],[11,4,7],[4,8,2]]
sj = [12,8,7]
v = [4,2,4,4,2]
J = [[1],[2],[1],[2],[3]]
I = [1,2,3,4,5]
"""
"""
#Beispiel aus Übung
kostenmatrix = [[0,3,10,4,10,5],[8,0,1,10,7,6],[5,7,0,3,3,10],[2,2,5,0,2,9],[6,10,3,9,0,5],[4,1,2,1,9,0]]
sj = [8,4,5,5,3,8]
v = [0,0,0,0,0,0]
J = [[1],[2],[3],[4],[5],[6]]
I = [1,2,3,4,5,6]

dualAscent(kostenmatrix,sj,I)
"""




