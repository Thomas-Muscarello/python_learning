# How to read from outside of a python file
#open("name_of_file_you_want_to_open", "mode_of_file")
#ex: open("employees.txt", "r")
#must set to a variable:
    #ex: employee_file = open("employee.txt", "r")

#Modes
#r-reading Allows you to read the file
#w-writing  Allows you to write on the file
#a-append Allows you to add to the end of the file
#r+-read and write Allows you to read and write on the file

#You always want to open and then close a file
#to close a file you add .close()
#ex: employee_file.close()

#read the first line
employee_file = open("employee.txt","r")
print(employee_file.readline())
employee_file.close()

#read all the lines as a list
employee_file = open("employee.txt","r")
print(employee_file.readlines())
employee_file.close()

#Use a For Loop to print individual
employee_file = open("employee.txt","r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()