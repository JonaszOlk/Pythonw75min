#data types
#int
#whole number
#float
#with any decimals
#string
#anything in quotations marks single or double
#bool
#True or False == 1 and 0

#output and printing
#print("Hello world") It will just print whatever is in ()
#print("Hello world!", 4.5) It will work but you have to remember to seperate them by comas, coma adds space between
# print("Hello world!", end = "|")
# print("Hello world!") #now it is seperate by the | sign we put inside end = ""
# print("Hello world", end= " ") #now it is seperated by space between them insted of going to the next line
# print("Hello world!")
# print("Hello world", end= "\n") 
# print("Hello world!") #this \n sign will move to the next line 

#Variables
#Variables are like buckets that store data
# hello = 'tim'
# print(hello) #here we gave value to variable hello so it is printing its content
# world = 'world'
# print(hello, world) #we can print few variables at the same time seperating it by comas
# world = hello # we can overwrite our variables in code or make them another value of already existing variable
# print(hello,world)
# #naming of variables
# #you cant have any special characters or start with the number, you can use underscore to mark a space in name 
# hello_world = 'hello'

#input

# x = input('Name: ') #in input user puts their input for program you can add in string a prompt that will be displayed
# print(x)
# age = input('age: ') #give variables to have access to stored data form inputs
# print('hello', x,'you are', age, 'years old')

#Arithmetic operators
# x = 9
# y = 3
# result = x + y #both datas on both sides of operator have to be in numbers category int, float, abstarct
# print(result)
# result_2 = x - y #substraction
# result_3 = x * y #multiplication
# result_4 = x / y #division always results in float ypu can always put the into int() to avoid floats numbers
# print(result_2, result_3, result_4)

#extra operators 
# x=10
# y=3
# exponents = x ** y #x to power of y
# floordivision = x // y #it will give us the intiger result of anything the result is
# mod = x % y #it will give us whatever is left after division of x by y
# print(exponents,floordivision,mod)

#oreder of operations 
#you can use bracekts for order of calculation
#Python works in BEDMAS
# B = Braclets
# E = exponents
# D = division
# M = multiplication
# A = addition
# S = substraction
#mod and floordivision is in order of operations below addition and substraction

#how to chang einput in strings to numbers to work with
# num = input("Number: ")
# print(int(num) - 5) #it will be an error unless we will change num string into num inter or float
# print(float(num)-5) #it will always return float even when there is only on float in whole operation

#string method
#method is something with dot and method name for example .upper()
# hello = 'hello'
# print(type(hello))
# print(hello.upper()) #everything in string is in uppercase
# print(hello.lower()) #everything in string is in lowercase it is usefull for user input
# print(hello.capitalize()) #it will make first letter in uppercase, and rest in lowercase
# print(hello.count('ll')) #will count specific thing put into brackets, in that case it will count double l
# #remember that python is case sensetive so it is usefull to put whole string in a size of counted part
# #you can chane string method with eachothers
# y = 3
# print(hello * y) #you can multiply a string and it will print it as many times as you want to
# z = 'yes'
# print(hello + z) # it will add string together

#condition and conditional operators
# == equality
# != not equal
# <= is smaller or equal
# >= is greater or equal
# < is smaller
# > is bigger
# it will return a boolean values as answers

# x = 'hello'
# y = 'hello'
# print(x == y)
# print(x != y)

#we can compare a strings value as geater or smaller than
# print('a' > 'Z') # True
# print(ord('A')) #every letter in python is calculeted as ordinal value  Big A is 65 to 90 as big Z
# print(ord('a')) #small letters are from 97 = a to 122 = z
# print('ab' > 'ad') #it will compare if first letter is greater, they are the same so next is b vs d and d wins so F
# print(7.5==7) #false
# result = 6 == 6 #store boolean value in variable
# print(result) #True

#chained conditionals
#combaining conditions multiple to create one large condition
# x=7
# y=8
# z=0

# result1 = x == y
# result2 = y > x
# result3 = z < x + 2 #comparing is last in order of operation

# #and logical and both are true
# #or one/both of them is true
# #not it will flips to another value for example not True is False

# result4 = result1 or  not result2 or result3 #if both or one of them is true it will be true
# #order of operations for or and not
# #1st is 'not', 2nd is 'and', 3rd place is taken by 'or'

#if/else/elif

# name = input('name: ').lower()

# if name == 'jonasz':
#     print("welcome back")
# elif name == 'kuba':
#     print("welcome back")
# elif name == 'filip':
#     print("welcome back")
# elif name == 'stasiu':
#     print("welcome back")
# else:
#     print("You're not from Stara Gwardia!")

