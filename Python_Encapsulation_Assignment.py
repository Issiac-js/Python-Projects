"""

This assignment is to show encapsulation and to also make use of a private attribute or function
this should also have a protected attribute or function


"""







class NumberSafe:

    
    # the number 2 is protected the number 6 is private
    def __init__(self):
        self._theNumber = 2
        self.__aNumber = 6
        


    
    # creating a function in the class to ask for a number then use the protected varible to multiply with it.
    def makeInt(num):
        numb = input("Enter a number: ")
        num = int(numb)
        return num

    # this multiplies the number by two using encapsulation 
    def makeMath(self, num):
        answer = num * self._theNumber
        print("The answer is: {} When {} X 2".format(answer,num,))

        answer1 = num * self.__aNumber
        print("The answer is: {} When {} X 6".format(answer1,num,))
        
        
        
    








if __name__ == "__main__":
    ns = NumberSafe()
    number = ns.makeInt()
    ns.makeMath(number)
