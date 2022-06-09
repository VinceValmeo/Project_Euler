# counter = 1
# sum = 0
# myList =[]
# while counter <= 7:
#     print(counter)
#     sum = counter + sum
#     # print("This is SUM: " + str(sum))
#     myList.append(sum)
#     counter = counter + 1
 
# print("="*20)
# print("Total")
# print(sum)


# print("="*20)
# print("List of Sum")
# print(myList)

def getDivisible(number):
    i = 1
    factor = 0
    while i != number:
        if(number / i % 2 == 0):
            factor = i
            i = i + 1
            return print(factor)
        i = i + 1
    i = i + 1
number = 10
getDivisible(number)