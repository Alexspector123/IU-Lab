import math

def solve(x, terms):
	result = 0
	for i in range(terms):
		temp = (x**i)/math.factorial(i)
		print(f'Terms {i}: {temp}')
		result += temp
	return result

print(f'The first 4 terms of the Taylor Series: ')
result = solve(1,4)
print('part 1')
print(f'Taylor approximate = {result}')
print(f'Taylor real = {math.exp(result)}')