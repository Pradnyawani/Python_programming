a=1
print(type(a))

b="1"
print(type(b))

c=int(b)
print(type(c))

print(a+c)

myname=26
mynum2=str(myname)
print(type(mynum2))


#implicity type casting 
var1=10
var2=15.5
var3=var1+var2
print(var3)
print(type(var3))


#explicit type casting

str_num="26"
int_num=int(str_num)
print(int_num)
print(type(int_num))

a0=bool(1)
print(a0)