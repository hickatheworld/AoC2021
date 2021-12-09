import sys

class VentLine:
	def __init__(self, raw):
		arrow = raw.index('->')
		end1 = raw[:arrow]
		end2 = raw[arrow+3:]
		comma1 = end1.index(',')
		A = (int(end1[:comma1]),int(end1[comma1+1:]))
		comma2 = end2.index(',')
		B = (int(end2[:comma2]),int(end2[comma2+1:]))
		self.ends = (A, B)
	
	def isOblique(self):
		return self.ends[0][0] != self.ends[1][0] and self.ends[0][1] != self.ends[1][1]

	def getAllPoints(self):
		points = []
		if self.isOblique():
			xi = -1 if self.ends[0][0] > self.ends[1][0] else 1
			yi = -1 if self.ends[0][1] > self.ends[1][1] else 1
			l = abs(self.ends[0][1] - self.ends[1][1])
			x = self.ends[0][0]
			y = self.ends[0][1]
			for i in range(l+1):
				points.append((x, y))
				x+=xi
				y+=yi
			return points
		j = 0 if self.ends[0][0] == self.ends[1][0] else 1
		k = 1 if j == 0 else 0
		s = min(self.ends[0][k], self.ends[1][k])
		l = abs(self.ends[0][k] - self.ends[1][k])
		for i in range(l+1):
			if j == 0:
				points.append((self.ends[0][j], s + i))
			else:
				points.append((s + i, self.ends[0][j]))
		return points

# Loading data
f = open('ressources/day5.txt')

lines =[]
line = f.readline()
while line:
	print(line)
	lines.append(VentLine(line))
	line = f.readline()
f.close()

print(lines[1].getAllPoints())

d = {}
c = 0
for l in lines:
	points = l.getAllPoints()
	for p in points:
		s = f'{p[0]},{p[1]}'
		if s in d:
			if d[s] == 1: c+=1
			d[s]+=1
		else:
			d[s] = 1
print(c)