#For loop
for i in range(1,101):
    print(i)

for i in range(7,76):
    print(i)

for i in range(6,66):
    print(i)    

for i in range(3,151):
    print(i)

 
# #   while loop

while True:
    x=int(input("Enter the number to print : "))
    if x==0:
        break
    print(x)
    print("Enter 0 to break")



for i in range(1,6):
    if(i==3):  #3 will not print it will skip it and print other values
        continue
    print(i)


for i in range(1,101):
    if(i%2==0):    #  if(i%2==0):  (even number)
        continue
    print(i)


import math
import random
print(math.sqrt(144))
print(math.floor(5.9))
print(math.ceil(5.1))            # if print upper value if 0.1
print(random.randint(1,10))
print(random.randrange(1,11))  #random.range=(n-1), random.randint=print exact  ex to print 50 in range 51 & in randint 50













## ositional arguments
## keyword arguments
## variable length arguments

def print_number(*args):
    for i in args:
        print(i)
print_number(5,6,8,9,7,6,2,244,6,57,688,945,47,32,55,75756,567,)        


def print_number(**kwargs):
    for i in kwargs.values():
        print(i)
    for k,v in kwargs.items():
        print(f"keys {k} : values {v}") 

print_number(Trainer="Govinthan",student1="Sahil",student2="Shivam",student3="Vishal",Grade=True,Marks=9.5)        

