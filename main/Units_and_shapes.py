#parent class
class Polygon:
    width = 0
    length = 0
    radius = 0
    def set_values(self, width = 0, length = 0, radius = 0):
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

      
class Length:
    in_unit = 0
    out_unit = 0
    in_value = 0
    def set_values(self, in_unit, out_unit, in_value):
        Length.in_u = in_unit
        Length.out_u = out_unit
        Length.in_value = in_value
        
# inharenting classes for each conversion
# these show what the value is going to be converted in to 
# ex) out_mm turns cm -> mm
class out_mm(Length):
    def cm(self):
        return self.in_value * 10
    def m(self):
        return self.in_value * 1000   
    def km(self):
        return self.in_value * 1000000 
    def inch(self):
        return self.in_value * 25.4 
    def foot(self):
        return self.in_value * 304.8 
    def mile(self):
        return self.in_value * 1609344
        

class out_cm(Length):
    def mm(self):
        return self.in_value * 10
    def m(self):
        return self.in_value / 100
    def km(self):
        return self.in_value / 100000
    def inch(self):
        return self.in_value * 2.54
    def foot(self):
        return self.in_value * 30.48
    def mile(self):
        return self.in_value * 160934

class out_m(Length):
    def mm(self):
        return self.in_value * 1000
    def cm(self):
        return self.in_value / 100
    def km(self):
        return self.in_value * 1000
    def inch(self):
        return self.in_value / 39.37
    def foot(self):
        return self.in_value /  3.281
    def mile(self):
        return self.in_value * 1609

class out_km(Length):
    def mm(self):
        return self.in_value / 1000000
    def cm(self):
        return self.in_value / 100000
    def m(self):
        return self.in_value / 1000
    def inch(self):
        return self.in_value / 39370
    def foot(self):
        return self.in_value /  3281
    def mile(self):
        return self.in_value * 1.609  

class out_foot(Length):
    def mm(self):
        return self.in_value * 305
    def cm(self):
        return self.in_value * 30.48
    def m(self):
        return self.in_value * 3.281
    def km(self):
        return self.in_value * 3281
    def inch(self):
        return self.in_value / 12
    def mile(self):
        return self.in_value * 5280

class out_inch(Length):
    def mm(self):
        return self.in_value / 25.4
    def cm(self):
        return self.in_value / 2.54
    def m(self):
        return self.in_value * 39.37   
    def km(self):
        return self.in_value * 39370
    def mile(self):
        return self.in_value * 63360
    def foot(self):
        return self.in_value * 12
      
class out_mile(Length):
    def mm(self):
        return self.in_value / 1609340
    def cm(self):
        return self.in_value / 160934
    def m(self):
        return self.in_value / 1609   
    def km(self):
        return self.in_value / 1.609
    def inch(self):
        return self.in_value / 63360
    def foot(self):
        return self.in_value / 5280


rect = rectangle()
tri = triangle()
cir = circle()

go = True

