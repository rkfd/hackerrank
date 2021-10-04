import time


def bonAppetit(bill, k, b):
  # code starts here
  anna_amount_actual = (sum(bill)/2) - bill[k]/2
  amount_to_return = b - anna_amount_actual
  
  if amount_to_return > 0:
      print(int(amount_to_return))
  else:
      print('Bon Appetit')
  # code ends here


# input
bill = [3, 10, 2, 9]
k = 1
b = 12

# output
start = time.time()
bonAppetit(bill, k, b)
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')