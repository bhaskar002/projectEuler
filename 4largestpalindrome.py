def ispalindrome(n):
    a = str(n)
    if a == "".join(reversed(a)):
        return 1
    return 0

def largestPalindrome():
    a = 999
    largest = 1
    for j in range(1000):
        for i in range(1000):
            if ispalindrome(a*i) is 1:
                if a*i > largest:
                    largest =  a*i

        a -= 1

    return largest


print largestPalindrome()
