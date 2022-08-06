# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

maxArr = []

def reverser(toReverse):
    reversedString = ""
    for counter in toReverse:
        reversedString = counter + reversedString
    return reversedString

def isPalindrome(testString):
    if testString == reverser(testString):
        # print(" Is palindrome")
        maxArr.append(testString)
    # else:
    #     print(" NOT a Palindrome")

# def largest(int_value):
#     max = 0
#     if int_value > max:
#         max = int_value
#     return max

first_counter = 100
while (first_counter < 1000):
    second_counter = 100
    while (second_counter < 1000):

        prod = 0

        # print(str(first_counter) + " X ", end="")
        # print(str(second_counter) + ": ", end="")
        prod = first_counter * second_counter
        # print(str(prod), end="")
        isPalindrome(str(prod))
        second_counter += 1

    # print() 
    first_counter += 1

# print(maxArr[-1])
# print(maxArr)
print(max(maxArr))


# Partial Solution 
# TODO see what is the largest number in the array by value and not by string