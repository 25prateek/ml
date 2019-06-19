import numpy as np

print("enter the dimension tu you want")
n=int(input("enter the no. of rows"))
m=int(input("enter the no. of column"))

a=np.random.random_sample((n,m)) #get random variable
print(a)
np.savetxt('a1.txt',a)        #Saving the array to a file
np.loadtxt('a1.txt')
