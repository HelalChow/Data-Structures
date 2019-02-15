def two_sum(srt_lst, target):
    curr_index = 0
    sum_found = False
    count =0
    while(sum_found==False and curr_index < len(srt_lst)-1):
        if (count >= len(srt_lst)):
            count = 0
            curr_index += 1
        elif srt_lst[curr_index] + srt_lst[count] == target and curr_index != count:
            sum_found = True
        else:
            count+=1
    if sum_found==True:
        return (curr_index, count)
    else:
        return None

def main():
    srt_lst = [-2, 7, 11, 15, 20, 21]
    target = 35
    print(two_sum(srt_lst, target))
