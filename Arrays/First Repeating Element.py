def firstRepeated(arr, n):
    index_dict = {}
    first_repeated_pos = -1
    for i in range(n):
        if arr[i] in index_dict:
            first_repeated_pos = index_dict[arr[i]]
            break
        else:
            index_dict[arr[i]] = i + 1  
    return first_repeated_pos
