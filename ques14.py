def len_collatz(n):
	y = 0
	cnt=0
	while n!=1:
		if n%2==0:
			n=n/2
		else:
			n=3*n+1
		cnt+=1
	return cnt

max=0
x=0
for i in xrange(2,1000000):
	if len_collatz(i)>max:
		max=len_collatz(i)
		x=i
print x
