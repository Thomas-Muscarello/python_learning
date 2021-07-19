from chef import Chef
#Pass the class of chef into the chinese chef class so that you can access the Chef functions
class Chinese(Chef):
    def make_fried_rice(self):
        print("The chinese chef makes a fried rice dish! ")
    
     def make_special_dish(self):
        print("The chinese chef makes their special wonton soup dish! ")