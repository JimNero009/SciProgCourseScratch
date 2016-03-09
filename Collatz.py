
def collatz(n):
    """Define the collatz sequence and return what that sequence is"""
    sequence = [n]
    while n != 1:
        if(n % 2 == 0):
            n = n / 2
            sequence.append(n)
        else:
            n = 3 * n + 1
            sequence.append(n)
    return sequence

#Now loop over all numbers and see which one gives the longest sequence

collatznum = 1
collatzlen = 1

for num in range(1,999999):
    res = collatz(num)
    if len(res) > collatzlen:
        collatznum = res[0]
        collatzlen = len(res)

print "Longest sequence is from: "
print collatznum
print "Which gives:"
print collatz(collatznum)
