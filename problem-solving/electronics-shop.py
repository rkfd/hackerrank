import time


def getMoneySpent(keyboards, drives, b):
  # code starts here
  max = i = j = 0
  
  for k in range(0,len(keyboards)):
    for d in range(0,len(drives)):
      if (keyboards[k] + drives[d]) > max and (keyboards[k] + drives[d] <= b):
        max = keyboards[k] + drives[d]

  if max == 0:
    return -1
  else:
    return max
  # code ends here


# input
keyboards = [3, 1]
drives = [5, 2, 8]
b = 10

# output
start = time.time()
print(getMoneySpent(keyboards, drives, b))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')