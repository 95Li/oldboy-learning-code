from days42.test2 import conn

class Field:
    def __init__(self,name,type,primary_key,default):
        self.name=name
        self.type=type
        self.primary_key=primary_key
        self.default=default
class StringField(Field):
    def __init__(self,name=None,type='varchar(200)',primary_key=False,default=None):
        super().__init__(name,type,primary_key,default)

class IntegerField(Field):
    def __init__(self, name=None, type='int', primary_key=False, default=0):
        super().__init__(name, type, primary_key, default)

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)

        table_name=attrs.get('table_name',None)
        primary_key=None

        if not table_name:
            table_name=name

        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                mappings[k]=v
                if v.primary_key:
                    if primary_key:
                        raise AttributeError('主键重复')
                    primary_key=k
        for k in mappings.keys():
            attrs.pop(k)

        if not primary_key:
            raise TypeError('没有主键')

        attrs['primary_key']=primary_key
        attrs['table_name']=table_name
        attrs['mappings']=mappings
        return type.__new__(cls,name,bases,attrs)


class Model(dict,metaclass=ModelMetaclass):
    def __setattr__(self, key, value):
        self[key]=value

    def __getattr__(self, key):
        return self[key]

    @classmethod
    def select_one(cls,**kwargs):
        ms=conn.Mysql.singleton()
        if not kwargs:
            sql='select * from %s' %cls.table_name
            res = ms.select(sql, None)
        else:
            key=list(kwargs.keys())[0]
            value=kwargs[key]
            sql='select * from %s where %s = ?' %(cls.table_name,key)
            sql=sql.replace('?','%s')
            res=ms.select(sql,value)
        if not res:
            return None
        return cls(**res[0])
    @classmethod
    def select_many(cls,**kwargs):
        ms=conn.Mysql.singleton()
        if not kwargs:
            sql='select * from %s' %cls.table_name
            res=ms.select(sql,None)
        else:
            key=list(kwargs.keys())[0]
            value=kwargs[key]
            sql='select * from %s where %s = ?' %(cls.table_name,key)
            sql=sql.replace('?','%s')
            res=ms.select(sql,value)
        if not res:
            return  None
        return [cls(**re) for re in res]


class User(Model):
    id=IntegerField(name=id,primary_key=True)
    name=StringField(name='name')


if __name__ == '__main__':
    re=User.select_one(id=2)
    print(re)

    print(User.table_name)



