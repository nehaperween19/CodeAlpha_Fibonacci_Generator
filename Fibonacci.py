num1 = 0
num2 = 1
num = int(input("Enter a number to obtain Fibonacci Series"))

if num == 1:
    print(num1)
else:
    print(num1)
    print(num2)
    for i in range (1,num+1):
        c = num1 + num2
        num1 = num2
        num2 = c
        print(c)