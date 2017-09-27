'''
Complexity of an program:
To find the complexity of program, there is a method called "Big O Notation".
The complexity of a program become more important when the input become very large.
According to the rate of complexity The programs are devided into six types.

1. O(1): Constant running time function.
2. O(log N): Logarithmic running time function.
3. O(N): Linear running time function.
4. O(N log N): Log linear running time function.
5. O(n^c): Polynomial running time function.(Here 'c' is a constant.)
6. O(c^n): Expotential base running time function. Its the most complex function.

The main focus of Algorithm to make a program from a flow from 6 >> 1. If the program get more close to '1',
 it will get more efficient.
'''
def intToStr(i):
    """Assumes i is a nonnegative int
        Returns a decimal string representation of i"""

    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

