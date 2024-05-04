# Calculate BMI
# forumla BMI=weight(kg)/height^2(m^2)

# 1st input: enter height in meters e.g: 1.65
height = input("Enter height in meters:\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter weight in kilograms:\n")

height_float = float(height)
weight_float = float(weight)

bmi = weight_float / height_float ** 2
print(int(bmi))


# Solution:
## height = input()
## weight = input()
## weight_as_int = int(weight)
## height_as_float = float(height)
## # Using the exponent operator **
## bmi = weight_as_int / height_as_float ** 2
## # or using multiplication and PEMDAS
## bmi = weight_as_int / (height_as_float * height_as_float)
## 
## bmi_as_int = int(bmi)
## print(bmi_as_int)
