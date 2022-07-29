# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def reverser(toReverse):
    reversedString = ""
    for counter in toReverse:
        reversedString = counter + reversedString
    return reversedString

testString = "9009"

print("Original String: " + testString)
print("Reversed String: " + reverser(testString))


if testString == reverser(testString):
    print("Is palindrome")
else:
    print("NOT a Palindrome")
    
