two_digit_number = input("Enter a two digit number:\n")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
two_digit_str = str(two_digit_number)
digit_one_str = two_digit_str[0]
digit_two_str = two_digit_str[1]
print(int(digit_one_str) + int(digit_two_str))


# actual solution
# input is actually a string not integer 
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)
