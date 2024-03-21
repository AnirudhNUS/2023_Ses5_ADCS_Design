import math
import numpy as np

class RWvals:
#this class contains reaction wheel related information
# Variables
    Rwheel, Mwheel, MOIwheel, maxPwheel, clstruc = 0.0, 0.0, 0.0, 0.0, 0.0

# Functions
    # Note that this only works if every single value used here is calculated within this function. 
    # If we try to use any existing values of variables, we get the 0.0 that we put in the initialization. 

    def Wheelcalc_int(self, side, hwheel, clwheel, clwall, rho, rpm, Dmagcover, name):
        # this function calculates intermediate values for the wheel
        self.Rwheel = (side-hwheel-clwheel)/2 - clwall      # use self.___ to refer to values of this class variable
        '''
        minimum rwheel is lmot+gmot+rmot+clwheel = 2+1+1.5+0.4 = 4.9cm
        if rwheel<4.9 give warning
        '''
        if (self.Rwheel < 4.9):
            print("WARNING for side length: ",side)
            print("Rwheel is smaller than minimum possible value. Use Rwheel = 4.9cm instead. Increase box size accordingly.")
    
        self.Mwheel = rho*math.pi*self.Rwheel*self.Rwheel*hwheel
        self.MOIwheel = (self.Mwheel*self.Rwheel*self.Rwheel)/2
        self.maxPwheel = (self.MOIwheel*rpm*math.pi)/30     # RPM/60 = RPS | RPS*2pi = rad/s | RPM*pi/30 = rad/s

        self.clstruc = (self.Rwheel+clwall-(Dmagcover/2))*math.sqrt(2) - (self.Rwheel+Dmagcover/2)

        if (self.clstruc < clwall):
            print("WARNING for side length: ",side)
            print("clstruc is smaller than clwall, reduce wheel size to ", self.Rwheel-0.2)
        
        print("\nThe values for box size ", side ,"cm are:")
        print("Rwheel (cm): ",self.Rwheel)
        print("Mwheel (g): ",self.Mwheel)
        print("MOIWheel (g cm^2): ",self.MOIwheel)
        print("maxPwheel (g cm^2 rad/s): ",self.maxPwheel)
        print("clstruc (cm): ",self.clstruc)

        outdat = open(name,'a')  # open outdat in append

        outdat.write(str(side) + "\t\t" + str(round(self.Rwheel,3)) + "\t\t" + str(round(self.Mwheel,2)) + "\t\t")
        outdat.write(str(round(self.MOIwheel,2)) + "\t\t" + str(round(self.maxPwheel,2)) + "\t\t" + str(round(self.clstruc,3)) + '\n')
        outdat.close()    # all values kept in CGS units

#########################################################################################################
        # change of class #
#########################################################################################################


class Magvals:
#this class contains magnetorquer related information
# Variables
    Lcore, Nd, resNeeded, minWlen, wlen, Iactual, moment = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0   # float values
    numLayers, turnsPL = 0, 0    # integer values

#########################################################################################################
# Functions
    def magcalc_int(self, side, Dmagcover, Lcap, Rcore, Voltage, twire, Imax, wireResist, uperm, name):
        self.Lcore = side - Dmagcover - 2*Lcap            # use self.___ to refer to values of this class variable
        temp = 4*math.log(self.Lcore/Rcore)
        self.Nd = (temp-4)/(math.pow((self.Lcore/Rcore),2) - temp)
        self.resNeeded = Voltage/Imax
        self.minWlen = 100*(self.resNeeded/wireResist)    # wire length in cm
        self.turnsPL = math.floor(self.Lcore/twire)  
        # max possible number of turns per layer filling everything
        self.wlen = 0.0
        self.numLayers = 0
        r = Rcore + twire/2   # radius in cm twire in cm

        while((self.wlen < self.minWlen) & (self.numLayers < 7)):   # max number of layers is 6
            self.wlen = self.wlen + 2*math.pi*r*self.turnsPL   # wire length in cm
            self.numLayers = self.numLayers+1
            r = r + twire/2
                
        self.Iactual = (Voltage*100)/(self.wlen*wireResist)     
        # wire resistance in m length in cm, compensated with 100*. Now current in A
        
        temp = 1 + (uperm - 1)/(1 + (uperm-1)*self.Nd)
        self.moment = (self.numLayers*math.pi*Rcore*Rcore*self.turnsPL*self.Iactual*temp)/10000    
        # moment in A cm^2 originally, then divided by 10,000 to get in A m^2

        print("\nNumber of layers: ", self.numLayers)
        print("Resistance needed (ohm): ", self.resNeeded)
        print("Actual resistance (ohm): ", self.wlen*wireResist)
        print("Total wire length (m): ", (self.wlen/100))   # wire length was originally in cm
        print("Actual current (A): ", self.Iactual)
        print("Total moment (Am^2): ", self.moment)

        
        outdat = open(name,'a')  # open outdat in append

        outdat.write(str(side) + "\t\t" + str(round(self.Lcore,3)) + "\t\t" + str(self.turnsPL) + "\t\t" + str(self.numLayers) + "\t\t")
        outdat.write(str(round((self.wlen/100),2)) + "\t\t" + str(round(self.Iactual,4)) + "\t\t" + str(round(self.moment,4)) + '\n')
        outdat.close()

########################################################################################################################################
   # finish #
########################################################################################################################################
