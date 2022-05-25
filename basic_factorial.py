num = int(input("Enter number for which factorial is required :"))
x = num
fact = 1
while (num > 1):
    fact = fact* num
    num = num -1
print("factrial of number {0} is {1}".format(x,fact))