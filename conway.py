import os
#os.system('clear')
M=[
    [1,1,0,0],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,0,0],
    ]
def get(M, x,y):
  if x <0 or y < 0:
    return 0
  elif x >= len(M) or y >= len(M[0]):
    return 0
  else:
    return M[x][y]

def calc(M, x, y):
  c = 0
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i==x and y==j:
        continue
      else:
        c+=get(M, i, j)
  return c

def p(M):
  for i in M:
    print i

for k in range(0,8):
  lastr = []
  lastv = 0
  curr = []
  p(M)
  tmpv=None
  for i in range(0,len(M)):
    curr = M[i][:]
    if i != 0:
      tmp = M[i-1]
      M[i-1] = lastr
    for j in range(0, len(M[i])):
      if j != 0:
         tmpv = M[i][j-1]
         M[i][j-1] = lastv
      lastv = M[i][j]
      c = calc(M,i,j)
      if M[i][j] == 0:
        if c == 3:
          M[i][j] = 1
      else:
        if c in [0,1]:
          M[i][j] = 0
        elif c in [2,3]:
          M[i][j] = 1
        else:
          M[i][j] = 0

      if j != 0:
        M[i][j-1] = tmpv
    if i != 0:
      M[i-1] = tmp
    lastr=curr
  print "\n"





