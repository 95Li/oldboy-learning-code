from days42.test3 import handler

class Field:
    def __init__(self,name,type,primary_key,default):
        self.name=name
        self.type=type
        self.primary_key=primary_key
        self.default=default

class StringField(Field):
    def __init__(self,name,type='varchar(200)',primary_key=False,default=None):
        super().__init__(name,type,primary_key,default)

class IntegerField(Field):
    def __init__(self,name,type='int',primary_key=False,default=0):
        super().__init__(name,type,primary_key,default)

class ModelMetaclass(type):
    def __new__(cls, name,bases,attr):
        if name=='Model':
            return type.__new__(cls,name,bases,attr)

        table_name=attr.get('table_name',None)
        primary_key=attr.get('primary_key',None)

        if not table_name:
            table_name=name

        mappings=dict()
        for k,v in attr.items():
            if isinstance(v,Field):
                mappings[k]=v
                if v.primary_key:
                    if primary_key:
                        raise TypeError('主键重复')
                    primary_key=k

        if not primary_key:
              raise TypeError('没有主键')

        attr['table_name']=table_name
        attr['primary_key']=primary_key
        attr['mappings']=mappings
        return type.__new__(cls,name,bases,attr)

class Model(dict,metaclass=ModelMetaclass):
    def __setattr__(self, key, value):
        self[key]=value

    def __getattr__(self, key):
        return self[key]

    @classmethod
    def select_one(cls,**kwargs):
        ms=handler.Mysql.singleton()
        if not kwargs:
            sql='select * from %s' %cls.table_name
            res =ms.execute(sql,None)
        else:
            key=list(kwargs.keys())[0]
            value=kwargs[key]
            sql='select * from %s where %s =?' %(cls.table_name,key)
            sql=sql.replace('?','%s')
            res=ms.execute(sql,value)
        if not res:
            return None
        return cls(**res[0])

    @classmethod
    def select_many(cls, **kwargs):
        ms = handler.Mysql.singleton()
        if not kwargs:
            sql = 'select * from %s' % cls.table_name
            res = ms.execute(sql, None)
        else:
            key = list(kwargs.keys())[0]
            value = kwargs[key]
            sql = 'select * from %s where %s =?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.execute(sql, value)
        if not res:
            return None
        return [cls(**re) for re in res]






