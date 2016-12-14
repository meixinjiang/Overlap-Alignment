"""
Creates a score matrix as a 2D list given the scores when x = y and x != y
parameters - score when x = y, score when x != y
returns - 2D list
"""
def createScoreMatrix(XisY, XnotY):
    scoreMatrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if i == j:
                scoreMatrix[i][j] = XisY #x = y
            elif i != j:
                scoreMatrix[i][j] = XnotY #x != y        
    return scoreMatrix
