

# def sweetAndSavory(dishes, target):
    
#     sweet_dishes = sorted([dish for dish in dishes if dish < 0], reverse=True)
#     savory_dishes = sorted([dish for dish in dishes if dish >=0])

#     best_pair = [0, 0]
#     sweet_idx = 0
#     savory_idx = 0
#     best_diff = float('inf')

#     while sweet_idx < len(sweet_dishes) and savory_idx < len(savory_dishes):

#         current_sum = sweet_dishes[sweet_idx] + savory_dishes[savory_idx]
#         if current_sum > target:
#             sweet_idx += 1
#             continue
        
#         current_diff = target - current_sum
#         if current_diff < best_diff:
#             best_diff = current_diff
#             best_pair = [
#                 sweet_dishes[sweet_idx],
#                 savory_dishes[savory_idx]
#             ]
#             savory_idx += 1

#     return best_pair


# def sweetAndSavory(dishes, target):
    
#     dishes = sorted(dishes)
#     sweet_idx, savory_idx = 0, len(dishes) - 1
#     best_pair = [0, 0]
#     best_diff = float("inf")
#     while sweet_idx < savory_idx and dishes[sweet_idx] < 0 and dishes[savory_idx] >= 0:

#         cs = dishes[sweet_idx] + dishes[savory_idx]

#         if cs <= target:
#             curr_diff = target - cs
#             if curr_diff < best_diff:
#                 best_diff = curr_diff
#                 best_pair = [
#                     dishes[sweet_idx],
#                     dishes[savory_idx]
#                 ]
                
#                 sweet_idx += 1
#         else:
#             savory_idx -= 1
            
#     return best_pair


def sweetAndSavory(dishes, target):
    res = [0,0]
    l = 0 
    r = len(dishes) - 1
    dishes.sort()
    lowest_diff = float('inf')
    while l < r and dishes[l] < 0 and dishes[r]>0:
        cs = dishes[l] + dishes[r]
        if cs > target:
            r -= 1
            continue

        diff = target - cs
        if diff <= lowest_diff:
            res = [
                dishes[l],
                dishes[r]
            ]
            lowest_diff = diff
        l += 1
            
    return res

inputs = [-3, -5, 1, 7]   
target = 8
res = sweetAndSavory(inputs, target)
print(f"sweetAndSavory {res}")
assert [-3, 7] == res


inputs = [2, 5, -4, -7, 12, 100, -25] 
target = -20
res = sweetAndSavory(inputs, target)
print(f"sweetAndSavory {res}")
assert [-25, 5] == res 

inputs  = [3, 5, 7, 2, 6, 8, 1]  
target = 10
res = sweetAndSavory(inputs, target)
print(f"sweetAndSavory {res}")
assert [0, 0] == res 