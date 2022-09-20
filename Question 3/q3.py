bigNum = 600851475143
num = 2
answer = 0
loop = 0
realAns = 0

while loop == 0:
    answer = bigNum/num
    realAns = num
    if (answer).is_integer() and answer*answer<bigNum and bigNum % answer == 0:
        loop = 1
    else:
        num = num + 1

print (realAns)

#failed this