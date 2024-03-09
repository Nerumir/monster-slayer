import random
import utility

class Arme:
    def __init__(self, lvl: int) -> None:
        self.degats = utility.Util.setDamage(utility.Util, lvl)
        crit = utility.Util.setCC(utility.Util, lvl)
        self.chance_cc = crit[0]
        self.force_cc = crit[1]
        self.name = random.choice(utility.Util.ARMES)
        self.level = max(1, min(lvl, 99))

class Armor:
    def __init__(self, lvl: int) -> None:
        self.resistance = utility.Util.setResistance(utility.Util, lvl)
        max_dura = utility.Util.setDurabilite(utility.Util, lvl)
        self.durabilite = max_dura
        self.maxDurabilite = max_dura
        self.name = random.choice(utility.Util.ARMURES)
        self.level = max(1, min(lvl, 99))

class Potion:

    price = 35

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity
        self.name = "Potion"