import os

# while True:
#     cmd=input('==>').strip()
#     if not cmd:
#         continue
#     os.system(cmd)

import subprocess

obj1=subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
obj2=subprocess.Popen('123124',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

res1=obj1.stdout.read()
res2=obj2.stderr.read()

print(res1.decode('gbk'))

print(res2.decode('gbk'))