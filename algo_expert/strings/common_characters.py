


def commonCharacters(strings):

    inter = set(strings[0])
    for idx in range(1, len(strings)):
        s = set(strings[idx])
        inter = inter.intersection(s)
    return list(inter)


inputs = ["abc", "bcd", "cbaccd"]
res = commonCharacters(inputs)
print(res)