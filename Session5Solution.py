import numpy as np
# import matplotlib.pyplot as plt

import reader
import calculator
# import writer

class adcspackage:
# this class has the main output values including the final values of the other 2 classes
# Variables
    side, maxPwheel, moment, FOSrw, FOSmag, minrpm = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

#########################################################################################################

rpm, hwheel, rho, clwheel, clwall, Rmot, Lmot, gmot = reader.read_motinps()

minp, maxp = reader.read_TPvals()

Rcore, Dmagcover, tstruct, Lcap, Voltage, Uperm, rhocore, twire, Imax, wireResist = reader.read_mag()

Pvals = np.linspace(minp,maxp,5)        # max range of values with ours in the center
boxside = np.linspace(11,15,5)          # give 11-15 to give our target 13 in center
momentneeded = np.linspace(0.2,0.6,5)   # give values 0.2, 0.3, 0.4, 0.5, 0.6 to get our target 0.4 in the center 

print("Pvals: ", Pvals)
print("boxsizes: ", boxside)
print("momentneeded: ", momentneeded)

ADCSset = [adcspackage()]*5
RWset = [calculator.RWvals()]*5
Magset = [calculator.Magvals()]*5

rwName = "wheel int vals.txt"

outdat = open(rwName,'w')  # open outdat in write mode truncated
outdat.write("Side (cm) \t Rwheel (cm) \t Mwheel (g) \t MOIwheel (gcm^2) \t maxPwheel (gcm^2 rad/s) \t clstruc (cm) \n")
outdat.close()

magName = "mag int vals.txt"

outdat = open(magName,'w')  # open outdat in write mode truncated
outdat.write("Side (cm) \t Lcore (cm) \t turnsPL \t numLayers \t wlen (m) \t Iactual (A) \t moment (Am^2) \n")
outdat.close()    # note it is possible to use the same variable outdat since we close each time and re-open a new one

outName = "ADCS system outputs.txt"

outdat = open(outName,'w')  # open outdat in write mode truncated
outdat.write("Side (cm) \t maxPwheel (gcm^2 rad/s) \t moment (Am^2) \t FOSrw \t FOSmag \t MinRPM \n")
outdat.close()

for i in range(5):
    ADCSset[i].side = boxside[i]
    RWset[i].Wheelcalc_int(ADCSset[i].side, hwheel, clwheel, clwall, rho, rpm, Dmagcover,rwName)
    ADCSset[i].maxPwheel = RWset[i].maxPwheel

    Magset[i].magcalc_int(ADCSset[i].side,Dmagcover,Lcap,Rcore,Voltage,twire,Imax,wireResist,Uperm,magName)
    ADCSset[i].moment = Magset[i].moment
    
    ADCSset[i].FOSrw = ADCSset[i].maxPwheel/Pvals[i]
    ADCSset[i].FOSmag = ADCSset[i].moment/momentneeded[i]
    ADCSset[i].minrpm = rpm/ADCSset[i].FOSrw

    print("FOSrw: ",ADCSset[i].FOSrw)
    print("FOSmag: ",ADCSset[i].FOSmag)

    outdatFinal = open(outName,'a')
    outdatFinal.write(str(ADCSset[i].side) + "\t\t" + str(round(ADCSset[i].maxPwheel,2)) + "\t\t" + str(round(ADCSset[i].moment,4)) + "\t\t")
    outdatFinal.write(str(round(ADCSset[i].FOSrw,3)) + "\t\t" + str(round(ADCSset[i].FOSmag,3)) + "\t\t" + str(round(ADCSset[i].minrpm,1)) + '\n')
    outdatFinal.close() 

