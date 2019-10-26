#displaying all factors
n=int(input('Enter a number : '))
r=1
print 'The factors of ',n,' are:'
while r<=(n/2):
    if n%r==0:
        print r
    r=r+1
print n
    
