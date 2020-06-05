# Python program to check whether a number is prime number

# 2,3,5,7,11,13,17,19

number = int(input("Enter a number "))
one =1
if(number<=1):
    print("Enter number greater than 1")
else:
    for i in range(2,number):
        if(number%i)==0:
            print(number ," is not a Prime ")
            break
    else:
        print(number," is Prime Number")

'''
Test Case 1
Enter a number 1
Enter number greater than 1

Test Case 2
Enter a number 2
2  is Prime Number

Test Case 3
Enter a number 7
7  is Prime Number

Test Case 4
Enter a number 10
10  is not a Prime 
'''