import time


def getTotalX(a, b):
  #code starts here
  numbers = []
  for number in range(a[-1],b[0]+1):
      aList = False
      bList = False
      temp = []
      
      [temp.append(True) if number%a_ == 0 else temp.append(False) for a_ in a]
      if all(i for i in temp):
          aList = True

      temp = []
      [temp.append(True) if b_%number == 0 else temp.append(False) for b_ in b]
      if all(i for i in temp):
          bList = True

      if aList and bList:
          numbers.append(number)
      
  return len(numbers)
  # code ends here


# input
a = [2,4]
b = [16,32,96]

# output
start = time.time()
print(getTotalX(a,b))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')