import time


def sockMerchant(n, ar):
  # code starts here
  sorted_ar = sorted(ar, key = int)
  iter = 0
  pair = 0
  
  while iter < n-1:
      if sorted_ar[iter] == sorted_ar[iter+1]:
          pair += 1
          iter += 2
      else:
          iter += 1
    
  return pair
  # code ends here


# input
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# output
start = time.time()
print(sockMerchant(n, ar))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')