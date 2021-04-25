## Iterate the sequence until you find a number with a known sequence
## Eg. if sequence of 10 is done, sequence of 20 is 20 -> sequence(10)

num = 1000000
collatz_dict = {1:1}

for number in range(2,num+1):
    start = number
    chain_len = 0
    while start not in collatz_dict:
        if start % 2 == 0:
            start = start/2
            chain_len += 1
        else:
            start = 3*start + 1
            chain_len += 1
    collatz_dict[number] = chain_len + collatz_dict[start]

max_num = max(collatz_dict, key=lambda key:collatz_dict[key])
max_len = max(collatz_dict.values())

print(max_num)
print(max_len)