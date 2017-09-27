# If there is any error which can be predicted earlier and to handle these kind of error in python,
# try/except is been used.
try:
    a = input("Please Enter a Number: \n")
    b = input("Please Enter a Number: \n")
    print("The division of two number is : ", a/b)
    print("The multipication of two number is ", a*b)
except ValueError:
    print("Could not convert to a number. \n") # ValueError is that kind of error where input is not given as expected.
                                                # Like where intiger is expected, string is given.
except ZeroDivisionError:
    print("No number can't be devided by zero! \n") # If something is devided by zero, it cause ZeroDivisionError.
except:
    print("Its a major kind of error.! \n") # This except handle all kind of error.