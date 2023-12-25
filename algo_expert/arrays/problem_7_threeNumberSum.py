


#  TC O(n^2) SC O(n)
def threeNumberSum(array, targetSum):
    
    array.sort()
    triplets = []

    for idx in range(len(array)-2):
        current = array[idx]
        left = idx + 1
        right = len(array) - 1
        while left < right:
            left_nb = array[left]
            right_nb = array[right]
            current_sum = current + left_nb + right_nb
            if current_sum == targetSum:
                triplets.append([current, left_nb, right_nb])
                left += 1
                right -= 1
            elif current_sum > targetSum:
                right -= 1
            elif current_sum < targetSum:
                left += 1
    
    return triplets



array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

res = threeNumberSum(array, targetSum)
print(f"threeNumberSum {res}")
