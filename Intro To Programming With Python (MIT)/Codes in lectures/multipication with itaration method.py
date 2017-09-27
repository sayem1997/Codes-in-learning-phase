# Finding the multipication in iteration algorithm.

def mul(a,b):
    '''
    return the multipication of intiger a &  b.
    '''
    result = 0
    while b>0:
        result = result + a
        b -= 1

    return result

print(mul(4,5))    