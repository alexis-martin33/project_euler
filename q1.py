## Project Euler problem 1
n = 0
m = 0
k = 0

for i in range(1,949):
	n += i
	if i < 200:
		m += i
	if i < 67:
		k += i

sol = 3*n + 5*m - 15*k
print("the solution is")
print(sol)
print("numbers are")
print(n)
print(m)
print(k)
