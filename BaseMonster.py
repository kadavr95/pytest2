class BaseMonster(object):
    __slots__ = ("_hp", "_damage")
    def __init__(self, hp, damage):
        self._hp = hp
        self._damage = damage
    @property
    def hp(self):
        return self._hp
    def take_damage(self, amount):
        self._hp -=amount
        if self._hp<=0:
            print("ORE WA MOU SHINDEIRU")