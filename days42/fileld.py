from days42 import conn


class Fileld:
    '''
    字段类父类
    '''

    def __init__(self, name, colum_type, primary_key, default):
        self.name = name  # 字段名
        self.colum_type = colum_type  # 字段类型
        self.primary_key = primary_key  # 字段是否为主键
        self.default = default  # 字段的默认值


class StringFileld(Fileld):
    '''
    varchar类型字段类
    '''

    def __init__(self, name=None, colum_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, colum_type, primary_key, default)


class IntegerFileld(Fileld):
    '''
    int类型字段类
    '''

    def __init__(self, name=None, colum_type='int', primary_key=False, default=0):
        super().__init__(name, colum_type, primary_key, default)


class ModelMetaclass(type):
    '''
    自定义元类，用于类和数据库表之间的类型转换
    '''

    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # 如果是构建Model类,则不用进行转换，直接调用 type创建类
            return type.__new__(cls, name, bases, attrs)

        table_name = attrs.get('table_name', None)  # 字典的get（）方法取值，若值不存在，则返回None
        if not table_name:
            table_name = name  # 若没有指定表名，则直接使用类名作为表名

        primary_key = None
        mappings = dict()  # 创建一个字典，用于存放表中的字段信息

        for k, v in attrs.items():  # 循环往字典中添加，表的字段信息
            if isinstance(v, Fileld):  # 判断 v是否是Fileld的对象； 用以判断类中的值是否作为表中的字段
                mappings[k] = v  # 将表的字段，放入appings中
                if v.primary_key:  # 判断主键是否存在
                    if primary_key:
                        raise TypeError('主键不唯一')
                    primary_key = k  # 为表设置主键

        # for k in mappings:         #如果不加 keys 默认循环取出key
        for k in mappings.keys():
            attrs.pop(k)  # 从类的命名空间中删除那些已经放入mappings中的属性名
        if not primary_key:
            raise TypeError('没有主键')

        # 重新为类的命名空间内容赋值，并创建该类
        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    '''
    有数据库对应表的类的父类，用于将类与数据库表进行转换，已经进行增删改查
    '''

    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)

    def __getattr__(self, key):
        '''
         __getattr__ 拦截点号运算。
         当对未定义的属性名称和实例进行点号运算时，就会用属性名作为字符串调用这个方法。
         如果继承树可以找到该属性，则不调用此方法
        :param key:
        :return:
        '''
        try:
            return self[key]
        except KeyError:
            raise AttributeError('没有属性： %s' % key)

    def __setattr__(self, key, value):
        '''
        __setattr__会拦截所有属性的的赋值语句。
        如果定义了这个方法，self.arrt = value 就会变成self,__setattr__("attr", value).
        :param key:
        :param value:
        :return:
        '''
        self[key] = value

    @classmethod
    def select_one(cls, **kwrags):
        '''
        只支持单一查询条件
        :param kwrags:  查询条件
        :return:  只返回查询结果中的一条作为返回值
        '''
        ms = conn.Mysql.singleton()  # 创建一个数据库连接对象
        # print(kwrags.keys()[0])
        key = list(kwrags.keys())[0]  # 取出查询条件
        value = kwrags[key]  # 取出查询判断的值
        sql = 'select * from %s where %s= ?' % (cls.table_name, key)
        sql = sql.replace('?', '%s')  # 拼 sql
        res = ms.select(sql, value)  # 执行该sql
        if res:
            return cls(**res[0])  # 取出res的第一条信息，并打散字典，将值传递给类，创建该条数据的对象
        else:
            return None

    @classmethod
    def select_many(cls, **kwargs):
        ms = conn.Mysql.singleton()
        if not kwargs:
            sql = 'select * from %s' % cls.table_name
            res = ms.select(sql, None)
        else:
            key = list(kwargs.keys()[0])
            value = kwargs[key]
            sql = 'select * from %s where %s=?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, value)

        if not res:
            return None
        else:
            return [cls(**re) for re in res]

    def save(self):
        ms = conn.Mysql.singleton()
        # insert into User (name) value(),()
        key = []  # 用于存放要插入的字段名
        enter = []  # 存放 ‘？’
        value = []  # 存放要存的值
        for k, v in self.mappings.items():
            if not v.primary_key:
                key.append(v.name)
                enter.append('?')
                value.append(getattr(self, v.name, None))

        #  ','.join(list)方法 将列表中的元素连接成一个字符串，每个元素用逗号隔开
        sql = 'insert into %s (%s) value (%s)' % (self.table_name, ','.join(key), ','.join(enter))
        sql = sql.replace('?', '%s')
        ms.execut(sql, value)

    def update(self):
        'update User set name=?,balance=? where id=?'
        ms = conn.Mysql.singleton()

        key = []
        value = []

        for k, v in self.mappings.items():
            if v.primary_key:
                pr_key = v.name
                pr_value = getattr(self, v.name, None)
            else:
                key.append(v.name + '= ?')
                value.append(getattr(self, v.name, None))
        sql = 'update %s set %s where %s=%s' % (self.table_name, ','.join(key), pr_key, pr_value)
        sql = sql.replace('?', '%s')

        ms.execut(sql, value)


class User(Model):
    id = IntegerFileld(name='id', primary_key=True, default=0)
    name = StringFileld(name='name')
    balance = IntegerFileld(name='balance', default=0)


if __name__ == '__main__':
    # print(User.select_one(id=1))
    # user=User(name='egon',balance=20)
    # user.save()
    user2 = User.select_one(id=4)
    user2.balance = 500
    user2.update()
    print(User.select_one(id=4))
