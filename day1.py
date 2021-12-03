# Loading data
f = open('ressources/depths.txt')

depths = []
line = f.readline()
while line:
	depths.append(int(line))
	line = f.readline()
f.close()

# Part 1
count = 0
last = depths[0]
for i in range(1, len(depths)):
	if depths[i] > last:
		count+=1
	last = depths[i]
print(count)




