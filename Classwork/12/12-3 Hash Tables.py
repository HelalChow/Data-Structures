def hashTable():
    pass


'''
********* HASH TABLES ************

U: Universe from which the keys will be taken

T = [None} * N
Hash Table of N slots where the entries will be stored

h: Hash function that maps keys from U (universe) to slots in the table

------------------------------------------------------------------------------------------

1) insert(key, value)
    i = h(key)
    T[i] = value
    
2) find(key)
    i = h(key)
    return T[i]
    
------------------------------------------------------------------------------------------

Collision Problem: Multiple keys could be mapped to the same slot

Solutions
1) Chaining Solution: Chain multiple values in the same key (Linked List etc)
    a) problem: A lot of keys could be stored at the same slot
    
2) Uniform Hash Functions: When given a key, it has equal chance of being mapped to any of the slots, 
                           independent of other keys
                           


*************** CODING FUNCTIONS ********************

Common Approaches:
1) Integer Casting: Look at binary representation of key
    - Take the 8 least significant bytes, and interpret it as a 64-bit 2's complement number
    a) problem: Ignores part of the data (the more significant bytes) eg: Will not work with emails

2) Component Sum: Breaks key into components 
    - Adds up all the components of key (as opposed to previous which takes only one component)
    a) problem: This apporach does not take into account the position of the components
        - "stop" = "tops" = "pots" etc
        
3) Polynomial Accumulation: z is and int >= 2. Break up its components. Each component is multiplied by z^(n-1)
    - Each component has a different weight based on position
    
Built in Function: hash(key)
- Can be called with immutable types (int, str, float, tuple)



*************** COMPRESSION *******************

Common Approaches:
1) Division Method: Given an integer k, h(k) = k % N
    a) problem: May end up with really long chains
    b) solution: Make N a prime number
    
2) Multiply-Ass-Divide: h(k) = [(ak + b) % p] % N
    - p is prime number
    - a is random number >= 1
    - b is a random number >= 0
    

UNIFORM HASH FUNCTION
- Each table entry has the same number of keys

Time Analysis of Find
alpha = n / N
    - N is size of table
    - n is the size of chain in each table entry
    **** n <= N
    









'''