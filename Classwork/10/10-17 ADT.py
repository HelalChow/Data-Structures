def Algorithm():
    pass

'''
***Stack ADT***
Data Model: Collection of items where the last element in is the first to come out (Last in, first out)
Operations: 
    s = Stack()
    len(s)
    s.is_empty()
    s.push() #Adds Item
    s.pop()  #Removes last item and returns it
    s.top()  #Returns last item
'''

def print_reverse(str):
    letters = Stack()
    for i in str:
        letters.push(i)
    while(letters.is_empty() == False):
        print(letters.pop(),end='')
        print()


'''
***Polish Notation***
Infix               Postfix                 Prefix
5                   5                       5
5+2                 5 2 +                   + 5 2
5-(3*4)             5 34 * -                - 5 * 3 4
(5-3)*4             5 3 - 4 *               * - 5 3 4  
((5+2)*(8-3))/4     5 2 + 8 3 - * 4 /       / * + 5 2 - 8 3 4
'''