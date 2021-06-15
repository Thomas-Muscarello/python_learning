#An object is an actual piece of data that is defined by a class

#from student file, import student class
from student import Student

student1= Student("Thomas", "Comm", 3.4, False)
student2= Student("Jim","Buss", 3.8, True)

print(student1.name +" and " + student2.name)