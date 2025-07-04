# a=''''GOOD MORNING
# GOOD AFTERNOON
# GOOD NIGHT'''
# B="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
# print(a)
# print(B[5])
# print(B[15:20])
# print(B[-11:-6])

#string method

a=" A B C D E F G H I G K L M N O P Q R S T U V W X Y Z"
b="abc"
# print(a.lower())
# print(a.upper())
# print(a.strip()+b)
# print(b.upper())
# print(a.replace("A","Vishal"))
# c=a.split("   ")
# print(" * ".join(c))
c=a+b
print(c.count("A"))
print(c.startswith("A B C D"))
print(c.endswith("abc"))
print(a*38)
print("y" in b)