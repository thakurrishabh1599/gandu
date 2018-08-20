def sqrt(y):
    a=y/2.0
    while True:
        b=(a+y/a)/2
        if abs(b-a)<0.01:
            return b
        a=b
print(sqrt(9))