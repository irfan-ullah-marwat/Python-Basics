# dicionary are used to store data values in key :value pair

# they are unorderd, mutable and don't allow duplicate keys

dict= {
    "name" : "marwat",
    "cgpa" : 4.5,
     "marks" : [98,100,30],
}
print(dict)


info = {
    "name" : "irfan khan",
    "subjects" :  ["python","cpp"],
    "topic" : ("dictg","set"),
    "age" : 20,
    "is_adult" : True,
    12.9 : 98.8
}
print(type(info))
print(info["name"])
print(info["subjects"])
print(info["topic"])
info["name"] = "marwat"
print(info)
