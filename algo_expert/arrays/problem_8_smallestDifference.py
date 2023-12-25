


def smallestDifference(arrayOne, arrayTwo):
    
    arrayOne.sort()
    arrayTwo.sort()
    p1, p2 = 0, 0
    n = len(arrayOne)
    m = len(arrayTwo)
    smallest = float("inf")

    while p1 < n and p2 < m:

        val1 = arrayOne[p1]
        val2 = arrayTwo[p2]

        if val1 < val2:
            current = val2 - val1
            p1 += 1
        elif val2 < val1:
            current = val1 - val2
            p2 += 1
        else:
            return [val1, val2]
        
        if current < smallest:
            res = [val1, val2]
            smallest = current

    return res




arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

res = smallestDifference(arrayOne, arrayTwo)
print(f"smallestDifference {res}")