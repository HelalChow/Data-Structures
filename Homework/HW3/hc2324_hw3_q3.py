def find_duplicates(lst):
    counter = [0] * (len(lst) - 1)
    res_lst = []

    for i in range(len(lst)):
        counter[lst[i] - 1] += 1

    for i in range(len(counter)):
        if (counter[i] > 1):
            res_lst.append(i + 1)

    return res_lst


print(find_duplicates([0,2,2]))