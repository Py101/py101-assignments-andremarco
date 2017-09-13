from functools import reduce
def num_fatt (n):
    lista=list(range(1,n+1))
    k=(reduce(lambda x, y: x*y, lista))
    return k

num_fatt(3)