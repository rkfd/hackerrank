import time


def birthday(s, d, m):
  # code starts here
  res = 0
  
  for i in range(0,len(s)-m+1):
      temp = 0
      for j in range(i,i+m):
          temp += s[j]
      if temp == d:
          res += 1
  return res
  # code ends here


# input
s = [1, 2, 1, 3, 2]
d = 3
m = 2

# output
start = time.time()
print(birthday(s, d, m))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')