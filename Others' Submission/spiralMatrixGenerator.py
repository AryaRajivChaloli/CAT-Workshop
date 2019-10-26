#! python 3
# spiralMatrixGenerator.py - Creates a spiral matrix given dimensions
# Created by Varun R. Gupta

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

for i in range(0, row):
    for j in range(0, col):
        a[i].append(0)
    a.append([])

direc = "U"
n = row*col
l = 0
RR = 0
DC = col - 1
LR = row - 1
UC = 0

while l != n:
    if direc == "U":
        r = RR
        RR += 1
        for c in range(0, col):
            if a[r][c] == 0:
                a[r][c] = l + 1
                l += 1
        direc = "R"
    elif direc == "R":
        c = DC
        DC -= 1
        for r in range(0, row):
            if a[r][c] == 0:
                a[r][c] = l + 1
                l += 1
        direc = "D"
    elif direc == "D":
        r = LR
        LR -= 1
        for c in range(col-1, -1, -1):
            if a[r][c] == 0:
                a[r][c] = l + 1
                l += 1
        direc = "L"
    elif direc == "L":
        c = UC
        UC += 1
        for r in range(row-1, -1, -1):
            if a[r][c] == 0:
                a[r][c] = l + 1
                l += 1
        direc = "U"

for i in range(0, row):
    for j in range(0, col):
        print(a[i][j], end = "\t")
    print()

input()
