#!/usr/bin/env python
# Auxiliary functions, such as releasing GPIO

#-------------------------------------------------------------------------------
#### Imports ####

import time
import RPi.GPIO as gpio


#### Objects ####

#-------------------------------------------------------------------------------
class AuxiliaryHelp(object):
    # Make sure there is only one instance of AuxiliaryHelp

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print "ERROR: One instance of AuxiliaryHelp is running already."
            exit(1)
        self._instances.append(self)


#-------------------------------------------------------------------------------
    #clean up GPIO
    def cleanup (self):
        gpio.cleanup()

#-------------------------------------------------------------------------------
    #write a value to a log file
    def writetofile (self,label,value):
    		logfile = 'logfile.txt'
    		mystring = label+': '+str(value)+'\n'
				try:
				    f=open(logfile, 'a')
				    f.write(mystring)
				    print 'Wrote the following to '+logfile+':\n'+label+': '+str(value)+'\n'
				    f.close()
				except IOError:
				    print("cannot find file: " + logfile)
				    exit()
