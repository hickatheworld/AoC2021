f = open('ressources/depths.txt')
count = 0
line = f.readline()
last = int(line)
while line:
	line = f.readline()
	if len(line) > 0:
		depth = int(line)
		if depth > last:
			count+=1
		last = depth
f.close()
print(count)