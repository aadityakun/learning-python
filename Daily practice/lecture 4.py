# # # # info={
# # # #     "key" : "value",
# # # #     "age" : 35,
# # # #     "marks" : 94.9,
# # # #     "is he male" : True,
# # # #     "marks2" : 34,
# # # #     "age2" : 34,
# # # #     "name" : "aadi",
# # # #     "subject" : ["coding", "painting", "arts"],
# # # #     "cha" : ("kiss","kill"),
# # # # }
# # # # pairs = (list(info.items()))
# # # # print(pairs[0])
# # # # print(info.get("name")) #gives error
# # # # print("fuck this hi")
# # # # info.update({"city" : "goa"})
# # # # print(info.get("city"))
# # # # new = ({"hero" : "not gay"})
# # # # info.update(new)
# # # # print(info)
# # # # info.update({"name" : "aaditya srivastava" , "aaditya has a girlfriend" : "false because a person who like ai is single for rest of his life"})
# # # # print(info)
# # # # print(len(info))
# # # # print(info.keys())
# # # # print(list(info.keys()))
# # # # print(info.values())
# # # # print(list(info.values()))
# # # # student={
# # # #     "name" : "aadi",
# # # #     "subject": {
# # # #         "maths" : 85,
# # # #         "che" : 99,
# # # #         "phy" : 100
# # # #     }
# # # # }
# # # # print(student["subject"] ["maths"], student["name"])

# # # # student={
# # # #     "name" : "aadi",
# # # #     "subject": {
# # # #         "test": {
# # # #             "maths":{
# # # #                 "exam" : 1,
# # # #                 "exam2": 2
# # # #                 }
# # # #             }
# # # #         }
# # # #     }
# # # # print(student["subject"] ["test"] ["maths"] ) 
# # # # collection = {1, 2, 3, 4, "hello", "world", "hello", 2 }
# # # # print(collection)
# # # # print(type(collection))
# # # # print(len(collection))         #total number of items
# # # # collection = {}
# # # # print(type(collection))
# # # # collection = set()
# # # # collection.add(1)
# # # # collection.add(2)
# # # # collection.add(3)
# # # # # collection.remove(3)
# # # # # collection.add((1, 2, 3))
# # # # # collection.add([1, 2, 3])
# # # # # collection.remove(4)
# # # # collection.add("aaditya")
# # # # collection = set() #empity set: syntax
# # # # collection.clear()
# # # # print(collection)
# # # # collection = {"hello", "apnacollege", "world", "coding", "python"}
# # # # print(collection.pop())
# # # set1 = {1, 2, 3}
# # # set2 = {2, 3, 4}
# # # print1 = set1.union(set2)
# # # print2 = set1.intersection(set2)
# # # # print(print1)
# # # # print(print2)
# # # print(print1 and print2)

# # dictinory = {
# #     "table" : (" a prace of furniture", "list of the facts and figure"),
# #     # "table" : "list of the facts and figure",
# #     "cat" : "a small animel"
# # }
# # print(dictinory)

# # set1 = {"python", "java", "c++", "python", "javascript"}
# # set2 = {"java", "python", "java", "c++", "c"}
# # print(set1.union(set2))
# # print(len(set1.union(set2)))

# marks = {}

# x  = int(input("enter phy : "))
# marks.update({"phy": x})
# y  = int(input("enter che : "))
# marks.update({"che": y})
# z  = int(input("enter maths : "))
# marks.update({"maths": z})

# print(marks)

set1 = {9}
set2 = {"9.0"}
print(set1.union(set2))
