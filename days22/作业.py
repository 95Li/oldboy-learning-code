'''
4月16
'''
'''
1、定义MySQL类（参考答案：http://www.cnblogs.com/linhaifeng/articles/7341177.html#_label5）
	　　1.对象有id、host、port三个属性
	　　2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
	　　3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
	　　4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，
	      保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
'''
import hashlib
import time
import pickle
import os
from days22 import setting


class MySQL:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__id = self.create_id()

    @staticmethod
    def create_id():
        m = hashlib.md5()
        m.update(str(time.clock()).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def creae_mysql(cla):
        return cla(setting.HOST, setting.PORT)

    def save(self):
        path = os.path.join(setting.DB_PATH, '%s.pk' % self.__id)
        if os.path.exists(path):
            raise ImportError('该id已存在')
        else:
            with open(path, 'wb')as f:
                pickle.dump(self, f)

    def get_obj_by_id(self):
        path = os.path.join(setting.DB_PATH, '%s.pk' % self.__id)
        if not os.path.exists(path):
            raise ImportError('该id不存在')
            # print('该id不存在')
        else:
            with open(path, 'rb')as f:
                return pickle.load(f)

# m1 = MySQL('h1', 'p1')
# m2 = MySQL.creae_mysql()
#
# m2.save()
# print(m2.get_obj_by_id().__dict__)
#
# # m1.save()
# m1.get_obj_by_id()

'''
2、定义一个类：圆形，该类有半径，周长，面积等属性，将半径隐藏起来，将周长与面积开放
	参考答案（http://www.cnblogs.com/linhaifeng/articles/7340801.html#_label4）
'''
class Circle:
    def __init__(self,radius):
        self.__radius=radius
    @property
    def perimeter(self):
        return 2*(3.14)*self.__radius
    @property
    def area(self):
        return (3.14)*(self.__radius**2)

# c1=Circle(3)
# print(c1.area)
# print(c1.perimeter)

'''
3、明日默写
		1、简述面向对象三大特性：继承、封装、多态
		    继承：继承是一种新建类的方式，新建类称之为子类或派生类，父类称之为基类或者超类，子类会‘遗传’父类的属性
		    封装：装就是把一对属性装起来，封就是把这些属性藏起来
		          封装对外隐藏，对内开放
		    多态：一种事物的多种形态；多态主要体现在继承、抽象类抽象方法、鸭子类型
		    多态性：调用同方一方法，有不同的执行效果
		2、定义一个人的类，人有名字，身高，体重，用property讲体质参数封装成人的数据属性
		    class People:
                def __init__(self,name,hight,weight):
                    self.__name=name
                    self.__hight=hight
                    self.__weight=weight
                @property
                def bmi(self):
                    return self.__weight/(self.__hight**2)
		3、简述什么是绑定方法与非绑定方法，他们各自的特点是什么？
		    绑定方法：在类内部定义的函数，默认就是给对象来用，而且是绑定给对象用的,称为对象的绑定方法
		             若该函数是绑定给类用的，称之为类的绑定方法
		    非绑定方法：既不跟类绑定，也不跟对象绑定，这意味着谁都能用 
                       谁来用都是一个普通函数，也就是说没有自动传值的特性了
'''
