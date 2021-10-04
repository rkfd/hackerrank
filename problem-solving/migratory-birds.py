import collections
import time
from typing import Counter


def migratoryBirds(arr):
  # code starts here
  category_dictionary = dict(Counter(arr))
  category_dictionary = collections.OrderedDict(sorted(category_dictionary.items()))
  return max(category_dictionary, key=category_dictionary.get)
  # code ends here


# input
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

# output
start = time.time()
print(migratoryBirds(s))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')