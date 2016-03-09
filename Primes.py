def primefactors(x):
    factorlist=[]
    loop=2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            factorlist.append(loop)
        else:
            loop += 1
    return factorlist

print primefactors(600851475143)
print primefactors(6857)
