'''Write a Python Program to print the Fibonoci Series'''



def Fibonoci(n):
    # if n == 0 return 0, n == 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # return Fibonoci n-1, n-2
        return Fibonoci(n-1) +Fibonoci(n-2)
    
# print range
for i in range(0, 20):
    print(Fibonoci(i))