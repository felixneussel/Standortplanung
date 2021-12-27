import math

class Circle:
	
	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	def toString(self):
		return '(' + str(round(self.center[0],2)) + ', ' + str(round(self.center[1],2)) + '); ' + str(round(self.radius,2))

	def contains(self,point):
		
		if(round(distance(point, self.center),2) <= round(self.radius,2)):

			return True
		else:
			return False

class Mittelsenkrechte:

	def __init__(self, point_i, point_j):
		self.steigung = (1.0*point_i[0] - point_j[0]) / (point_j[1] - point_i[1])
		self.abschnitt = (1.0 * point_j[0]**2 + point_j[1]**2 - point_i[0]**2 - point_i[1]**2) / (2*(point_j[1] - point_i[1]))

	def toString(self):
		if (self.abschnitt >= 0):
			operator = ' + '
		else:
			operator = ' - '
		return str(round(self.steigung, 2)) + 'x' + operator + str(round(math.fabs(self.abschnitt), 2))


def difference(vec_a, vec_b):
	return [vec_a[0] - vec_b[0], vec_a[1] - vec_b[1]]

def distance(vec_a, vec_b):
	summands = difference(vec_a, vec_b)
	return math.sqrt(summands[0]**2 + summands[1]**2)

def twoCircle(vec_a, vec_b):
	middle_x = (1.0*vec_a[0] + vec_b[0])/2.0
	middle_y = (1.0*vec_a[1] + vec_b[1])/2.0
	radius = distance([middle_x, middle_y], vec_a)
	c1 = Circle([middle_x, middle_y], radius)
	return c1

def threeCircle(vec_a, vec_b, vec_c):
	ij = Mittelsenkrechte(vec_a, vec_b)
	ik = Mittelsenkrechte(vec_b, vec_c)
	middle_x = (1.0*ik.abschnitt - ij.abschnitt) / (ij.steigung - ik.steigung)
	middle_y = (1.0*ij.steigung*ik.abschnitt - ij.abschnitt*ik.steigung) / (ij.steigung - ik.steigung)
	radius = distance([middle_x, middle_y], vec_a)
	c1 = Circle([middle_x, middle_y], radius)
	return c1

def allTwos(points):
	for x in range(0, len(points)):
		for y in range(x+1,len(points)):
			print('Punkte: ' + str(points[x]) + ', ' + str(points[y]))
			circle = twoCircle(points[x], points[y])
			print('Kreis: ' + circle.toString())
			containsAll = True
			for z in points:
				if(not(circle.contains(z))):
					containsAll = False
					print('Enthaelt nicht ' + str(z))
					break
			print('Enthaelt alle: ' + str(containsAll))
			print('')
			print('')

def allThrees(points):
	for x in range(0, len(points)):
		for y in range(x+1,len(points)):
			for z in range(y+1,len(points)):
				print('Punkte: ' + str(points[x]) + ', ' + str(points[y]) + ', ' + str(points[z]))
				circle = threeCircle(points[x], points[y], points[z])
				print('Kreis: ' + circle.toString())
				containsAll = True
				for p in points:
					if(not(circle.contains(p))):
						containsAll = False
						print('Enthaelt nicht ' + str(p))
						break
				print('Enthaelt alle: ' + str(containsAll))
				print('')
				print('')




klausur = [(1,0),(2,3),(4,5)]
allTwos(klausur)
allThrees(klausur)