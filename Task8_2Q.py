##(2Q) create proper member variables inside the task if required and use them when necessary.
# For example for this task create a class private variable named pi=3.141

class circle:
    _pi =3.141

    def __init__(self,list):
       self.list = list

    def area1(self):
       area =[self._pi * r**2 for r in self.list]
       return area

    def circumference1(self):
        circumference =[2 * self._pi * r for r in self.list]
        return circumference

list = [10,501,22,37,100,999,87,351]

output = circle(list)
stage1 = output.area1()
print(f"area:{stage1}")
stage2 = output.circumference1()
print(f"circumfernce:{stage2}")



#Output-> area:[314.1, 788394.1410000001, 1520.244, 4300.029, 31410.0, 3134721.141, 23774.229, 386974.341]
# circumfernce:[62.82, 3147.282, 138.204, 232.434, 628.2, 6275.718, 546.534, 2204.982]