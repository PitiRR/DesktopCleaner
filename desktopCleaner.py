import os, glob

os.chdir("/Users/piotr/Desktop")
for file in glob.glob("Screenshot*"):
    os.remove(file)