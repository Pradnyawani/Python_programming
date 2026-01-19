year=int(input("Enter the year:"))

if year%4==0:
    print("year is leap")

else:
     print("year is not  leap")

###############################################################################################

predefined_username='Madhav'

predefined_Password='Madhav123'


Username=(input("Enter the user name:"))
password=(input("Enter the password:"))

if Username==predefined_username:
     if password==predefined_Password:
          print("welcome!you are login succesfully!!")
     else:
          print("Incorrect password!!")     

else:
     print("Invalid username")    







################################################################################    
#user input

print("Enter pcm marks")

physics_marks=int(input("Enter Physics marks:"))
maths_marks=int(input("Enter maths marks:"))
chemistry_marks=int(input("Enter chemistry marks:"))

#egibility check

if (maths_marks >=65 and
   physics_marks>=55 and
   chemistry_marks>=50 and
   (maths_marks+physics_marks+chemistry_marks)>=180) or \
   (maths_marks+physics_marks) >=140:  

   print("you are eligible!!!!!!!!!")

else:
    print("you are not eligible!!!!!!!!!")        


