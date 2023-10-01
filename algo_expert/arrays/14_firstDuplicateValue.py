
def firstDuplicateValue(array):

    if len(array) < 2:
        return -1
    
    hash_set = set()

    for num in array:
        if num in hash_set:
            return num
        hash_set.add(num)

    return -1






arr  = [2, 1, 5, 2, 3, 3, 4]
res = firstDuplicateValue(arr)

print(f"firstDuplicateValue {res}")