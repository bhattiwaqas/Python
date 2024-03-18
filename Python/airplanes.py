# how many planes, longest flight, shortest flight, what plane flew the longest flight, average flight time, which plane had the most number of flights


f = open("AirTaylor2", 'r') # open file
ddf = f.read()
f.close()

dds = ddf.split('\n')

ttg = []

for i in dds:
    pts = i.split(',')
    ttg.append( [pts[0],float(pts[1])] )

count = 0

planes = [] #empty list for planes

for i in ttg: #for every flight
    if i[0] not in planes: #if the id is not in planes,
        planes.append(i[0])#then add it to planes
        count = count + 1  #count how many different planes

print('There are', count,'planes')
print(planes)

#making list with plane and the total number of flights for each of those planes
planesnum = []
for i in planes:
    count = 0
    for n in ttg:
        if n[0] in i:
            count = count+1
    #print(i,count)
    planesnum.append( [i,count] )

from operator import itemgetter
print(sorted(planesnum, key = itemgetter(1)))

#loop that prints total number of flights for all planes:
totalflights = 0
for i in planesnum:
    totalflights = totalflights + i[1]
print("There were a total of", count, "flights")

#similar to before, we will now find planes and total time for each plane
planestime = []
for i in planes:
    count = 0
    for n in ttg:
        if n[0] in i:
            count = count+n[1]
    #print(i,count)
    planestime.append( [i,count] )
    
print(sorted(planestime, key = itemgetter(1)))

#loop that gives us total time for all planes
totaltime = 0
for i in planestime:
    totaltime = totaltime+n[1]
print(totaltime)
    



