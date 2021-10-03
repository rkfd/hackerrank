import time


def staircase(n):
  # code starts here
  for i in range(0,n):
    print(' '*(n-i-1)+'#'*(i+1))
  # code ends here


# input
n = 6

# output
start = time.time()
staircase(n)
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')