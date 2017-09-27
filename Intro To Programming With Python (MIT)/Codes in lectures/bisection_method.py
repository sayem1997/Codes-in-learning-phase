# cube = 27.0
# epsilon = 0.1
# low = 0
# high = cube
# number_of_guess = 0
# guess = (low + high)/2
# while guess**3 <= cube:
#     if guess**3 > cube:
#         guess = high
#         number_of_guess += 1
#     else:
#         low = guess    
#         number_of_guess += 1

# print('Number of guess = ', number_of_guess) 
# print('Cube root of {} is close to {}.'.format(cube,guess))       

####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 27
# cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
# cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low) / 2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
