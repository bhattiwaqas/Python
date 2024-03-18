#test script

sheIs= 'the one and only '
ga = 'Lady Gaga'

ts = 'Taylor Slow'
print(sheIs + ts)

f = open("shirts_shipM3Jb", 'r' ) #open file for reading. connection
ddt = f.read()

#now have data as one single string

# want list of list str int str

ttg=[] # empty list

#ddt = one single string line
dds = ddt.split('\n') # split into lists wherever there is new line
#'green, 3, WI'
#now change into right format

for i in dds : #for every string in dds
    pts = i.split(',') # split into 3 parts
    newL =[ pts[0], int(pts[1]), pts[2] ] #turn numbers into int
    # [color, number_shirts, state]
    ttg.append(newL)        #save order record


count = 0 #number of shirts shipped
#print all red shirts
for i in ttg : #for every order
    if i[0] == 'red' : #if red
        count = count + i[1] #add all number of shirts if red

print("we have", count,"red shirts" )


#get a list of all different colors
sColors=[] #empty list of all different colors
#check each shipment- if color is not on color list - append it.
#if color is on color list, dont add it

for i in ttg : #for every order
    if i[0] not in sColors: #if color is not in list
        sColors.append( i[0] )

for i in sColors:                #for every color
    count = 0                    #reset counter
    for n in ttg:                #check through every order
        if n[0] == i:            #if color is the color we are in the loop of, then:
            count = count + n[1] #add all of that colors shirts
            
    print('You have', count, i, "shirts")              #print current color and shirt count before moving to next
    
       


print("call gaga for dinner")


