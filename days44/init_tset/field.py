from days44.init_tset import conn


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
                        raise TypeError('主键重复')
                    primary_key = v.name

        if not primary_key:
            raise TypeError('没有主键')
        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    @classmethod
    def select_one(cls, **kwargs):
        ms = conn.Mysql()
        # 'select * from User where %s =?'
        key = list(kwargs.keys())[0]
        value = kwargs[key]

        sql = 'select * from %s where %s = ? ' % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, value)
        if not res:
            return None
        return cls(**res[0])

    def save(self):
        ms = conn.Mysql()
        # 'insert into User (,,,) value()'
        key = []
        on = []
        value = []
        for v in self.mappings.values():
            if v.primary_key:
                pr = getattr(self, v.name, None)
            else:
                key.append(v.name)
                on.append('?')
                value.append(getattr(self, v.name, None))
        sql = 'insert into %s (%s) value (%s)' % (self.table_name, ','.join(key), ','.join(on))
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)


class User(Model):
    id = IntegerField(name='id', primary_key=True)
    name = StringField(name='name')
    balance = IntegerField(name='balance')

    def __init__(self,  name, balance,id=None):
        self.id = id
        self.name = name
        self.balance = balance


if __name__ == '__main__':
    user1 = User(name='000', balance=100)
    # user1.save()
    print(user1.__dict__)
    print(user1.name)

    user2 = User.select_one(id=3)
    print(user2.__dict__)
    print(user2.name)
