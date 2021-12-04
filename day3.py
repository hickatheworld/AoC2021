# Loading data
f = open('ressources/diagnostic.txt')

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

# Part 1

# Finding gamma/epsilon binary values
numbers_length = len(numbers[0])
gamma_bits = ''
for i in range(numbers_length):
	bits0 = 0
	bits1 = 0
	for n in numbers:
		if n[i]=='0':
			bits0+=1
		else:
			bits1+=1
	if bits0 > bits1:
		gamma_bits+='0'
	else:
		gamma_bits+='1'
epsilon_bits = invertBin(gamma_bits)
# Converting gamma/epsilon rates to decimal
gamma_rate = bin2dec(gamma_bits)
epsilon_rate = bin2dec(epsilon_bits)

print(gamma_rate*epsilon_rate)

# Part 2
