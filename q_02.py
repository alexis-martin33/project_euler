prev = 2
veryprev = 1
i = 0
n = 0
soln = 2

while i < 4000000:
	i = prev + veryprev
	veryprev = prev
	prev = i
	n = n+1
	if n == 3:
		soln = soln + i
		n = 0
print(soln)


