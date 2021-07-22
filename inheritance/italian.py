from chef import Chef
#You can pass the class of Chef into the italian chef class so that you can access the Chef functions
class Italian(Chef):
    #Now the italian chef can do eveything the normal chef can do.
    #You can also create another class for just the italian chef.
    def make_pasta(self):
        print("The italian chef makes a pasta dish!")
