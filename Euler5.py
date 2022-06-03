# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

arrays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = 1
isRunning = True
print("Running...")
while(isRunning):
    if(number/all(array) % 2== 0 for array in arrays):
        print(number)
        number = number + 1
    else:
        number = number + 1
    isRunning = False