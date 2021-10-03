import time


def solveMeFirst(a,b):
  # code starts here
  return a+b
  # code ends here


# input
num1 = int(input())
num2 = int(input())

# output
start = time.time()
res = solveMeFirst(num1,num2)
end = time.time()
print(res)
print(f'Time Elapsed: {abs(end-start)}')