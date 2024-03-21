import csv

def read_motinps():
    inpdat = open("motor and structure inputs.txt",'r')

    line = inpdat.readline() # get the line
    row = line.split(":")      # get row as an array
    rpm = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    hwheel = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    rho = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    clwheel = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    clwall = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Rmot = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Lmot = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    gmot = float(row[0])   
    inpdat.close()     # close the file after done reading

    return rpm, hwheel, rho, clwheel, clwall, Rmot, Lmot, gmot

########################################################################################################################################

def read_TPvals():
    inpdat = open("Min Max TP centered at 8.5.txt",'r')

    line = inpdat.readline() 
    line = inpdat.readline() # truncate the first 2 rows
    # these are just torque values. We need angular momentum
    line = inpdat.readline() # get the line
    row = line.split(":")      # get row as an array
    minp = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    maxp = float(row[0])   
    inpdat.close()     # close the file after done reading
    
    return minp, maxp

########################################################################################################################################

def read_mag():
    inpdat = open("magnetorquer specs.txt",'r')

    line = inpdat.readline() # get the line
    row = line.split(":")      # get row as an array
    Rcore = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Dmagcover = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    tstruct = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Lcap = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Voltage = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Uperm = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    rhocore = float(row[0])   
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    twire = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    Imax = float(row[0])    
    line = inpdat.readline() # get the next line
    row = line.split(":")     
    wireResist = float(row[0]) 
    inpdat.close()     # close the file after done reading

    return Rcore, Dmagcover, tstruct, Lcap, Voltage, Uperm, rhocore, twire, Imax, wireResist

########################################################################################################################################

