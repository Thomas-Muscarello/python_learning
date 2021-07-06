from Student import Student
# Class functions can be used within a class and it can either modify the objects of the class or give us info

student1= Student("Oscar", "Communication", 3.1)
student2= Student("Jessica", "Mathmatics", 4.0)

print(student1.on_honor_roll())
print(student2.on_honor_roll())