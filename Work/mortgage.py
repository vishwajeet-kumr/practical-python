# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000
extra_payment_start = input ("extra_payment_start: ")
extra_payment_end = input("extra_payment_end: ")

while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    if payment > principal:
            payment = principal
    total_paid = total_paid + payment
    
    if months >= int(extra_payment_start) and months <= int(extra_payment_end):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

print(months, round(total_paid, 2), round(principal, 2))
print (f'{months} months take to pay {total_paid:0.2f} with principal {principal} ')


print('Total paid', round(total_paid, 2))
print('Months', months)

