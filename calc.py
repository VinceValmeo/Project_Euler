fnum = input("Input First number: ") 
snum = input("Input second number: ") 

print("""
0 - add
1 - subtract 
2 - multi
3 - divide

""")
operation = input("Input operation") 

sum = int(fnum) + int(snum)
sub = int(fnum) - int(snum)
mul = int(fnum) * int(snum)
div = int(fnum) / int(snum)

if (operation == '0'):
    print(sum)
if (operation == '1'):
    print(sub)
if (operation == '2'):
    print(mul)
if (operation == '3'):
    print(div)