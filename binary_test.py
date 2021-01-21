def bin_search(x):
    column = ["a","c","d","e","e","e","t"]
    bottom = 0
    top = len(column)-1
    found = False
    location = -1
    while(bottom <= top) and not(found):
        middle = int((bottom + top)//2)
        if(column[middle] == x):
            location = middle
            found = True
        else:
            if x < column[middle]:
                top = middle - 1
            else:
                bottom = middle + 1
    # Index of last occurrence
    location2 = -1
    # Index of first occurrence
    location3 = -1

    # Finds last index that matches x
    for I in range(len(column)):
        if column[I] == x:
            location2 = I
    # Finds first index that matches x
    for I in range(len(column)):
        if column[I] == x:
            location3 = I
            break


    return location3, location2

print(bin_search("c"))
