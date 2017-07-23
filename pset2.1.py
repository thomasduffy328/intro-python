monthlyIntRate = annualInterestRate/12
monthlyPaymentRate = monthlyPaymentRate
months_left = 12

while months_left > 0:
    months_left -= 1
    balance = balance - (balance * monthlyPaymentRate)
    balance = balance + (monthlyIntRate * balance)
    if months_left == 0:
        break
print('Remaining balance: ' + str(round(balance, 2)))
