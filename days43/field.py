from days43 import model


class Field:
    def __init__(self, name, type, primary_kay, default):
        self.name = name
        self.type = type
        self.primary_key = primary_kay
        self.default = default


class IntegerField(Field):
    def __init__(self, name=None, type='int', primary_kay=False, default=0):
        super().__init__(name, type, primary_kay, default)


class StringField(Field):
    def __init__(self, name=None, type='varchar(200)', primary_kay=False, default=0):
        super().__init__(name, type, primary_kay, default)


class ModelMetacalss(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)

        table_name = attrs.get('table_name', None)
        if not table_name:
            table_name=name
        primary_key = None
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise TypeError('primary key error')
                    primary_key = v.name
        if not primary_key:
            raise TypeError('primary key dose not exist')

        for k in mappings:
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings

        return type.__new__(cls, name, bases, attrs)

class Model(dict,metaclass=ModelMetacalss):
    def __setattr__(self, key, value):
        self[key]=value

    def __getattr__(self, key):
        return self[key]

    @classmethod
    def select_one(cls,**kwargs):
        ms=model.Mysql()
        if kwargs:
            key=list(kwargs.keys())[0]
            value=kwargs[key]

            sql='select * from %s where %s=?'%(cls.table_name,key)
            sql=sql.replace('?','%s')
            res=ms.select(sql,value)
        else:
            sql='select * from %s' %cls.table_name
            res = ms.select(sql, None)
        if not res:
            return None
        return cls(**res[0])

    @classmethod
    def select_many(cls,**kwargs):
        ms = model.Mysql()
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs[key]

            sql = 'select * from %s where %s=?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res=ms.select(sql, value)
        else:
            sql = 'select * from %s' % cls.table_name
            res = ms.select(sql,None)
        if not res:
            return None
        return [cls(**re) for re in res]

    def save(self):
        'insert into User (name,balance) value(?,?)'
        ms = model.Mysql()

        key=[]
        enter=[]
        value=[]
        for v in self.mappings.values():
            if not v.primary_key:
                key.append(v.name)
                enter.append('?')
                value.append(getattr(self,v.name,None))

        sql='insert into %s (%s) value(%s)' %(self.table_name,','.join(key),','.join(enter))
        sql=sql.replace('?','%s')
        ms.execute(sql,value)

    def update(self):
        'update  User set name=?,balance=? where id=?'
        ms = model.Mysql()

        key = []
        value = []
        for v in self.mappings.values():
            if not v.primary_key:
                key.append(v.name+'=?')
                value.append(getattr(self, v.name, None))
            else:
                pr=getattr(self,v.name,None)

        sql = 'update  %s set %s where %s = %s' % (self.table_name, ','.join(key), self.primary_key,pr)
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)


class User(Model):
    id=IntegerField(name='id',primary_kay=True)
    name=StringField(name='name')
    balance=IntegerField(name='balance')

if __name__ == '__main__':

    user1=User.select_one(id=1)
    print(user1)
    user2=User.select_many(balance= 1000)
    print(user2)

    # user3 = User(name='lyj', balance=200)
    # print(user3)
    # user3.save()

    user1.name='lyj'
    user1.update()
    user4 = User.select_one(id=1)
    print(user4)




