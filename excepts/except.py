try:
    number = int(input("Enter a Number: "))
    print(number)
#Allows you to classify each error individually
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input, please enter a number! ")

