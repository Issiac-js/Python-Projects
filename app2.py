"""
app 2 is going to user the dunder method
and import app 1 and call the function in app one

"""

import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    # The following is calling code from within this script
    print("I am running code from {}".format(print_app2()))

    # The following is calling code from importated script app.py
    print("I am running code from {}".format(app.print_app()))
