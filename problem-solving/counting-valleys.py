import time


def countingValleys(n, s):
  # code starts here
  level = 0
  valley = 0

  for step in s:
      if level == 0 and step == 'D':
          valley += 1
      if step == 'U':
          level += 1
      else:
          level -= 1
  
  return valley
  # code ends here


# input
n = 8
s = 'UDDDUDUU'

# output
start = time.time()
print(countingValleys(n, s))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')