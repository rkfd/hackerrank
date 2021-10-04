import time


def catAndMouse(x, y, z):
  # code starts here
  d_xz = abs(x-z)
  d_yz = abs(y-z)

  if d_xz == d_yz:
    return 'Mouse C'
  elif d_xz < d_yz:
    return 'Cat A'
  elif d_xz > d_yz:
    return 'Cat B'
  # code ends here


# input
x = 1
y = 2
z = 3

# output
start = time.time()
print(catAndMouse(x, y, z))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')