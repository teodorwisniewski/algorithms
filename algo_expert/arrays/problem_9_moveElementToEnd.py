


def moveElementToEnd(array, toMove):
    
    left, right = 0, len(array) - 1

    while left < right:

        right_val = array[right]
        if right_val == toMove:
            right -= 1
            continue
    
        left_val = array[left]
        if left_val == toMove:
            array[left], array[right] = right_val, left_val
            left += 1
        
        if array[left] != toMove:
            left += 1
        
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

res = moveElementToEnd(array, toMove)
print(f"moveElementToEnd {res}")