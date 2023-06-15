"""Write a program to calculate the total bill tax amount for a list of billing amounts passed as an array of long integers.
upto the amount of 1000, there is no tax applicable, subsequently, a flat tax of 10% is applicable for the remaining amount as per the tax rate.
Note:- All calculations and results should be integer based ignoring fractions.
"""
def calculateTotalBillTax(billing_amounts):
    total_tax_amount = 0

    for amount in billing_amounts:
        if amount > 1000:
            tax_amount = int((amount - 1000) * 0.1)  # Flat tax rate of 10% for the remaining amount
            total_tax_amount += tax_amount

    return total_tax_amount

# Example usage:
billing_amounts = [500, 1200, 800, 1500]
total_tax = calculateTotalBillTax(billing_amounts)
print("Total Bill Tax Amount:", total_tax)
