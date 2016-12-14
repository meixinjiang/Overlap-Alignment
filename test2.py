from numberToBase import *
from overlapAlignment import *
from scoreMatrix import *

scoreMatrix = createScoreMatrix(2, -2)
x = [3,4,2,1,2]
y = [1,2,3,4,2]
A, B = overlapAlignment(x, y, scoreMatrix, -2)

print("Expected output: ")
print("--GTCAC")
print("ACGTC--")
print("")
print("Computed output: ")
print(numberToBase(A))
print(numberToBase(B))
