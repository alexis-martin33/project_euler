## Generate the triples with n and m formula
##   we know from handwork that c < 500
##   therefore m > n, m < sqrt(500)

n=1
stop ='no'
for m in range(2,24):
	print(m)
	while n < m and stop == 'no':
		print(n)
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		if a + b + c == 1000:
			answer = a*b*c
			stop='yes'
		n += 1
	m += 1
	n = 1

print(a)
print(b)
print(c)
if stop =='yes':
	print(answer)

