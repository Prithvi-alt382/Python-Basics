#Conditional Statement for eligibility of voters

'''Name = input("Name:")
age= float(input("age :"))
if(age>18):
    print("Eligible to vote")
elif(age<18):
    print("Ineligible to vote")
else:
    print("Voter is Invalid")
'''
#Coditional Statement for Traffic lights
'''
light =input("Light: ")
if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
else:
    print("Light is broken")
'''

#Conditional Statement for Grade Allocation
'''
marks = int(input("marks :"))
if(marks>=90 and marks<100):
   print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
else:
    print("Grade D")    
'''
#Single Statement For Traffic Lights
'''
Light = input("Light :")
Action = "Go" if Light == "Green" else "Stop" if Light == "Red" else "Wait" if Light == "Yellow" else "Caution"
print(Action)
'''
#Double Statements for Traffic Lights
'''
light = input("light :")
print("Signal") if light == "Red" or light =="Green"or light=="Yellow" else print("No Signal")
'''
#Clever if

age = int(input("Age:"))
Vote = ("No" , "Yes") [age>=18]
print(Vote)