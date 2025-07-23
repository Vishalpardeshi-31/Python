class Bird:
    def sound(self):
        print("Chirp")
class Cat:
    def sound(self):
        print("Meow")        

def make_sound(animal):
        animal.sound()       
b=Bird()    
c=Cat()
make_sound(b)
make_sound(c)


# ## Method Overiding(Run-Time Polymorphism)

class Parent:
     def show(self):
          print("Parents method")

class Child(Parent):
     def show(self):
          print("child")    


# Operator Overloading (COMPILE-TIME POLYMORPHISM)

 
class point:
     def __init__(self,x,y):
          self.x=x
          self.y=y
     def __add__(self,other):
          return point(self.x+other.x, self.y+other.y)                     
p1 = point(1,2)
p2 = point(3,4)        
p3 = p1 + p2
print(p3.x,p3.y)

##ERRORS              


try:
    print(int("Hello"))
except ZeroDivisionError:
    print("We cannot divide by zero , try another number")
except ValueError:
    print("Cannot convert this string to number")     
print    

#RAISING EXAPTION MANUALLY (You can raise exaptions using keyword.)

age = int(input("Enter your age:"))
if age < 18:
    raise ValueError("Age must be 18 or older.")
else:
    print("Acces granted.")  

# with open("missing.txt","r")as f:
#     data=f.read()     
# except FileNotFoundError:
# print("The file does not exist.")    
# exceptIO   

