import time


def aVeryBigSum(ar):
  # code starts here
  return sum(ar)
  # code ends here


# input
input_array = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

# output
start = time.time()
print(f'A Very Big Sum: {aVeryBigSum(input_array)}')
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')