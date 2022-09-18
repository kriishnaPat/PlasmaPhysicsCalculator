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

    def vOscillatory(intensity,wavelength):
        """ The (maximum) oscillatory velocity of an electron in 
            the field of an EM wave (non-relativistic)
            
            wavelength in microns
            intensity in W/cm^2
            
            Returns the velocity in cm/sec
        """

        vOsc = 8.095e8*np.sqrt(1.e-15*intensity)*wavelength  # cm/sec

        return vOsc

        
    def DebyeLength(temperature, density):
        """ The Debye length for electrons. 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            temperture in eV
            density in 1/cm^3
            
            Returns the Debye length in cm
        """

        debye = 7.43e2*np.sqrt(temperature)/np.sqrt(density)

        return debye


    def numInDebyeSphere(temperature, density):
        """ The number of electrons in a Debye sphere. 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            temperture in eV
            density in 1/cm^3
            
            Returns the dimensionless number
        """

        numInSphere = 1.72e9*np.sqrt(temperature)*temperature/np.sqrt(density)

        return numInSphere


    def electronPlasma(density):
        """ The electron plasma frequency 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            density in 1/cm^3
            
            Returns the electron plasma frequency in radians per second
        """

        ePlasma = 5.64e4*np.sqrt(density)

        return ePlasma

    def ionPlasma(ionDensity,Z,mu):
        """ The ion plasma frequency 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            density in 1/cm^3
            
            Returns the ion plasma frequency in radians per second
        """

        iPlasma = 1.32e3*Z*np.sqrt(ionDensity)/np.sqrt(mu)

        return iPlasma


    def electronCollisionFreq(density,temperature,Z,coulLog):
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


    def CoulLog_ei(density,etemp,itemp,Z,mu):
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


    def electronThermal(temperature):
        """ The electron thermal velocity 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            temperature in eV
            
            Returns the electron thermal velocity in cm per second
        """

        eThermal = 4.19e7*np.sqrt(temperature)

        return eThermal


    def ionThermal(temperature,mu):
        """ The ion thermal velocity 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            temperature in eV
            mu is ion mass in units of the proton mass (atomic number)
            
            Returns the ion thermal velocity in cm per second
        """

        iThermal = 9.79e5*np.sqrt(temperature)/np.sqrt(mu)

        return iThermal


    def coldIonSoundSpeed(temperature,Z,mu,gamma):
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


    def soundSpeed(eTemp,iTemp,Z,mu,gammaE,gammaI):
        """ The ion sound speed
            
            eTemp is electron temperature in eV
            iTemp is ion temperature in eV
            Z is the ion charge
            mu is the ion mass in units of proton mass (atomic number)
            gammaE is the electron adiabatic index (1 is isothermal)
            gammaI is the ion adiabatic index (3 is 1-D)
            
            Returns the ion sound speed in cm per second
        """

        ionSound = Plasma_functions.coldIonSoundSpeed(eTemp,Z,mu,gammaE)*np.sqrt(1.0+gammaI*iTemp/gammaE/Z/eTemp)

        return ionSound


    def criticalDensity(wavelength):
        """ The critical electron density. 
            Taken from the NRL plasma formulary, J.D. Huber 2007.
            
            Laser wavelength in microns
            
            Returns the density in 1/cm^3
        """

        ncrit = 1.1e21/(wavelength**2)

        return ncrit

# parent class for lenth unit conversions
class Units:
     in_unit = 0
     out_unit = 0
     in_value = 0
     def set_values(self, in_unit, out_unit, in_value):
        Units.in_u = in_unit
        Units.out_u = out_unit
        Units.in_value = in_value

class out_micron(Units):
    def mm(self):
        return self.in_value * 1000
    def cm(self):
        return self.in_value * 10000
    def m(self):
        return self.in_value * 1000000
    def km(self):
        return self.in_value * 1000000000

# class for minute unit conversions      
class out_min(Units):
    def s (self):
        return self.in_value / 60
    def h (self):
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

## overwrite "in_value" here so the classes will effect the following statments
        if uni == "CM":
          in_value = formulas_dict["cm-micron"]
          print(in_value)

        elif uni == "M":
          in_value = formulas_dict["m-micron"]  
          #print(new1)

        elif uni == "KM":
          in_value = formulas_dict["km-micron"]
          #print(new2)

        elif uni == "MM":
          in_value = formulas_dict["mm-micron"]    
          #print(new3)       
      
      
        in_value = Plasma_functions.laserFrequency(in_value)
        print("""Unit options:
        rad/min
        rad/s
        Hz
        """) 
      
        units_final = input("What units would you like the answer in?: ").upper()
    

        if units_final == "RAD/MIN":
              new1 =  formulas_dict["s-min"]
              
              print(new1)

        elif units_final == "RAD/S":
              new1 = Plasma_functions.laserFrequency(in_value)

        elif units_final == "HZ":
              new1 = formulas_dict["rads/sec-hz"]
              #print(new)
          
        else: 
              print("Enter a valid unit")

        print("Here is your final answer {}, {}." . format(new1, units_final))

        

        stop = input("Stop the program?: Y/N ")
        if stop.upper() == "Y":
              go = False
        elif stop.upper() == "N":
              go = True
        else:
              print("enter Y of yes and N for no")                                                      