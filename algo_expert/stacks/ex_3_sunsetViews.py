


# def sunsetViews(buildings, direction):

#     stack = []
#     if direction == "EAST":
#         for i, val in enumerate(buildings):
#             stack.append((i, val))
#     else:
#         count = len(buildings) - 1
#         while buildings:
#             heigth = buildings.pop()
#             stack.append((count, heigth))
#             count -= 1
    
#     max_value = float("-inf")
#     outputs = []
#     while stack:
#         idx, val = stack.pop()
#         if val > max_value:
#             outputs.append(idx)
#             max_value = val
#     if direction == "EAST":
#         return outputs[::-1]
#     else:
#         return outputs



# def sunsetViews(buildings, direction):

#     outputs = []
#     running_max = 0
#     if direction == "EAST":
#         for i, val in reversed(list(enumerate(buildings))):
#             if val > running_max:
#                 outputs.append(i)
#                 running_max = val
#     else:
#         for i, val in enumerate(buildings):
#             if val > running_max:
#                 outputs.append(i)
#                 running_max = val
    

            
#     if direction == "EAST":
#         return outputs[::-1]
#     else:
#         return outputs


def sunsetViews(buildings, direction):

    stack = []

    if direction == "EAST":
        for i, val in reversed(list(enumerate(buildings))):
            if not stack or val > buildings[stack[-1]]:
                stack.append(i)
    else:
        for i, val in enumerate(buildings):
            if not stack or val > buildings[stack[-1]]:
                stack.append(i)
    

            
    if direction == "EAST":
        return stack[::-1]
    else:
        return stack