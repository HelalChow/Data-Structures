import math as m
#version 1
def is_prime1(num):
    count=0
    for curr in range(1,num+1):
        if num%curr==0:
            count+=1
    if (count == 2):
        return True
    else:
        return False

#version 2
def is_prime2(num):
    count=0
    for curr in range(1,num/2+1):
        if num%curr==0:
            count+=1
    if (count == 1):
        return True
    else:
        return False

#version 3
def is_prime3(num):
    count = 0
    for curr in range(1, m.sqrt(num)  + 1):
        if num % curr == 0:
            count += 1
    if (count == 1):
        return True
    else:
        return False


