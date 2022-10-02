#week 2
from datetime import datetime
today=datetime.now()
day_of_week=today.weekday()
subtotal=float(input("Please enter the subtotal: "))
discount_subtotal=0.1*subtotal
sales_tax=None
total=None
if subtotal >=50:
    if day_of_week== 2 or 3:
        new_subtotal=subtotal-discount_subtotal
        sales_tax=0.06*new_subtotal
        total=new_subtotal+sales_tax
        #print(f"Discount amount: {discount_subtotal:.2f}")
        #print(f"Sales tax amount: {sales_tax:.2f}")
        #print("total: "+str(total))
    elif day_of_week != 2 or 3:
        sales_tax=0.06*subtotal
        total=subtotal+sales_tax      
elif subtotal <50:
    sales_tax=0.06*subtotal
    total= subtotal+sales_tax

print(f"Discount amount: {discount_subtotal:.2f}")
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"total: {total:.2f}")
