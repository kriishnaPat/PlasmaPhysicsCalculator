#parent class
class Polygon:
    width = 0
    length = 0
    radius = 0
    def set_values(self, width, length, radius):
        Polygon.width = width
        Polygon.length = length
        Polygon.radius = radius
        
#inharenting classes       
class rectangle(Polygon):
    def area(self):
        return self.width * self.length
    
    
class triangle(Polygon):
    def area(self):
        return self.width * self.length / 2
    
    
class circle(Polygon):
    def area(self):
        return 3.14159265358979323846 * self.radius * 2
    
    
rect = rectangle()
tri = triangle()
cir = circle()

go = True

while go: 
    
# list of the shapes 
    print()
    print()
    print("Avalible Shapes:")
    print("----------------")
    print()
    print("Hexigon")
    print()
    print("Circle")
    print()
    print("Rectangle")
    print()
    print("Triangle")
    print()
    print("Trapizoide")
    print()
    print()


# can choose the shapes/ decides what inputs are applicable 
    in_shape = input("What shape would you like to calculate?: ")
    
    if in_shape.upper() == ("CIRCLE"):
        Z = float(input("enter the redius of the object- without units: "))
    elif in_shape.upper() == ("HEXIGON"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
    elif in_shape.upper() == ("RECTANGLE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
    elif in_shape.upper() == ("TRIANGLE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
    elif in_shape.upper() == ("TRAPIZOIDE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
    else:
        print("Please enter a valid shape from the list")
   

    rect.set_values(X, Y, Z)
    tri.set_values(X, Y, Z)
    cir.set_values(X, Y, Z)


# dictionary of formulas/ pulls dict keys 
    formulas_dict = {"h6": rect.area() + tri.area() * 2,
               "c0": cir.area(),
               "r4": rect.area(),
               "t3": tri.area(),
               "t4":(rect.area() + tri.area() * 2) / 2}


    if in_shape.upper() == "HEXIGON":
        print("The area of your hexigon is:")
        print(formulas_dict['h6'])

    elif in_shape.upper() == "CIRCLE":
        print("The area of your circle is:")
        print(formulas_dict['c0'])

    elif in_shape.upper() == "RECTANGLE":
        print("The area of your rectangle is:")
        print(formulas_dict['r4'])

    elif in_shape.upper() == "TRIANGLE":
        print("The area of your triangle is:")
        print(formulas_dict['t3'])

    elif in_shape.upper() == "TRAPIZOIDE":
        print("The area of your trapizoide is:")
        print(formulas_dict['t4'])

    else:
        print()
        print("Error, shape not in dict- fix")
        
# Continue or stop the program
    going = input("Would you like to find calculate another shape?(Y)es or (N)o: ")
    
    if going.upper() == 'Y':
        go = True
    elif going.upper() == 'N':
        go = False
    else:
        print("Enter Y for yes or N for no")