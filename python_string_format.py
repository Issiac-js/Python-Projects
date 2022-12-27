

fname = input('what is your first name? ')
lname = input('What is your last name? ')

print("Hello {} {}, Welcome to Python!".format(fname, lname))


# This is formating a number into binary

x = format(63, 'b')
print(x)

print('Binary: {0:b} Hexadecimal: {0:x}, Percentage: {0:%}'.format(5))
