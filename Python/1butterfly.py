# Waqas Bhatti Com-250

f = open("butterFly_T2.csv", 'r')
ddf = f.read()  #open connection    
f.close()       #close connection

dds = ddf.split('\n')


ttg = []       #format data

for i in dds:
    pts = i.split(",")
    ttg.append ( [ pts[0], int(pts[1]) ] )

count = 0

#list of butterfly types
types = []      #empty list for butterflys
for i in ttg:                  
    if i[0] not in types:            #if not in types
        types.append(i[0])          #then add it in list
        count = count+ 1

print("There are " ,count, " different butterflies")

#making list with plane and total amount of butterflies
typesnum = [] 
for i in types:                     #for all types
    count = 0
    for n in ttg:                   #for all
        if n[0] in i:               # if n[0]=name is in the type we are on (i)
            count = count+ n[1]     #add hm times they show up
    typesnum.append( [count, i] )    #place into list showing name and hm times
    #print(f"{i : <25}{count : ^20}")
    

from operator import itemgetter
alpsorted = sorted(typesnum, key = itemgetter(1))      #alphabetically ordered
for i in alpsorted:
    print(i)

print('\n') 
numsorted = sorted(typesnum, key = lambda x : x[0],reverse=False)   #numerically ordered
for i in numsorted:
    print(i)
