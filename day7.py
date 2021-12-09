from math import inf

f = open('ressources/day7.txt')
content = f.readline()
crabs = [int(i) for i in content.split(',')]

# Part 1
cheapest = inf
for i in range(min(crabs), max(crabs)):
	cost = 0
	for j in crabs:
		cost += abs(j - i)
	if cost < cheapest:
		cheapest = cost

print(cheapest)

# Part 2

cheapest = inf
for i in range(min(crabs), max(crabs)):
	cost = 0
	for j in crabs:
		n = abs(j - i)
		cost += n*(n+1)//2
	if cost < cheapest:
		cheapest = cost

print(cheapest)