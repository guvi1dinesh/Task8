#(3Q) From the given list create two class methods Area and perimeter,
# which will be going to calculate the area and perimeter:





class Circle:
    _pi= 3.141

    def __init__(self,r):
        self.r = r

    @classmethod
    def area1(self,r):
        return self._pi * r**2

    @classmethod
    def perimeter1(self,r):
        return 2 * self._pi *r


list1 = [10,501,22,37,100,999,87,351]

for r in list1:
    area = Circle.area1(r)
    perimeter = Circle.perimeter1(r)
    print(f"area:{area}")
    print(f"perimeter:{perimeter}")




#Output->
# area:314.1
# perimeter:62.82
# area:788394.1410000001
# perimeter:3147.282
# area:1520.244
# perimeter:138.204
# area:4300.029
# perimeter:232.434
# area:31410.0
# perimeter:628.2
# area:3134721.141
# perimeter:6275.718
# area:23774.229
# perimeter:546.534
# area:386974.341
# perimeter:2204.982

