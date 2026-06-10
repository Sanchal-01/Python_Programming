# Encapsulation is the process of hiding an object's internal data and providing controlled access to it through methods.
# In Python, encapsulation is commonly achieved using double underscore (__) attributes and public methods such as getters and setters.

# Example 1 :
class Mobiles:
    def __init__(self):
        self.__battery = 98

    def check_battery(self):
        print(self.__battery)


m = Mobiles()
m.check_battery()

#print(Mobiles.battery) This won't work because python encapsulated the class attributehere. Python __variable  -> Strong hint + name mangling

# ---------------------------------------------------------------------------------------------#-----------------------------------------------------------#---------------------------------------------------------


# Simple Example demonstrating howto change password and see the number of followers.
 
class Instagram:
    def __init__(self):
        self.__password ="Akshay12345"     #__password is private. # This is private cannot be accessed directlty.
        self.__followers =300

    def change_Password(self,old,new):
        if old == self.__password:
            self.__password = new
        else:
            print("Wrong Password")

    def add_Followers(self):
        self.__followers += 1
        print(f"New follower: Total: {self.__followers}")


    
    def get_followers(self):
        print(f"Current Followers: {self.__followers}")

# direct access nahi milega
# print(acc.__password)
# print(acc.__followers)


acc = Instagram()
acc.change_Password("Rahul123","newpass12")
acc.add_Followers()
acc.get_followers()




print("\n")


#-------------------------------------------------------------------------------------------------#-------------------------------------------------------------------#---------------------------------------------------------


# TASK: Completed 

class Mobile_Phone:
    def __init__(self):
        self.__battery = 99

    def charge(self):
        self.__battery += 10
        print("New battery stats =", self.__battery)

    def use_phone(self):
        self.__battery -= 10
        print("Battery is discharging, current stats:", self.__battery)

    def check_battery(self):
        print("Current Battery Level:", self.__battery)



# Create object
phone = Mobile_Phone()
phone.charge()
phone.use_phone()
phone.check_battery()







