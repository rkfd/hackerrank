import time


def compareTriplets(a, b):
  # code starts here
  results = [0,0]
  for i in range(0,len(a)):
    if a[i] > b[i]:
      results[0] += 1
    elif a[i] < b[i]:
      results[1] += 1
  
  return results
  # code ends here


# input
a = [1,3,5]
b = [2,1,4]

# output
start = time.time()
print(f'Results: {compareTriplets(a,b)}')
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')