"""
Performs an overlap alignment given 2 sequences
parameters - sequence 1, sequence 2, score matrix, gap penalty
returns - sequence 1 aligned to sequence 2, sequence 2 aligned to sequence 1
"""
def overlapAlignment(sequence1, sequence2, scoreMatrix, gapPenalty):

    #make F matrix
    F = [[0 for i in range(len(sequence1)+1)] for j in range(len(sequence2)+1)]
    for i in range(len(sequence2)+1): #left boundary set to 0
        F[i][0] = 0
    for j in range(len(sequence1)+1): #top boundary set to 0
        F[0][j] = 0
        
    #completes the F matrix
    for i in range(1,len(F)): 
        for j in range(1,len(F[0])):
            match = F[i-1][j-1] + scoreMatrix[sequence1[j-1]-1][sequence2[i-1]-1]
            delete = F[i-1][j] + gapPenalty
            insert = F[i][j-1] + gapPenalty
            F[i][j] = max(match, delete, insert)

    #get the maximum value for the bottom and right boundaries of F Matrix
    bottomMaximum = 0
    rightMaximum = 0
    bottomjMax = 0
    rightiMax = 0
    for i in range(len(F)): #get the maximum value in the right boundary
        if F[i][len(F[0])-1] > rightMaximum or F[i][len(F[0])-1] == rightMaximum:
            rightMaximum = F[i][len(F[0])-1]
            rightiMax = i
    for j in range(len(F[0])): #get the maximum value in the bottom boundary
        if F[len(F)-1][j] > bottomMaximum or F[len(F)-1][j] == bottomMaximum:
            bottomMaximum = F[len(F)-1][j]
            bottomjMax = j

    iMax = 0
    jMax = 0
    
    #chooses whether to use the right or bottom boundary based on the maximum values
    if bottomMaximum > rightMaximum: #choose bottom boundary
        iMax = len(F)-1
        jMax = bottomjMax
    elif bottomMaximum < rightMaximum: # choose right boundary
        iMax = rightiMax
        jMax = len(F[0])-1
    #chooses whether to use the right of bottom boundary based on how close they are to the location of last element
    else:
        if len(F) - rightiMax < len(F[0]) - bottomjMax: #choose right boundary
            iMax = rightiMax
            jMax = len(F[0])-1
        elif len(F) - rightiMax > len(F[0]) - bottomjMax: #choose bottom boundary
            iMax = len(F)-1
            jMax = bottomjMax
        else: #maximum bottom and maximum right are the same distance away from the location of last element in F
            iMax = len(F)-1
            jMax = bottomjMax   
    
    alignmentA = []
    alignmentB = []
    
    #inserts gaps to the left of the sequences
    if iMax < len(F)-1: #gap for horizontal
        count = len(F) - 1 - iMax
        index = len(F) - 1 - 1 #compensates for F and for index in sequence
        for i in range(count):
            alignmentA.insert(0, "-")
            alignmentB.insert(0, sequence2[index])
            index -= 1
    elif jMax < len(F[0])-1: #gap for vertical
        count = len(F[0]) - 1 - jMax
        index = len(F[0]) - 1 - 1 #compensates for F and for index in sequence
        for i in range(count):
            alignmentB.insert(0, "-")
            alignmentA.insert(0, sequence1[index])
            index -= 1

    #begins backtracking   
    while iMax > 0 or jMax > 0:
        if iMax > 0 and jMax > 0 and F[iMax][jMax] == F[iMax-1][jMax-1] + scoreMatrix[sequence1[jMax-1]-1][sequence2[iMax-1]-1]:
            alignmentA.insert(0, sequence1[jMax-1])
            alignmentB.insert(0, sequence2[iMax-1])
            iMax -= 1
            jMax -= 1
        elif iMax == 0: #top boundary is reached
            while jMax > 0:
                alignmentB.insert(0, "-")
                alignmentA.insert(0, sequence1[jMax-1])
                jMax -= 1
        elif jMax == 0: #right boundary is reached
            while iMax > 0:
                alignmentB.insert(0, sequence2[iMax-1])
                alignmentA.insert(0, "-")
                iMax -= 1
        elif iMax > 0 and F[iMax][jMax] == F[iMax-1][jMax] + gapPenalty:
            alignmentB.insert(0, sequence2[iMax-1])
            alignmentA.insert(0, "-")
            iMax -= 1
        elif jMax > 0 and F[iMax][jMax] == F[iMax][jMax-1] + gapPenalty:
            alignmentB.insert(0, "-")
            alignmentA.insert(0, sequence1[jMax-1])
            jMax -= 1

    return alignmentA, alignmentB
