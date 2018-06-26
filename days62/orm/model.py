from days62.orm import function


class Field:
    def __init__(self, name, field_type, primary_key, default):
        self.name = name
        self.field_type = field_type
        self.primary_key = primary_key
        self.default = default


class IntegerField(Field):
    def __init__(self, name, field_type='int', primary_key=False, default=0):
        super().__init__(name, field_type, primary_key, default)


class StringField(Field):
    def __init__(self, name, field_type='varchar(32)', primary_key=False, default=None):
        super().__init__(name, field_type, primary_key, default)


class Metaclass(type):
    def __new__(cls, name, base, attrs):
        if name == 'Model':
            return super().__new__(cls, name, base, attrs)
        primary_key = None
        table_name = attrs['table_name']
        if not table_name:
            table_name = name

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise ('主键重复')
                    primary_key = k
        if not primary_key:
            raise ('主键不存在')
        for k in mappings:
            attrs.pop(k)
        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings
        return super().__new__(cls, name, base, attrs)


class Model(dict, metaclass=Metaclass):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # AttributeError('该属性不存在')
            raise AttributeError('该属性不存在')

    @classmethod
    def select(cls, **kwargs):
        ms = function.Mysql()
        # select *  from tablename where key=value
        key = list(kwargs)[0]
        value = kwargs[key]
        sql = 'select *  from %s where %s= ?' % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, value)
        return [cls(**re) for re in res]

    def save(self):
        ms = function.Mysql()
        # inset into table(name,?,?) values(xxx,?,?)
        key = []
        on = []
        value = []
        for v in self.mappings.values():
            if not v.name == self.primary_key:
                key.append(v.name)
                on.append('?')
                value.append(getattr(self, v.name, v.default))
        sql = 'insert into %s (%s) values(%s)' % (self.table_name, ','.join(key), ','.join(on))
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)

    def update(self):
        ms = function.Mysql()
        # update table set name=?,xxx=?... where id=?
        key = []
        value = []
        for v in self.mappings.values():
            if v.name == self.primary_key:
                pk = getattr(self, v.name, v.default)
            else:
                key.append(v.name + '= ?')
                value.append(getattr(self, v.name, v.default))
        sql = 'update %s set %s where %s=%s' % (self.table_name, ','.join(key), self.primary_key, pk)
        sql = sql.replace('?', '%s')
        ms.execute(sql, value)


class User(Model):
    table_name = 'user'
    id = IntegerField(name='id', primary_key=True)
    name = StringField(name='name')
    balance = IntegerField(name='balance', default=100)


if __name__ == '__main__':
    user1 = User.select(id=2)
    print(user1)

    user2 = User(name='lyj')
    user2.save()

    user3 = User.select(name='lyj')[0]
    print(user3)

    user3.balance = 200
    user3.update()
