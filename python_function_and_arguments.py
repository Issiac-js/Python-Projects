mySentence = 'loves the color'

color_list = ['red','blue','pink','green','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg ="{} {} {}".format(name, mySentence,i)
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('What is your name?')
        if name == '':
            print('you need to provide a name!')
        elif name == 'Loraine':
            print('Loraine cannont access this software!')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()
