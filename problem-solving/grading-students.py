import time
import math


def gradingStudents(grades):
    # code starts here
    results = []
    for grade in grades:
        multiple = math.ceil(grade/5) * 5
        if grade < 38 or (multiple - grade) >= 3:
            results.append(grade)
        elif (multiple - grade) < 3:
            results.append(multiple)
            
    return results
    # code ends here


# input
input_array = [4,73,67,38,33]

# output
start = time.time()
print(gradingStudents(input_array))
end = time.time()
print(f'Time Elapsed: {abs(end-start)}')