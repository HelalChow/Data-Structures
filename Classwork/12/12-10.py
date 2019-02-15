def Heap():
    pass


'''
*********** HEAP *************
1) Heap Order Property: Priority of node is less than or equal to the property of its children
2) Nearly Complete Property: All levels before the last are filled. The last level gets filled from left to right

--- Minimum element is stored in the root
--- If n is number of entries, h is the height. Then h = O(log(n))


Insert: 
- Add it to the lowest level starting from left
- Compare to parent, and swap based on priority

Delete_Min:
- Replace root value with value of last node (lowest level at the right)
- Delete the last node
- Compare children of root based on priority
- Compare that priority with the new root priority
- Swap
- Compare the children of the new sub_roots


Store Values in an Array:
- Index 0 is blank (Start at 1)
- 







'''

print(3%11)