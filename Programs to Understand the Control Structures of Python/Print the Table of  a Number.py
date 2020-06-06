# Python program to Print a Table of Given Number

number = int(input("Enter a number "))
print("TABLE OF ",number)
for i in range(1,11):
    print("{} * {} = {} ".format(i,number,i*number))
'''
Enter a number 23
TABLE OF  23
1 * 23 = 23 
2 * 23 = 46 
3 * 23 = 69 
4 * 23 = 92 
5 * 23 = 115 
6 * 23 = 138 
7 * 23 = 161 
8 * 23 = 184 
9 * 23 = 207 
10 * 23 = 230 
'''