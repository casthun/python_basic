def pay(wage, hours):
    # Calculate weekly pay with time-and-a-half for overtime
    if hours <= 40:
        amount = wage * hours
    else:
        amount = (wage * 40) + ((1.5)* wage * (hours - 40))
    return amount

def futureValue(p, r, m, t):
    # Find the future value of a savings account deposit
    # p principal, the amount deposited
    # r annual rate of interest in decimal form
    # m number of times interest is compounded per year
    # t number of years    
    i = r/m
    n = m * t
    amount = p * ((1+i)**n)
    return amount 
