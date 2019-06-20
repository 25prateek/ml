import numpy as np
a=np.arange(100,126,5) #take rows with diffrence 5
for i in a:
	j=i+80 # +80 because from 125 its goes on 200 not more than that value
	b=np.arange(i,j,5).reshape(8,2) # now arrange thatcoloumn an d rows with 5 diffrance in aaray is goes reshape for 8*2 matrix of that
	print(b)

