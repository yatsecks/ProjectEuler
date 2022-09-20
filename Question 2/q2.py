nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
sum = 0

#why would anyone put zero
if nterms <= 0:
   print("Please enter a positive integer")
else:
   while n1 < nterms:
       if n1 % 2 == 0:
           sum = sum + n1
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth

print ("the sum of the even numbers is", sum)