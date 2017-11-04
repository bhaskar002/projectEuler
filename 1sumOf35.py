def sumOf(a,b):
    sum = 0;
    for i in range(a,b+1):
        #print i
        if ((i%3 is 0) or (i%5 is 0)):
            #print i
            #print "is divisible by 3 or 5"
            sum += i

    return sum


print(sumOf(0,999))
