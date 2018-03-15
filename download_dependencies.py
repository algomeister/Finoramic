import json
import pip
import os

def install(package):
    pip.main(['install', package])

with open('dependencies.json') as json_data:
    json_object = json.load(json_data)
    d = json_object["Dependencies"]
    count = 0
    while(count < len(d)):
        install(d[str(count)])
        count = count + 1
    
    os.system('pip freeze > installedfiles.txt')
    
    count = 0
    installed_files = []
    with open('installedfiles.txt') as open:
        for line in open:
            installed_files.append(line.rstrip("\n\r"))
      
    count = 0
    flag = 0
    while(count < len(d)):
        if(installed_files.count(d[str(count)]) == 0):
            print d[str(count)]
	    flag = 1
        count = count + 1
    if(flag == 0):
	print("success")