# print("I'm always there!")
# y = ("jonasz",'filip','stasiu','kuba')
# name = input("Name: ").lower()
# if name in y:
#     print('Welcome Back!')
# else:
#     print("GTFO!")

#You can use elif without else statement

#COLLECTIONS
#collection is unordered or ordered group of elemnets
#list and tuple
#LIST 
#list is []
#lists can have diffrent type of data in them
# x = [True,4,"Hi"] 
# #list is ordered collection and is mutable
# print(len(x)) #it will give us length of the list it will work on strings as well
# x.append("Hello") # it will add this element as last on the list
# print(x,len(x))
# x.extend([4,5,6,7,8,9,10]) # it will extend a list adding all this elements in the end of the list
# print(x)
# print(x.pop()) #it will remove last element of the list and return it so with print we can see what was popped
# print(x)
# print(x.pop(5)) #it will remove and return element on index 5, index start at 0 and ends on len -1
# print(x)
# print(x[2]) #it will print an elemnet of the list x with index 2(3rd element)
# x[0] = 4.55 #it will overwrite indexed element of the list for the new value
# print(x)
# y = x #it will be the same as the other list even when we do changes to the list after this statment
# x[1] = 23.47 #now modifying x will change y as well, cuz x is only a reference(not copy) to the list not 
# #list itself, list is stored somewhere else
# print(x,y)
# y = x[:] #now it is just a copy not the referance but more about in the future
# x[0] = 12.34567
# print(x,y)

#TUPLES
#ordered but immutable
#they use round brackets and comas instead of square brackets
# x = (0,0,2,2)
#we cannot append,remove or change elements
# print(x[0]) #it will give us a item from tuple indexed 0
#you can have tuple inside a list or a list inside list or even a list inside list inside list
#for example:
# y = [[2,3,4],(2,5,7), [[1,2,3],[4,5,6],[[10,11,12],[13,14,15]]]]
# print(y)

#there are sets and dictionary as well but it will be later

#FOR LOOPS 
#allows us iterate a set number of times
#while run infinitly

# for i in range(10): 
#     print(i)

# #range is created from start,stop,step it will take with start but without value of stop
# for i in range(10,-1,-1):
#     print(i) #it will print form ten to 0 cuz -1 is not included and it is in reverse

# for i in range(-10,-1,-1):
#     print(i) #it doesnt do antyhing since we are alredy past -1 so we cant go past stop value

# for i in [3,4,43,456,756,3452,12]: #we can make iteration through list 
#     print(i,end=" ") #it will print all values from the list, with end=" " it will be in one line with spaces

# x = [3,4,43,456,756,3452,12] #now when info about list is stored in the x
# for i in range(len(x)): #for every iteration in range of len x thats 7 so range is to minus 1 = 6
#     print(x[i]) #it will go like x[0,1,2,3,4,5,6] so all of the list

# for i,element in enumerate(x): #enemerate will return indexes and their value when we iterate through list
#     print(i,element) #we use i,element for that and it will give us 0 3 1 4 etc 
#     #print(i,element,end="|") #without print above we can put them in one line with end option

#WHILE LOOPS
#it works like that
#while condition == True -> do your job

# i = 0 #define starting value of variable
# while i < 10: #while i < 10 == Ture print run
#     print('run')
#     i += 1 #after printing run once add 1 to i and check condition again, it will work as long as i not > 10

#we can write it like that as well:
# x = 0 #x equal 0
# while True: #run it always
#     print('run') #run
#     x += 1 #add 1 to x
#     if x == 10: #if x reaches 10
#         break #break the nearet while loop it will be this one it is in right now

#SLICE OPERATOR
#allows to take a slice of collections and do something with it 
# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi','hello','goodbye','cya','sure']
# s = 'hello'

#sliced = [start:stop:step]

# sliced = x[0:4:2] #empty space means for start to start from the 0, for stop to go to the end, for step jump by 1
# print(sliced)
# sliced2 = x[::-1] #it will reverse the part we put into slice
# print(sliced2)
# string_revers = s[::-1] #it works on list,strings and tuples
# print(string_revers)

