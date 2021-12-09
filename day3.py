# Loading data
f = open('ressources/day3.txt')

numbers = []
line = f.readline()
while line:
	numbers.append((line).strip())
	line = f.readline()
f.close()

def bin2dec(bin):
	N = len(bin)
	dec = 0
	for i in range(N):
		power = N-1-i
		if bin[i] == '1':
			dec+= 2**power
	return dec

def invertBin(bin):
	result = ''
	for c in bin:
		result+= '0' if c=='1' else '1'
	return result

def most_common_bit(numbers, position):
	bits0 = 0
	bits1 = 0
	for n in numbers:
		if n[position]=='0':
			bits0+=1
		else:
			bits1+=1
	if bits0 > bits1:
		return '0'
	elif bits1 > bits0:
		return '1'
	else:
		return 'b' #both
# Part 1

# Finding gamma/epsilon binary values
numbers_length = len(numbers[0])
gamma_bits = ''
for i in range(numbers_length):
	gamma_bits+=most_common_bit(numbers, i)
epsilon_bits = invertBin(gamma_bits)
# Converting gamma/epsilon rates to decimal
gamma_rate = bin2dec(gamma_bits)
epsilon_rate = bin2dec(epsilon_bits)

print(gamma_rate*epsilon_rate)

# Part 2

def find_rating(numbers, type):
	filtered = list(numbers)
	for i in range(len(numbers[0])):
		bit = most_common_bit(filtered, i)
		if bit == 'b':
			if type == 'o2':
				bit = '1'
			else:
				bit = '0'
		elif type == 'co2':
			bit = '0' if bit == '1' else '1'
		j = 0
		while j<len(filtered):
			if filtered[j][i] != bit:
				del filtered[j]
			else:
				j+=1
		if len(filtered) == 1:
			break
	return filtered[0]


o2_binary = find_rating(numbers, 'o2')
co2_binary = find_rating(numbers, 'co2')

o2_rating = bin2dec(o2_binary)
co2_rating = bin2dec(co2_binary)
print(o2_rating*co2_rating)