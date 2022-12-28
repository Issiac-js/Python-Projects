"""
This script is going to check a specific folder on the hard drive,
verify weather those files end with a ".txt" file extension and,
if they do print those qualifying file names and
their corresponding modified time-stamps to the console

python 3.10.7

 ~ISSIAC
"""
import os


fPath = "C:\\A"

def start():
    files = [f for f in os.listdir(fPath) if os.path.isfile(os.path.join(fPath, f))]
    for file in files:
       time_stamp = os.path.getmtime(fPath + "\\" + file)
       print("File Name: {}  Last Modified: {}".format(file,time_stamp))
    


if __name__ == "__main__":
    start()
