# Based on the opinion you will only live 90 years
# calculate the number of weeks remaining
age = input("Enter your age:\n")
year90_weeks = 90 * 52
age_int = int(age)
age_in_weeks = age_int * 52
weeks_left = year90_weeks - age_in_weeks
print(f"You have {weeks_left} weeks left.")

## Solution
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
