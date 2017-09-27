'''
This is an example of an linear complexity algorithm.
Factorial is the example of an linear complexity algoritghm.
'''
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

print(fact(6))