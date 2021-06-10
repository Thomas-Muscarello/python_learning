#Append to the file
employee_file = open("employee.txt","a")
#To append on a new line, you use the .write method, and "\n......"
#Failure to do "\n" will result in adding exactly where the original code ended
#rather than a new line
#\n = escape character
employee_file.write("\nJenna - Customer Service")
employee_file.close()

#Write a new file
#Overrides the original file
employee_file = open("employee.txt","w")
employee_file.write("Jenna - Customer Service")
employee_file.close()

#you can also create a new file from this.
employee_file = open("employee1.txt","w")
employee_file.write("Jenna - Customer Service")
employee_file.close()
