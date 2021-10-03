import time


def simpleArraySum(ar):
    # code starts here
    return sum(ar)
    # code ends here


# input
input_array = [1,3,2,6,3]

# output
start = time.time()
print(f'Sum of array: {simpleArraySum(input_array)}')
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')