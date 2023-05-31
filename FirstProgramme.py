import os
if os.path.exists("G:/Note folder/notefile.txt"):
    os.remove("G:/Note folder/notefile.txt")
else:
    print("The file does not exists")

