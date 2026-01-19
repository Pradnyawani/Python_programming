#Checking data in python

a=1
b=1
print(a+b)
print(type(a))
print(type(b))           #checking datatype:Integer


a="1"
b="1"
print(a+b)
print(type(a))
print(type(b))           #checking datatype:Integer

#basic data types in python

#1.Numeric
a1=1
b1=1.5
c1=complex(3,2)
print(type(a1))      #int
print(type(b1))      #float
print(type(c1))      #numeric


#2.Sequence
a2="Madhav"
print(type(a2))     #strinng

b2=[1,4,6,18,'Madhav']
print(type(b2))     #list

c2=(1,4,6,18,'Madhav')
print(type(c2))     #tuple

#3.Dictionary
my_dictionary={'name':'Rishabh','Age':24,'city':'Shirdi'}
print(type(my_dictionary))

#4.sets
my_sets={1,4,6,18,'Madhav'}
print(type(my_sets)) 

#5.Boolean
bool1=True
bool2=False
print(type(bool1))

 #6.Binary
byte1=b"Madhav"
print(type(byte1))



