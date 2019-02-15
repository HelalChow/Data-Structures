def findChange(lst01):
    left = 0
    right = len(lst01)-1
    one = None
    index_found = False
    while(index_found==False):
        curr = (left+right)//2
        if lst01[curr]==0 and lst01[curr+1]==1:
            one = curr+1
            index_found=True
        elif lst01[curr]==0 and lst01[curr+1]!=1:
            left = curr+1
        elif lst01[curr]==1 and lst01[curr-1]==0:
            one = curr
            index_found=True
        elif lst01[curr]==1 and lst01[curr-1]!=0:
            right = curr-1
    return one

def main():
    print(findChange([0,0,0,0,0,0,1]))
