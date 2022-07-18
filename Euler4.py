# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


first_num = 0
seconed_num = 0

test_number = 9009

counter = 0
while counter < len(str(test_number)):
    print(str(test_number)[counter])
    counter = counter + 1