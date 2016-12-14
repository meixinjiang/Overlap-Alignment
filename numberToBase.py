"""
Takes a list of numbers [1,2,3,4] and converts it to its corresponding
base [A, C, G, T]. If list contains "-" and/or "+", it is retained in the
output.
parameters - list of bases in numerical form
returns - string of bases
"""
def numberToBase(basesList):
    baseString = ""
    for item in basesList:
        if item == 1:
            baseString += "A"
        elif item == 2:
            baseString += "C" 
        elif item == 3:
            baseString += "G" 
        elif item == 4:
            baseString += "T"
        else:
            baseString += item
    return baseString
