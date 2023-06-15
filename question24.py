"""
Write a program to calculate the electricity bill of a customer while taking input from the user and print name of the customer, contact no., address, meter no.,new reading,current reading , old reading, meter rent,meter no.,  calculate bill depending upon the following conditions :  - 

Current reading(units)                           Charges(Rs.)                          Tax 
>1 & <100                                             .80 paise per unit                     2%
>100 & <300                                         Rs. 1 per unit                           5%
>300 & < 500                                        Rs. 1.20 per unit                      7%
>500 & <800                                         Rs. 2 per unit                           11%
>800 & <1200                                       Rs. 2.50 per unit                      15%
>1200                                                    Rs. 3.40 per unit                      18%

Meter rent is fixed at rs. 50

"""
def calculateElectricityBill():
    # Input customer details
    name = input("Enter customer name: ")
    contact_no = input("Enter contact number: ")
    address = input("Enter address: ")
    meter_no = input("Enter meter number: ")
    old_reading = float(input("Enter old reading (in units): "))
    current_reading = float(input("Enter current reading (in units): "))

    # Calculate units consumed
    units_consumed = current_reading - old_reading

    # Calculate charges based on units consumed
    if units_consumed > 1 and units_consumed < 100:
        charges_per_unit = 0.80
        tax_rate = 0.02
    elif units_consumed > 100 and units_consumed < 300:
        charges_per_unit = 1.00
        tax_rate = 0.05
    elif units_consumed > 300 and units_consumed < 500:
        charges_per_unit = 1.20
        tax_rate = 0.07
    elif units_consumed > 500 and units_consumed < 800:
        charges_per_unit = 2.00
        tax_rate = 0.11
    elif units_consumed > 800 and units_consumed < 1200:
        charges_per_unit = 2.50
        tax_rate = 0.15
    else:
        charges_per_unit = 3.40
        tax_rate = 0.18

    # Calculate bill amount
    bill_amount = units_consumed * charges_per_unit
    tax_amount = bill_amount * tax_rate
    total_amount = bill_amount + tax_amount + 50  # Adding meter rent of Rs. 50

    # Print customer details and bill amount
    print("\nCustomer Details:")
    print("Name:", name)
    print("Contact Number:", contact_no)
    print("Address:", address)
    print("Meter Number:", meter_no)
    print("Old Reading:", old_reading)
    print("Current Reading:", current_reading)
    print("\nBill Details:")
    print("Units Consumed:", units_consumed)
    print("Charges per Unit:", charges_per_unit)
    print("Bill Amount:", bill_amount)
    print("Tax Amount:", tax_amount)
    print("Total Amount:", total_amount)


# Call the function to calculate electricity bill
calculateElectricityBill()
