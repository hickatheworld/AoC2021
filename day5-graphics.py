import sys, pygame
from pygame import draw
pygame.init()

screen = pygame.display.set_mode((1000, 1000))

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

# Loading data
f = open('ressources/day5.txt')

lines =[]
line = f.readline()
while line:
	lines.append(VentLine(line))
	line = f.readline()
f.close()


drawObliques = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_o: drawObliques = not drawObliques
	
	pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 1000, 1000))
	for line in lines:
		if not drawObliques and line.isOblique(): continue
		pygame.draw.line(screen, (255, 0, 0) if line.isOblique() else (0, 0, 0), line.ends[0], line.ends[1])
	
	pygame.display.flip()