import time


def divisibleSumPairs(n, k, ar):
  # code starts here
  num_pairs = 0
  
  for i in range(0, n):
      for j in range(i+1, n):
          if (ar[i]+ar[j])%k == 0:
              num_pairs += 1
  
  return num_pairs
  # code ends here


# input
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]

# output
start = time.time()
print(divisibleSumPairs(n, k, ar))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')