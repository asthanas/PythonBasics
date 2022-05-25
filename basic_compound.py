# Python3 program to find compound
# interest for given values.

def compound_interest(principle,rate,time):
    amount=principle * (pow((1+rate/100),time))
    ci = amount-principle

    print("Compound interest id {0}".format(ci))

# Driver Code
compound_interest(5000,5,10)



