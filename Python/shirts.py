f = open("shirts_shipm3Jb", 'r') #open file for connection
ddf = f.read() #ddt = file
f.close()
#we have the input as 1 string

dds = ddf.split('\n')
#dds = list split where new line, individual strings

ttg = [] #ttg equals empty list. real data formatted

for i in dds :              #for every string in dds
    pts = i.split(',')      #split into 3 parts. color, amt, state
    ttg.append( [pts[0], int(pts[1]), pts[2]] ) #color amount state into a list of list

count = 0
for i in ttg:       #for every
    if i[0] == 'maroon':
        count = count+ i[1]

print(count)

colors =[]
for i in ttg:
    if i[0] not in colors:
        colors.append(i[0])

print(colors)

colorSums = [] #list of colors with sums

for i in colors:
    count =0
    for n in ttg:
        if n[0] in i:
            count = count + n[1]
    print(i, count)
    colorSums.append( [i, count] ) 

from operator import itemgetter
print(sorted(colorSums, key = itemgetter(1)))

from operator import itemgetter
print(sorted(colorSums))


sumC = colorSums
