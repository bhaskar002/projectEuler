def isprime(x):
    for i in range(2,x):
        if x%i is 0:
            return 0


    return 1


def largestPrimeFactor(n):
    largest = 1;
    i = 2

    while (n != 1 or largest < n/2):
        if (n%i is 0) and (isprime(i) is 1):
            #print i
             n = n/i
             largest = i
        i += 1;

    return largest


a = 600851475143
print a

print largestPrimeFactor(a)
