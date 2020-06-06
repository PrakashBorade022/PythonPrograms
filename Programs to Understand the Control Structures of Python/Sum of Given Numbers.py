# Python Program to Print Sum of n given numbers
sum =0
n = int(input("Enter value of n "))

for i in range(1,n+1):
    sum +=i
print("Sum of first {} numbers is {} ".format(n,sum))

# Test Case 1
'''
Enter value of n 5
Sum of first 5 numbers is 15 
'''
# Test Case 2
'''
Enter value of n 10
Sum of first 10 numbers is 55 
'''