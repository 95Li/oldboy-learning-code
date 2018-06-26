'''
1.Python中re模块match()和search()的区别
match()是从字符串0位置开始匹配，如果开头不符合匹配条件，就匹配不到内容
search()是匹配字符串任意位置，只要有符合条件的，就能匹配到

在search()匹配的字符串前加 '^' 则两个方法效果相同
'''

'''
2.Python之随机生成六位验证码（包含数字，大小写字母）

'''
# import random
# def yanzhengma(n):
#     res = ''
#     for i in range(n):
#         index = random.randint(1, 3)
#         # print(index)
#         if index == 1:
#             res = res + str(random.randint(0, 9))
#         if index == 2:
#             res = res + chr(random.randint(65, 90))
#         if index == 3:
#             res = res + chr(random.randint(97, 122))
#     return res
# print(yanzhengma(6))
#

'''
3.简要描述Python的垃圾回收机制（garbage collection）
自动清理垃圾数据  让出内存
引用计数  清除标记  分代
'''
'''
4.补充缺失的代码

	def print_directory_contents(sPath):
	    """
	    这个函数接受文件夹的名称作为输入参数，
	    返回该文件夹中文件的路径，
	    以及其包含文件夹中文件的路径。
	    """
	    # 补充代码

'''
import shutil
import os
def print_directory_contents(sPath):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    real_file_path = os.path.join(BASE_DIR, sPath)
    dir_path, dir_names, filenames = os.walk(real_file_path)
    # dir_path: 根目录 dir_names: 文件夹 filenames： 文件

    return (real_file_path, filenames)


real_file_path, filenames = print_directory_contents('days71')
print(real_file_path, filenames)

'''
5.Python3之交换变量（三种方式）
	a=1,b=2
	
#-----第一种：----
a,b=b,a
#-----第二种：----
c=a
a=b
b=c
#-----第三种:----
a=a+b
b=a-b
a=a-b
'''
