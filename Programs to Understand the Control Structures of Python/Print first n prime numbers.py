# python programs to print first n prime numbers

firstNumber =1
lastNumber = int(input("Enter The Value of n "))
print("First {} Prime Numbers ".format(lastNumber))
while firstNumber<=lastNumber:

    for i in range(lastNumber+1):
        if i==lastNumber:
            firstNumber +=1

    # print("number now ", number)

    for j in range(2, lastNumber):
        if firstNumber!=j:
            if(firstNumber%j)==0:
                # print(number)
                break
    else:
        print(firstNumber)
'''
Enter The Value of n 15
First 15 Prime Numbers 
2
3
5
7
11
13
'''