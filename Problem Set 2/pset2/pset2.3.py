def remainingBal(balance, annualInterestRate, monthlyPayment):
        months_left = 12
        while months_left > 0:
            monthlyIntRate = annualInterestRate/12
            upb = (balance - monthlyPayment)
            balance = upb + (upb * monthlyIntRate)
            months_left -= 1
        return balance

# test case
# balance = 281165
# annualInterestRate = 0.15

# define lower bound
floor = balance/12

# define upper bound
monthlyIntRate = annualInterestRate/12
ceiling = (balance * ((1 + monthlyIntRate) ** 12))/12

# what should your initial guess be?
# the below ran faster than guess = balance
guess = (ceiling + floor) / 2

while ceiling - floor > .1:
    testBalance = remainingBal(balance, annualInterestRate, guess)
    if testBalance <= 0:
        ceiling = guess
        guess = floor + (ceiling-floor)/2
    else:
        floor = guess
        guess = floor + (ceiling-floor)/2
# print(testBalance)
# print(floor, ceiling)
print('Lowest payment: ', round(guess,2))
