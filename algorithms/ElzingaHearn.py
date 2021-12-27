import Enumeration as enum

def ElzingaHearn(punkte, start_a, start_b):
    circle = enum.twoCircle(punkte[start_a],punkte[start_b])
    uncovered = getUncovered(circle,punkte))
    if (uncovered = empty):
        return circle
    else:
        circle = enum.threeCircle(punkte[start_a], punkte[start_b],uncovered[0])

def getUncovered(kreis,punkte):
    result = True
    uncovered = []
    for punkt in punkte:
        if(not kreis.contains(punkt)):
            result = False
            uncovered.append(punkt)
    return uncovered


punkte = [(1,1),(2,5),(3,3),(4,2)]
print(ElzingaHearn(punkte,0,1))