

#  TC O(2^(M+N)) SC O(M+N)
# def interweavingStrings(one, two, three):
#     if len(three) != len(one) + len(two):
#         return False
#     return areInterwoven(one, two, three, 0, 0)


# def areInterwoven(one, two, three, pointer_one, pointer_two):
#     pointer_three = pointer_one + pointer_two
#     if pointer_three == len(three):
#         return True
    
#     if pointer_one < len(one) and one[pointer_one] == three[pointer_three]:
#         if areInterwoven(one, two, three, pointer_one+1, pointer_two):
#             return True

#     if pointer_two < len(two) and two[pointer_two] == three[pointer_three]:
#         return areInterwoven(one, two, three, pointer_one, pointer_two+1)
    
#     return False

#  TC O(2^(M*N)) without caching.... with caching O(mxn) SC O(M*N)
def interweavingStrings(one, two, three):

    if len(three) != len(one) + len(two):
        return False
    cache = dict()
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, p1, p2, cache):

    hash_key = (p1, p2)
    if hash_key in cache:
        return cache[hash_key]

    p3 = p1 + p2
    if p3 == len(three):
        return True
    
    if p1 < len(one) and one[p1] == three[p3]:
        cache[hash_key] = areInterwoven(one, two, three, p1+1, p2, cache)
        if cache[hash_key]:
            return True

    if p2 < len(two) and two[p2] == three[p3]:
        cache[hash_key] = areInterwoven(one, two, three, p1, p2+1, cache)
        return cache[hash_key]
    
    cache[hash_key] = False
    return False

            



one = "algoexpert"
two  = "your-dream-job"
three = "your-algodream-expertjob"

res = interweavingStrings(one, two, three)
print(f"interweavingStrings {res}")



one = "a"
two  =  "b"
three = "ac"
res = interweavingStrings(one, two, three)
print(f"interweavingStrings {res}")

