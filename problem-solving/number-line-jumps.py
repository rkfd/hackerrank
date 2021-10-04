import time


def kangaroo(x1, v1, x2, v2):
  # code starts here
  if x1 > x2 and v1 < v2:
      while (x1 > x2):
          x1 += v1
          x2 += v2
      if x1 == x2:
          return 'YES'
      else:
          return 'NO'
  elif x2 > x1 and v2 < v1:
      while (x2 > x1):
          x1 += v1
          x2 += v2
      if x2 == x1:
          return 'YES'
      else:
          return 'NO'
  else:
      return 'NO'
  # code ends here


# input
x1 = 0
v1 = 2
x2 = 5
v2 = 3

# output
start = time.time()
print(kangaroo(x1, v1, x2, v2))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')