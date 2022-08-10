# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# f1 = 1
# f2 = 1
# temp = 0 

# num_array = [1 ,1 ]
# while f2 < 90:
#     temp = f1 + f2
#     f1 = f2
#     f2 = temp 
#     num_array.append(f2)
#     temp = 0

# print(num_array)
# print("Program Ended")

# # print(num_array[-1])
# print(index(num_array[4]))
# print(len(num_array))



testDig = 123456789

def digitCounter(number):
    counter = 0
    for i in str(testDig):
        counter = counter + 1

    print(counter)

digitCounter(testDig)