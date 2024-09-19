# get loan amount, annual interest rate, and loan duration in years
# then get the monthly interest rate from the annual interest rate
# then calculate the loan duration in months
# then calculate the monthly payment using the formula

while True:
    try:
        loan_amount = float(input("Enter loan amount: "))
        break
    except ValueError:
        print("Invalid loan amount. Please enter a valid amount.")

while True:
    try:
        annual_interest_rate = float(input("Enter annual interest rate"
                                           "(5 not 0.05, "
                                           "10 not 0.1, etc): "))
        break
    except ValueError:
        print("Invalid annual interest rate. Please enter a valid rate.")

while True:
    try:
        loan_duration = float(input("Enter loan duration in years"
                                    "(2.5, 3.1, etc.): "))
        break
    except ValueError:
        print("Invalid loan duration. Please enter a valid duration.")

monthly_interest_rate = annual_interest_rate / 1200
loan_duration_months = loan_duration * 12

monthly_payment = loan_amount * (monthly_interest_rate /
                                (1 - 1 / (1 + monthly_interest_rate)
                                ** loan_duration_months))
print(f"Monthly payment: ${monthly_payment:.2f}")