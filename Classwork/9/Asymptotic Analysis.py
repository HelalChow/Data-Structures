#We find the asymtotic order of the number of primitive operations as a function of its input size
''' = Theta*(Highest order)
        Ex: 3n^2 + 6n - 15  >>>  Theta*(n^2)'''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***** O definition *****
1. When we say f(n)= O(g(n)), it means g is an upper bound of f
    - f(n) <= constant*g(n) starting at some number n 
    - g(n) has a larger asymptotic order than f(n)
        - g(n) has a higher power than f(n)
   
***** Ω definition *****
1. When we say f(n) = Ω(f(n)), it means that g is a lower bound of f
    - f(n) >= constant*g(n) starting at some number n
    - g(n) has a lower asymptotic order than f(n)
        - g(n) has a lower power than f(n)

***** θ definition *****
1. When we say f(n) = θ(f(n)), it means that g is a lower bound of ff and g is a tight bound
    - f(n) = g(n)
    - They have the same asymptotic order 
        - highest power must be the same
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
Q1) Show that 3n^2+6n-15 = θ(n^2)

3n^2 <= 3n^2 +6n - 15 <= 3n^2+6n <= 3n^2+6n^2 <= 9n^2
  ^^ Only when n>2.5
c1 = 9
c2 = 3
n = 3
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
******** Important sums *************
1) 1+2+3+4......+n = (n(n+1))/2 or (1/2)n^2 + (1/2)n == θ(n^2)

2) 


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''