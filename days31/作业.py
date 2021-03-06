'''
	4、基于线程池实现一个可以支持并发通信的套接字，完成以下功能？
		执行客户端程序，用户可选的功能有：
		1、登录
		2、注册
		3、上传
		4、下载

		思路解析：
		1、执行登录，输入用户名egon，密码123，对用户名egon和密码进行hash校验，并加盐处理，将密文密码发送到服务端，与服务端事先存好用户名与密文密码进行对比，对比成功后，
		在服务端内存中用hash算法生成一个随机字符串比如eadc05b6c5dda1f8772c4f4ca64db110
		然后将该字符串发送给用户以及登录成功的提示信息发送给客户端,然后在服务存放好
			current_users={
				'a3sc05b6c5dda1f8313c4f4ca64db110':{'uid':0,'username':'alex'},
				'e31adfc05b6c5dda1f8772c4f4ca64b0':{'uid':1,'username':'lxx'},
				'eadc05b6c5dda1f8772c4f4ca64db110':{'uid':2,'username':'egon'},

			}

		用户在收到服务端发来的'eadc05b6c5dda1f8772c4f4ca64db110'以及登录成功的提示信息后，以后的任何操作都会携带该随机字符串'eadc05b6c5dda1f8772c4f4ca64db110‘，服务端会根据该字符串获取用户信息来进行与该用户匹配的操作

		在用户关闭连接后，服务端会从current_users字典中清除用户信息，下次重新登录，会产生新的随机字符串
		这样做的好处:
			1、用户的敏感信息全都存放到服务端，更加安全
			2、每次登录都拿到一个新的随机的字符串，不容易被伪造

		2、执行注册功能，提交到服务端，然后存放到文件中，如果用户已经存在则提示用户已经注册过，要求重新输入用户信息

		3、执行上次下载功能时会携带用户的随机字符串到服务端，如果服务端发现该字符串not in current_users，则要求用户先登录
'''





