'''a = "Hello, World!"
print(a[3:5])'''

'''b = "Hello, World!"
print(b[-5:-1])'''                              #prints of the given no.to given no. in reverse

'''for x in "banana":
  print(x)'''                                     #prints string vertically

'''a = "Hello, World!"
print(len(a))'''                                    #length of string

'''a = "The best things in life are free!"
print("freee" in a)'''                              #check wheather the word is there or not

'''a=' Halo zee'
print(a.replace("z","j"))'''                #replace

'''a=' Halo zee'
print(a.upper())                            #upper case
print(a.count(e)) '''                       #count the number of "e" in the string

'''a = "Hello. World!. and. jupiter"
print(a.split("."))'''                            #prints the elements of string as a list

'''age = 'kid'
a = "My name is adult, and I am " + age         #adding variable to a string
print(a)'''

'''age = 1
age2 = 2
a = f"My name is {age * age2}, I am {age: .1f} years old"
print(a)        '''                                    #f strings(modification inside strings)

'''a = ["apple", "banana", "cherry"]
a[1] = "peach"
print(a)'''                                           #replacing item to a list

'''a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1:3] = ["peach", "watermelon"]
print(a)'''                                            #replacing with index

'''thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")                         #use .append to add without index
print(thislist)    '''                                     #adding item with index no.

'''thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")                           # del.thslist[0]  (with index)
print(thislist)    '''                                 #remove

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thesaurus= {
    "kids" : "children",
    "senoirs" : "old"
}
print(thesaurus)'''

'''thisdict = dict(name = "John", age = 36, country = "Norway")
thisdict["colour"]= "black"
print(thisdict)'''

'''all= ["a","b","c"]
if "a" in all:
    print("ok")'''

myfamily = {
  "child1" : {
    "name" : "teri",
    "year" : 2004
  },
  "child2" : {
    "name" : "meri",
    "year" : 2007
  },
  "child3" : {
    "name" : "uski",
    "year" : 2011
  }
}
print(myfamily["child1"]["name"])
'''try:
    a= int(input("enter; "))
    result= 10/a
except (ZeroDivisionError, ValueError):
    print("no ")
else:
    print(result)'''
    
x=0
assert x>0,"greater than 0"

    




