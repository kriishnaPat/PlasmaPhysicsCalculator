import numpy as np
# Plasma formulary class 
class Plasma_functions:
  def CriticalElectronDensity(wavelength):
    """ The critical electron density. 
        Taken from the NRL plasma formulary, J.D. Huber 2007.
        
        Laser wavelength in microns
        
        Returns the density in 1/cm^3
    """

    ncrit = 1.1e21/(wavelength**2)

    return ncrit
  def DebyeLength(temperature, density):
      """ The Debye length for electrons. 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
      """

      debye = 7.43e2*np.sqrt(temperature)/np.sqrt(density)

      return debye
  def LaserFrequency(wavelength):
      """ The frequency of a laser given its wavelength
          
          wavelength in microns
          
          Returns the frequency in rads/sec
      """

      freq = 2.0*(np.pi)*2.9979e10/(1.e-4*wavelength)

      return freq
  def OscillatoryVelocity(intensity,wavelength):
      """ The (maximum) oscillatory velocity of an electron in 
          the field of an EM wave (non-relativistic)
          
          wavelength in microns
          intensity in W/cm^2
          
          Returns the velocity in cm/sec
      """

      vOsc = 8.095e8*np.sqrt(1.e-15*intensity)*wavelength

      return vOsc
  
  
  def NumberOfElectronsInDebyeSphere(temperature, density):
      """ The number of electrons in a Debye sphere. 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          temperature in eV
          density in 1/cm^3
          
          Returns the dimensionless number
      """

      numInSphere = 1.72e9*np.sqrt(temperature)*temperature/np.sqrt(density)

      return numInSphere

  def ElectronPlasma(density):
      """ The electron plasma frequency 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          density in 1/cm^3
          
          Returns the electron plasma frequency in radians per second
      """

      ePlasma = 5.64e4*np.sqrt(density)

      return ePlasma

  def IonPlasma(ionDensity,Z,mu):
      """ The ion plasma frequency 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          density in 1/cm^3
          
          Returns the ion plasma frequency in radians per second
      """

      iPlasma = 1.32e3*Z*np.sqrt(ionDensity)/np.sqrt(mu)

      return iPlasma

  def ElectronCollisionFrequency(density,temperature,Z,coulLog):
      """ The electron-ion collision frequency 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          electron density in 1/cm^3
          electron temperature in eV
          Z - ionization state (<Z^2>/<Z> for multispecies)
          couLog - the Coulomb logaritm [log(lambda)]
          
          Returns the electron collision frequency in radians per second
      """

      eColFreq = 2.91e-6*density*coulLog*Z/(temperature**(3.0/2.0))

      return eColFreq


  def CoulLog_eiCollisions(density,etemp,itemp,Z,mu):
      """ The Coulomb logarthim for e-i collisions evaluated according 
          to the NRL plasma formulary, J.D. Huber 2007 (p. 34).
          
          Z           - ionization state
          mu          - is the ion mass in units of proton mass (atomic number)
          density  - electron density is in 1/cm^3
          etemp    - electron temperature in eV
          itemp    - ion temperature in eV
      """
      
      # should probably do a sanity check on the input...
      
      meToMp = 1./(1836.2) # electron to proton mass ratio
      meToMi = meToMp/mu   # electron to ion mass 
      
      testRat1 = itemp*meToMi
      testRat2 = 10*Z**2
      testRat3 = Z*itemp*meToMi
      
      if (etemp > testRat1) & (etemp < testRat2):
          # have expression 1
          coulog = 23. - np.log(np.sqrt(density)*Z*etemp**(-3/2))
      elif (testRat2 > testRat1) & (testRat2 < etemp):
          # have expression 2
          coulog = 24. - np.log(np.sqrt(density)/etemp)
      elif etemp < testRat3:
          # expression 3
          coulog = 30. - np.log(np.sqrt(density/Z)*itemp**(-3/2)*Z**2/mu)
      else:
          # flag an error
          coulog = 0.0
                  
      return coulog


  def ElectronThermalVelocity(temperature):
      """ The electron thermal velocity 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          temperature in eV
          
          Returns the electron thermal velocity in cm per second
      """

      eThermal = 4.19e7*np.sqrt(temperature)

      return eThermal


  def IonThermalVelocity(temperature,mu):
      """ The ion thermal velocity 
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          temperature in eV
          mu is ion mass in units of the proton mass (atomic number)
          
          Returns the ion thermal velocity in cm per second
      """

      iThermal = 9.79e5*np.sqrt(temperature)/np.sqrt(mu)

      return iThermal


  def ColdIonSoundSpeed(temperature,Z,mu,gamma):
      """ The cold-ion sound speed
          Taken from the NRL plasma formulary, J.D. Huber 2007.
          
          temperature in eV
          Z is the ion charge
          mu is the ion mass in units of proton mass (atomic number)
          gamma is the electron adiabatic index (1 is isothermal)
          
          Returns the cold-ion sound speed in cm per second
      """

      coldIon = 9.79e5*np.sqrt(gamma*Z*temperature/mu)

      return coldIon


  def IonSoundSpeed(eTemp,iTemp,Z,mu,gammaE,gammaI):
      """ The ion sound speed
          
          eTemp is electron temperature in eV
          iTemp is ion temperature in eV
          Z is the ion charge
          mu is the ion mass in units of proton mass (atomic number)
          gammaE is the electron adiabatic index (1 is isothermal)
          gammaI is the ion adiabatic index (3 is 1-D)
          
          Returns the ion sound speed in cm per second
      """

      ionSound = Plasma_functions.ColdIonSoundSpeed(eTemp,Z,mu,gammaE)*np.sqrt(1.0+gammaI*iTemp/gammaE/Z/eTemp)

      return ionSound

# parent class for length unit conversions
class Units:
  in_unit = 0
  out_unit = 0
  in_value = 0 
  def set_values(self, in_unit, out_unit, in_value):
      Units.in_u = in_unit
      Units.out_u = out_unit
      Units.in_value = in_value

#class for micron conversions
class out_micron(Units):
  def mm(self):
    return self.in_value * 1000
  def cm(self):
    return self.in_value * 10000
  def m(self):
    return self.in_value * 1000000
  def km(self):
    return self.in_value * 1000000000
  def inch(self):
    return self.in_value * 25400
  def foot(self):
    return self.in_value * 304800
  def mile(self):
    return self.in_value * 1.609e9

class out_mm(Units):
    def micron(self):
        return self.in_value / 1000
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
        
