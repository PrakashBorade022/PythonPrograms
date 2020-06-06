# Python program to print sum of a first n even numbers

sum =0
n = int(input("Enter a value of n "))

for i in range(1,n+1):
    if i%2==0:
        sum+=i

print("Sum of first {} even numbers = {}".format(n,sum))
# Test case 1
'''
# 2+4+6+8+10 
Enter a value of n 10
Sum of first 10 even numbers = 30
'''
# Test Case 2
'''
#2,4
Enter a value of n 5
Sum of first 5 even numbers = 6
'''