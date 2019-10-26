#! python 3
# towerOfHanoi.py - Displays the steps to solve the Tower of Hanoi
# Created by Varun R. Gupta

def solver(n, f, t, u):
    if n == 1:
        print("Please shift Disk 1 from Rod %s to Rod %s" %(f, t))
        return
    solver(n-1, f, u, t)
    print("Please shift Disk %d from Rod %s to Rod %s" %(n, f, t))
    solver(n-1, u, t, f)

while True:
    n = input("Please enter the number of disks - ")
    print()
    try:
        n = int(n)
        break
    except ValueError:
        print("Please enter a valid integer")
        continue
    if n < 1:
        print("Please enter a valid integer greater than 1")

solver(n, 'F', 'T', 'U')

print("\nTotal number of moves =", (2 ** n) - 1)

input()
