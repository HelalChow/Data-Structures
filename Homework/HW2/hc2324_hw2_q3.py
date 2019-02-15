def factors(num):
    sqrt_num = int(num**.5)
    for i in range(1,sqrt_num+1):
        if num%i==0:
            yield i
    for j in range(sqrt_num-1,0,-1):
        if num%j==0:
            yield num//j
