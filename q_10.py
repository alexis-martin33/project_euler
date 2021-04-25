## modify the code from Q7 (find the 10001st prime) 
##   but we don't need to keep track of the list anymore
k = 1
prime = 3
answer = 2
num_list = list(range(3, 2000000,2))
for i in num_list[0:710]:
	for j in range(i, 2000000//i+1,2):
		if i*j in num_list:
			num_list.remove(i*j)
		print(j)
	print(i)


print(sum(num_list)+2)
print(num_list)