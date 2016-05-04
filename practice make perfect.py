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