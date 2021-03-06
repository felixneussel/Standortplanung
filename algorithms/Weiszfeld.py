import math

#Eingabepunkte

a = [18,2]
b = [4,0]
c = [6,20]
d = [12,18]
e = [6,5]

standorte = [a, b,c,d]

wa = 10
wb = 1
wc = 1
wd = 1
we = 1

gewichte = [wa, wb,wc,wd]

deltakriterium = 0.001

def difference(vec_a, vec_b):
	return [vec_a[0] - vec_b[0], vec_a[1] - vec_b[1]]

def distance(vec_a, vec_b):
	summands = difference(vec_a, vec_b)
	return math.sqrt(summands[0]**2 + summands[1]**2)

def summand(point_a, point_b, weight):
	first = weight * difference(point_a,point_b)[0] / distance(point_a,point_b)
	second = weight * difference(point_a,point_b)[1] / distance(point_a,point_b)
	return [first, second]

def sum(index, vectors, weights):
	first = 0
	second = 0
	for x in range(0,len(vectors)):
		if(x == index):
			continue
		first += summand(vectors[index], vectors[x], weights[x])[0]
		second += summand(vectors[index], vectors[x], weights[x])[1]
	return [first, second]

def gamma(index, vectors, weights):
	first = sum(index, vectors, weights)
	return distance(first, [0,0])
	

def dominance(vectors, weights):
	output = False
	for index in range(0,len(vectors)):
		g = gamma(index,vectors,weights)
		dominant = g <= weights[index]
		outputindex = index + 1
		if(dominant):
			print(f"Location {outputindex}: Gamma = {g} <= {weights[index]} = w, dominance criterion fulfilled.")
			return vectors[index]
		else:
			print(f"Location {outputindex}: Gamma = {g} > {weights[index]} = w, dominance criterion not fulfilled.")
	return output


def initial(vectors, weights):
	upperfirst = 0.0
	uppersecond = 0.0
	lower = 0.0
	for x in range(0, len(vectors)):
		upperfirst += weights[x]*vectors[x][0]
		uppersecond += weights[x]*vectors[x][1]
		lower += weights[x]
	return[upperfirst / lower, uppersecond / lower]

def next(pre, vectors, weights):
	upperfirst = 0.0
	uppersecond = 0.0
	lower = 0.0
	for x in range(0, len(vectors)):
		upperfirst += weights[x]*vectors[x][0]/distance(pre, vectors[x])
		uppersecond += weights[x]*vectors[x][1]/distance(pre, vectors[x])
		lower += weights[x]/distance(pre, vectors[x])
	return[upperfirst / lower, uppersecond / lower]

def goal(point, vectors, weights):
	output = 0.0
	for x in range(0,len(vectors)):
		output += weights[x] * distance(point, vectors[x])
	outputHyperboloid = 0.0
	for x in range(0,len(vectors)):
		#Hier fuer das 0.001 den tatsaechlich gegebenen wert fuer epsilon eingeben.
		outputHyperboloid += weights[x]*math.sqrt((vectors[x][0]-point[0])**2 + (vectors[x][1]-point[1])**2 + 0.001)
	#Falls hyperboloid drankommt, return outputHyperboloid
	return outputHyperboloid

def delta(point, nextpoint, vectors, weights):
	pointGoal = goal(point,vectors, weights)
	nextPointGoal = goal(nextpoint, vectors, weights)
	return (pointGoal - nextPointGoal) / pointGoal

def stop(point, nextpoint, vectors, weights, d):
	if(delta(point, nextpoint, vectors, weights) <= d):
		return True
	else:
		return False

def weiszfeld(vectors, weights,d):
	dom = dominance(vectors,weights)
	if dom != False:
		return dom
	prePoint = initial(vectors, weights)
	nextPoint = next(prePoint,vectors,weights)
	counter = 0
	print('Iteration '+ str(counter))
	print('x1: ' + str(prePoint[0]))
	print('x2: ' + str(prePoint[1]))
	print('f(x): ' + str(goal(prePoint,vectors,weights)))
	print('delta: ---')
	print('')
	print('')
	while(not(stop(prePoint,nextPoint,vectors,weights,d))):

		counter += 1
		print('Iteration '+ str(counter))
		print('x1: ' + str(nextPoint[0]))
		print('x2: ' + str(nextPoint[1]))
		print('f(x): ' + str(goal(nextPoint,vectors,weights)))
		print('delta: ' + str(delta(prePoint, nextPoint, vectors, weights)))
		print('')
		print('')
		prePoint = nextPoint
		nextPoint = next(prePoint, vectors,weights)
	print('Iteration '+ str(counter +1))
	print('x1: ' + str(nextPoint[0]))
	print('x2: ' + str(nextPoint[1]))
	print('f(x): ' + str(goal(nextPoint,vectors,weights)))
	print('delta: ' + str(delta(prePoint, nextPoint, vectors, weights)))
	print('')
	print('')
		
	return nextPoint

print(weiszfeld(standorte,gewichte,deltakriterium))

