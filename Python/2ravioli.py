# Waqas Bhatti Com-250

f = open("tri_sides.txt", 'r')
ddf = f.read()  #open connection    
f.close()       #close connection

dds = ddf.split('\n')

ttg = []                #create empty list for list of lists
for i in dds:
    pts = i.split(",")
    ttg.append( [ int(pts[0]), int(pts[1]), int(pts[2]) ] )     #convert to ints



class Ravioli:
    def __init__(self, a, b, c):        #sides a,b,c
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"{self.a} {self.b} {self.c}"
    def perimeter(self):
        p = self.a + self.b + self.c
        return p
    def area(self, p):                          #plug in our p to find area
        import math
        s = p/2
        area = math.sqrt( s*(s-self.a)*(s-self.b)*(self.c) )    #area formula
        area = round(area,2)                                    #round 2 places
        return area

objlist = []
for i in ttg:
    obj = Ravioli(i[0], i[1], i[2])         #make numbers into object
    objlist.append(obj)                     #list of objects

count = 1                       #counts from ravioli 1
totalarea = 0                   
for i in objlist:
    print(i)                    #print all objects
    p = i.perimeter()           #p = return perimeter from method
    area = i.area(p)            #import p, returns area
    print("Perimeter for ravioli" ,count, "is", p )
    print("Area for ravioli" ,count, "is", area, '\n')
    count = count+1

    totalarea = totalarea + area        #find total area

print("The total area is", totalarea )


#******************************************************************************
tri = []                                        #create empty list for raviolis

tri1 = Ravioli(10,32,28)                        #create triangular raviolis
tri2 = Ravioli(3,4,5)
tri3 = Ravioli(32,15,38)
tri4 = Ravioli(6,7,8)
tri5 = Ravioli(24,25,18)

tri.extend( [tri1, tri2, tri3, tri4, tri5] )    #append into list


total = []                                      #create empty list to store areas

count = 1                                       #counter to show triangle #
for i in tri:
   # print(i)                                    #print sides
    p = i.perimeter()                           #p=perimeter
   # print("Perimeter for ravioli", count , "is" , i.perimeter() )
   # print("Area for ravioli", count ,"is", i.area(p), '\n')
    count = count + 1

    total.append( i.area(p) ) 

#print( "Total area is", sum(total) )
    
