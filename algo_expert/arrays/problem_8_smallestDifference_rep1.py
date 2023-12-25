


def smallestDifference(arrayOne, arrayTwo):
    
    arrayOne.sort()
    arrayTwo.sort()
    p1, p2 = 0, 0
    lowest_diff = float("inf")

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        val_one = arrayOne[p1]
        val_two = arrayTwo[p2]
        if val_one < val_two:
            p1 += 1
            diff = val_two - val_one
        elif val_one > val_two:
            p2 += 1
            diff = val_one - val_two
        else:
            return [val_one, val_two]
        
        if diff < lowest_diff:
            lowest_diff = diff
            res = [val_one, val_two]      

    return res











# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# res = smallestDifference(arrayOne, arrayTwo)
# print(f"smallestDifference {res}")


arrayOne = [-1, 5, 10, 20, 3]
arrayTwo = [26, 134, 135, 15, 17]
res = smallestDifference(arrayOne, arrayTwo)
print(f"smallestDifference {res}")