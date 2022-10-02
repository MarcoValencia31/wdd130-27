"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
user_age=input("What is your age? ")
maximum_heart_rate=220-int(user_age)
print(maximum_heart_rate)
min_percentage=65/100*int(maximum_heart_rate)
max_percentage=85/100*int(maximum_heart_rate)
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_percentage:0f} and {max_percentage:0f} beats per minute.")
