


def productSum(array, multiplier=1):
    
    total_sum = 0
    for el in array:
        if isinstance(el, list):
            total_sum += productSum(el, multiplier+1)
        else:
            total_sum += el

    return total_sum * multiplier



arr  = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
res = productSum(arr)
print(f'productSum {res}')