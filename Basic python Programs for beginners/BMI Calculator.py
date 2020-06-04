# Python Program to calculate BMI
# BMI (Body Mass Index)
# Formula: weight (kg) / [height (m)]2
"""
Calculating your BMI is a popular and easy way to tell if your weight is putting your health at risk.
The higher the BMI, the greater the risk of developing health problems. The World Health Organization (WHO)
 regard a BMI of less than 18.5 as underweight and a BMI of 25 or more as overweight.

"""

weight = int(input("Enter Weight in kg "))
height = float(input("Enter Height in feet "))
# height = height*0.3048
BMI = weight /(height*height)
print("Your BMI",round(BMI,2))

'''
Enter Weight in kg 54
Enter Height in feet 1.66
Your BMI 19.6
'''

