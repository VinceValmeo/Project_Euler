# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# first_num = 10

# while first_num > 0:
#     print("*" * first_num)
#     first_num = first_num - 1
# test_number = 9009
# arr_reverse = []
# arr = []

# counter = 0
# while counter < len(str(test_number)):
#     # print(str(test_number)[counter])
#     arr.append(str(test_number)[counter])
#     arr_reverse.append(str(test_number)[counter])

#     counter = counter + 1

# arr_reverse.reverse()
# print(arr_reverse)

# if arr_reverse == arr:
#     print("Palindrome")
# else:
#     print("NOT Palindrome")

myString = "Hello"

def reverser(toReverse):
    reversedString = ""
    for counter in toReverse:
        reversedString = counter + reversedString
    
    return reversedString

print("Original String: " + myString)

print("Reversed String: " + reverser(myString))