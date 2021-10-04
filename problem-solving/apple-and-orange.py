import time


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0
    
    for d in apples:
        if s <= a+d <= t:
            apples_on_house += 1
    
    for d in oranges:
        if s <= b+d <= t:
            oranges_on_house += 1
    
    print(apples_on_house)
    print(oranges_on_house)


# input
s = 7
t = 11
a = 5
b = 15
apples = [-2,2,1]
oranges = [5,-6]

# output
start = time.time()
countApplesAndOranges(s, t, a, b, apples, oranges)
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')