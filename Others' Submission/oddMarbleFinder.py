#! python 3
#  oddMarbleFinder.py - Program that accepts a marble number to be set as odd
#  and finds if it is heavier or lighter than 11 other similar marbles.
#  Created by Varun R. Gupta

marbleList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]                                               # Set of 12 Marble Weights
print("There are 12 marbles numbered from 1 to 12.\nOne of them should be odd.")

while True:
    inputNumber = input("Please mention which marble is to be set as an Odd Marble - ")         # Input of Random Marble Number
    try:
        oddMarble = int(inputNumber)
    except ValueError:
        print("Please enter a valid marble number between 1 and 12 (inclusive).")
        continue
    if oddMarble > 0 and oddMarble < 13:
        print("Thank you for entering a valid marble number.")
        break
    else:
        print("Please enter a valid marble number between 1 and 12 (inclusive).")
        continue

while True:
    inputState = input("Please enter whether the marble is heavier or lighter than the other marbles (H/L) - ").upper() # Input Marble State.
    if inputState.startswith('H') or inputState.startswith('L'):
        print("Thank you for entering a valid marble state.")
        break
    else:
        print("Please enter a valid option, (H)eavier or (L)ighter.")
        continue

if inputState.startswith('H'):                          # Assignment of User Defined Marble and Weight
    marbleList[oddMarble - 1] = 2
else:
    marbleList[oddMarble - 1] = 0.5

print("Dividing 12 balls into 3 sets.\nSet 1 - 1, 2, 3, 4\nSet 2 - 5, 6, 7, 8\nSet 3 - 9, 10, 11, 12")

print("\n(1) Weighing Set 1 and 2")

if sum(marbleList[:4]) == sum(marbleList[4:8]):         # 1st Try
    print("    Both Sets are found to be Equal")
    if sum(marbleList[:3]) == sum(marbleList[8:11]):    # 2nd Try
        print("(2) 12 is Heavier")
        resultNum = 12
        if marbleList[0] < marbleList[11]:              # 3rd Try
            resultState = 'Heavier'
        else:
            resultState = 'Lighter'
    elif sum(marbleList[:3]) > sum(marbleList[8:11]):   # Same way for each test
        print("(2) 8, 9, 10 are found to be Lighter")
        resultState = 'Lighter'
        if marbleList[8] == marbleList[9]:
            resultNum = 11
        elif marbleList[8] < marbleList[9]:
            resultNum = 9
        else:
            resultNum = 10
    else:
        print("(2) 8, 9, 10 are found to be Heavier")
        resultState = 'Heavier'
        if marbleList[8] == marbleList[9]:
            resultNum = 11
        elif marbleList[8] < marbleList[9]:
            resultNum = 10
        else:
            resultNum = 9
elif sum(marbleList[:4]) < sum(marbleList[4:8]):
    print("    Sets 1 is Lighter")
    if sum(marbleList[8:11])+marbleList[4] == marbleList[0]+sum(marbleList[5:8]):
        print("(2) 2, 3, 4 are found to be Lighter")
        resultState = 'Lighter'
        if marbleList[1] == marbleList[2]:
            resultNum = 4
        elif marbleList[1] < marbleList[2]:
            resultNum = 2
        else:
            resultNum = 3
    elif sum(marbleList[8:11])+marbleList[4] > marbleList[0]+sum(marbleList[5:8]):
        print("(2) 1, 5, 6, 7 are found to be Lighter")
        if marbleList[4] == marbleList[8]:
            resultNum = 1
            resultState = 'Lighter'
        else:
            resultNum = 5
            resultState = 'Heavier'
    else:
        print("(2) 1, 5, 6, 7 are found to be Heavier")
        resultState = 'Heavier'
        if marbleList[5] == marbleList[6]:
            resultNum = 8
        elif marbleList[5] < marbleList[6]:
            resultNum = 7
        else:
            resultNum = 6
else:
    print("    Sets 2 is Lighter")
    if sum(marbleList[8:11])+marbleList[0] == marbleList[4]+sum(marbleList[1:4]):
        print("(2) 6, 7, 8 are found to be Lighter")
        resultState = 'Lighter'
        if marbleList[5] == marbleList[6]:
            resultNum = 8
        elif marbleList[5] < marbleList[6]:
            resultNum = 6
        else:
            resultNum = 7
    elif sum(marbleList[8:11])+marbleList[0] > marbleList[4]+sum(marbleList[1:4]):
        print("(2) 1, 2, 3, 5 are found to be Heavier")
        if marbleList[0] == marbleList[8]:
            resultNum = 5
            resultState = 'Lighter'
        else:
            resultNum = 1
            resultState = 'Heavier'
    else:
        print("(2) 1, 2, 3, 4 are found to be Heavier")
        resultState = 'Heavier'
        if marbleList[1] == marbleList[2]:
            resultNum = 4
        elif marbleList[1] < marbleList[2]:
            resultNum = 3
        else:
            resultNum = 2

print("(3) Ball Number", resultNum, "is found to be", resultState)      #Final Print Call (Result)

input()
