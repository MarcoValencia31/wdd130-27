from datetime import datetime, date
import math
add_text= open("volumes.txt", "a")
width=float(input("Enter the width of the tire in mm: "))
aspect=float(input( "Enter the aspect ratio of the tire: "))
diameter=float(input("Enter the diameter of the wheel in inches: "))
first_part= math.pi * (width)**2 * aspect 
parenthesis= width*aspect + (2540*diameter)
volume=first_part * parenthesis / 10000000000
print(f"The approximate volume is {volume:.2f} liters")

week=datetime.today()
current_time=datetime.now()
print(f"{current_time:%Y-%m-%d}")
price.tire=None

with open("volumes.txt", mode="at") as tire_file:    
    print(f"{current_time:%Y-%m-%d},{width},{aspect},{diameter},{volume:.2f}", file=tire_file)

with open("volumes.txt", mode="at") as tire_file:    
    if volume<50:
        print("It's possible that 2 persons can lift it")
    else:
        print("It's impossible that 2 persons can lift it")

if volume<30:
    price.tire=35

question=input("Do you want to buy the tire? ")
if question == "yes":
    number=input("What's your phone number: ") 
    with open("volumes.txt", "a") as tire_file:
        print(number, file=tire_file)
else:
    print("We hope see you later.")        

add_text.write(week)    