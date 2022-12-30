"""
Using python to create 'parent' and 'child' classes.


"""


class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(self.name))
        else:
            print("You are not authorized for this page.")


#creating new class
class Employee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = '1888'


    # this is the same method in the parent class "User"
    # The difference is that, instead of using the entry_password var we're using a pin var.
    def login(self):
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(self.name))
        else:
            print("You are not authorized for this page.")

class Customer(User):
    mailing_address = ' '
    mailing_list = True

    # will be using the same login this time it will tell them if they are on the mailing list
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(self.name))
            # checking to see if they are on the mailing list
            if self.mailing_list:
                print("\n{} thank you for being included on our mailing list!".format(self.name))
            else:
                print("{}, you are not on our mailing list. you can contact our reps to put you on the list".format(self.name))
        else:
            print("You are not authorized for this page.")


# creating a new user

##New_user = User("John Doe", "jdoe@outlook.com", "password1", 123)

# call the login method using the new object

##New_user.login()


# this is creating a employee instance and utilizes the pin in 'pin_number' to login

##manager = Employee("John doe", "jdoe@outlook.com", "password1", 1234)
##manager.login()

# This is the customer class instance

customer1 = Customer("John doe", "jdoe@outlook.com", "password1", 1234)
customer1.login()
