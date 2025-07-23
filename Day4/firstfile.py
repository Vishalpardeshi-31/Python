f=open("firstfile.txt","x") #x->create
r=open("firstfile.txt","r")  #r-> read the file
content=r.read()
r.close()
print(content)

f=open("File2.txt","a") #creates a file if file dose not exist
f.write("This is new content")
f.close()

try:
    r=open("File2.txt","r")
    content=r.read()
    r.close()
    print(content)
except FileNotFoundError:    
    print("The file not there!!") 


import os

print(os.path.exists("File5.txt"))  #check whether file exists in the path or

# # os.remove("firstfile.txt") #deletes the given file

