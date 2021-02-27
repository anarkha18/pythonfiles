a = {'key':'value', 'cow':'mooh'}
print(a['cow'])
#will print "mooh" on the screen# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
# I mean by this is that Python provides us with a long list of already defined methods for dictionaries that can
# help us to do our work in a shorter span of time with a very little amount of code. Some of these methods are,
# clear(), copy(), popitem(), etc. The best part about them is that no extra effort is required to be put in order
# to learn the functionality as their names explain their functions (in most of the cases),
# such as clear() will clear all the data from the dictionary, making it empty, copy() will make a
# copy of the dictionary, etc.
# Some distinct features that a dictionary provides are:
# We can store heterogeneous data into our dictionary i.e. numbers, strings, tuples, and the other
# objects can be stored in the same dictionary.
# Different data types can be used in a single list, which can be made the value of some keys in the dictionary. etc.
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2["Shubham"])
d3 = d2.copy()
del d3["Harry"]
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())
#####################

d=input("enter the word: ")
print(d2[d])

print(d2["harry"])
print(d2["shubam"])
print(d2["shubam"]["roti"])
d2["aogzb"]="jnk food"
d2["dded"]="fghhvgbb"
print(d2)
del d2["dded"]
print(d2)
d3=d2.copy()
print(d3.get("harry"))
#d3=d2
d2.update({"leen":"ffsdf"})
print(d2)
print(d2.keys())
print(d2.items())

