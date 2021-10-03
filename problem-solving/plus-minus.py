import time


def plusMinus(arr):
  # code starts here
  n = len(arr)
  pos = neg = neu = 0

  for i in arr:
    if i > 0:
      pos += 1
    elif i < 0:
      neg += 1
    else:
      neu += 1

  print(float(pos/n))
  print(float(neg/n))
  print(float(neu/n))
  # code ends here


# input
input_array = [1,1,0,-1,-1]

# output
start = time.time()
plusMinus(input_array)
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')