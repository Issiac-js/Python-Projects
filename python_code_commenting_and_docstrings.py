num1 = int(input("Give first Integer:\n"))


def do_math(num):
    """ This uses (*) and takes the input multiply by 4 """
    result = num * 4
    return result

# This prints the comment for documentation of the user defined function
print(do_math.__doc__)

print(do_math(num1))


