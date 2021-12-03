# Loading data
f = open('ressources/commands.txt')

commands = []
line = f.readline()
while line:
	commands.append(line)
	line = f.readline()
f.close()

# Part 1
horizontal = 0
depth = 0
for command in commands:
	# len('forward') == 7
	# len('up') == 2
	# len('down') == 4
	instruction = command.index(' ')
	X = int(command[instruction + 1])
	if instruction == 7:
		horizontal+=X
	elif instruction == 2:
		depth-=X
	else:
		depth+=X
print(horizontal*depth)

# Part 2
horizontal = 0
depth = 0
aim = 0
for command in commands:
	instruction = command.index(' ')
	X = int(command[instruction + 1])
	if instruction == 7:
		horizontal+=X
		depth+=aim*X
	elif instruction == 2:
		aim-=X
	else:
		aim+=X
print(horizontal*depth)