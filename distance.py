import math
def distance(a, b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

x=distance((3,4), (0,0))
print(x)
 