counter = 10
quotient = 0
limit = 2520
while (counter != limit and counter != 0):
    quotient = limit / counter
    if(quotient % 2 == 0 ):
        print(counter)

    counter = counter - 1