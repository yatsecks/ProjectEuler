number = 0
answer = 0

while number < 1000:
    if number % 3 == 0 or number % 5 == 0:
        answer = answer + number
        number = number + 1
    elif number % 5 == 0:
        answer = answer + number
        number = number + 1
    else:
        number = number + 1



print (answer)