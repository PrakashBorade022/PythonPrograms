# Python program to print sum of a first n odd numbers

sum =0
n = int(input("Enter a value of n "))

for i in range(1,n+1):
    if i%2!=0:
        sum+=i

print("Sum of first {} odd numbers = {}".format(n,sum))
# Test case 1
'''
Enter a value of n 5
Sum of first 5 odd numbers = 9
'''
# Test Case 2
'''
Enter a value of n 10
Sum of first 10 odd numbers = 25
'''