def bisect_search2(L, e):
    def bisection_search_helper(L, e, high, low):
        if high == low:
            return L[low] == e
        mid = (low + high) //2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == high: # Nothing to search here
                return False
            else:
                return bisection_search_helper(L, e, low, mid - 1)
        else:
            return bisection_search_helper(L, e, mid + 1, high )
    if len(L) == 0:
        return False
    else:
        return bisection_search_helper(L, e, 0, len(L) - 1)