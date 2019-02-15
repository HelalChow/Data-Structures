def fibs(n):
    prev = 0
    prev2 = 0
    for i in range(n):
        if (prev == 1 and prev2 != 1) or prev==0:
            yield 1
            prev2 = prev
            prev = 1
        else:
            curr = prev + prev2
            yield curr
            prev2 = prev
            prev = curr


