def primes(n):
    sieve = [True] * n
    for j in xrange(3,int(n**0.5)+1,2):
        if sieve[j]:
            sieve[j*j::2*j]=[False]*((n-j*j-1)/(2*j)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

print sum(primes(2000000))
