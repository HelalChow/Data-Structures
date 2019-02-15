def e_approx(n):
    approx = 0
    factorial = 0
    for i in range(1,n+1):
        if i == 1 or i == 2:
            factorial = i
        else:
            factorial = factorial*i
        approx = approx + (1/factorial)
    return (1+approx)

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
