import time
from typing import Counter


def birthdayCakeCandles(candles):
  # code starts here
  c = dict(Counter(candles))
  return max(c.values())
  # code ends here


# input
input_array = [4,4,1,3]

# output
start = time.time()
print(birthdayCakeCandles(input_array))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')