def remainingBal(balance, annualInterestRate, monthlyPayment):
        months_left = 12
        while months_left > 0:
            months_left -= 1
            monthlyIntRate = annualInterestRate/12
            balance = (balance - monthlyPayment) + (balance * monthlyIntRate)
        return balance
#
# balance = 829
# annualInterestRate = 0.18

floor = 0
ceiling = balance
guess = balance

while ceiling - floor > 10:
    testBalance = remainingBal(balance,annualInterestRate, guess)
    if testBalance <= 0:
        ceiling = guess
        guess = floor + (ceiling-floor)/2
    else:
        floor = guess
        guess = floor + (ceiling-floor)/2

# print(testBalance)
# print(floor, ceiling)
print('Lowest payment: ', round(guess,-1))
