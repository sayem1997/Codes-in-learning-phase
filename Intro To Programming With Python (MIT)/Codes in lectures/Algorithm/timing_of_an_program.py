'''
Complexity of an program:
To find the complexity of program, there is a method called "Big O Notation".
The complexity of a program become more important when the input become very large.
According to the rate of complexity The programs are devided into six types.
'O'  is order here.
1. O(1): Constant running time function.
2. O(log N): Logarithmic running time function.
3. O(N): Linear running time function.
4. O(N log N): Log linear running time function.
5. O(n^c): Polynomial running time function.(Here 'c' is a constant.)
6. O(c^n): Expotential base running time function. Its the most complex function.

The main focus of Algorithm to make a program from a flow from 6 >> 1. If the program get more close to '1',
 it will get more efficient.
'''
import time

def c_to_f(centigrate):
    return centigrate*9/5 + 32

t0 = time.clock()

c_to_f(100)

t1 = time.clock() - t0
print('t = ', t1, 's,')