while go:
    # can choose the units/ in value
    in_shape = input("What shape would you like to calculate?: ")

    

    if in_shape.upper() == ("CIRCLE"):
        Z = float(input("enter the redius of the object: "))
        U = input("enter the units of the value: ")
        X = 0
        Y = 0
    elif in_shape.upper() == ("HEXIGON"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
        U = input("enter the units of the value: ")
    elif in_shape.upper() == ("RECTANGLE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
        U = input("enter the units of the value: ")
    elif in_shape.upper() == ("TRIANGLE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
        U = input("enter the units of the value: ")
    elif in_shape.upper() == ("TRAPIZOIDE"):
        Y = float(input("enter the length of the object- without units: "))
        X = float(input("enter the width of the object- without units: "))
        Z = 0
        U = input("enter the units of the value: ")
    else:
        print("Please enter a valid shape from the list")
  

    cm_convt = {"mm-cm":     out_cm().mm(),
                 "m-cm":     out_cm().m(),
                 "km-cm":    out_cm().km(),
                 "inch-cm":  out_cm().inch(),
                 "foot-cm":  out_cm().foot(),
                 "mile-cm":  out_cm().mile(),}

    if U.upper() != "CM":

      if U.upper() =='MM':
              x = X / 10
              y = Y / 10
              z = Z / 10
      elif U.upper() =='M':
              x = X * 100
              y = Y * 100
              z = Z * 100
      elif U.upper() =='KM':
              x = X * 1000
              y = Y * 1000
              z = Z * 1000
      elif U.upper() =='INCH':
              x = X * 2.54
              y = Y * 2.54
              z = Z * 2.54
      elif U.upper() =='FOOT':
              x = X * 30.48
              y = Y * 30.48
              z = Z * 30.48
      elif U.upper() =='MILE':
              x = X * 160934
              y = Y * 160934
              z = Z * 160934
      else:
            print()
            print("Error, unit not found in dict")

    rect.set_values(x, y, z)
    tri.set_values(x, y, z)
    cir.set_values(x, y, z)
    
  # dictionary of formulas/ pulls dict keys 
    formulas_dict = {"h6": rect.area() + tri.area() * 2,
               "c0": cir.area(),
               "r4": rect.area(),
               "t3": tri.area(),
               "t4":(rect.area() + tri.area() * 2) / 2}

    if in_shape.upper() == "HEXIGON":
        print("The area of your hexigon is:")
        print(formulas_dict['h6'])
        answer = formulas_dict["h6"]

    elif in_shape.upper() == "CIRCLE":
        print("The area of your circle is:")
        print(formulas_dict['c0'])
        answer = formulas_dict["c0"]

    elif in_shape.upper() == "RECTANGLE":
        print("The area of your rectangle is:")
        print(formulas_dict['r4'])
        answer = formulas_dict["r4"]
        
    elif in_shape.upper() == "TRIANGLE":
        print("The area of your triangle is:")
        print(formulas_dict['t3'])
        answer = formulas_dict["t3"]

    elif in_shape.upper() == "TRAPIZOIDE":
        print("The area of your trapizoide is:")
        print(formulas_dict['t4'])
        answer = formulas_dict["t4"]

    else:
        print()
        print("Error, shape not in dict- fix")

    out_unit = input("What unit would you like to calculate?: ") 
    print() 
    in_unit = "cm"
    print()
    in_value = answer
    x = 0
  

# setes the input functions to spacific values  
    out_mm.set_values(x, in_unit, out_unit, in_value)
    out_cm.set_values(x, in_unit, out_unit, in_value)
    out_m.set_values(x, in_unit, out_unit, in_value)


# dictionary of formulas/ pulls dict keys 
    formulas_dict = {"mm-cm": out_cm().mm(),
                    "m-cm":         out_cm().m(),
                    "km-cm":        out_cm().km(),
                    "inch-cm":      out_cm().inch(),
                    "foot-cm":      out_cm().foot(),
                    "mile-cm":      out_cm().mile(),
                    "cm-mm":        out_mm().cm(),
                    "m-mm":         out_mm().m(),
                    "km-mm":        out_mm().km(),
                    "inch-mm":      out_mm().inch(),
                    "foot-mm":      out_mm().foot(),
                    "mile-mm":      out_mm().mile(),
                    "mm-km":        out_km().mm(),
                    "cm-km":        out_km().cm(),
                    "m-km":         out_km().m(),
                    "inch-km":      out_km().inch(),
                    "foot-km":      out_km().foot(),
                    "mile-km":      out_km().mile(),
                    "mm-inch":      out_inch().mm(),
                    "cm-inch":      out_inch().cm(),
                    "m-inch":       out_inch().m(),
                    "km-inch":      out_inch().km(),
                    "foot-inch":    out_inch().foot(),
                    "mile-inch":    out_inch().mile(),
                    "mm-foot":      out_foot().mm(),
                    "cm-foot":      out_foot().cm(),
                    "m-foot":       out_foot().m(),
                    "km-foot":      out_foot().km(),
                    "inch-foot":    out_foot().inch(),
                    "mile-foot":    out_foot().mile(),
                    "mm-mile":      out_mile().mm(),
                    "cm-mile":      out_mile().cm(),
                    "m-mile":       out_mile().m(),
                    "km-mile":      out_mile().km(),
                    "foot-mile":    out_mile().foot(),
                    "inch-mile":    out_mile().inch(),}

  # uses and gates to decide what formula to pull from dictionary
    if out_unit.upper() == "MM": 
        if in_unit.upper() =='CM':
              print("The conversion from cm to mm is:")
              print(formulas_dict["cm-mm"])

        elif in_unit.upper() =='M':
              print("The conversion from m to mm is:")
              print(formulas_dict['m-mm'])

        elif in_unit.upper() =='KM':
              print("The conversion from km to mm is:")
              print(formulas_dict['km-mm'])

        elif in_unit.upper() =='INCH':
              print("conversion from inches to mm is:")
              print(formulas_dict['inch-mm'])

        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to mm is:")
              print(formulas_dict['foot-mm'])
        
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to mm is:")
              print(formulas_dict['mile-mm'])
            
        else:
              print()
              print("Error, unit not found in dict")

    elif out_unit.upper() == "CM":

        if in_unit.upper() =='MM':
              print("The conversion from mm to cm is:")
              print(formulas_dict['cm-mm'])

        elif in_unit.upper() =='M':
                print("The conversion from m to cm is:")
                print(formulas_dict['m-mm'])

        elif in_unit.upper() =='KM':
                print("The conversion from km to cm is:")
                print(formulas_dict['km-mm'])

        elif in_unit.upper() =='INCH':
                print("conversion from inches to cm is:")
                print(formulas_dict['inch-mm'])

        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to cm is:")
              print(formulas_dict['foot-mm'])
          
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to cm is:")
              print(formulas_dict['mile-mm'])
              
        else:
              print()
              print("Error, unit not found in dict")

    elif out_unit.upper() == "M":

        if in_unit.upper() =='MM':
              print("The conversion from mm to m is:")
              print(formulas_dict['mm-m'])

        elif in_unit.upper() =='CM':
                print("The conversion from cm to m is:")
                print(formulas_dict['cm-m'])

        elif in_unit.upper() =='KM':
                print("The conversion from km to m is:")
                print(formulas_dict['km-m'])

        elif in_unit.upper() =='INCH':
                print("conversion from inches to m is:")
                print(formulas_dict['inch-m'])

        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to m is:")
              print(formulas_dict['foot-m'])
          
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to m is:")
              print(formulas_dict['mile-m'])
              
        else:
              print()
              print("Error, unit not found in dict")

    elif out_unit.upper() == "KM":

        if in_unit.upper() =='MM':
              print("The conversion from mm to km is:")
              print(formulas_dict['cm-km'])

        elif in_unit.upper() =='CM':
                print("The conversion from cm to km is:")
                print(formulas_dict['m-km'])

        elif in_unit.upper() =='M':
                print("The conversion from m to km is:")
                print(formulas_dict['km-km'])

        elif in_unit.upper() =='INCH':
                print("conversion from inches to km is:")
                print(formulas_dict['inch-km'])

        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to km is:")
              print(formulas_dict['foot-km'])
          
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to km is:")
              print(formulas_dict['mile-km'])
              
        else:
              print()
              print("Error, unit not found in dict")

    elif out_unit.upper() == "INCH":

        if in_unit.upper() =='MM':
              print("The conversion from mm to inches is:")
              print(formulas_dict['mm-inch'])

        elif in_unit.upper() =='CM':
                print("The conversion from cm to inches is:")
                print(formulas_dict['cm-inch'])

        elif in_unit.upper() =='M':
                print("The conversion from m to inches is:")
                print(formulas_dict['m-inch'])

        elif in_unit.upper() =='KM':
                print("conversion from inches to inches is:")
                print(formulas_dict['km-inch'])

        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to inches is:")
              print(formulas_dict['foot-inch'])
          
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to inches is:")
              print(formulas_dict['mile-inch'])
              
        else:
              print()
              print("Error, unit not found in dict")
            
    elif out_unit.upper() == "FOOT":

        if in_unit.upper() =='MM':
              print("The conversion from mm to feet is:")
              print(formulas_dict['mm-foot'])

        elif in_unit.upper() =='CM':
                print("The conversion from cm to feet is:")
                print(formulas_dict['cm-foot'])

        elif in_unit.upper() =='M':
                print("The conversion from m to feet is:")
                print(formulas_dict['m-foot'])

        elif in_unit.upper() =='KM':
                print("conversion from km to feet is:")
                print(formulas_dict['km-foot'])

        elif in_unit.upper() =='INCH':
              print("The conversion from inches to feet is:")
              print(formulas_dict['inch-foot'])
          
        elif in_unit.upper() =='MILE':
              print("The conversion from miles to feet is:")
              print(formulas_dict['mile-foot'])
              
        else:
              print()
              print("Error, unit not found in dict")

    elif out_unit.upper() == "MILE":

        if in_unit.upper() =='MM':
              print("The conversion from mm to miles is:")
              print(formulas_dict['mile-mm'])

        elif in_unit.upper() =='CM':
                print("The conversion from cm to miles is:")
                print(formulas_dict['cm-mile'])

        elif in_unit.upper() =='M':
                print("The conversion from m to miles is:")
                print(formulas_dict['m-mile'])

        elif in_unit.upper() =='KM':
                print("conversion from km to miles is:")
                print(formulas_dict['km-mile'])

        elif in_unit.upper() =='INCH':
              print("The conversion from inch to miles is:")
              print(formulas_dict['inch-mile'])
          
        elif in_unit.upper() =='FOOT':
              print("The conversion from feet to miles is:")
              print(formulas_dict['foot-mile'])
              
        else:
              print()
              print("Error, unit not found in dict")

    end = input("would you like to end the program? (Y) or (N)")
    if end.upper() == "Y":
      go = False
