#Dicitioaries are a stucture that allows us to store info in key:value pairs.
#Use a variable and set it equal to curly boys "{}". 
#Each Key should be unique
#Key value pairs made by.... KEY : VALUE,
nicknameconverter = {
    "Tom":"Thomas",
    "Jim":"James",
    "Mike":"Michael",
    "Jess":"Jessica",
    "Mandy":"Amanda"
}

#Find a value in the dictionary
print(nicknameconverter["Tom"])
#or
print(nicknameconverter.get("Jess"))
#OR to have a defualt value incase the key:value doesnt exisit:
print(nicknameconverter.get("Charlie", "ALERT: Key does not exisist!"))
