#-----------------------------------------------------------------------------#
# CSci 1133 HW 1
# Matt Jass
# HW Problem 1A
#
# Due Date: Thursday, September 8, 2016 at 11:55 pm
#-----------------------------------------------------------------------------#
# Description:
#
# This program converts a temperature in Fahrenheit to a temperature in Celsius.
#-----------------------------------------------------------------------------#

print('Hello, Welcome to the Fahrenheit to Celsius Temperature Conversion Program\n')

# Input
Tf = float(input('Please enter the temperature in Fahrenheit: '))

# Calculation
Tc = (Tf  - 32) * 5/9

# Output
print ('The temperature in Celsius is: ', Tc)
