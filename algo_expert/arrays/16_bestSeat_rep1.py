



def bestSeat(seats):

    best_seat = -1
    max_space = 0
    left, right = 0, 0
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1
        available_space = right - left - 1
        if available_space > max_space:
            max_space = available_space
            best_seat = (right + left)//2
        left = right
    
    return best_seat




seats  = [1, 0, 1, 0, 0, 0, 1]
res = bestSeat(seats)
print(f"bestSeat {res}")