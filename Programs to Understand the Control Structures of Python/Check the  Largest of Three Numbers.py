# Python Program to print largest of three given number

number1= int(input("Enter First Number "))
number2= int(input("Enter Second Number "))
number3= int(input("Enter Third Number "))
print(number1," ",number2," ",number3)
if number1> number2 and number1> number3:
    print(number1," is lergest ")
elif number2> number1 and number2>number3:
    print(number2," is lergest")
else:
    print(number3," is lergest")
'''
Enter First Number 300
Enter Second Number 400
Enter Third Number 90
300   400   90
400  is lergest
'''