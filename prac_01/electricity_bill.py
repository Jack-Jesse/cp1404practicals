"""
electricity bill
CP1404/CP5632 - Practical
A program that estimates the electricity bill
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
VALID_TARIFF_CHOICE = [11, 31]

print("Electricity Bill Estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
while tariff_choice not in VALID_TARIFF_CHOICE:
    print("Invalid tariff choice")
    tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in KWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff_choice == 11:
    estimated_bill = (TARIFF_11 * daily_use) * number_of_billing_days
else:
    estimated_bill = (TARIFF_31 * daily_use) * number_of_billing_days
print(f"{estimated_bill:.2f}")
