

def generateDivTags(numberOfTags):

    res = []
    def rec(prefix, opening, closing):

        if opening == closing == 0:
            res.append(prefix)
            return
        
        if opening > 0:
            new_prefix = prefix + '<div>'
            rec(new_prefix, opening-1, closing)
        
        if closing > opening:
            new_prefix = prefix + '</div>'
            rec(new_prefix, opening, closing-1)            


    rec('', numberOfTags, numberOfTags)

    return res




res = generateDivTags(3)
print(f"generateDivTags {res}")
