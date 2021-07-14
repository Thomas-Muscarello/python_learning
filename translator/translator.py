#Made Up Language
#All vowels (a,e,i,o,u) change to "oo"

#fish -> foosh
#dog -> doog
#--------------------------------------#

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            #Allows to keep uppercase is a vowel starts the phrase
            if letter.isupper():
                translation = translation + "Oo"
            else:
                translation= translation + "oo" 
        else:
            translation=translation + letter
    return translation

print(
    translate(input("Please Enter a Phrase: "))
)