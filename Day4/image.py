with open("Doremon.jpg","rb") as f:
    content=f.read()

print(content)    #convert to binary

with open("Acha.jpg","wb")as f:
     f.write(content)