##how to know if a num is an integer with x.0
def is_int(x):
    if x - round(x) > 0:
            return False
    else:
            if x < 0 and x - round(x) < 0:
                return False
            else:
                return True
    ##sum of digits in digit_sum(n)
    
def digit_sum(n):
        b = []
        n = str(n)
        for a in n:
                a = int(a)
                b.append(a)
        return sum(b)
        print sum(b)
        
##factorial
def factorial(x):
    if x == 1 or x == 0:
        print 1
        return 1
    else:
        return x*factorial(x - 1)

##is_prime
def is_prime(x):
    if x<2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
    return True
print is_prime(3)

