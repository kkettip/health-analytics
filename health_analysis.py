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