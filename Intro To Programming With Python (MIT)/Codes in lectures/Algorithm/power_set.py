### Expotential Complexity ####

def get_sub_sets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = get_sub_sets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)

    return smaller + new

print(get_sub_sets(['1','2','3','4','5']))
