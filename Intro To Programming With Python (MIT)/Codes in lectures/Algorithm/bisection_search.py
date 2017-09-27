def bisection_search(list, item):
    '''
    Here it is logarithmic run time algorithm.
    In this case for worst case, we need to go 2^i step.
    here,
        1 = n/2^i
     so,i = log(2)n (2 is the base of the logarithm)

     So, its a logarithmic runtime example.
    '''
    if list = []:
        return False
    elif len(list) == 1:
        return list[0] == item
    else:
        half = len(list) // 2
        if list[half] > item:
            return bisection_search(list[:half], item)
        else:
            return bisection_search(list[half:], item)