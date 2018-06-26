import random

#产生一个随机验证码
def ver_code(n):
    l=''
    for i in range(n):
        s1=chr(random.randint(65,90))
        s2 = chr(random.randint(97,122))
        s3=random.randint(0,9)
        code=random.choice([s1,s2,s3])
        l=l+str(code)
    return l
print(ver_code(4))