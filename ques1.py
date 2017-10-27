a=[3*i for i in range(1,334)]
for j in range(1,200):
	a.append(5*j)
print sum(list(set(a)))

