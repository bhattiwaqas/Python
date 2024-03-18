f = open("balancesJ6.txt", 'r')
ddf = f.read()  #open connection    
f.close()       #close connection

import math
import statistics

dds = ddf.split('\n')

l1 = []                     #create list1 = l1
del dds[-1]                 #delete blank last element
for i in dds:
    l1.append(int(i))       #turn into an int list

l1.sort()                   #sorted list 1 into smallest to largest

print("We have", len(l1), "numbers") #display how many numbers

print("The smallest number is", l1[0])  #min
print("The largest number is", l1[-1])  #max
print("The sum is", sum(l1) )           #sum

avg = sum(l1) / len(l1)                 #average = sum/len
avg = round(avg, 3)
print("The average is", round(statistics.mean(l1),3) ) #use stat import to find mean or manually

print("The 271th number is", l1[270]) #271 num

print("The median is", round(statistics.median(l1),0) ) #median with stat import

print("The mode is", statistics.mode(l1) ) #mode with stat import

#l1[0:49] first 49 numbers
avg49 = sum(l1[0:49]) / len(l1[0:49]) #sum of first 49 / length of first 49
print("The average for the first 49 numbers is", round(avg49,3) ) #round to 3 places

std = statistics.stdev(l1)
std = round(std, 3)
print("The sample standard deviation is", str(std)) #sample standard deviation  

size = len(l1)
conv = math.sqrt( (len(l1) -1) / len(l1)) # sqrt( (n-1)/n)

print("The population standard deviation is", str(round(std*conv, 3))) #population standard deviation

print("***************************************************************************")
#                   Problem 2
print('\n               Problem 2 l2= first 320 numbers')
l2 = l1[0:320]      #create list of first 320 numbers
avgl2 = sum(l2) / len(l2) #avg = sum/len
print("The average is", round(avgl2,3) )        #print avg of list2 rounded to 3
print("The median is", statistics.median(l2) )  #print median
print("The mode is", statistics.mode(l2) )      #print mode

for i in l2:                                    #add 12 to all val under 187
    if i<187:
        i = i+12
for i in l2:                                    #subtract 32 for all val over 202
    if i>202:
        i=i-32
        
l2[0], l2[-1] = l2[-1], l2[0]       #swap last and first values with eachother

print("***********************************************************************"
)#                       Problem 3
print('\n               Problem 4 Array')
import numpy as np
array2 = np.loadtxt("balancesJ6.txt", dtype=int) 
print(array2)         #array we created
print(ddf)           #original list created

print('We have', len(array2), 'numbers in our array')
print("average is:", np.average(array2) )
print("max is", np.max(array2), "min is", min(array2) )
#This matches our values in our list but is much easier

count = 0                               #find num between 100-199
for i in array2:
    if (i>=100 and i<=199):
        count = count +1
print("There are", count, "numbers between 100 and 199")

print("The average of the first 128 values is", np.average(array2[0:128]) )

print("************************************************************************")
#                       Problem 4
print('\n               Problem 4 Array')
array2 = np.array(l2)       #convert l2 into array2
print("Length of array2 is", len(array2) )      #verify we have 320 numbers
print("The sum of array2 is", sum(array2), "and the sum of l2 is", sum(l2) )

print("****************************************************************************")
#                       Problem 5
print('\n               Problem 5 Array')
array3 = array2.reshape(32,10)              #array3 sorted in 32 rows,10 columns

sumrows = np.sum(array3,axis=1)
print("The sum of each row is", sumrows )         #sum of rows
sumcol = np.sum(array3, axis=0)
print("The sum of each column is", sumcol )     #sum of columns

np.sum(array3, axis=1).argmin()         #gives the index of the smallest sum

avgrows = np.average(array3, axis=1)
print("The average of each row is", avgrows )   #avg of rows
avgcol = np.average(array3, axis=0)
print("The average of each column is", avgcol )   #avg of columns

print("****************************************************************************")
#                       Problem 6
print('\n               Problem 6 Array')
array4 = array3[0:8, 0:6 ]                #top left 8 rows, 6 columns

array5 = array3[-5 :, -4: ]               #bottom right 5x4
#array5

