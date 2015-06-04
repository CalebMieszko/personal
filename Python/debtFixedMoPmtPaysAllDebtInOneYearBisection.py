#This will find the minimum fixed monthly payment necessary to completely pay off all debt in twelve months - but faster, by the power of bisection!
print chr(27) + "[2J" #this ANSI escape code clears the screen without resetting the cursor position
balance = float(raw_input('Enter the remaining balance of your debt: '))
annualInterestRate = float(raw_input('Enter the annual interest rate of your debt as a decimal: '))
potentialNecessaryPayment = 0
solved = False

def minimumNecessaryPayment(balance,annualInterestRate,payment):
    '''
    balance - the outstanding balance on the card, provided by the system
    annualInterestRate - the annual interest rate on the card, given by the system
    payment - the fixed amount of money paid for one month, to be repeated each month and discovered by this program
    '''
    month = 1
    while month <= 36:
        balance -=  potentialNecessaryPayment
        balance += (annualInterestRate/12.0)*balance 
        month += 1
    if balance <= 0:
        return potentialNecessaryPayment
    else:
        return False

while solved == False:
    if minimumNecessaryPayment(balance,annualInterestRate,potentialNecessaryPayment):
        solved = True
        print 'Lowest Payment:',minimumNecessaryPayment(balance,annualInterestRate,potentialNecessaryPayment)
    else:
        potentialNecessaryPayment += .01
        minimumNecessaryPayment(balance,annualInterestRate,potentialNecessaryPayment)