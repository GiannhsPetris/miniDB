def bin_search(x, list1):

    bottom = 0
    top = len(list1)-1
    found = False
    location = -1
    while(bottom <= top) and not(found):
        middle = int((bottom + top)//2)
        if(list1[middle] == x):
            location = middle
            found = True
        else:
            if x < list1[middle]:
                top = middle - 1
            else:
                bottom = middle + 1
    # Index of last occurrence
    location_l = -1
    # Index of first occurrence
    location_f = -1

    # Finds last index that matches x
    for I in range(len(list1)):
        if list1[I] == x:
            location_l = I
    # Finds first index that matches x
    for I in range(len(list1)):
        if list1[I] == x:
            location_f = I
            break


    return list1[location_f:location_l+1]
