# Python program to print Prime Numbers Between 1  to 20

firstNumber =1
lastNumber =20
print("Prime Numbers Between 1 to 20 are :")
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
Prime Numbers Between 1 to 20 are :
2
3
5
7
11
13
17
19
'''