#SETS
#sets are unordered uniqe collections of elements, thats mean that elements in sets aren't indexed
#it doesn't care about duplicatns, track order or frequency of elements
#all wwe care about is if something is there or not
#it's very fast collection for example removing something from the list have to move elements and keep track of 
#their positions in case of sets it just removes or adds something
#use only when you care if something exists or not
# x = set()
# #or but it is not popular version cuz of dictionary
# y = {1,2,3,4,5,6,7,8,9,7,6,5,4,3}
# #it's okay when we are not creating an empty set, cuz the empty one wrote like that create dictionary
# print(y)
# y.add(15) #add to the set| use remove() if you want to remove uniqe element from the set
# print(y)
# print(4 in y)#it will tell us if something is in the set
# #sets are relly much faster if you want to check if something is in, add or remove when compared to other collections
# s1 = {4,32,2,2}
# s2 = {3,4,22,1}
# print(s1.union(s2)) #it will join two sets to create set of all elements|adds uniqe elements from s2 to s1
# print(s1.difference(s2)) #it will print what elemnts are diffrent in s1 comparing to s2
# print(s2.difference(s1)) #prove of diffrent results 
# print(s1.intersection(s2)) #it will print what is similar between sets
# print(s1.symmetric_difference(s2)) #print all elements that are diffrent between them but without the ones that are same

#DICTIONARIES
#key value pair
#x = {'key':'value'} value can be any data from int, string to list, tuples etc

# x = {'key': 4}
# print(x['key']) #it will print a value of key named in that case "key"

# x['key2'] = 5 #you can define new keyvalue pair outside a dictionary

# print(x)

# x[2] = 7 #name of the key doesn't need to be a string and value can be anything 
# print(x)

# #it is very fast cuz it uses hash value, you could almost assume it is in constant time working almost like sets
# #there might be hash collisions

# print('key' in x) #check if something is in dictionary
# print(x.values()) #it will print all values of dictionary
# print(list(x.values())) #it will print all values of dictionary in a list which is better to use
# print(list(x.keys())) #lists of all keys 
# print(list(x.items())) #it will print a list of keyvalues pairs
# #del x['key'] #it will remove a keyvalue pair named in ()

# for key,value in x.items(): #it will iterate through x and return all key value pairs
#     print(key,value)

# #other option to do the same as above is
# for key in x:
#     print(key, x[key])

#COMPREHENSIONS
#one line initialization of the list, tuple dict and etc
# x = [x for x in range(5)] #x is list in which we have in one line creted a for loop inside list
# print(x)
# y = [y + 5 for y in range(5)] #it will add to the list a thing on the left side in that case from 0 to 4 and +5
# print(y)
# z = [z % 3 for z in range(10)] #it will add to the list 0 to 9 % by 3 so 0 1 2 0 1 2 (...)
# print(z)
# # t = [[0 for t in range(100)] for t in range(5)] #it will create a list of 100 zeros 5 times
# # print(t)
# ad = [ i for i in range(101) if i % 5 == 0] #it will create a list of i in range 0-100 if i is divided by 5 without rest
# print(ad)
# dicad = {i:0 for i in range(101) if i % 5 == 0} #we can create a dictionary like that too with keys from above 
# print(dicad)#and values equal 0 for everything
# alks = {i for i in range(191) if i % 3 == 2} #here we have a set, cuz there is no key values pair of numbers in range
# print(alks)# from 0 to 190 that divided by 3 will give a rest equal 2
# posk = tuple(i *2 + 3 for i in range(10) if i % 2 == 0)#here is a tuple it have to start with tuple cuz in other case
# print(posk) # it will create a generator object

#FUNCTIONS
#functions are objects so you can technicly return them to the program
#to create a function you have to define it
# def func(): #def then name of the function and in () you can put some information for function to work with
#     print("Run")

# func()
# #You can put a function inside a function:
# def pol(): #define outer function
#     print(2+3+3+4,end=" ") #what it does
#     def sal(): #def inner function
#         print("run") #what it does
#     sal() #call inner function in lines of outer function to work when outer function is called

# pol() #calling outer function and inner function will work as well

#  #now putting variables in functions
# def qwer(x,y): #we are def and name a function with variables in ()
#     print("The value of adding yours number is: ",end="") #this is what it does
#     print(x + y) #here the function is using our variables

# qwer(7,9) #we are calling our function so we have to give values asigned to variables x  and y
# #With return function
# def hasghs(i,p): #den function with variables i and p
#     print("Running operations with:",i,p) #print for us what numbers we are using
#     return i*p,i/p,i+p #math operations returned

# print(hasghs(10,5)) #without print it won't show what are the results of returned operations #it will be given in
# #a tuple version of answer 
# #to unpack a tuple we can just do it like that:
# r1,r2,r3=hasghs(10,5) #it will return them as numbers int and float in that case and print msg
# print(r1,r2,r3)
# #we could as well index the tuple but version above is cleaner with shorter collections of data
# print(hasghs(10,5)[0])

# #you can add optional variable and give it starting value of None or any other option
# def jasbhj(x,y,z=1):
#     print('run',x,y,z)
#     return(x*y*z,x*z/y)

# print(jasbhj(4,2)) #here z is automaticly 1
# print(jasbhj(4,2,5)) #here z is overwriten from 1 to 5



