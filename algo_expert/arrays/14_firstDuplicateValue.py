
# def firstDuplicateValue(array):

#     if len(array) < 2:
#         return -1
    
#     hash_set = set()

#     for num in array:
#         if num in hash_set:
#             return num
#         hash_set.add(num)

#     return -1


def firstDuplicateValue(array):
    if len(array) < 2:
        return -1

    for idx in range(len(array)):
        num = array[idx]
        new_idx = abs(num-1)
        if array[new_idx] < 0:
            return num
        array[new_idx] = -array[idx]

    return -1






arr  = [2, 1, 5, 2, 3, 3, 4]
res = firstDuplicateValue(arr)

print(f"firstDuplicateValue {res}")