class out_cm(Units):
    def micron(self):
        return self.in_value / 10000
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

class out_m(Units):
    def micron(self):
        return self.in_value / 1000000
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

class out_km(Units):
    def micron(self):
        return self.in_value / 1000000000
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

class out_foot(Units):
    def micron(self):
        return self.in_value / 304800
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

class out_inch(Units):
    def micron(self):
        return self.in_value / 25400
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
      
class out_mile(Units):
    def micron(self):
      return self.in_value / 1.609e9
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

# class for minute unit conversions      
class out_min(Units):
  def s(self):
    return self.in_value / 60
  def h(self):
    return self.in_value * 60
        
# class for seconds unit conversions      
class out_s(Units):
  def min(self):
    return self.in_value * 60
  def h(self):
    return self.in_value * 3600

# class for hours unit conversions      
class out_h(Units):
  def min(self):
    return self.in_value / 60
  def s(self):
    return self.in_value  / 3600

# class for kelvin unit converions
class out_k(Units):
  def c(self):
      return self.in_value + 273.15
  def f(self):
    return (self.in_value - 32) * 5/9 + 273.15
  def eV(self):
      return self.in_value / 8.621738e-5

# class for celsius unit converions
class out_c(Units):
  def k(self):
      return self.in_value - 273.15
  def f(self):
    return (self.in_value - 32) * 5/9
  def eV(self):
      return self.in_value / 1.1853248076851e+22

# class for farenheit unit converions
class out_f(Units):
  def c(self):
      return (self.in_value * 9/5) + 32
  def k(self):
    return (self.in_value - 273.15) * 9/5 + 32 
  def eV(self):
      return (self.in_value / 1.1853248076851e+22) / (5/9) - 32

# class for electron volt unit converions
class out_eV(Units):
  def c(self):
      return self.in_value * 1.1853248076851e+22
  def f(self):
    return (self.in_value - 32) * 5/9 * 1.1853248076851e+22
  def k(self):
      return self.in_value * 8.621738e-5

# class for gram unit converions
class out_g(Units):
  def kg(self):
      return self.in_value * 1000
 
 # class for Kg volt unit converions
class out_kg(Units):
  def g(self):
      return self.in_value / 1000
  
#Calculation and conversion while loop begins Here
go = True
while go:

#Retreieves formulas options(Method) for user using an automated function
  method_list = [method for method in dir(Plasma_functions) if method.startswith('__') is False]
  print() 
  print()
  x = 0
#Prints formula names with a number so user can easily pick a formula
  for i in method_list:
    x = x + 1
    print("{})  {}".format(x,i))
  print()
  print()
  print()
#Prompts user to input what formula they want calculated
  Formula = input("Enter number of the formula you would like to calculate: ")
  
  master = {      "mm-cm":       out_cm().mm(),
                  "m-cm":         out_cm().m(),
                  "cm-m":         out_m().cm(),
                  "km-cm":        out_cm().km(),
                  "inch-cm":      out_cm().inch(),
                  "foot-cm":      out_cm().foot(),
                  "mile-cm":      out_cm().mile(),
                  "cm-mm":        out_mm().cm(),
                  "m-mm":         out_mm().m(),
                  "km-mm":        out_mm().km(),
                  "mm-km":        out_km().mm(),
                  "cm-km":        out_km().cm(),
                  "m-km":         out_km().m(),
                  "inch-km":      out_km().inch(),
                  "foot-km":      out_km().foot(),
                  "mile-km":      out_km().mile(),
                  "inch-mm":      out_mm().inch(),
                  "foot-mm":      out_mm().foot(),
                  "mile-mm":      out_mm().mile(),
                  "mm-inch":      out_inch().mm(),
                  "m-inch":       out_inch().m(),
                  "km-inch":      out_inch().km(),
                  "foot-inch":    out_inch().foot(),
                  "mile-inch":    out_inch().mile(),
                  "mm-foot":      out_foot().mm(),
                  "m-foot":       out_foot().m(),
                  "km-foot":      out_foot().km(),
                  "inch-foot":    out_foot().inch(),
                  "mile-foot":    out_foot().mile(),
                  "mm-mile":      out_mile().mm(),
                  "cm-mile":      out_mile().cm(),
                  "cm-foot":      out_foot().cm(),
                  "cm-inch":      out_inch().cm(),
                  "m-mile":       out_mile().m(),
                  "km-mile":      out_mile().km(),
                  "foot-mile":    out_mile().foot(),
                  "inch-mile":    out_mile().inch(),
                  "mm-micron":    out_micron().mm(),
                  "cm-micron":    out_micron().cm(),
                  "km-micron":    out_micron().km(),
                  "m-micron":     out_micron().m(),
                  "inch-micron":  out_micron().inch(),
                  "foot-micron":  out_micron().foot(),
                  "mile-micron":  out_micron().mile(),
                  "micron-mm":    out_mm().micron(),
                  "micron-cm":    out_cm().micron(),
                  "micron-m":     out_m().micron(),
                  "micron-km":    out_km().micron(),
                  "micron-inch":  out_inch().micron(),
                  "micron-foot":  out_foot().micron(),
                  "micron-mile":  out_mile().micron(),
                  "min-s":        out_s().min(),
                  "h-s":          out_s().h(),
                  "s-min":        out_min().s(),
                  "h-min":        out_min().h(),
                  "s-h":          out_h().s(),
                  "min-h":        out_h().min(),
                  "kg-g":         out_g().kg(),
                  "g-kg":         out_kg().g(),
                  "c-f":          out_c().f(),
                  "c-k":          out_c().k(),
                  "c-eV":         out_c().eV(),
                  "k-f":          out_k().f(),
                  "k-c":          out_k().c(),
                  "k-eV":         out_k().eV(),
                  "f-c":          out_f().c(),
                  "f-k":          out_f().k(),
                  "f-eV":         out_f().eV(),
                  "eV-f":         out_eV().f(),
                  "eV-k":         out_eV().k(),
                  "eV-c":         out_eV().c()}
              

###############################################################

