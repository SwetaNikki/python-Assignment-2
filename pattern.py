#Create the below pattern using nested for loop in Python.
#     *
#     **
#     ***
#     ****
#     *****
#     ****
#     ***
#     **
#     *

n=5;

# '*' in increasing order from 0 to 5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

# '*' in increasing order from 5 to 0
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
