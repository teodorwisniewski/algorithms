


# # TC O(n) SC O(n)
# def maxSubsetSumNoAdjacent(array):
#     if len(array) == 0:
#         return 0
#     if len(array) < 3:
#         return max(array)
    
#     sum_array = [0 for _ in array]
#     sum_array[0] = array[0]
#     sum_array[1] = max(array[0], array[1])
    
#     for i in range(2, len(array)):
#         second_el = sum_array[i-2] + array[i]
#         sum_array[i] = max(sum_array[i-1], second_el)

#     return sum_array[-1]
    



# TC O(n) SC O(1)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) < 3:
        return max(array)
    
    sum_array = []
    sum_array.append(array[0])
    sum_array.append(max(array[0], array[1]))
    
    for i in range(2, len(array)):
        first_el = sum_array[1]
        second_el = sum_array[0] + array[i]
        current_max = max(first_el, second_el)
        sum_array[0], sum_array[1] = sum_array[1], current_max

    return current_max
    






array = [75, 105, 120, 75, 90, 135]
res = maxSubsetSumNoAdjacent(array)
assert res == 330
print(f"maxSubsetSumNoAdjacent {res}")
