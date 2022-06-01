import math

counter = 1
sumSquared = 0
squaredSum = 0
squaredSumAnswer = 0
difference = 0
while counter < 101:
    sumSquared = sumSquared + math.pow(counter,2)
    
    squaredSum = squaredSum + counter
    squaredSumAnswer = math.pow(int(squaredSum), 2)
    counter = counter + 1
    difference = squaredSumAnswer - sumSquared

print("Sum of Squared: " + str(int(sumSquared)))
print("Squared of Sum: " + str(int(squaredSumAnswer)))
print("Difference: " + str(int(difference)))
