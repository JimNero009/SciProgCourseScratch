#Add the 2 previous numbers
def fibseq(twotermsback, onetermback):
    newterm = twotermsback + onetermback
    return newterm

#Start the sequence
fib = [1,1]

#Keep appending numbers until we get too large 
while True:
    if fibseq(fib[len(fib) - 2], fib[len(fib) - 1]) <= 4000000:
        fib.append(fibseq(fib[len(fib) - 2], fib[len(fib) - 1]))
    else:
        break

#Now loop through and add together all even terms
sum = 0

for element in fib:
    if(element % 2 == 0):
        sum = sum + element

#Display sum
print sum
