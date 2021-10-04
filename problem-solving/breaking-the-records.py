import time


def breakingRecords(scores):
  # code starts here
  min = max = scores[0]
  min_rec = 0
  max_rec = 0
  
  for score in scores:
      if score < min:
          min = score
          min_rec += 1
      elif score > max:
          max = score
          max_rec += 1
  
  return [max_rec, min_rec]
  # code ends here


# input
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

# output
start = time.time()
print(breakingRecords(scores))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')