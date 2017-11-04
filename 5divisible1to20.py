def isPrime(n):
    for i in range(2,n):
        if n%i is 0:
            return 0

    return 1


def divsible(n):
    reqNum = 1
    for i in range(1,n+1):
        if isPrime(i):
            for j in range(1,n+1):
                if i*i > n:
                    reqNum *= i
                    break
                else:
                    i *= i
    return reqNum

print divsible(20)
