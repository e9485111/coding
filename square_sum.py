import math
N=100
A = []
A = range(0,N+1)
for i in range(1,N+1):
  for j in range(0, int(math.ceil(math.sqrt(i))+1)):
      A[i] = min(
        1 + A[i-int(math.pow(j,2))],
        A[i]
        )
for i,j in enumerate(A):
  print i,j
