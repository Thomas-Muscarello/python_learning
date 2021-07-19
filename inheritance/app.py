#What is inheritance?
#Define a attribute and objects within a class, and then create another class that can inherit those same attributes

from italian import Italian
from chinese import Chinese
from chef import Chef

print(" ")
myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

print(" ")

myItalianChef = Italian()
myItalianChef.make_chicken()
myItalianChef.make_salad()
myItalianChef.make_special_dish()
myItalianChef.make_pasta()

print(" ")

myChineseChef = Chinese()
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()