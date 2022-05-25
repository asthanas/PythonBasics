def simple_interest(p,r,t):
    print("Principle is :", p)
    print("Rate of interest is : ",r)
    print("Time period is ",t)

    si=(p*r*t)/100

    print("Simple interest is : ",si)

    return si

simple_interest(5000,6,7)