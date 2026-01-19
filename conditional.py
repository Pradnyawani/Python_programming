#1.if statements

a=26
b=108
if b < a:
    print("b is greater than A")


#if-else
age=int(input("Enter your age:"))
if age>19:
    print("you are adult")
else:
    print("you are not adult")

    #if-elif-statement

marks=int(input("Enter you marks:"))

if marks >= 90:
    print("Grade-A")
elif marks>=80:
    print("Grade-B")
elif  marks>=70:
     print("Grade-c")
else:
     print("Grade-D") 

     #nested if else


number=(int(input("Enter a number:"))) 

if number>0:
    if number % 2==0:
        print("This is even number:")
    else:
        print("This is odd number:")
else:
    if number==0:
        print("THis is Zero")

    else:
        print("THis is negative number")

       # conditional expression
        
age=int(input("Enter you age:"))
status="Adult"  if age>=18 else " minor" 
print(status)      

        

  
