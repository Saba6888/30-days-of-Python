#simple Calculator using python

num1=float(input("Enter the first number: "))
num2=float(input("ENter the second number: "))
option=int(input("Enter an option: "))
if(option==1):
    result=num1+num2
elif(option==2):
    result=num1-num2
elif(option==3):
    result=num1*num2
elif(option==4):
    result=num1/num2
print(result)
