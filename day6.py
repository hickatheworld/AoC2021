# Loading data
from os import system


f = open('ressources/day6.txt')

content = f.readline()
fishes = [int(i) for i in content.split(',')]

synced = {}

def fill_dict(d, fishes):
	for i in range(9):
		d[i] = 0
	for f in fishes:
		d[f]+=1

def pass_days(d, n):
	for _ in range(n):
		zeros = d[0]
		for i in range(8):
			d[i] = d[i+1]
		d[8] = zeros
		d[6] += zeros

fill_dict(synced, fishes)
pass_days(synced, 80)
print('After 80 days:', sum(synced.values()))

fill_dict(synced, fishes)
pass_days(synced, 256)
print('After 256 days:', sum(synced.values()))