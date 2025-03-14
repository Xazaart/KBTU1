import json

with open("sample-data.json") as f:
    data = json.load(f)

# print(type(data))

for i in data["imdata"]:
    print(type(i))
    for j in i["l1PhysIf"]["attributes"]["adminSt"]:
        print(j)
    j = i["l1PhysIf"]["attributes"]["adminSt"]
    print(j)
    del i["l1PhysIf"]["attributes"]["adminSt"]

# print(json.dumps(data, indent=2))

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(type(x), type(y))

i = data["imdata"]
print(type(data))
print(len(i))
print(type(i))
    