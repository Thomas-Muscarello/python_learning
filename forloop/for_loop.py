for letter in "Bird":
#for every letter/variable in "Bird"
    print(letter)
    #we can define a variable that will change on every iteration

beer_styles = ["sour", "ipa", "lager", "brown ale"]
for styles in beer_styles:
    #variable can be anyting but must match in order to access it
    print(styles)

for index in range(3,10):
    #will start at 3, but end before 10
    print(index)

for index in range(5):
    if index == 0:
         print("first iteration")
    else:
        print("Not first")

