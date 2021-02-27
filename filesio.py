# open("filename" ,"mode")
# open("myfile.txt")
# f = open("myfile.txt," "w")
# f = open("myfile.txt", "r")
# f.read(2); #Here, you will get the first two characters of the file.
# f=open("myfile.txt","r");
# f.readlines() #Returns a list object
# f.close()


f = open("harry.txt", "rt")
print(f.readlines()) #reads full contenst
print(f.readline()) #reads next line if repeated same commnd
print(f.readline())
content = f.read()

for line in f:
    print(line, end="")
print(content)
content = f.read(34455)
print("1", content)

content = f.read(34455)
print("2", content)
f.close()

################

f = open("harry.txt", "w")
a = f.write("Harry bhai bahut achhe hain\n")
print(a)
f.close()

#####################

f = open("harry2.txt", "a")
a = f.write("Harry bhai bahut achhe hain\n")
print(a)
f.close()


# Handle read and write both
f = open("harry2.txt", "r+")
print(f.read())
f.write("thank you")

#########################

# blockstatements
# With open(“file_name.txt”) as f:
# With open(“file1txt”) as f, open(“file2.txt”) as g:
with open("harry.txt") as f:
    a = f.readlines()
    print(a)

# f = open("harry.txt", "rt")
# Question of the day - Yes or No and why?
# f.close()


# f=content=open("harry.txt")
# content=f.read()
# print(content)
# f.close()
# append
# f=open("harry.txt","r+")
# print(f.read())
# f.write("thnkyu")
a=f.write("harryddnfjfjfj dfswedweehf dfh")
# #return the noof chrcters