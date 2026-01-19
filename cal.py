#Function to add two numbers

def add(num1,num2):
    return num1+num2

#Function to sub two numbers

def sub(num1,num2):
    return num1-num2

#Function to mul two numbers

def mul(num1,num2):
    return num1*num2

#Function to div two numbers

def div(num1,num2):
    return num1/num2


def avg(num1,num2):
    return (num1+num2)/2

print("please select a operstion:\n " \
      "1.Addition\n" \
        "2.Substraction\n" \
            "3.Multiplication\n" \
                "4.Division\n" \
                    "5.Average\n")

select=int(input("Select frome t to 5:"))

number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))

if select==1:
    print(number1,"+",number2,"=",\
          add(number1,number2))
    
elif select==2:
    print(number1,"-",number2,"=",\
          sub(number1,number2))

elif select==3:
    print(number1,"*",number2,"=",\
          mul(number1,number2))  
    
elif select==4:
    print(number1,"/",number2,"=",\
          div(number1,number2)) 
    
elif select==5:
    print("(",number1,"+",number2,")","/","2","=", \
          div(number1,number2)) 
    
else:
    print("invalid Condition!!!!!!!")    

       



    
    




