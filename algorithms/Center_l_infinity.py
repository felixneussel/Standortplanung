import math

def transformation(punkt):
    return (punkt[0]+punkt[1], -punkt[0]+punkt[1])

def backTransformation(punkt):
    return (0.5*(punkt[0]-punkt[1]), 0.5*(punkt[0]+punkt[1]))

def solve_l1(A,w):
    #punkte Transformieren
    A_transformed = []
    for point in A:
        print('Untransformierter Punkt: ' + str(point),end='')
        a_trans = transformation(point)
        print(', Transformiert: ' + str(a_trans))
        A_transformed.append(a_trans)
    result = solveOnPlane(A_transformed,w)
    print('')
    #print('Nicht ruecktransformiertes Ergebnis: ' + str(result))
    print('Nicht ruecktransformiertes Ergebnis: fuer x:' + str(result[2][0]) +' fuer y: ' +str(result[2][1]) +' Optimalpunkt: ' + str(result[0]) +' Kosten: ' + str(result[1]))

     #Ergebnis ruecktransformieren
    optimalPoint_trans = result[0]
    optimal_Point = backTransformation(optimalPoint_trans)
    allSolutions = (backTransformation([result[2][0][0],result[2][1][0]]),backTransformation([result[2][0][1],result[2][1][1]]))
    print('Ruecktransformiertes Ergebnis: x* = ' + str(optimal_Point) + ', z* = ' + str(result[1]))
    print('Alle optimale Punkte (ruecktransformiert: ' + str(allSolutions))
    return (optimal_Point,result[1],allSolutions)


def solveOnPlane(A,w):
    x_dir = []
    y_dir = []
    for a in A:
        x_dir.append(a[0])
        y_dir.append(a[1])
    x_solution = solveOnLine(x_dir,w)
    y_solution = solveOnLine(y_dir,w)
    optimalPosition = (x_solution[1],y_solution[1])
    x_goal = x_solution[0]
    y_goal = y_solution[0]
    if(x_goal > y_goal):
        cost = x_goal
    else:
        cost = y_goal

    #Alle Loesungen
    A_x_minus = []
    A_x_plus = []
    A_y_minus = []
    A_y_plus = []
    for i in range(0,len(A)):
        A_x_minus.append(A[i][0] - cost/w[i])
        A_x_plus.append(A[i][0] + cost/w[i])
        A_y_minus.append(A[i][1] - cost/w[i])
        A_y_plus.append(A[i][1] + cost/w[i])
    A_x_minus.sort()
    A_x_minus.reverse()
    A_x_plus.sort()
    A_y_minus.sort()
    A_y_minus.reverse()
    A_y_plus.sort()
    allSolutions = [(A_x_minus[0],A_x_plus[0]),(A_y_minus[0],A_y_plus[0])]
    
    return (optimalPosition, cost,allSolutions)

def solveOnLine(A,w):
    deltaij = []
    
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            d = getDelta(A[i],w[i],A[j],w[j])
            deltaij.append((i+1,j+1,math.fabs(d)))
    deltaij.sort(key=lambda x:x[2])
    deltaij.reverse()
    optimalVal = deltaij[0]
    z = optimalVal[2]
    p = optimalVal[0]-1
    q = optimalVal[1]-1
    x = getOptimalPosition(w[p],w[q],A[p],A[q])
    
    return (z,x,p+1,q+1,)

def getDelta(ai,wi,aj,wj):
    return (1.0*wi*wj/(wi+wj)*(aj-ai))

def getOptimalPosition(wp,wq,ap,aq):
    return (wp*ap + wq*aq)/(wp+wq)

def printLineSolution(solution):
    print('p = ' + str(solution[2]) + ', q = ' + str(solution[3]) + ', z* = ' + str(solution[0]) + ', x* = ' + str(solution[1]))

def printPlaneSolution(solution):
    print('x* = ' + str(solution[0]) + ', z* = ' + str(solution[1]))



#standorte = [(4,12),(8,2),(14,10),(2,3),(14,4)]
#gewichte = [4,2,2,8,9]


#print(solveOnPlane(standorte,gewichte))

standorte = [(3,5),(7,9),(10,3),(14,7)]


gewichte = [1,1,1,1,1]

print(solve_l1(standorte,gewichte))

print(solveOnPlane(standorte,gewichte))







#standorte = [(1,4),(2,6),(5,1),(4,2),(6,5)]
#gewichte = [2,3,1,1,2]
#solution = solveOnPlane(standorte,gewichte)

#print(solution)





