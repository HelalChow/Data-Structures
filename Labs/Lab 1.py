import random

def add_binary(num1_str, num2_str):
    num1 = 0
    num2= 0
    for i in range(len(num1_str),0,-1):
        if num1_str[i] == 0:





def main():
    add_binary("1101","0111")
main()"""

"""def can_construct(ransom_note, magazine):
    note = ransom_note
    letters = magazine
    for i in letters:
        if i in note:
            note = note.replace(i,"",1)
    if note == "":
        print(True)
    else:
        print(False)
def main():
    can_construct("abca", "aaaab")
main()

def create_permutation(n):
    lst=[]
    while len(lst) != n:
        num = random.randint(0,n-1)
        if num in lst:
            pass
        else:
            lst.append(num)
    return lst

def scramble_word(word):
    num = len(word)
    lst = create_permutation(num)
    new = ""
    for i in lst:
        letter=word[i]
        new+=letter
    print(new)
def main():
    scramble_word("pokemon")
main()"""



