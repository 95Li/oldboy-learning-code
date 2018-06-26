import hashlib
import json

def get_hash(path):
    m=hashlib.md5()
    with open(path,'r',encoding='utf-8')as f:
        f=f.read()
        for line in f:
            m.update(line.encode('gbk'))
    return m.hexdigest()

print(get_hash(r'F:\python\object\days2\days18\123.txt'))




