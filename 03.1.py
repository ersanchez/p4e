#!/usr/bin/python

# computer gross pay

hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter the rate: "))

if hours >  40:
    overtime = hours - 40
    reg_pay = 40 * rate
    overtime_pay = overtime * 1.5 * rate
    print(reg_pay + overtime_pay)

else:
    gross = hours * rate
    print(gross)
