# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 17:03:40 2015

@author: Anand Biradar
Credits: Martin Tomasz
"""

"""~~ Some conventions, comment = #
                   Value change = ##
                    Code change = ###
"""                   
 
#from pyvisa import visa
import visa
import unicodedata

rm = visa.ResourceManager()
rm.list_resources()
ElectronicLoad = rm.open_resource('GPIB0::6::INSTR')
ElectronicLoad.query('*IDN?')

# ElectronicLoad.query('')
# ElectronicLoad.query('MEAS:CURR?')
# ElectronicLoad.query('MEAS:VOLT?')
# ElectronicLoad.query('MEAS:POW?')

"""### Add loop to 1. Stop the battery discharging at 22.2 V
                   2. Recording the Voltage and current readings initially /sec, ouput it into CSV
"""

# Initialization
ElectronicLoad.write('CHAN 1')
ElectronicLoad.write('INPUT ON')
ElectronicLoad.write('MODE:CURR') # Setting up for constant current mode

# Initializing arrays for storing values
Battery_Voltage = [] 
Battery_Current = []
Battery_Power   = []

output = open("ElectronicLoadData.csv","w")
variables = ['Battery Voltage' + 'Battery Power' + "\n"] 
output.writelines(variables)
 
 
ElectronicLoad.write('CURR 5') ## change this to required discharge current rate

n = 20000

for i in range(1,n):
    i = i + 1
    bat_volt  = float(ElectronicLoad.query('MEAS:VOLT?'))
    bat_power = float(ElectronicLoad.query('MEAS:POW?'))
    print "Battery Voltage = ", bat_volt, bat_power
    
    Battery_Voltage.append(bat_volt)
    Battery_Power.append(bat_power)
    
    output_data = bat_volt + bat_power
    store = [str(output_data) + "\n"]
    output.writelines(store)

    
    if bat_volt <= 22.120:
        ElectronicLoad.write('INPUT OFF')
        break
    

    