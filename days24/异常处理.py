# try :
#     x=123
#     p
#     i=[]
#     i[2]
# except Exception as e:
#     print(e)
# else:print('else')
# finally:print('finally')
#
# print(x)
# # print(i)


# class RegisterError(BaseException):
#     def __init__(self,msg,user):
#         self.msg=msg
#         self.user=user
#
#     def __str__(self):
#         return '<%s：%s>' %(self.user,self.msg)
#
# raise RegisterError('注册失败','teacher')
import os

file_list=os.listdir('F:\python\object\days2\days23')
file_list=[x.strip('.py') for x in file_list]
print(file_list)

for x in range(len(file_list)):
    print('%s. %s' % (x, file_list[x]))