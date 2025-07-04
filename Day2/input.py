#MATHEMATICS OPERATIONS
a=int(input("Enter the number A="))
b=int(input("Enter the number=B"))
print("The addition is ",(a+b))
print("the substraction is",(a-b))
print(f"The multtiplication is"),(a*b)
print(f"The division is",(a/b))
print(f" The modulus operation is {a%b}")
print(f"The exponential is {a**b}")


#Email

email=input("Enter you email:")
if"@"in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")    

#Check age for vote

age=18
if age >= 18:
   print("you are not eligible to vote.")

#Check result
 
marks = 40
if marks >=35:
    print("You are passed")
else:
    print("you failed")    