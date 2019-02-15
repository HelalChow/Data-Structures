import ArrayQueue
import ArrayStack

def most_frequent(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    max = None
    ind = 0
    for i in dic:
        if max is None:
            max = dic[i]
            ind = i
        elif dic[i] > max:
            max = i
            ind = i
    return ind

'''lst=[5,9,2,9,0,5,9,7]
print(most_frequent(lst))'''

def target_sum(lst, target):
    dic = {}
    for i in range(len(lst)):
        complement = target - lst[i]
        dic[complement] = i
    for i in range(len(lst)):
        if lst[i] in dic:
            j = dic[lst[i]]
            if i != j:
                return (i,j)
    return (None, None)

'''lst = [-2, 11, 15, 21, 20, 7]
print(target_sum(lst, 22))'''

def palindrome(str):
    palindrome = ""
    dic = {}
    stack = ArrayStack.ArrayStack()
    queue = ArrayQueue.ArrayQueue()

    for i in str:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    no_dup = False
    for i in dic:
        if dic[i] > 1:
            no_dup = True

    if no_dup == False:
        for i in dic:
            return i

    for i in dic:
        for j in range(dic[i] //2):
            queue.enqueue(i)
            stack.push(i)

    for i in range(len(queue)):
        palindrome = palindrome + queue.dequeue()

    for i in range(len(stack)):
        palindrome = palindrome + stack.pop()

    return palindrome


str1 = "aaaabbccccddde"
str2 = "abcdefg"
str3 = "wxyzwxyz"
print(palindrome(str1))