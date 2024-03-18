#ravioli time. Manage a set of ravioli:

#10,32,28
#3,4,5
#32,15,38
#6,7,8
#24,25,18

#import math
#s = (a+b+c)/2
#math.sqrt( s*(s-a)*(s-b)*(s-c) )


class Ravioli:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"{self.a} {self.b} {self.c}"
    def perimeter (self):
        p = self.a+self.b+self.c
        return p
    def area(self,p):
        import math
        s = p/2
        area = math.sqrt( s*(s-self.a)*(s-self.b)*(self.c) )
        area = round(area,2)
        return area

tri = []

tri1 = Ravioli(10,32,28)
tri2 = Ravioli(3,4,5)
tri3 = Ravioli(32,15,38)
tri4 = Ravioli(6,7,8)
tri5 = Ravioli(24,25,18)

tri = [tri1, tri2, tri3, tri4, tri5]


for i in tri:
    print(i)


for i in tri:
    #print("triangle", i.perimeter() )
    p = i.perimeter()
    print ("perimeter is", p)
    print("area is", i.area(p) )
    
