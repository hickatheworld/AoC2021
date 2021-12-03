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
for i in range(len(depths)-1):
	current = depths[i]
	next = depths[i+1]
	if next > current:
		count+=1
print(count)

# Part 2
count = 0
for i in range(0, len(depths)-3):
	current = depths[i] + depths[i+1] + depths[i+2]	
	next = depths[i+1] + depths[i+2] + depths[i+3]
	if next > current:
		count+=1
print(count)