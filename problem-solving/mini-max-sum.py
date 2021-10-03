import time


def miniMaxSum(arr):
  # code starts here
  possbile_sums = []

  for i in range(0,len(arr)):
    possbile_sums.append(sum(arr)-arr[i])

  print(str(min(possbile_sums)) + ' ' + str(max(possbile_sums)))
  # code ends here


# input
input_array = [1,3,5,7,9]

# output
start = time.time()
miniMaxSum(input_array)
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')