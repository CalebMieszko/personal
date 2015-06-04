#This will display your monthly progress at paying off your debts over the course of one year if you pay a fixed amount every month, and will display the amount you paid for the 
#year and how much interest accrued for the year.  
print chr(27) + "[2J" #this ANSI escape code clears the screen without resetting the cursor position
balance = float(raw_input('Enter the remaining balance of your debt: '))
annualInterestRate = float(raw_input('Enter the annual interest rate of your debt as a decimal: '))
monthlyPaymentRate = 0.20
monthlyInterestRate = annualInterestRate / 12.0
paidTotal = 0

for month in range(0, 12):
    payment = monthlyPaymentRate * balance #set to monthlyPaymentRate * balance, this finds min pmt/mo progress, set to an int/float display progress at that #
    paidTotal += payment
    monthlyUnpaidBalance = balance - payment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    print('Month: {}\nMinimum monthly payment: {}\nRemaining balance:{}\n'.format(month, round(payment, 2), round(balance, 2)))

print('Total paid: ' +str(round(paidTotal, 2)))
print('Remaining balance: ' +str(round(balance, 2)))
