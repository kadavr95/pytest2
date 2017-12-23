class Monster(object):
    __slots__ = ("_hp", "_armor", "_damage")
    def __init__(self, hp, armor, damage):
        self._hp = hp
        self._armor = armor
        self._damage = damage
    @property
    def hp(self):
        return self._hp
    @property
    def armor(self):
        return self._armor
    @armor.setter
    def armor(self, val):
        self._armor=val
    def take_damage(self, amount):
        self._hp -=amount
        if self._hp<=0:
            print("ORE WA MOU SHINDEIRU")