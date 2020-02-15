def linear_search(s, a):
    found_index = None
    for i in range(0, len(a)):
        if a[i] == s:
            found_index = i
            break
    return found_index
