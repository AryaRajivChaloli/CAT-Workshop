#! python 3
# sortedMatrixFinder.py - Finds a given element in a randomly generated
# sorted matrix.
# Created by Varun R. Gupta

import random

while True:
    row = input("Please enter the number of rows in the matrix - ")
    try:
        row = int(row)
        break
    except ValueError:
        print("Please enter a valid integer")
        continue
    if row < 1:
        print("Please enter a valid integer greater than 1")

while True:
    col = input("Please enter the number of columns in the matrix - ")
    try:
        col = int(col)
        break
    except ValueError:
        print("Please enter a valid integer")
        continue
    if col < 1:
        print("Please enter a valid integer greater than 1")

a = [[]]

a[0].append(random.randint(1, 10))
a.append([])

for i in range(1, row):
    tmp = random.randint(1, 10) + a[i-1][0]
    a[i].append(tmp)
    a.append([])

for j in range(1, col):
    tmp = random.randint(1, 10) + a[0][j-1]
    a[0].append(tmp)

for i in range(1, row):
    for j in range(1, col):
        tmp = random.randint(1, 10) + a[i-1][j]
        while not (tmp > a[i][j-1]):
            tmp += random.randint(1, 10)
        a[i].append(tmp)

print("\nGenerated Matrix:")

for i in range(0, row):
    for j in range(0, col):
        print(a[i][j], end = "\t")
    print()

while True:
    ele = input("\nPlease enter the element to be searched for - ")
    try:
        ele = int(ele)
        break
    except ValueError:
        print("Please enter a valid integer")

i = 0
j = col-1
check = 0

while i < row and j >= 0:
    if a[i][j] == ele:
        print("\nThe element %d has been found at location a[%d][%d]." %(ele, i, j))
        check = 1
    if a[i][j] > ele:
        j -= 1
    else:
        i += 1

if check == 0:
    print("\nThe element", ele, "is not present in the matrix.")

input()
