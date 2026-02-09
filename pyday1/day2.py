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

a = [1, 2 , 1 ,2,4, 6,1,2,3, 4]

target =1

count =0


for i in a:
    if i ==target:
        count+=1


print("The count of target "
 + str(target) + " is " + str(count))
