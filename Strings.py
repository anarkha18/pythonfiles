# String Functions:

demo = "Aakash is a good boy"
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("good"))
mystr = "Harry is a good boy"
print(len(mystr))
print(mystr[::-2])
print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))
print(mystr[-4:-2])
print(mystr.isupper())
print(mystr.find("is"))
print(mystr.upper(4))
# more ex:
str="my name is anargha"
var1= str[0:4]
print(var1)
var2= str[4:]
var3= var2.capitalize()
print(var1+var3,end="")

# open files with help of strings
# op=open("client[n]"+ "locks[g]"+".txt", "a")
# op.write("fgerg")
