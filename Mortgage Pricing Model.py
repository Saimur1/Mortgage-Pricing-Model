
import numpy as np

def calculate_monthly_payment(principal, annual_rate, term_years):
    """
    Calculate the monthly mortgage payment.

    :param principal: The loan amount (principal).
    :param annual_rate: The annual interest rate in percentage.
    :param term_years: The loan term in years.
    :return: Monthly mortgage payment.
    """
    monthly_rate = (annual_rate / 100) / 12  # Convert annual rate to monthly and percentage to decimal
    num_payments = term_years * 12  # Total number of payments over the loan term

    # Amortization formula
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                      ((1 + monthly_rate) ** num_payments - 1)
    return monthly_payment


# Example Usage
principal = 300000  # $300,000 loan
annual_rate = 3.5  # 3.5% interest rate
term_years = 30  # 30-year mortgage

monthly_payment = calculate_monthly_payment(principal, annual_rate, term_years)
print(f"Monthly Payment: ${monthly_payment:.2f}")

def calculate_return_on_equity(principal, down_payment, annual_rate, term_years, expenses):
    """
    Calculate the Return on Equity (ROE) for the mortgage.

    :param principal: The loan amount (principal).
    :param down_payment: The amount of the down payment.
    :param annual_rate: The annual interest rate in percentage.
    :param term_years: The loan term in years.
    :param expenses: Annual operating expenses for managing the mortgage.
    :return: The ROE as a percentage.
    """
    monthly_payment = calculate_monthly_payment(principal, annual_rate, term_years)

    # Total income from interest (ignoring principal repayment for simplicity)
    total_interest_paid = monthly_payment * 12 * term_years - principal
    annual_interest_income = total_interest_paid / term_years

    # Annual Net Income = Annual Interest Income - Expenses
    annual_net_income = annual_interest_income - expenses

    # Equity Invested = Down Payment
    equity_invested = down_payment

    # ROE = (Annual Net Income / Equity Invested) * 100
    roe = (annual_net_income / equity_invested) * 100
    print(f"The return on equity is: {roe}")
    return roe

calculate_return_on_equity(300000, 10000, 3.5, 30, 5000)