from numberToBase import *
from overlapAlignment import *
from scoreMatrix import *

scoreMatrix = createScoreMatrix(2, -2)
x = [1,2,3,4,2]
y = [3,4,2,1,2]
A, B = overlapAlignment(x, y, scoreMatrix, -2)

print("Expected output: ")
print("ACGTC--")
print("--GTCAC")
print("")
print("Computed output: ")
print(numberToBase(A))
print(numberToBase(B))
