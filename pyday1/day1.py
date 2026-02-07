# task 1

def task1():
    name = input("Enter Your Name: ")
    age= int(input("Enter your age:"))
    city= input("Enter your city:")

    print("Hello, " + name + " your age is " + str(age)+ " and your city is "+ city)

#task 2
def task2(opp):
    num1 = int(input("Enter the Number 1"))
    num2 = int(input("Enter the Number 2"))
    if opp =="+":
        print("The Sum of " + str(num1) + " and " + str(num2) + " is " + str(num1+num2))
    elif opp =="-":
        print("The Subraction of " +str(num1) +  " and " + str(num2) + " is " + str(num1 - num2))

task2("+")
task2("-")