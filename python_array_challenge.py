names = ['Dave','Mark','Bill','Larry','Alex']
sentence = 'characters long'
def get_count():
    names.sort()
    for i in names:
        num = len(i)
        print('{} is {} {}'.format(i,num,sentence))

get_count()

#this is the lambda challenge
xyz = lambda x: x * 5

print(xyz(5))
