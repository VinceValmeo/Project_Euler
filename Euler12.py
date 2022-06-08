counter = 1
sum = 0
myList =[]
while counter <= 7:
    print(counter)
    sum = counter + sum
    # print("This is SUM: " + str(sum))
    myList.append(sum)
    counter = counter + 1
 
print("="*20)
print("Total")
print(sum)


print("="*20)
print("List of Sum")
print(myList)
