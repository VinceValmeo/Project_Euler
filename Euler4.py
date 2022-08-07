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
        # print(" NOT a Palindrome")

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

# Prints the last item on the array, it does not mean that it is the largest
# print(maxArr[-1])             

#Prints the largest string value, outputs 99999
# print(max(maxArr))

# Converts the string items to integers and prints the largest value on the array.
result = [int(item) for item in maxArr]
print(max(result))
