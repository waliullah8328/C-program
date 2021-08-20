#Dictionary
d = {"key1" : "value1","key2" : "value2","key3" : "value3"}
print(d)
print(d["key1"])
print(d["key2"])
data = {"name": "MD Kamal","age":32,"dep":"CSE"}
print(data)
for i in data.items():
    print(i)
print(data.keys())
print(data.values())
print(d.get("key1"))
v = d.get("key2")
print(v)

# nested dictionary
stu_data = {
    "Name":{"saddam","amir","Tarek"},
    "age": {32,65,35}
}
print(stu_data)
stu_data1 = {
    "2345": {
        "name": "saddam",
        "age": 34,
        "dep" :"CSE"
    }
}
print(stu_data1["2345"])

