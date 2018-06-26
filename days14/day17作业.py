'''
用谷歌浏览器打开http://maoyan.com/，点击榜单，然后点击鼠标右键选择：显示网页源代码，然后将显示出的内容存储到文件index.html中
	1、匹配出文件index.html所有的链接
	2、有字符串'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
		匹配出所有的邮箱地址：['378533872@qq.com', '333312312@163.com', 'alexsb123@gmail.com']
	3、编写程序，
		1、让用户输入用户名，要求用户输入的用户名只能是字母或数字，否则让用户重新输入，
		2、让用户输入密码，要求密码的长度为8-10位，密码的组成必须为字母、数字、下划线，密码开头必须为字母，否则让用户重新输入

	4、有字符串"1-12*(60+(-40.35/5)-(-4*3))"，匹配出所有的数字如['1', '-12', '60', '-40.35', '5', '-4', '3']
	5、有字符串"1-2*(60+(-40.35/5)-(-4*3))"，找出所有的整数如['1', '-2', '60', '', '5', '-4', '3']

'''


import re

str='1-2*(60+(-40.35/5)-(-4*3))'
# print(re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))"))
print(re.findall(r'-?\d+\.\d*|(-?\d+)',str))

# str='1-12*(60+(-40.35/5)-(-4*3))'
# print(re.findall('\d',str))
# print(re.findall(r'-?\d+\.?\d*',str))

# with open(r'F:\python\object\days2\days14\indext.html','r',encoding='utf-8')as f:
#      f=f.read()
#      print(re.findall(r'"http:(.*?)"',f))

# str='email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
# print(re.findall(':(.*?@.*?com)',str))
