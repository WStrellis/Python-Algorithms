
def binary_search(s, a) -> int:
    at_index = -1

    if len(a) == 0:
        return at_index

    high = len(a) - 1
    low = 0
    while high != low:
        middle = ((high - low) // 2) + low
        if a[middle] == s:
            at_index = middle
            break
        # if middle > s eliminate numbers greater than middle
        elif a[middle] > s:
            high = middle
        # if middle < s eliminate numbers lower than middle
        elif a[middle] < s:
            low = middle + 1

    return at_index


""" 
def binary_search(s, a) -> int:
    if len(a) == 0:
        return -1
    middle = len(a) // 2
    if len(a) == 1 and a[middle] != s:
        return -1
    elif a[middle] == s:
        return middle
    # if middle > s eliminate numbers greater than middle
    elif a[middle] > s:
        binary_search(s, a[0: middle])
    # if middle < s eliminate numbers lower than middle
    elif a[middle] < s:
        binary_search(s, a[middle + 1: len(a)])
 """
