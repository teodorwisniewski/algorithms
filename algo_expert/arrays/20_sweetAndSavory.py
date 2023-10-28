

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


def sweetAndSavory(dishes, target):
    
    sweet_dishes = sorted([dish for dish in dishes if dish < 0], reverse=True)
    savory_dishes = sorted([dish for dish in dishes if dish >=0])

    best_pair = [0, 0]
    sweet_idx = 0
    savory_idx = 0
    best_diff = float('inf')

    while sweet_idx < len(sweet_dishes) and savory_idx < len(savory_dishes):

        current_sum = sweet_dishes[sweet_idx] + savory_dishes[savory_idx]
        
        if current_sum <= target:
            current_diff = target - current_sum
            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [
                    sweet_dishes[sweet_idx],
                    savory_dishes[savory_idx]
                ]
                savory_idx += 1
        else:
            sweet_idx += 1

    return best_pair



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