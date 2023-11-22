##                    Using the pythons object oriented programing scheme (OOPS)*

#(1Q) create a python class called circle with constructor which will take a list as an argument for the task.
# The list is [10,501,22,37,100,999,87,351]



import math
class circle:


    def __init__(self,list):
       self.list = list

    def area1(self):
       area =[math.pi * r**2 for r in self.list]
       return area

    def circumference1(self):
        circumference =[2 * math.pi * r for r in self.list]
        return circumference

list = [10,501,22,37,100,999,87,351]

output = circle(list)
stage1 = output.area1()
print(f"area:{stage1}")
stage2 = output.circumference1()
print(f"circumference:{stage2}")




#Output-> area:[314.1592653589793, 788542.8976436916, 1520.53084433746, 4300.840342764427, 31415.926535897932, 3135312.609875267, 23778.714795021144, 387047.3565149161]
# circumference:[62.83185307179586, 3147.8758388969727, 138.23007675795088, 232.4778563656447, 628.3185307179587, 6276.9021218724065, 546.637121724624, 2205.398042820035]