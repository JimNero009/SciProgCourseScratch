
sum = 0
for num in range(1,1000):
   if(num%3==0 or num%5==0):
      sum=sum+num

print "Sum of numbers between 1 and 1000 that are divisible by 3 or 5 is:"
print sum
