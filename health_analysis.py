import pandas as pd
import numpy as np

#number variable

x = 1
print(x)

#string variable

y = 'a'
print(y)

#list

myList = [ 'a', 'b', 'c', 'd']
print(myList)


#dictionary that contains at least 3 key:value pairs - which includes at least one list and one nested dictionary 

myDict = {
	'fruitVeg' : {
    	'fruit' : ['apple', 'banana'],
        'veg' : ['carrots', 'celery'],
        'other' : 'lime'
        },
        'fruitVeg2' : {
    	'fruit2' : ['apple2', 'banana2'],
        'veg2' : ['carrots2', 'celery2'],
        'other2' : 'lime2'
      }
     }
print(myDict)


#function that takes in at least two inputs

def volumeChecker(waterIn, waterOut):
    #check volume level coming into tank
    if waterIn <= 50:
        volumeIn = 'low'
    else:
        volumeIn = 'high'

    fillTank = 200 - waterIn
    print('Add', fillTank, 'gallons to fill tank.')

    #check volume level going out of tank
    if waterOut >= 50:
        volumeOut = 'high'
    else:
        volumeOut = 'low'

    fillTank = 200 - waterOut
    print('Remaining', fillTank, 'gallons in tank.')

    output = [volumeIn, volumeOut]
    return output 

waterIn = 10 
waterOut = 20 

function_output = volumeChecker(waterIn, waterOut)

print('volumeIn is: ', waterIn, 'gallons')
print('volumeIn is: ', function_output[0]) 
print('volumeOut is: ', waterOut, 'gallons')
print('volumeOut is: ', function_output[1])