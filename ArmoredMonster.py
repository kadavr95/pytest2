class ArmoredMonster(BaseMonster):
    def __init__(self, hp, damage,armor):
        super(ArmoredMonster, self).__init__(hp, damage)
        self._armor = armor
        self.__private_var=10
    def _protected_method(self):
        pass
    def __private_method(self):
        pass
    def take_damage(self,amount):
        if self._armor>=amount:
            self._armor-=amount
        else:
            amount-=self._armor
            self._armor=0
            super().take_damage(amount)