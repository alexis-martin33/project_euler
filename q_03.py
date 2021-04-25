number = 600851475143
factor_1 = 2
upper = number // 2 + 1
factor_2 = number
k = 0
while factor_1 <= upper:
	if number %factor_1 == 0:
		factor_2 = number / factor_1
		number = factor_2
		upper = number // factor_1 +1
		k +=1
	else:
		factor_1 += 1
		upper = number // factor_1 + 1 
		k+=1

print("this is factor_1")
print(factor_1)
print("this is factor_2")
print(factor_2)
print(number)
print(k)
