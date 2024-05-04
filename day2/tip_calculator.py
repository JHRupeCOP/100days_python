#!/usr/bin/python3

print("Welcome to the tip calculator!")
bill_amount = float(input("What as the total bill?\n"))
tip = int(input("What percentage of tip would you like to give? 10, 12, 15? \n"))
tip_percent = tip / 100 + 1 
split_num = int(input("How many people to split the bill?\n"))

total_w_tip = bill_amount * tip_percent
person_owed = round(total_w_tip / split_num, 2)

print(f"Each person owes: ${person_owed:.2f}")
