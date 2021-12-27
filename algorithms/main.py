from Greedy import greedy

"""
Input cost matrix as 2-d list. For example, the cost matrix

1 2 3
4 5 6
7 8 9

is

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