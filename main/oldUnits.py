# parent class
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
 

# while loop to continue propting the program 
go = True

while go: 
    
# list of the units 
    print()
    print()
    print("Avalible Units:")
    print("----------------")
    print()
    print("mm")
    print()
    print("cm")
    print()
    print("m")
    print()
    print("km")
    print()
    print("inch")
    print()
    print("foot")
    print()
    print("mile")
    print()
    print()


# can choose the units/ in value
    out_unit = input("What unit would you like to calculate?: ") 
    print() 
    in_unit = input("what unit are you currentley using: ")
    print()
    in_value = float(input("what value do you have: "))
    print()
    x = 0
  

# setes the input functions to spacific values  
    out_mm.set_values(x, in_unit, out_unit, in_value)
    out_cm.set_values(x, in_unit, out_unit, in_value)
    out_m.set_values(x, in_unit, out_unit, in_value)


# dictionary of formulas/ pulls dict keys 
    formulas_dict = {"cm-mm": out_mm().cm(),
               "m-mm": out_mm().m(),
               "km-mm": out_mm().km(),
               "inch-mm": out_mm().inch(),
               "foot-mm": out_mm().foot(),
                "mile-mm": out_mm().mile()}


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
          print(formulas_dict['cm-mm'])

    elif in_unit.upper() =='CM':
            print("The conversion from cm to m is:")
            print(formulas_dict['m-mm'])

    elif in_unit.upper() =='KM':
            print("The conversion from km to m is:")
            print(formulas_dict['km-mm'])

    elif in_unit.upper() =='INCH':
            print("conversion from inches to m is:")
            print(formulas_dict['inch-mm'])

    elif in_unit.upper() =='FOOT':
          print("The conversion from feet to m is:")
          print(formulas_dict['foot-mm'])
      
    elif in_unit.upper() =='MILE':
          print("The conversion from miles to m is:")
          print(formulas_dict['mile-mm'])
          
    else:
          print()
          print("Error, unit not found in dict")

elif out_unit.upper() == "KM":

    if in_unit.upper() =='MM':
          print("The conversion from mm to km is:")
          print(formulas_dict['cm-mm'])

    elif in_unit.upper() =='CM':
            print("The conversion from cm to km is:")
            print(formulas_dict['m-mm'])

    elif in_unit.upper() =='M':
            print("The conversion from m to km is:")
            print(formulas_dict['km-mm'])

    elif in_unit.upper() =='INCH':
            print("conversion from inches to km is:")
            print(formulas_dict['inch-mm'])

    elif in_unit.upper() =='FOOT':
          print("The conversion from feet to km is:")
          print(formulas_dict['foot-mm'])
      
    elif in_unit.upper() =='MILE':
          print("The conversion from miles to km is:")
          print(formulas_dict['mile-mm'])
          
    else:
          print()
          print("Error, unit not found in dict")

elif out_unit.upper() == "INCH":

    if in_unit.upper() =='MM':
          print("The conversion from mm to inches is:")
          print(formulas_dict['cm-mm'])

    elif in_unit.upper() =='CM':
            print("The conversion from cm to inches is:")
            print(formulas_dict['m-mm'])

    elif in_unit.upper() =='M':
            print("The conversion from m to inches is:")
            print(formulas_dict['km-mm'])

    elif in_unit.upper() =='KM':
            print("conversion from inches to inches is:")
            print(formulas_dict['inch-mm'])

    elif in_unit.upper() =='FOOT':
          print("The conversion from feet to inches is:")
          print(formulas_dict['foot-mm'])
      
    elif in_unit.upper() =='MILE':
          print("The conversion from miles to inches is:")
          print(formulas_dict['mile-mm'])
          
    else:
          print()
          print("Error, unit not found in dict")
        
elif out_unit.upper() == "FOOT":

    if in_unit.upper() =='MM':
          print("The conversion from mm to feet is:")
          print(formulas_dict['cm-mm'])

    elif in_unit.upper() =='CM':
            print("The conversion from cm to feet is:")
            print(formulas_dict['m-mm'])

    elif in_unit.upper() =='M':
            print("The conversion from m to feet is:")
            print(formulas_dict['km-mm'])

    elif in_unit.upper() =='KM':
            print("conversion from km to feet is:")
            print(formulas_dict['inch-mm'])

    elif in_unit.upper() =='INCH':
          print("The conversion from inches to feet is:")
          print(formulas_dict['foot-mm'])
      
    elif in_unit.upper() =='MILE':
          print("The conversion from miles to feet is:")
          print(formulas_dict['mile-mm'])
          
    else:
          print()
          print("Error, unit not found in dict")

elif out_unit.upper() == "MILE":

    if in_unit.upper() =='MM':
          print("The conversion from mm to miles is:")
          print(formulas_dict['cm-mm'])

    elif in_unit.upper() =='CM':
            print("The conversion from cm to miles is:")
            print(formulas_dict['m-mm'])

    elif in_unit.upper() =='M':
            print("The conversion from m to miles is:")
            print(formulas_dict['km-mm'])

    elif in_unit.upper() =='KM':
            print("conversion from km to miles is:")
            print(formulas_dict['inch-mm'])

    elif in_unit.upper() =='INCH':
          print("The conversion from inch to miles is:")
          print(formulas_dict['foot-mm'])
      
    elif in_unit.upper() =='FOOT':
          print("The conversion from feet to miles is:")
          print(formulas_dict['mile-mm'])
          
    else:
          print()
          print("Error, unit not found in dict")


# Continue or stop the program by setting the True while loop to False 
print()
going = input("Continue? (Y)es or (N)o: ")
    
if going.upper() == 'Y':
        go = True
elif going.upper() == 'N':
        go = False
else:
        print("Enter 'Y' for yes or 'N' for no")
