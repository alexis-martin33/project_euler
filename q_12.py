from math import sqrt, ceil
## i is the triangular number
i = 3
# y is the list 1,2,3,4...
y = 3
list_divisors = []
while len(list_divisors) < 500:
    list_divisors = []
    ## Find divisors
    for divisor in range(1,ceil(sqrt(i))+1):
        if int(i/divisor) == divisor:
            list_divisors.append(divisor)
        elif i%divisor == 0:
            list_divisors.extend([divisor, int(i/divisor)])

    print('i=' + str(i))
    i += y
    print('y=' + str(y))
    y += 1
    print(list_divisors)
    print(len(list_divisors))
