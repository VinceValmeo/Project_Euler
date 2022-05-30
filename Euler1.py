# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

print("fgfgfd")
counter = 0
sum = 0
while counter < 1000:
    if(counter % 3 == 0 or counter % 5 == 0):
        print(counter)        
        sum = counter + sum
    counter += 1
print(sum)
print("FINISHED")
    