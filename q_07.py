## assume 2 is prime and all even numbers are not prime, fimd the 10000th prime
prime_list = []
num_list = []
u_limit = 0
l_limit = 3

while len(prime_list) < 10000:
	u_limit += 10000
	num_list += list(range(l_limit, u_limit,2))
	if prime_list == []:
		for i in num_list:
			for j in range(2, u_limit//i+1):
				if i*j in num_list:
					num_list.remove(i*j)
		prime_list = num_list
	else:
		for i in num_list:
			for j in range(2, u_limit//i+1):
				if i*j in num_list:
					num_list.remove(i*j)
		prime_list = num_list
	l_limit = u_limit+1
	print(len(prime_list))

print(len(prime_list))
print(prime_list[9800:10200])