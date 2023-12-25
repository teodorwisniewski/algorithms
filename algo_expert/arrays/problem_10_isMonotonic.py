import operator


def isMonotonic(array):

    if len(array) < 2:
        return True
    
    left = 0
    right = 1
    comp_operator = None

    while right < len(array) and left < right:
        diff = array[right] - array[left]
        if diff:
            if diff > 0:
                comp_operator = operator.ge
            else:
                comp_operator = operator.le
            break
        right += 1
    
    if comp_operator is None:
        return True
    
    left = 0
    right = 1
    while right < len(array):
       
        if comp_operator(array[right], array[left]):
            left += 1
            right += 1 
            continue
        return False
    
    return True


        



arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
res = isMonotonic(arr)
print(f"isMonotonic {res}")


arr = [-1, -1, -1, -1, -1, -1]
res = isMonotonic(arr)
print(f"isMonotonic {res}")