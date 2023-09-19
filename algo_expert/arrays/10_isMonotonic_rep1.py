import operator


def isMonotonic(array):

    if len(array) < 2:
        return True
    
    is_non_deacrising = True
    is_non_increasing = True

    for idx in range(1, len(array)):

        diff = array[idx] - array[idx-1]

        if diff > 0:
            is_non_deacrising = False
        elif diff < 0:
            is_non_increasing = False

    return is_non_increasing or is_non_deacrising


        



arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
res = isMonotonic(arr)
print(f"isMonotonic {res}")


arr = [-1, -1, -1, -1, -1, -1]
res = isMonotonic(arr)
print(f"isMonotonic {res}")