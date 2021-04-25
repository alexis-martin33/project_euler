## First, build a list of palindromes with 5 digits
listp = []

for a in range(10,100):
	for b in range(0,10):
		listp.append(int(str(a)+str(b)+str(a)[::-1]))

## second, append all palindromes with 6 digits
for a in range(100, 998):
	listp.append(int(str(a)+str(a)[::-1]))
listp.reverse()


## Perform the search
divisor = 100
stop = 0
answer = 0
mult_1 = 0
mult_2 = 0
for palindrome in listp:
	while divisor <= 999 and palindrome/divisor >= 100 and stop == 0:
		if palindrome % divisor == 0 and palindrome/divisor <= 999:
			mult_1 = palindrome/divisor
			mult_2 = divisor
			answer = palindrome
			stop = 1
		else:
			divisor += 1
	divisor = 100

print(listp)
print(answer)
print(mult_1)
print(mult_2)
print(stop)
print(divisor)


