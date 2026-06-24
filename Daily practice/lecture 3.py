# # # marks=[23, 34, 54]
# # # print(marks)
# # # print(list(marks))
# # # print(marks[2])
# # # str="hello"
# # # print(str[0])                                     #immutable
# # # str[0]= "yo"


# # student=["aadi", 85.5, 18, "patna"]                 #mutable
# # # print(student[0])
# # # student[0]= "abhi"
# # # print(student)
# # student0=student[-2:-1]
# # print(student0) 
# # print(len(student))

# list=[6,5,8,3,4,7]
# # print(list.sort())
# # list.append(1)
# # list.sort()
# # list.sort(reverse=True)
# # list.reverse()
# list.insert(6,9)
# print(list)
# list= [2, 5, 3]
# list.insert(5, 55)
# print(list)
# tup=(2, 1, 3, 32,)
# print(type(tup))
# movies = []
# movies.append(input("1 "))
# movies.append(input("2 "))
# movies.append(input("3 "))
# list.sort(movies)
# # print(movies)

list = [1, 2, 3, 2, 1]
# wtf = list.copy()
# wtf.reverse()
# print(list)
# if(wtf == list ):
#     print("this shit is true ")
# else:
#     print("false")

wtf = list.copy()
wtf.reverse()
print(list)
if(wtf == list ):
    print("this shit is true ")
else:
    print("false")