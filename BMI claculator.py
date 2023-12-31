#calculating BMI 
#formula=weight in kg / height in meter square (m*2)
a=float(input("enter the weight of the person in kg: "))
b=float(input("enter the height of the person in meter :"))

BMI=a/(b*b)
print("your BMI clacuated is: ",BMI)
 
if(BMI>0):
      if(BMI<=16):
        print("you are very underweight")
      elif(BMI<=18.5):
        print("you are underweight")
      elif(BMI<=25):
        print("*YOU ARE HEALTHY*")
      elif(BMI<=30):
        print("you are overweight")
      else:
        print("you are very overweight")
else:
   print("enter the correct body mass index")
   
#time : 1.5 hours 
# :-((((
