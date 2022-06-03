# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# arrays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = 1
isRunning = True
print("Running...")
while(isRunning):

    if(number/1 % 2== 0 and number/2 % 2== 0 and number/3 % 2== 0 and  number/4 % 2== 0 and  number/5 % 2== 0 and 
      number/6 % 2== 0 and  number/7 % 2== 0 and  number/8 % 2== 0 and  number/9 % 2== 0 and  number/10 % 2== 0 and  
      number/11 % 2== 0 and  number/12 % 2== 0 and  number/13 % 2== 0 and  number/14 % 2== 0 and  number/15 % 2== 0 and  
      number/16 % 2== 0 and  number/17 % 2== 0 and  number/18 % 2== 0 and  number/19 % 2== 0 and  number/20 % 2== 0 ):
        print(number)
        number = number + 1
        isRunning = False
    else:
        number = number + 1
    