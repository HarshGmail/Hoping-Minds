"""Q1. Mr. Kapil singh is a software eng. And he pays annual income tax as per the conditions.
Income                             	tax
4lc-7lc                               	no tax
7lc – 10 lc                             5% on first exceeding 7 lcs
10lc-14lc                           	10% on exceeding 10 lcs
14lc – 18lc                         	15% on exceeding 14 lcs
>18lcs                               	25% on exceeding 18 lcs
"""
def calculate_income_tax(income):
    if income <= 400000:
        tax = 0
    elif income <= 700000:
        tax = (income - 400000) * 0.05
    elif income <= 1000000:
        tax = 15000 + (income - 700000) * 0.1
    elif income <= 1400000:
        tax = 55000 + (income - 1000000) * 0.15
    else:
        tax = 155000 + (income - 1400000) * 0.25

    return tax


# Example usage:
annual_income = 1200000
income_tax = calculate_income_tax(annual_income)
print(f"The income tax for Mr. Kapil Singh is: {income_tax}")
