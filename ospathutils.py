import os
from os import path
from datetime import datetime
print(os.name) # 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'
print("file exists: ", path.exists("sample.txt"))
print("is file: ", path.isfile("sample.txt"))
print("is directory: ", path.isdir("sample.txt"))
print("file name: ", path.basename("sample.txt"))
#file path
print("absolute path: ", path.abspath("sample.txt"))   
print("split path: ", path.split(path.realpath("sample.txt")))
print("split extension: ", path.splitext("sample.txt"))    

#get the modification time of the file
print("modification time: ", datetime.fromtimestamp(path.getmtime("sample.txt")))
td = datetime.now() - datetime.fromtimestamp(path.getmtime("sample.txt"))
print("time since modification: ", td)
print("create time: ", datetime.fromtimestamp(path.getctime("sample.txt")))
td1 = datetime.now() - datetime.fromtimestamp(path.getctime("sample.txt"))
print("time since creation: ", td1)
print("access time: ", datetime.fromtimestamp(path.getatime("sample.txt")))
td2 = datetime.now() - datetime.fromtimestamp(path.getatime("sample.txt"))
print("time since access: ", td)