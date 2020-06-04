# Python Program to calculate Simple Interest
'''
Formula : A = P (1 + rt)
A	= 	final amount
P	= 	initial principal balance
r	= 	annual interest rate
t	= 	time (in years)
'''
p= int(input("Enter Initial Principle Balance "))
r = float(input("Enter annual interest rate "))
t= int(input("Enter time (in years) "))
A = p* (1+r*t)
print("Final Amount ",A)


'''
Enter Initial Principle Balance 3000
Enter annual interest rate 0.05
Enter time (in years)4
Final Amount  3600.0
'''