from days49.orm import mysql


class Field:
    def __init__(self, name, type, primary_key, default):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.default = default


class IntegerField(Field):
    def __init__(self, name=None, type='int', primary_key=False, default=0):
        super().__init__(name, type, primary_key, default)


class StringField(Field):
    def __init__(self, name=None, type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, type, primary_key, default)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        table_name = attrs['table_name']
        if not table_name:
            table_name = name
        primary_key = None
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise KeyError('主键重复')
                    primary_key = v.name
        if not primary_key:
            raise KeyError('没有主键')
        for k in mappings:
            attrs.pop(k)
        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings

        return super().__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('该属性不存在')

    @classmethod
    def select_one(cls, **kwargs):
        ms = mysql.Mysql()
        if kwargs:
            key = list(kwargs)[0]
            value = kwargs[key]

            sql = 'select *  from %s where %s = ?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, value)
        else:
            sql = 'select *  from %s' % cls.table_name
            res = ms.select(sql, None)
        if not res:
            return None
        else:
            return cls(**res[0])

    @classmethod
    def select_many(cls, **kwargs):
        ms = mysql.Mysql()
        if kwargs:
            key = list(kwargs)[0]
            value = kwargs[key]

            sql = 'select * from %s where %s = ?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, value)
        else:
            sql = 'select * from %s ' % cls.table_name
            res = ms.select(sql, None)
        if not res:
            return None
        else:
            return [cls(**re) for re in res]

    def save(self):
        ms = mysql.Mysql()
        # insert into User (name,..) value (?,?,)
        key = []
        on = []
        value = []

        for v in self.mappings.values():
            if not v.primary_key:
                key.append(v.name)
                on.append('?')
                value.append(getattr(self, v.name, v.default))
        sql = 'insert into %s (%s) value (%s)' % (self.table_name, ','.join(key), ','.join(on))
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)

    def update(self):
        ms = mysql.Mysql()
        # update User set name=?.. where id=?
        key = []
        value = []
        for v in self.mappings.values():
            if v.primary_key:
                pr = getattr(self, v.name)
            else:
                key.append(v.name + '=?')
                value.append(getattr(self, v.name, v.default))

        sql = 'update %s set %s where %s=%s' %(self.table_name, ','.join(key),self.primary_key,pr )
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)


class User(Model):
    table_name='user'
    id=IntegerField(name='id',primary_key=True)
    name=StringField(name='name')
    balance=IntegerField(name='balance')


if __name__ == '__main__':
    # user=User(name='lyj',balance=111)
    # user.save()
    # print(user)

    # user1=User.select_many()
    # print(user1)

    user2=User.select_one(name='lyj')
    user2.balance=222
    user2.update()

    user3 = User.select_one(name='lyj')
    print(user3)