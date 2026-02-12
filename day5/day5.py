# word ="Iam Piere,What is your name"
# sentence= " ".join(word)
# print(sentence)

# eplitw=word.split(",")
# print(eplitw)

# find len
# data = "applebanana orange"
# fruits = data.split(" ")
# print(len(fruits))

# filename= open("test.txt","r")

# with open("test.txt","w") as file:
#     file.write("Hello, iam Piere")
#     file.write("\nStill wonderning  who is this")


# with open("test.txt","r") as readd:
#     data=readd.read()
#     print(data)


# text ="Python"

# print(text.index("P")) 

# num = int(input("Enter a Number :  "))
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print(fact)



#day5 exercise

# with open("test.txt", "w") as f:
#     f.write("\n Hello, this is added on 12/02/26")


# with open("test.txt","r") as readf:
#     fdata= readf.read()
#     print(fdata)

import csv

# data = [

#     [ "Name", "Age", "Dept"],
#     [ "Piere", 25, "IT"],
#     [ "John", 30, "HR"],
#     [ "Alice", 28, "Finance"]

# ]


# with open("user.csv", "a", newline="") as csvf:
#     addd= csv.writer(csvf)
#     addd.writerows(data)

# with open("user.csv", "r") as readcsv:
#     read=csv.reader(readcsv)
#     for row in read:
#         print(row)


import json

# data = [
# {
#     "Name" : "Piere",
#     "Degree" : "MCA",
#     "Age" : 21
# },
# {
#     "Name" : "Alvin",
#     "Degree" : "MSC. CS",
#     "Age" : 21
# }
# ]
# with open("test.json", "a") as jsonw:
#     json.dump(data,jsonw , indent=4)


# with open("test.json", "r") as jr:
#     data = json.load(jr)

# print(json.dumps(data, indent=4 ))