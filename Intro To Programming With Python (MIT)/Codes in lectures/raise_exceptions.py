def get_ratios(list1, list2):
    '''
    :argument: both lists have same length.
    :return: return the ratio of the index of both list.
    '''
    ratios = []
    try:
        for index in range(len(list1)):
            ratios.append(list2[index]/list[index])
    except ZeroDivisionError:
        ratios.append(float('nan')) # Not a number.
    except:
        print("get_ratios got bad args")
        