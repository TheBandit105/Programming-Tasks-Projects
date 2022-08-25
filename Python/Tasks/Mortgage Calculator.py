# Ask user to input the amount of loan they wish to borrow.
loanAmount = float(input("Enter loan amount to borrow: £"))
print('\nLoan amount L = £%.2f' % loanAmount)

# Ask the user to input the current interest rate that they are going by.
interestRate = float(input("\nEnter the interest rate on loan(%): "))
print('\nThe interest rate is i = ', interestRate/100)
print('Which is', interestRate,'%')

# Ask the user how many years they need to pay off the loan they borrowed. 
yearsPayLoan = float(input("\nNumber of years needed to pay off loan: "))
print('\nThe number of years needed to pay off loan is y = %.2f years' % yearsPayLoan)

# Based on the number of years the user needs to pay off the loan, 
# the number of payments in 1 year can be calculated.
paymentNumber = yearsPayLoan * 12
print('\nTherefore, since payments are once per month, number of payments is ', yearsPayLoan, ' * 12 = ', paymentNumber)  

# Using the loan amount, interest rate and the number of payments in 1 year, the monthly
# payments can be calculated.
monthlyPayment = loanAmount * interestRate *(1 + interestRate) * paymentNumber/((1 + interestRate)* paymentNumber - 1) 
print('\nThe calculated monthly payments are £%.2f per month.' % monthlyPayment)
