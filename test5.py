from numberToBase import *
from overlapAlignment import *
from scoreMatrix import *

scoreMatrix = createScoreMatrix(2, -2)
x = [1,2,3,4,2,1,3]
y = [2,1,3]
A, B = overlapAlignment(x, y, scoreMatrix, -2)

print("Expected output: ")
print(numberToBase(x))
print("----CAG")
print("")
print("Computed output: ")
print(numberToBase(A))
print(numberToBase(B))
