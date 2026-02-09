# marks=20
# if marks>=35:
#     print("He is passed")
# elif marks<35:
#     print("He failed in the exam")
# else:
#     print("Exit")

# for i in range(1, 11, 2):
#     print(i)

# for i in range(1, 21):
#     if i%2 ==0:
#         print(str(i) + " is even number")

# a = [1, 2 , 1 ,2,4, 6,1,2,3, 4]

# target =1

# count =0


# for i in a:
#     if i ==target:
#         count+=1


# print("The count of target "
#  + str(target) + " is " + str(count))

#3.  Reverse a list using loop

# list1 = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
# listrev=[]
# for i in range(len(list1)-1, -1, -1):
#     listrev.append(list1[i])
# print(listrev)


students = {}

name_val = input("Enter Your Name: ")
students["name"]=name_val

age_val=int(input("Enter Your Age"))

students["age"]=age_val


print()
print(students)