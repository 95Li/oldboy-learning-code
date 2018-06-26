from days42.test1 import conn

class Field:
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    def __init__(self, name=None, column_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, column_type, primary_key, default)


class IntegerField(Field):
    def __init__(self, name=None, column_type='int', primary_key=False, default=0):
        super().__init__(name, column_type, primary_key, default)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        table_name = attrs.get('table_name', None)
        if not table_name:
            table_name = name
        primary_key = None

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise AttributeError('主键重复')
                    else:
                        primary_key = v.name
        for k in mappings.keys():
            attrs.pop(k)

        if not primary_key:
            raise TypeError('没有主键')

        attrs['primary_key'] = primary_key
        attrs['table_name'] = table_name
        attrs['mappings'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        return self[key]

    @classmethod
    def select_one(cls,**kwargs):
        ms=conn.Mysql()

        key=list(kwargs.keys())[0]
        value=kwargs[key]
        sql='select * from %s where %s= ? ' %(cls.table_name,key)
        sql=sql.replace('?','%s')

        res=ms.select(sql,value)
        if not res:
            return None
        else:
            return cls(**res[0])

    @classmethod
    def select_many(cls,**kwargs):
        ms=conn.Mysql()

        if not kwargs:
            sql='select * from %s' %cls.table_name
            res=ms.select(sql,None)
        else:
            key=list(kwargs.keys())[0]
            value=kwargs[key]
            sql='select * from %s where %s =?' %(cls.table_name,key)
            sql=sql.replace('?','%s')
            res=ms.select(sql,value)

        if not res:
            return  None
        else:
            return [cls(**re) for re in res]

    def save(self):
        'insert into User (name,balance) value(?,?)'
        ms=conn.Mysql()
        key=[]
        enter=[]
        value=[]
        for k,v in self.mappings.items():
            if not v.primary_key:
                key.append(v.name)
                enter.append('?')
                value.append(getattr(self,v.name,None))
        sql='insert into %s (%s) value (%s)' %(self.table_name,','.join(key),','.join(enter))
        sql=sql.replace('?','%s')

        ms.execute(sql,value)

    def update(self):
        'update User set name=?,balance=? where id = '
        ms=conn.Mysql()
        key=[]
        value=[]
        for v in self.mappings.values():
            if v.primary_key:
                pr_key=v.name
                pr=getattr(self,v.name,None)
            else:
                key.append(v.name+'=?')
                value.append(getattr(self,v.name,None))
        print(self)
        sql='update %s set %s where %s=%s' %(self.table_name,','.join(key),pr_key,pr)
        sql=sql.replace('?','%s')
        ms.execute(sql,value)

class User(Model):
    id=IntegerField(name='id',primary_key=True)
    name=StringField(name='name')
    balance=IntegerField(name='balance')


if __name__ == '__main__':
    # user=User(name='123',balance=30)
    # user.save()
    print(User.__dict__)
    res=User.select_many(name='qwe')
    if res:
        res=res[0]
    print(res)
    res.name='qwe'
    res.update()
    print(User.select_many(name='qwe'))
    print(User.select_many())

    # res=User.select_one(id=2)
    # print(res)
    # print(User,User.__dict__)



