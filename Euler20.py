# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from math import factorial

number = 100
sum = 0
factorialed = str(factorial(number))
counter = 0
arr = []
# print("Total characters of the factorialed: "  + str(len(factorialed)))
# while counter <= len(factorialed):
#     sum = sum + int(factorialed[counter])
#     counter = counter + 1

for counter in str(len(factorialed)):
    arr.append(factorialed)


print(arr)
