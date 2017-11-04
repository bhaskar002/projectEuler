def sumOf(x):
    a = 1
    b = 2
    sum = 2
    while b < x:
        c = b
        b += a;
        a = c
        if b%2 is 0:
            sum += b


    return sum

print sumOf(1000000*4)
