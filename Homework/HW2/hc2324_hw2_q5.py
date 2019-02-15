def split_parity(lst):
   left=0
   right=len(lst)-1
   while (left<=right):
      if lst[left]%2!=0 and lst[right]%2==0:
         left+=1
         right-=1
      elif lst[left]%2==0 and lst[right]%2!=0:
         switched=lst[left]
         lst[left]=lst[right]
         lst[right]=switched
         left+=1
         right-=1
      elif lst[left]%2!=0 and lst[right]%2!=0:
         left+=1
      else:
         right-=1
   return lst
