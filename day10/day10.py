import datetime
import json
# import pandas as pd
current_time = datetime.datetime.now()


def loaduser():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            # df= pd.DataFrame(data)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
    
def insertuser():
    try:
        data  = loaduser()
        name = input("Enter Your Name : ")
        age = int(input("Enter Your Age : "))
        dept = input("Enter Your Department : ")
        with open("data.json", "w") as file:
            data.append({"Name" : name , "Age" : age, "Department" : dept})
            json.dump(data, file, indent=4)
    except ValueError:
        print("Invalid Input")
        return None

option = input("Choose a option : \n1. Load User data \n2. Enter New User Data \n3. Update User \n4. Delete User\n ")

match option:
    case "1":
         print(loaduser())
    case "2":
        insertuser()
        print(loaduser())
    case "3":
        print("Wait")
    case "4":
        print("Wait")
    case _:
        print("Enter Correct Option")