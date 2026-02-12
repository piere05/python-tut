#Read a text file and count words
# with open("test.txt", "r") as data:
#     dataf= data.read()

# finalval=dataf.strip()

# count = finalval.split(" ")

# print(len(count))


#2. Save user input to a file

# user_input = input(" Enter Your Name : ")

# user_input1 = int(input("Enter your age : "))

# with open("test.txt", "a") as file:
#     file.write("\n" + user_input)
#     file.write("\n" + str(user_input1))


#3. Convert a dictionary to JSON and back


import json

data = {
    "name" : " Piere",
    "age" : 25,
    "dept" : "Development"
}


with open("user.json" , "a") as f :
    json.dump(data,f, indent=4)



with open("user.json","r") as read:
    loadd = json.load(read)

print(loadd)