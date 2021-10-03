import time


def diagonalDifference(arr):
  # code starts here
  n = len(arr)
  ltor = 0
  rtol = 0
  
  for i in range(0,n):
    ltor += arr[i][i]
    rtol += arr[i][n-i-1]

  return abs(ltor-rtol)
  # code ends here


# input
input_array = [
  [1,2,3],
  [4,5,6],
  [9,8,9]
]

# output
start = time.time()
print(f'Diagonal Difference: {diagonalDifference(input_array)}')
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')