cube = 27.0
guess = 0.00
epsilon = 0.01 
increment = 0.00001
number_of_guess = 0 

while (cube - guess**3) != epsilon and guess <= cube:
  guess = guess + increment 
  number_of_guess += 1

print('Number of guess = ',number_of_guess)

if (cube - guess**3) != epsilon:
  print('There is not any cube root of ',cube)
else:
  print('The closest cube root of {} is {}'.format(cube,guess))
