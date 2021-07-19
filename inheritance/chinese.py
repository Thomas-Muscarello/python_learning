from chef import Chef
class Chinese(Chef):
    def make_fried_rice(self):
        print("The chinese chef makes a fried rice dish! ")
    
    #You can overide the inherited function from chef by recreating the function with your new value for just this class
    def make_special_dish(self):
        print("The chinese chef makes their special orange chicken dish! ")