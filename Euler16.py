# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
import math

counter = 0
sum = 0
base = 2
power = 1000
answer = math.pow(base,power)
intAnswer = str(int(answer))

while counter < len(intAnswer):
    # print(intAnswer[counter])
    sum = sum + int(intAnswer[counter])
    counter = counter + 1

print(sum)
