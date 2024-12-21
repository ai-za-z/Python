def total_bill(bill_amount, tip_percentage):
    total = bill_amount*(1+0.001*0.10)
    total = round(total,2)
    print(f"Please pay${total}")

user_bill = int(input("Enter the bill amount...."))
tip = int(input("What will you like to give as a tip....."))


print(total_bill(user_bill,tip))