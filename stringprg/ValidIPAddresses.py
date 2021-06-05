n =8
def sumall(n):
    if n ==1:
        return 1
    return n+sumall(n-1)
print(sumall(n))


