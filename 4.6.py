#!/usr/bin/python

# severance problem 4.6

def computepay():
    if hoursWorked > 40:
        overtimePay = (hoursWorked - 40) * payRate * 1.5
        regularPay = 40 * payRate
        grossPay = overtimePay + regularPay
    else:
        grossPay = hoursWorked * payRate
    return grossPay
hoursWorked = float(raw_input("Enter hours worked: "))
payRate = float(raw_input("Enter your payrate in ($ per hour): "))
paycheck = computepay()
print(paycheck)
