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
    def micron(self):
        return self.in_value / 1000
        
class out_cm(Length):
    def mm(self):
        return self.in_value * 10
    def m(self):
        return self.in_value / 100
    def km(self):
        return self.in_value / 100000
    def micron(self):
        return self.in_value /10000

class out_m(Length):
    def mm(self):
        return self.in_value * 1000
    def cm(self):
        return self.in_value / 100
    def km(self):
        return self.in_value * 1000
    def micron(self):
        return self.in_value /1000000

class out_km(Length):
    def mm(self):
        return self.in_value / 1000000
    def cm(self):
        return self.in_value / 100000
    def m(self):
        return self.in_value / 1000
    def micron(self):
        return self.in_value /1000000000

"mm-cm":         out_cm().mm(),
                  "m-cm":         out_cm().m(),
                  "km-cm":        out_cm().km(),
                  "micron-cm":    out_cm().micron(),
                  "cm-mm":        out_mm().cm(),
                  "m-mm":         out_mm().m(),
                  "km-mm":        out_mm().km(),
                  "micron-mm":    out_mm().micron(),
                  "mm-km":        out_km().mm(),
                  "cm-km":        out_km().cm(),
                  "m-km":         out_km().m(),
                  "micron-km":    out_km().micron(),