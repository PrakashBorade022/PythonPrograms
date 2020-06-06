# Python Program to Understand Break,Pass and Continue
# Understanding Break
# suppose we have to stop a program when we reach to any condition

for i in range(1,10):
    print(i)
    if i ==3: #condition to stop loop
        print("we reach break")
        break
'''
1
2
3
we reach break
'''

# This code will not show  "division by zero" error
# Because we will continue the program if there is division by zero
# we can use pass or continue
lst = [1,0,3,0]
for i in lst:
    if i==0:
        continue
        # pass
    else:
        print(i/i)

'''
1.0
1.0
'''