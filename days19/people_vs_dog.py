class People:
    def __init__(self,name,agg,life_value):
        self.name=name
        self.agg=agg
        self.life_value=life_value
    def bite(self,enemy):
        enemy.life_value-=self.agg
        print('''
           人[%s]咬了狗[%s]一口
           狗掉血[%s]
           狗剩余血量[%s]
        '''%(self.name,enemy.name,self.agg,enemy.life_value))


class dog:
    def __init__(self,name,agg,life_value,dog_type):
        self.name=name
        self.agg=agg
        self.life_value = life_value
        self.dog_type=dog_type
    def bite(self,enemy):
        enemy.life_value-=self.agg
        print('''
            狗{0}咬了人{1}一口
            人{1}掉血{2}
            剩余血量{3}'''.format(self.name,enemy.name,self.agg,enemy.life_value))


dog1=dog('金毛',50,80,'大狗')
people1=People('egon',30,100)

dog1.bite(people1)
people1.bite(dog1)