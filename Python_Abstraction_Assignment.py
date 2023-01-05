"""

This class utilizes the concept of abstraction



"""

#importing functions to use in my class from another module that is abstraction

from time import gmtime, strftime
from abc import ABC, abstractmethod


# Going to use my class to tell time with my own function and this is like a 'child' function as it gets its important function from another library
class MyTime():

    #use self to hold a varible that hold the important arguments that are passed to the time library
    def __init__(self):
        self.theDate = strftime("%A, %d %B %y", gmtime())

    # prints the date / "regular" method as its just printing a varible
    def GiveDate(self):
        print(self.theDate)



class speedingticket(ABC):
    #no amount argument  given
    def ticket(self, amount):
        print("Your speeding ticket owed payment: ", amount)
    # right now we aren't passing any arguments
    @abstractmethod
    def payment(self, amount):
        pass


class PaymentMethod(speedingticket):
    # speeding ticket is now the parent class here making the payment "PaymentMethod" the child class
    def payment(self, amount):
        print("The amount paid: {}, The amount still owed is $100".format(amount))










# control program flow.

if __name__ == "__main__":
    mt = MyTime()
    mt.GiveDate()
    pay = PaymentMethod()
    pay.ticket("400")
    pay.payment("300")
