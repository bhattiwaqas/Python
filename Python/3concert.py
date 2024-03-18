# Waqas Bhatti Com-250

import numpy as np
import array as arr
array = np.loadtxt("concert_dns.txt", dtype=int)        #original array


sarray = array.reshape(320,40)                #320 rows by 40 seats/columns

print("The average donation for all attendees is $",round( np.mean(sarray) , 2) )

no0 = []                                #create empty list to store non 0 values
for i in array:
    if i!=0:
        no0.append(i)
print("\nThe average donation for all donations is $",round(np.mean(no0) , 2) )


print('\n', np.average(sarray, axis=1) )             #avg of rows
print('\n', np.average(sarray, axis=0 ) )            #avg of columns


#gives index of row with the largest.
#assumming there is no row 0:
#we want row number not index. so +1 
print("\nThe", np.sum(sarray,axis=1).argmax() +1, "th row had the most donations" )
#gives index of row with the least sum:
print("\nThe", np.sum(sarray, axis=1).argmin() +1, "th row had the least donations")


count = 0                   #empty counter to find # of donations more than 210
for i in array:                     
    if i>210:
        count = count+1
print('\n')
print(count, "donors gave more than $210")
        
