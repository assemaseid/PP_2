import json

with open('data.json') as file:
    jsondata = file.read()

data = json.loads(jsondata)

print("=======================================================================================" "\n"
      "DN                                                 Description           Speed    MTU" "\n"
      "-------------------------------------------------- --------------------  ------  ------"
      )

imdata = data["imdata"]

for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{0} {1} {2} {3}".format(dn, descr, speed, mtu))
    if dn == "topology/pod-1/node-201/sys/phys-[eth1/35]":
        break



