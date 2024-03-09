import utility
import item
import random
import mob

class Entity:

    def __init__(self, lvl: int, name: str, arme: item.Arme, armor: item.Armor, potion: item.Potion, money: int) -> None:
        
        self.exp = utility.Util.baseLevel(utility.Util, lvl)
        self.arme = arme
        self.armor = armor
        self.potion = potion
        self.money = money
        self.name = name

    def hit(self, target: "Entity") -> None:

        damage = self.arme.degats
        if(random.randint(0,100) <= self.arme.chance_cc):
            damage *= 1+self.arme.force_cc/100
        
        debuff = 1
        if(type(self) == mob.Mob):
            debuff = 0.4
        inflicted = int((damage - damage*target.armor.resistance/100)*debuff)
        target.armor.durabilite = max(0, target.armor.durabilite-inflicted)

    def getLevel(self) -> int:
        return utility.Util.levelOf(utility.Util, self.exp)
    
    def displayHealth(self) -> str:

        full = int((self.armor.durabilite/self.armor.maxDurabilite)*60)
        incr_name = int((62-len(self.name))/2)
        res_lines = []
        res_lines.append(" "*(8+incr_name)+self.name)
        res_lines.append(" "*8+"_"*62)
        res_lines.append(" "*8+"|"+"◼"*full+" "*(60-full)+"|")
        res_lines.append(" "*8+"‾"*62)
        return "\n".join(res_lines)