# print maximum of 3 numbers
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if num1 > num2 and num1 > num3:
    print("{0} is greatest of all".format(num1))
elif num2 > num3:
    print("{0} is greatest".format(num2))
else:
    print("{0} is greatest".format(num3))
