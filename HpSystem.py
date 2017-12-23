class HPSystem(object):
    def __init__(self, hp):
        self.hp = hp
    def take_damage(self,amount):
        self.hp -=amount
        return self.hp>=0