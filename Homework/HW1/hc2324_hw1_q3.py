def a_sum_square(n):
    sum=0
    for i in range(n):
        sum+=i**2
    return sum

def b_sum_square(n):
    return sum(i**2 for i in range(n))

def c_sum_square(n):
    sum = 0
    for i in range(n):
        if i%2 != 0:
            sum += i**2
    return sum

def d_sum_square(n):
    return sum(i**2 for i in range(n) if i%2 != 0)

