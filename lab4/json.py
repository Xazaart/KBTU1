# import json

# with open('sample-data.json') as f:
#     data = json.load(f)

# print("Interface Status")
# print('=' * 80)
# print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
# print('-' * 50, '-' * 20, '-' * 8, '-' * 6)

# for item in data["imdata"]:
#     attributes = item["l1PhysIf"]["attributes"]
#     dn = attributes["dn"]
#     description = attributes.get("descr", "")
#     speed = attributes["speed"]
#     mtu = attributes["mtu"]

#     print(f"{dn:50} {description:20} {speed:8} {mtu:6}")
