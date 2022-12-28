'''

Using the splite3 module to create and write to a database
Gonna be taking information from tuple in python and getting it stored in the database.


'''
# importing the module as s3 to make it faster to type 
import sqlite3 as s3

# adding the list of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
# creating an empty list to store the values sorted out of the tuple
txtList = []
# checking the items in the tuple and adding the ones ending in txt to the txtList.
for file in fileList:
    #splice the items and look for the extensions that match 'txt' to add to list
    if file[-3::] == 'txt':
        # adding to list the items that end in txt
        txtList.append(file)

# tuple the list we made
txtTuple = tuple(txtList)

# connecting with database / creating it in the folder
conn = s3.connect('test.db')


# making a loop and opening the database to create the tables in the database.
with conn:
    # this creates a cursor object using cursor() method
    cur = conn.cursor()
    # This allows us to execute a sql statement
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT)")
    # This commits our statement to the database
    conn.commit()
#closing connection with the database for memory
conn.close()

"""
    Already have my tuple list I could have used the .endswith() method
    I wanted to catch the whole 'txt' extension to add it to my list instead of the 't' alone.

"""
# connecting with database 
conn = s3.connect('test.db')

#creating a loop to add item to database.
for item in txtTuple:
    with conn:
        cur = conn.cursor()
    #The value of each row will be one file name out of the tuple therefore (item,)
    #will denote a one element tuple for each item
        cur.execute("INSERT INTO tbl_txtFiles (col_fname) VALUES (?)", (item,))
        print(item)
#closing connection with the database for memory
conn.close()

