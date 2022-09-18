import numpy as np
# laser function class
class Plasma_functions:
    def laserFrequency(wavelength):
        """ The frequency of a laser given its wavelength
            
            wavelength in microns
            
            Returns the frequency in rads/sec
        """

        freq = 2.0*(np.pi)*2.9979e10/(1.e-4*wavelength)

        return freq
        
# parent class for lenth unit conversions
class Length:
     in_unit = 0
     out_unit = 0
     in_value = 0
     def set_values(self, in_unit, out_unit, in_value):
        Length.in_u = in_unit
        Length.out_u = out_unit
        Length.in_value = in_value
# class for micron unit conversions      
class out_micron(Length):
    def mm(self):
        return self.in_value * 1000
    def cm(self):
        return self.in_value * 10000
    def m(self):
        return self.in_value * 1000000
    def km(self):
        return self.in_value * 1000000000

class out_rads_min(Length):
    def rads_sec(self):
        return self.in_value * 60
    def hz(self):
        return self.in_value * 376.99112

class out_hz(Length):
    def rads_sec(self):
        return self.in_value / 0.159155
    def rads_min(self):
        return self.in_value / 0.002655258238864920

# unit conversions for laser function, step one in laser function

go = True
#user interact here
while go:

  # can choose the units/ in value
    Formula = input("What formula would you like to calculate: ").upper()
# defined the formulas to pull from functions class
    if Formula == ("LASER"):
        tagged = tuple(input("Enter the wavelength value and units separated by a space: ").upper().split(" "))
        in_value = float(tagged[0])
        uni = tagged[1].upper()
        x = 0
        units_final = 0

        out_micron.set_values(x, uni, units_final, in_value)
        #out_cm.set_values(x, in_unit, out_unit, in_value)
        #out_m.set_values(x, in_unit, out_unit, in_value)

        formulas_dict = {
                  "mm-micron":    out_micron().mm(),
                  "cm-micron":    out_micron().cm(),
                  "km-micron":    out_micron().km(),
                  "m-micron":    out_micron().m(),
                  "rads/sec-hz":    out_hz().rads_sec(),
                  "rads/sec-rads/min":    out_rads_min().rads_sec()
}

        if uni == "CM":
          new = formulas_dict["cm-micron"]
          #print(new)

        elif uni == "M":
          new1 = formulas_dict["m-micron"]  
          #print(new1)

        elif uni == "KM":
          new2 = formulas_dict["km-micron"]
          #print(new2)

        elif uni == "MM":
          new3 = formulas_dict["mm-micron"]    
          #print(new3)       
       

    # re packages the tuple
      
        print("""Unit options:
        rad/min
        rad/s
        Hz
        """) 
      
        units_final = input("What units would you like the answer in?: ").upper()
        

        if units_final == "RAD/MIN":
              new = formulas_dict["rads/sec-rads/min"]
              #print(new)

        elif units_final == "RAD/S":
              new = Plasma_functions.laserFrequency(in_value)

        elif units_final == "HZ":
              new = formulas_dict["rads/sec-hz"]
              #print(new)
          
        else: 
              print("Enter a valid unit")

        print("Here is your final answer {}, {}." . format(new, units_final))

        

        stop = input("Stop the program?: Y/N ")
        if stop.upper() == "Y":
              go = False
        elif stop.upper() == "N":
              go = True
        else:
              print("enter Y of yes and N for no")                                                      