#Defined the formulas to pull from functions class      
  if Formula == "2":
        in_value5 = int(input("""Enter the value for mu: """))
        in_value4 = int(input("""Enter the value for z: """))
        tagged = tuple(input("Enter the itemperature value/units separated by a space: " ).upper().split(" "))
        tagged2 = tuple(input("Enter the etemperature value/units, sperated. by a space: "))
        tagged3 = tuple(input("Enter the density value/units, sperated. by a space: "))
        in_value3 = float(tagged[0])
        uni = tagged[1].upper()
        in_value2 = float(tagged2[0])
        uni2 = tagged2[1].upper()
        in_value = float(tagged3[0])
        uni3 = tagged3[1].upper()
        x = 0 
        units_final = 0
        out_kg.set_values(x, uni, units_final, in_value)
        out_g.set_values(x, uni, units_final, in_value)
        out_eV.set_values(x, uni, units_final, in_value2)
        out_eV.set_values(x, uni, units_final, in_value3)
        
        formulas_dict = {
          "min-s":        out_s().min(),
          "h-s":          out_s().h(),
          "s-min":        out_min().s(),
          "h-min":        out_min().h(),
          "s-h":          out_h().s(),
          "min-h":        out_h().min(),
          "micron-cm":    out_cm().micron(),
          "mm-cm":        out_cm().mm(),
          "km-cm":        out_cm().km(),
          "m-cm":         out_cm().m(),
          "c-f":          out_c().f(),
          "c-k":          out_c().k(),
          "c-eV":         out_c().eV(),
          "k-f":          out_k().f(),
          "k-c":          out_k().c(),
          "k-eV":         out_k().eV(),
          "f-c":          out_f().c(),
          "f-k":          out_f().k(),
          "f-eV":         out_f().eV(),
          "eV-f":         out_eV().f(),
          "eV-k":         out_eV().k(),
          "eV-c":         out_eV().c(),
          "kg-g":         out_g().kg(),
          "g-kg":         out_kg().g(),
    }
      
        if uni  == "K":
          in_value = formulas_dict['k-eV']
        elif uni == "C":
          in_value = formulas_dict['c-eV']
        elif uni == "f":
          in_value = formulas_dict['f-eV']
        elif uni == "EV":
          in_value = in_value
        elif uni  == "K":
          in_value6 = formulas_dict['k-eV']
        elif uni == "C":
          in_value6 = formulas_dict['c-eV']
        elif uni == "f":
          in_value6 = formulas_dict['f-eV']
        elif uni == "EV":
          in_value6 = in_value

        if uni2  == "K":
          in_value = formulas_dict['k-eV']
        elif uni2 == "C":
          in_value = formulas_dict['c-eV']
        elif uni2 == "f":
          in_value = formulas_dict['f-eV']
        elif uni2 == "EV":
          in_value = in_value
        elif uni2  == "K":
          in_value6 = formulas_dict['k-eV']
        elif uni2 == "C":
          in_value6 = formulas_dict['c-eV']
        elif uni2 == "f":
          in_value6 = formulas_dict['f-eV']
        elif uni2 == "EV":
          in_value6 = in_value

        if uni3 == "G/CM^3":
          in_value = in_value  
        elif uni3 == "G/M^3":
          in_value = in_value * formulas_dict["m-cm"]
        elif uni3 == "G/KM^3":
          in_value = in_value * formulas_dict["km-cm"]
        elif uni3 == "G/MM^3":
          in_value = in_value * formulas_dict["mm-cm"]
        elif uni3 == "G/MICRON":
          in_value = in_value * formulas_dict["micron-cm"]
        elif uni3 == "KG/CM^3":
          in_value = in_value * formulas_dict["kg-g"]
        elif uni3 == "KG/M^3":
          in_value = in_value * formulas_dict["m-cm"] * formulas_dict["kg-g"]
        elif uni3 == "KG/KM^3":
          in_value = in_value * formulas_dict["km-cm"] * formulas_dict["kg-g"]
        elif uni3 == "KG/MM^3":
          in_value = in_value * formulas_dict["mm-cm"] * formulas_dict["kg-g"]
        elif uni3 == "KG/MICRON":
          in_value = in_value * formulas_dict["micron-cm"] * formulas_dict["kg-g"]
        
        final_answer = Plasma_functions.CoulLog_eiCollisions(in_value, in_value2, in_value3, in_value4, in_value5)


        final = "Here is your final answer {0:.2e}.".format(final_answer)
        print(final)     

  # Critical Electron Density
  elif Formula == "3":
    tagged = tuple(input("Enter the wavelength value and units separated by a space: ").upper().split(" "))
    print(tagged)
    in_value = float(tagged[0])
    print(in_value)
    uni = tagged[1].upper()
    x = 0
    units_final = 0

    out_micron.set_values(x, uni, units_final, in_value)
    out_cm.set_values(x, uni, units_final, in_value)
    out_m.set_values(x, uni, units_final, in_value)
    out_km.set_values(x, uni, units_final, in_value)
    out_m.set_values(x, uni, units_final, in_value)
    out_kg.set_values(x, uni, units_final, in_value)
    out_g.set_values(x, uni, units_final, in_value)

    formulas_dict = { "kg-g":         out_g().kg(),
                      "g-kg":         out_kg().g(),
                      "mm-micron":    out_micron().mm(),
                      "cm-micron":    out_micron().cm(),
                      "km-micron":    out_micron().km(),
                      "m-micron":     out_micron().m(),
                      "cm-km":        out_km().cm(),
                      "cm-m":         out_m().cm(),
                      "cm-mm":        out_mm().cm()}

    if uni == "CM":
      in_value = formulas_dict["cm-micron"]

    elif uni == "M":
      in_value = formulas_dict["m-micron"]  

    elif uni == "KM":
      in_value = formulas_dict["km-micron"]

    elif uni == "MM":
      in_value = formulas_dict["mm-micron"]
      
      
    in_value2 = Plasma_functions.CriticalElectronDensity(in_value)

    print()
    print("""Unit options:
    g/cm^3
    g/m^3
    g/mm^3
    g/km^3
    g/micron^3
    kg/cm^3
    kg/m^3
    kg/mm^3
    kg/km^3
    kg/micron^3
    """) 

    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "G/M^3":
          in_value2 = out_m().cm()

    elif units_final == "G/CM^3":
          in_value2 = Plasma_functions.CriticalElectronDensity(in_value)

    elif units_final == "G/MM^3":
          in_value2 = out_mm().cm()

    elif units_final == "G/KM^3":
          in_value2 = out_km().cm()

    elif units_final == "G/MICRON^3":
          in_value2 = in_value * 10000

    elif units_final == "KG/MICRON^3":
          in_value2 = out_kg().g() * out_micron().cm()

    elif units_final == "KG/MM^3":
          in_value2 = out_kg().g() * out_mm().cm()
          
    elif units_final == "KG/CM^3":
          in_value2 = out_kg().g() 
                
    elif units_final == "KG/M^3":
          in_value2 = out_kg().g() * out_m().cm()
                
    elif units_final == "KG/KM^3":
          out_min.set_values(x, uni, units_final, in_value2)
          in_value2 = out_kg().g() * out_km().cm()
      
    else: 
          print("Enter a valid unit")

    final = "Here is your final answer {0:.2e}, {1}.".format(in_value2, units_final)
    print(final)

  # Debye Length
  elif Formula == "4":
    print("""Enter the temperature value/units and density value/units separated by a space: """)
    tagged = tuple(input(">" ).upper().split(" "))
    in_value = float(tagged[0])
    in_value2 = float(tagged[2])
    uni = tagged[1].upper()
    uni2 = tagged[3].upper()
    x = 0
    units_final = 0
    out_g.set_values(x, uni, units_final, in_value2)
    out_eV.set_values(x, uni, units_final, in_value)
    
    formulas_dict = {
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "micron-cm":    out_cm().micron(),
      "mm-cm":        out_cm().mm(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m(),
      "c-f":          out_c().f(),
      "c-k":          out_c().k(),
      "c-eV":         out_c().eV(),
      "k-f":          out_k().f(),
      "k-c":          out_k().c(),
      "k-eV":         out_k().eV(),
      "f-c":          out_f().c(),
      "f-k":          out_f().k(),
      "f-eV":         out_f().eV(),
      "eV-f":         out_eV().f(),
      "eV-k":         out_eV().k(),
      "eV-c":         out_eV().c()
  }

    if uni == "K":
      in_value = formulas_dict['k-eV']
    elif uni == "C":
      in_value = formulas_dict['c-eV']
    elif uni == "f":
      in_value = formulas_dict['f-eV']
      
    if uni2 == "G/CM^3":
      in_value2 = in_value2
    elif uni2 == "KG/CM^3":
      in_value2 = formulas_dict['kg-g']
    
    final_answer = Plasma_functions.DebyeLength(in_value, in_value2)
    print()
    print("""Unit options:
    micron
    mm
    cm
    m
    km
    inch
    foot
    mile
    """) 

    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "MM":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm()

    elif units_final == "CM":
          final_answer = Plasma_functions.DebyeLength(in_value, in_value2)

    elif units_final == "M":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm()

    elif units_final == "MICRON":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm()

    elif units_final == "KM":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm()

    elif units_final == "INCH":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm()

    elif units_final == "FOOT":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm()
    
    elif units_final == "MILE":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm()
      
    else: 
          print("Enter a valid unit")

    final = "Here is your final answer {0:.2e}, {1}.".format(final_answer, units_final)
    print(final)

  #Electron Collision Frequency
  elif Formula == "5":
        tagged = tuple(input("Enter the density value and units separated by a space: ").upper().split(" "))
        tagged2 = tuple(input("Enter the temperature value/units separated by a space:" ).upper().split(" "))
        in_value2 = int(input("Enter Coulomg logarithm value: "))
        in_value3 = int(input("Enter Z value: "))
        in_value = float(tagged[0])
        in_value4 = float(tagged2[0])
        uni = tagged[1].upper()
        uni2 = tagged2[1].upper()
        x = 0
        units_final = 0
        out_g.set_values(x, uni, units_final, in_value2)
        out_eV.set_values(x, uni, units_final, in_value4)

        formulas_dict = {
            "g-kg":         out_kg().g(),
            "kg-g":         out_g().kg(),
            "h-s":          out_s().h(),
            "mm-cm":        out_cm().mm(),
            "km-cm":        out_cm().km(),
            "m-cm":         out_cm().m(),
            "min-s":        out_s().min(),
            "s-min":        out_min().s(),
            "h-min":        out_min().h(),
            "s-h":          out_h().s(),
            "min-h":        out_h().min(),
            "micron-cm":    out_cm().micron(),
            "c-f":          out_c().f(),
            "c-k":          out_c().k(),
            "c-eV":         out_c().eV(),
            "k-f":          out_k().f(),
            "k-c":          out_k().c(),
            "k-eV":         out_k().eV(),
            "f-c":          out_f().c(),
            "f-k":          out_f().k(),
            "f-eV":         out_f().eV(),
            "eV-f":         out_eV().f(),
            "eV-k":         out_eV().k(),
            "eV-c":         out_eV().c()
        }
      
        if uni2  == "K":
          in_value = formulas_dict['k-eV']
        elif uni2 == "C":
          in_value = formulas_dict['c-eV']
        elif uni2 == "f":
          in_value = formulas_dict['f-eV']
        elif uni2 == "EV":
          in_value = in_value
        elif uni2  == "K":
          in_value6 = formulas_dict['k-eV']
        elif uni2 == "C":
          in_value6 = formulas_dict['c-eV']
        elif uni2 == "f":
          in_value6 = formulas_dict['f-eV']
        elif uni2 == "EV":
          in_value6 = in_value

        if uni == "G/CM^3":
          in_value = in_value  
        elif uni == "G/M^3":
          den = in_value * formulas_dict["m-cm"]
        elif uni == "G/KM^3":
          den = in_value * formulas_dict["km-cm"]
        elif uni == "G/MM^3":
          in_value = in_value * formulas_dict["mm-cm"]
        elif uni == "G/MICRON":
          in_value = in_value * formulas_dict["micron-cm"]
        elif uni == "KG/CM^3":
          in_value = in_value * formulas_dict["kg-g"]
        elif uni == "KG/M^3":
          den = in_value * formulas_dict["m-cm"] * formulas_dict["kg-g"]
        elif uni == "KG/KM^3":
          den = in_value * formulas_dict["km-cm"] * formulas_dict["kg-g"]
        elif uni == "KG/MM^3":
          in_value = in_value * formulas_dict["mm-cm"] * formulas_dict["kg-g"]
        elif uni == "KG/MICRON":
          in_value = in_value * formulas_dict["micron-cm"] * formulas_dict["kg-g"]
                
        final_answer = Plasma_functions.ElectronCollisionFrequency(in_value,in_value4,in_value3, in_value2 )
        print()
        print("""Unit options:
        rad/min
        rad/s
        rad/h
        """) 

        units_final = input("What units would you like the answer in?: ").upper()

        if units_final == "RAD/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_min().s()

        elif units_final == "RAD/S":
              final_answer = final_answer

        elif units_final == "RAD/H":
              out_h.set_values(x, uni, units_final, final_answer)
              final_asnwer = out_h().s()
          
        else: 
              print("Enter a valid unit")

        final = "Here is your final answer {0:.2e}, {1}.".format(final_answer, units_final)
        print(final)

  #Ion Plasma
  elif Formula == "8":
      tagged = tuple(input("Enter the density value and units separated by a space: ").upper().split(" "))
      in_value2 = int(input("Enter mu value: "))
      in_value3 = int(input("Enter Z value: "))
      in_value = float(tagged[0])
      uni = tagged[1].upper()
      x = 0
      units_final = 0

      out_micron.set_values(x, uni, units_final, in_value)

      formulas_dict = {
        "g-kg":         out_kg().g(),
        "kg-g":         out_g().kg(),
        "min-s":        out_s().min(),
        "h-s":          out_s().h(),
        "s-min":        out_min().s(),
        "h-min":        out_min().h(),
        "s-h":          out_h().s(),
        "min-h":        out_h().min(),
        "mm-cm":        out_cm().mm(),
        "micron-cm":    out_cm().micron(),
        "km-cm":        out_cm().km(),
        "m-cm":         out_cm().m()
    }
      
      if uni == "G/CM^3":
        in_value = in_value  
      elif uni == "G/M^3":
        den = in_value * formulas_dict["m-cm"]
      elif uni == "G/KM^3":
        den = in_value * formulas_dict["km-cm"]
      elif uni == "G/MM^3":
        in_value = in_value * formulas_dict["mm-cm"]
      elif uni == "G/MICRON":
        in_value = in_value * formulas_dict["micron-cm"]
      elif uni == "KG/CM^3":
        in_value = in_value * formulas_dict["kg-g"]
      elif uni == "KG/M^3":
        den = in_value * formulas_dict["m-cm"] * formulas_dict["kg-g"]
      elif uni == "KG/KM^3":
        den = in_value * formulas_dict["km-cm"] * formulas_dict["kg-g"]
      elif uni == "KG/MM^3":
        in_value = in_value * formulas_dict["mm-cm"] * formulas_dict["kg-g"]
      elif uni == "KG/MICRON":
        in_value = in_value * formulas_dict["micron-cm"] * formulas_dict["kg-g"]
              
      final_answer = Plasma_functions.IonPlasma(in_value,in_value3,in_value2 )
      print()
      print("""Unit options:
      rad/min
      rad/s
      rad/h
      """) 

      units_final = input("What units would you like the answer in?: ").upper()

      if units_final == "RAD/MIN":
            out_min.set_values(x, uni, units_final, final_answer)
            final_answer = out_min().s()

      elif units_final == "RAD/S":
            final_answer = final_answer

      elif units_final == "RAD/H":
            out_min.set_values(x, uni, units_final, final_answer)
            final_asnwer = out_h().s()
        
      else: 
            print("Enter a valid unit")

      final = "Here is your final answer {0:.2e}, {1}.".format(final_answer, units_final)
      print(final)

  #Electron Thermal Velocity
  elif Formula == "7":
    tagged = tuple(input("Enter the temperature value/units separated by a space:>" ).upper().split(" "))
    in_value = float(tagged[0])
    uni = tagged[1].upper()
    x = 0
    units_final = 0
    out_eV.set_values(x, uni, units_final, in_value)
    
    formulas_dict = {
      "micron-cm":    out_cm().micron(),
      "mm-cm":        out_cm().mm(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m(),
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "c-f":          out_c().f(),
      "c-k":          out_c().k(),
      "c-eV":         out_c().eV(),
      "k-f":          out_k().f(),
      "k-c":          out_k().c(),
      "k-eV":         out_k().eV(),
      "f-c":          out_f().c(),
      "f-k":          out_f().k(),
      "f-eV":         out_f().eV(),
      "eV-f":         out_eV().f(),
      "eV-k":         out_eV().k(),
      "eV-c":         out_eV().c()
  }

    if uni == "K":
      in_value = formulas_dict['k-eV']
    elif uni == "C":
      in_value = formulas_dict['c-eV']
      print(in_value)
    elif uni == "f":
      in_value = formulas_dict['f-eV']
    
        
    final_answer = Plasma_functions.ElectronThermalVelocity(in_value)
    print()
    print("""Unit options:
    micron/s
    mm/s
    cm/s
    m/s
    km/s
    inch/s
    foot/s
    mile/s
    micron/min
    mm/min
    cm/min
    m/min
    km/min
    inch/min
    foot/min
    mile/min
    micron/h
    mm/h
    cm/h
    m/h
    km/h
    inch/h
    foot/h
    mile/h
    """) 
  
    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "MICRON/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm()

    elif units_final == "CM/S":
          final_answer = Plasma_functions.ElectronThermalVelocity(in_value)

    elif units_final == "MM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm()

    elif units_final == "M/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm()

    elif units_final == "KM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm()

    elif units_final == "INCH/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm()

    elif units_final == "FOOT/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm()
    
    elif units_final == "MILE/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm()

    elif units_final == "MICRON/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-min"]

    elif units_final == "CM/MIN":
          final_answer = Plasma_functions.ElectronThermalVelocity(in_value) * formulas_dict["s-min"]

    elif units_final == "MM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-min"]
 
    elif units_final == "M/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-min"]

    elif units_final == "KM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-min"]

    elif units_final == "INCH/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-min"]

    elif units_final == "FOOT/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-min"]
    
    elif units_final == "MILE/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-min"]

    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.ElectronThermalVelocity(in_value) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]
    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.ElectronThermalVelocity(in_value) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]

    else: 
          print(" ")

    final = "Here is your final answer {0:.2e}.".format(final_answer)
    print(final)

  #Electron Plasma 
  elif Formula == "6":
    tagged = tuple(input("Enter the density value and units separated by a space: ").upper().split(" "))
    in_value = float(tagged[0])
    uni = tagged[1].upper()
    x = 0
    units_final = 0

    out_micron.set_values(x, uni, units_final, in_value)

    formulas_dict = {
      "g-kg":         out_kg().g(),
      "kg-g":         out_g().kg(),
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "mm-cm":        out_cm().mm(),
      "micron-cm":    out_cm().micron(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m()
  }
    if uni == "G/CM^3":
      in_value = in_value  
    elif uni == "G/M^3":
      den = in_value * formulas_dict["m-cm"]
    elif uni == "G/KM^3":
      den = in_value * formulas_dict["km-cm"]
    elif uni == "G/MM^3":
      in_value = in_value * formulas_dict["mm-cm"]
    elif uni == "G/MICRON":
      in_value = in_value * formulas_dict["micron-cm"]
    elif uni == "KG/CM^3":
      in_value = in_value * formulas_dict["kg-g"]
    elif uni == "KG/M^3":
      den = in_value * formulas_dict["m-cm"] * formulas_dict["kg-g"]
    elif uni == "KG/KM^3":
      den = in_value * formulas_dict["km-cm"] * formulas_dict["kg-g"]
    elif uni == "KG/MM^3":
      in_value = in_value * formulas_dict["mm-cm"] * formulas_dict["kg-g"]
    elif uni == "KG/MICRON":
      in_value = in_value * formulas_dict["micron-cm"] * formulas_dict["kg-g"]
            
    in_value2 = Plasma_functions.ElectronPlasma(in_value)
    
    #print(in_value2)
    print()
    print("""Unit options:
    rad/min
    rad/s
    rad/h
    """) 

    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "RAD/MIN":
          out_min.set_values(x, uni, units_final, in_value2)
          in_value2 = out_min().s()

    elif units_final == "RAD/S":
          in_value2 = Plasma_functions.ElectronPlasma(in_value)

    elif units_final == "RAD/H":
          out_min.set_values(x, uni, units_final, in_value2)
          in_value2 = out_h().s()
      
    else: 
          print("Enter a valid unit")

    final = "Here is your final answer {0:.2e}, {1}.".format(in_value2, units_final)
    print(final)

  elif Formula == "10":
    tagged = tuple(input("Enter the temperature value/units separated by a space: " ).upper().split(" "))
    in_value2 = int(input("Enter mu value: "))
    in_value = int(tagged[0])
    uni = tagged[1].upper()
    x = 0
    units_final = 0
    out_eV.set_values(x, uni, units_final, in_value)
    
    formulas_dict = {
      "micron-cm":    out_cm().micron(),
      "mm-cm":        out_cm().mm(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m(),
      "cm-mile":      out_mile().cm(),
      "cm-foot":      out_foot().cm(),
      "cm-inch":      out_inch().cm(),
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "c-f":          out_c().f(),
      "c-k":          out_c().k(),
      "c-eV":         out_c().eV(),
      "k-f":          out_k().f(),
      "k-c":          out_k().c(),
      "k-eV":         out_k().eV(),
      "f-c":          out_f().c(),
      "f-k":          out_f().k(),
      "f-eV":         out_f().eV(),
      "eV-f":         out_eV().f(),
      "eV-k":         out_eV().k(),
      "eV-c":         out_eV().c()
  }

    if uni == "K":
      in_value = formulas_dict['k-eV']
    elif uni == "C":
      in_value = formulas_dict['c-eV']
      print(in_value)
    elif uni == "f":
      in_value = formulas_dict['f-eV']
    
        
    final_answer = Plasma_functions.IonThermalVelocity(in_value, in_value2)
    print()
    print("""Unit options:
    micron/s
    mm/s
    cm/s
    m/s
    km/s
    inch/s
    foot/s
    mile/s
    micron/min
    mm/min
    cm/min
    m/min
    km/min
    inch/min
    foot/min
    mile/min
    micron/h
    mm/h
    cm/h
    m/h
    km/h
    inch/h
    foot/h
    mile/h
    """) 
  
    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "MICRON/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm()

    elif units_final == "CM/S":
          final_answer = Plasma_functions.IonThermalVelocity(in_value, in_value2)

    elif units_final == "MM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm()

    elif units_final == "M/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm()

    elif units_final == "KM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm()

    elif units_final == "INCH/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm()

    elif units_final == "FOOT/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm()
    
    elif units_final == "MILE/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm()

    elif units_final == "MICRON/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-min"]

    elif units_final == "CM/MIN":
          final_answer = Plasma_functions.IonThermalVelocity(in_value, in_value2) * formulas_dict["s-min"]

    elif units_final == "MM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-min"]
 
    elif units_final == "M/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-min"]

    elif units_final == "KM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-min"]

    elif units_final == "INCH/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-min"]

    elif units_final == "FOOT/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-min"]
    
    elif units_final == "MILE/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-min"]

    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.IonThermalVelocity(in_value, in_value2) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]
    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.IonThermalVelocity(in_value, in_value2) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]

    else: 
          print(" ")

    final = "Here is your final answer {0:.2e}.".format(final_answer)
    print(final)
    
  #Laser Frequency
  elif Formula == "11":
    tagged = tuple(input("Enter the wavelength value and units separated by a space: ").upper().split(" "))
    print(tagged)
    in_value = float(tagged[0])
    print(in_value)
    uni = tagged[1].upper()
    x = 0
    units_final = 0

    formulas_dict = {
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "mm-micron":    out_micron().mm(),
      "cm-micron":    out_micron().cm(),
      "km-micron":    out_micron().km(),
      "m-micron":     out_micron().m()
  }

    out_micron.set_values(x, uni, units_final, in_value)

    if uni == "CM":
      in_value = master["cm-micron"]
    elif uni == "M":
      in_value = formulas_dict["m-micron"]  
    elif uni == "KM":
      in_value = formulas_dict["km-micron"]
    elif uni == "MM":
      in_value = formulas_dict["mm-micron"] 

    in_value2 = Plasma_functions.LaserFrequency(in_value)
    
    print()
    print("""Unit options:
    rad/min
    rad/s
    rad/h
    """) 

    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "RAD/MIN":
          out_min.set_values(x, uni, units_final, in_value2)
          in_value2 = out_min().s()

    elif units_final == "RAD/S":
          in_value2 = Plasma_functions.LaserFrequency(in_value)

    elif units_final == "RAD/H":
          out_min.set_values(x, uni, units_final, in_value2)
          in_value2 = out_h().s()
      
    else: 
          print("Enter a valid unit")

    final = "Here is your final answer {0:.2e}, {1}.".format(in_value2, units_final)
    print(final)

  # Number of Electrons In Debye Sphere
  elif Formula == "12":
    print("""Enter the temperature value/units and density value/units separated by a space: """)
    tagged = tuple(input(">" ).upper().split(" "))
    in_value = float(tagged[0])
    in_value2 = float(tagged[2])
    uni = tagged[1].upper()
    uni2 = tagged[3].upper()
    x = 0
    units_final = 0
    out_g.set_values(x, uni, units_final, in_value2)
    out_eV.set_values(x, uni, units_final, in_value)
    
    formulas_dict = {
      "g-kg":         out_kg().g(),
      "kg-g":         out_g().kg(),
      "micron-cm":    out_cm().micron(),
      "mm-cm":        out_cm().mm(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m(),
      "c-f":          out_c().f(),
      "c-k":          out_c().k(),
      "c-eV":         out_c().eV(),
      "k-f":          out_k().f(),
      "k-c":          out_k().c(),
      "k-eV":         out_k().eV(),
      "f-c":          out_f().c(),
      "f-k":          out_f().k(),
      "f-eV":         out_f().eV(),
      "eV-f":         out_eV().f(),
      "eV-k":         out_eV().k(),
      "eV-c":         out_eV().c()
  }

    if uni == "K":
      in_value = formulas_dict['k-eV']
    elif uni == "C":
      in_value = formulas_dict['c-eV']
    elif uni == "f":
      in_value = formulas_dict['f-eV']
    if uni2 == "G/CM^3":
      in_value = in_value
    elif uni2 == "KG/CM^3":
      in_value = formulas_dict['kg-g']
    
    final_answer = Plasma_functions.NumberOfElectronsInDebyeSphere(in_value)
    
    final = "Here is your final answer {0:.2e}.".format(final_answer)
    print(final)

  # Oscillatory Velocity
  elif Formula == "13":
    print("""Enter the wavelength value/units and intensity value/units separated by a space: """)
    tagged = tuple(input(">" ).upper().split(" "))
    in_value = float(tagged[0])
    in_value2 = float(tagged[2])
    uni = tagged[1].upper()
    uni2 = tagged[3].upper()
    x = 0
    units_final = 0
    out_micron.set_values(x, uni, units_final,in_value)
    formulas_dict = {
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "mm-micron":    out_micron().mm(),
      "cm-micron":    out_micron().cm(),
      "km-micron":    out_micron().km(),
      "m-micron":     out_micron().m()
  }

    if uni == "CM":
      in_value = formulas_dict["cm-micron"]

    elif uni == "M":
      in_value = formulas_dict["m-micron"]  

    elif uni == "KM":
      in_value = formulas_dict["km-micron"]

    elif uni == "MM":
      in_value = formulas_dict["mm-micron"]  
      
    if uni2 == "W/M^2":
      in_value2 = in_value2 / 10000
      print(in_value2)

    elif uni2 == "W/KM^2":
      in_value2 = in_value2 / 100000000000

    elif uni2 == "W/MM^2":
      in_value2 = in_value2 * 100

    elif uni2 == "W/CM^3":
      in_value2 = in_value2

    in_value = Plasma_functions.OscillatoryVelocity(in_value2, in_value)
    print(in_value)
    print()
    print("""Unit options:
    cm/sec
    m/sec
    cm/min
    m/min
    """) 
  
    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "M/SEC":
          in_value = in_value / 100 

    elif units_final == "CM/MIN":
          in_value = in_value * 60 

    elif units_final == "M/MIN":
          in_value = in_value / 1.667

  #Ion sound speed and cold ion sound speed  
  elif Formula == "1" or "9":
    in_value2 = int(input("""Enter the value for Z: """))
    in_value3 = int(input("""Enter the value for mu: """))
    in_value4 = int(input("""Enter the value for gamma: """))
    tagged = tuple(input("Enter the temperature value/units: " ).upper().split(" "))
    in_value = float(tagged[0])
    uni = tagged[1].upper()
    x = 0
    units_final = 0
    out_eV.set_values(x, uni, units_final, in_value)
    
    formulas_dict = {
      "min-s":        out_s().min(),
      "h-s":          out_s().h(),
      "s-min":        out_min().s(),
      "h-min":        out_min().h(),
      "s-h":          out_h().s(),
      "min-h":        out_h().min(),
      "micron-cm":    out_cm().micron(),
      "mm-cm":        out_cm().mm(),
      "km-cm":        out_cm().km(),
      "m-cm":         out_cm().m(),
      "c-f":          out_c().f(),
      "c-k":          out_c().k(),
      "c-eV":         out_c().eV(),
      "k-f":          out_k().f(),
      "k-c":          out_k().c(),
      "k-eV":         out_k().eV(),
      "f-c":          out_f().c(),
      "f-k":          out_f().k(),
      "f-eV":         out_f().eV(),
      "eV-f":         out_eV().f(),
      "eV-k":         out_eV().k(),
      "eV-c":         out_eV().c()
}
  
    if uni == "K":
      in_value = formulas_dict['k-eV']
    elif uni == "C":
      in_value = formulas_dict['c-eV']
    elif uni == "f":
      in_value = formulas_dict['f-eV']
    elif uni == "EV":
      in_value = in_value
        
    final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4)
    print()
    print("""Unit options:
    micron/s
    mm/s
    cm/s
    m/s
    km/s
    inch/s
    foot/s
    mile/s
    micron/min
    mm/min
    cm/min
    m/min
    km/min
    inch/min
    foot/min
    mile/min
    micron/h
    mm/h
    cm/h
    m/h
    km/h
    inch/h
    foot/h
    mile/h
    """) 
  
    units_final = input("What units would you like the answer in?: ").upper()

    if units_final == "MICRON/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm()

    elif units_final == "CM/S":
          final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4)

    elif units_final == "MM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm()

    elif units_final == "M/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm()

    elif units_final == "KM/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm()

    elif units_final == "INCH/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm()

    elif units_final == "FOOT/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm()
    
    elif units_final == "MILE/S":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm()

    elif units_final == "MICRON/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-min"]

    elif units_final == "CM/MIN":
          final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-min"]

    elif units_final == "MM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-min"]
 
    elif units_final == "M/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-min"]

    elif units_final == "KM/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-min"]

    elif units_final == "INCH/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-min"]

    elif units_final == "FOOT/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-min"]
    
    elif units_final == "MILE/MIN":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-min"]

    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]
    elif units_final == "MICRON/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_micron().cm() * formulas_dict["s-h"]

    elif units_final == "CM/H":
          final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-h"]

    elif units_final == "MM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mm().cm() * formulas_dict["s-h"]
 
    elif units_final == "M/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_m().cm() * formulas_dict["s-h"]

    elif units_final == "KM/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_km().cm() * formulas_dict["s-h"]

    elif units_final == "INCH/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_inch().cm() * formulas_dict["s-h"]

    elif units_final == "FOOT/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_foot().cm() * formulas_dict["s-h"]
    
    elif units_final == "MILE/H":
          out_min.set_values(x, uni, units_final, final_answer)
          final_answer = out_mile().cm() * formulas_dict["s-h"]

    else: 
          print(" ")

    if Formula == "1":
      final = "Here is your final answer {0:.2e}, {1}.".format(final_answer, units_final)
      print(final)

    Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) 

    if Formula == "9":
        in_value6 = in_value2 #z
        in_value7 = in_value3 #mu
        in_value8 = int(input("""Enter the value for gammaE: """))
        in_value9 = int(input("""Enter the value for gammaI: """))
        tagged = tuple(input("Enter the itemperature value/units separated by a space: " ).upper().split(" "))
        tagged2 = tuple(input("Enter the etemperature value/units, sperated. by a space: "))
        in_value5 = float(tagged[0])
        uni = tagged[1].upper()
        in_value10 = float(tagged2[0])
        uni2 = tagged2[1].upper()
        x = 0
        units_final = 0
        out_eV.set_values(x, uni, units_final, in_value)
        
        formulas_dict = {
          "min-s":        out_s().min(),
          "h-s":          out_s().h(),
          "s-min":        out_min().s(),
          "h-min":        out_min().h(),
          "s-h":          out_h().s(),
          "min-h":        out_h().min(),
          "micron-cm":    out_cm().micron(),
          "mm-cm":        out_cm().mm(),
          "km-cm":        out_cm().km(),
          "m-cm":         out_cm().m(),
          "c-f":          out_c().f(),
          "c-k":          out_c().k(),
          "c-eV":         out_c().eV(),
          "k-f":          out_k().f(),
          "k-c":          out_k().c(),
          "k-eV":         out_k().eV(),
          "f-c":          out_f().c(),
          "f-k":          out_f().k(),
          "f-eV":         out_f().eV(),
          "eV-f":         out_eV().f(),
          "eV-k":         out_eV().k(),
          "eV-c":         out_eV().c()
    }
      
        if uni  == "K":
          in_value = formulas_dict['k-eV']
        elif uni == "C":
          in_value = formulas_dict['c-eV']
        elif uni == "f":
          in_value = formulas_dict['f-eV']
        elif uni == "EV":
          in_value = in_value
        elif uni2  == "K":
          in_value6 = formulas_dict['k-eV']
        elif uni2 == "C":
          in_value6 = formulas_dict['c-eV']
        elif uni2 == "f":
          in_value6 = formulas_dict['f-eV']
        elif uni2 == "EV":
          in_value6 = in_value
        
        final_answer = Plasma_functions.IonSoundSpeed(in_value6, in_value, in_value2, in_value3, in_value4, in_value5)
        print()
        print("""Unit options:
        micron/s
        mm/s
        cm/s
        m/s
        km/s
        inch/s
        foot/s
        mile/s
        micron/min
        mm/min
        cm/min
        m/min
        km/min
        inch/min
        foot/min
        mile/min
        micron/h
        mm/h
        cm/h
        m/h
        km/h
        inch/h
        foot/h
        mile/h
        """) 
      
        units_final = input("What units would you like the answer in?: ").upper()

        if units_final == "MICRON/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_micron().cm()

        elif units_final == "CM/S":
              final_answer = Plasma_functions.IonSoundSpeed(in_value6, in_value, in_value2, in_value3, in_value4, in_value5)

        elif units_final == "MM/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mm().cm()

        elif units_final == "M/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_m().cm()

        elif units_final == "KM/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_km().cm()

        elif units_final == "INCH/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_inch().cm()

        elif units_final == "FOOT/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_foot().cm()
        
        elif units_final == "MILE/S":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mile().cm()

        elif units_final == "MICRON/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_micron().cm() * formulas_dict["s-min"]

        elif units_final == "CM/MIN":
              final_answer = Plasma_functions.IonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-min"]

        elif units_final == "MM/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mm().cm() * formulas_dict["s-min"]
    
        elif units_final == "M/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_m().cm() * formulas_dict["s-min"]

        elif units_final == "KM/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_km().cm() * formulas_dict["s-min"]

        elif units_final == "INCH/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_inch().cm() * formulas_dict["s-min"]

        elif units_final == "FOOT/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_foot().cm() * formulas_dict["s-min"]
        
        elif units_final == "MILE/MIN":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mile().cm() * formulas_dict["s-min"]

        elif units_final == "MICRON/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_micron().cm() * formulas_dict["s-h"]

        elif units_final == "CM/H":
              final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-h"]

        elif units_final == "MM/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mm().cm() * formulas_dict["s-h"]
    
        elif units_final == "M/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_m().cm() * formulas_dict["s-h"]

        elif units_final == "KM/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_km().cm() * formulas_dict["s-h"]

        elif units_final == "INCH/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_inch().cm() * formulas_dict["s-h"]

        elif units_final == "FOOT/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_foot().cm() * formulas_dict["s-h"]
        
        elif units_final == "MILE/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mile().cm() * formulas_dict["s-h"]
        elif units_final == "MICRON/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_micron().cm() * formulas_dict["s-h"]

        elif units_final == "CM/H":
              final_answer = Plasma_functions.ColdIonSoundSpeed(in_value, in_value2, in_value3, in_value4) * formulas_dict["s-h"]

        elif units_final == "MM/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mm().cm() * formulas_dict["s-h"]
    
        elif units_final == "M/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_m().cm() * formulas_dict["s-h"]

        elif units_final == "KM/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_km().cm() * formulas_dict["s-h"]

        elif units_final == "INCH/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_inch().cm() * formulas_dict["s-h"]

        elif units_final == "FOOT/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_foot().cm() * formulas_dict["s-h"]
        
        elif units_final == "MILE/H":
              out_min.set_values(x, uni, units_final, final_answer)
              final_answer = out_mile().cm() * formulas_dict["s-h"]
          
        else: 
              print("Enter a valid unit")

        final = "Here is your final answer {0:.2e}, {1}.".format(final_answer, units_final)
        print(final) 
    else: 
          print("Enter a valid unit")       
    
    print("Here is your final answer {}, {}." . format(in_value, units_final))

  stop = input("Stop the program?: Y/N ")
  if stop.upper() == "Y":
        go = False
  elif stop.upper() == "N":
        go = True
  else:
        print("enter Y of yes and N for no")   