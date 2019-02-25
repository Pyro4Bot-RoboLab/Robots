import os
import sys
import pkgutil
import fileinput

current_dir = os.getcwd()


with open("source-list.json", "w") as f:
    f.write("{")
    components = []
    services = []
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if 'init' not in file and '.py' in file and 'template'.lower() != file.lower():
                item = root.replace("/Users/alberto/PycharmProjects/Org_Pyro/Components/", "") + "/" + file
                obj = {"content": file.replace(".py", ""), "path": item, "type": "driver" if "services" in item else "TODO",
                       "controller": "gpio", "stable": True if 'stable' in item else False}
                item = item.split("/")
                if item[0] == "components":
                    components.append(obj)
                elif item[0] == "services":
                    services.append(obj)
            #  f.write(item)

    f.write('"components":{')
    for it in components:
        string = "'" + it["content"] + "':" + it.__str__() + ","
        f.write(string)
    f.write("},")
    f.write("},")
    f.write('"services":{')
    for it in services:
        string = "'" + it["content"] + "':" + it.__str__() + ","
        f.write(string)
    f.write("}")

    f.write("}")
