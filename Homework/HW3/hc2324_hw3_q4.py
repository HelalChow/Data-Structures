def remove_all(lst, value):
    num = 0
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i]=None
            num +=1
    count =0
    round = num
    while round>0:
        if lst[count]==None and count+1<len(lst):
            lst[count]=lst[count+1]
            lst[count+1]=None
            count+=1
        else:
            count+=1
        if count==len(lst):
            count=0
            round-=1
    for i in range(num):
        lst.pop()
    return lst
