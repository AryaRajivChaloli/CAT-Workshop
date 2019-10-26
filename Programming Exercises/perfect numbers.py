#Perfect square
n=int(input('Enter a number : '))
i=1
s=0
while (i*i)<n:
    if n%i==0:
        s=s+i+(n/i)
    i=i+1
if (i*i)==n:
    s=s+i
s=s-n
if s==n:
    print'perfect square'
else:
    print'not a perfect square'
