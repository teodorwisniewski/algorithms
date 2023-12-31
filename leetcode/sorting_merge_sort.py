
def merge(lst1, lst2):

    combined = []

    p1, p2 = 0, 0

    while p1 < len(lst1) and p2 < len(lst2):

        if lst1[p1] < lst2[p2]:
            combined.append(lst1[p1])
            p1 += 1
        else:
            combined.append(lst2[p2])
            p2 += 1        

    if p1 < len(lst1):
        combined.extend(lst1[p1:])

    if p2 < len(lst2):
        combined.extend(lst2[p2:])
    
    return combined


if __name__ == "__main__":

    ...
