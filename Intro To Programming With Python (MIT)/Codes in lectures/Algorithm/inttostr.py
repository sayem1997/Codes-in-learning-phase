def inttostr(i):
    '''This is an example of logarithmic compexity! '''
    digit = '0123456789'
    if i == 0:
        return '0'
    else:
        result = ''
        while i > 0:
            result = digit[i % 10] + result
            i = i//10
        return result

print(inttostr(100))

