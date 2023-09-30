


def arrayOfProducts(array):
    products = [1 for _ in array]
    n = len(array)

    left_product = 1
    for idx in range(n):
        products[idx] = left_product
        left_product *= array[idx]

    right_running_product = 1
    for idx in reversed(range(n)):
        products[idx] *= right_running_product
        right_running_product *= array[idx]

    return products









        

arr  = [5, 1, 4, 2]
res = arrayOfProducts(arr)

print(f"arrayOfProducts {res}")