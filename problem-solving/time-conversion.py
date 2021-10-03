import time


def timeConversion(s):
  # code starts here
  ap = s[-2:]
  h = int(s[:2])
  m = s[3:5]
  s = s[6:8]
  
  if h == 12 and ap == 'AM':
    h = '00'
  elif h == 12 and ap == 'PM':
    h = '12'
  elif ap == 'PM' and h < 12:
    h += 12
  elif h < 10:
    h = str(f'0{h}')
  
  return (str(h)+':'+str(m)+':'+str(s))

  # code ends here


# input
h12 = '12:45:54PM'

# output
start = time.time()
print(timeConversion(h12))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')