import utility
import item
import entity
import mob

class Player(entity.Entity):

    def __init__(self, name: str) -> None:
        
        arme = item.Arme(2)
        armor = item.Armor(2)
        potion = item.Potion(0)
        money = 0
        super().__init__(1, "name", arme, armor, potion, money)
        self.exp = 0
        self.name = name
        self.skin = utility.Util.PLAYER_SKIN

    def displayPlayer(self) -> str:
        res_lines = []
        res_lines.append("-"*120)
        tab = self.skin.split("\n")
        for i in range(len(tab)):
            displayed = "|  "+tab[i]+"*"
            if(i == 0):
                displayed += f"  {self.name} (Lv. {self.getLevel()})" + "   " + self.displayExp()
            if(i == 2):
                displayed += f"  ⚔️  Arme >> {self.arme.name} Lv. {self.arme.level} ( Dégâts {'{:,}'.format(self.arme.degats).replace(',', ' ')} - Chance CC {self.arme.chance_cc}% - Force CC {self.arme.force_cc}% )"
            if(i == 4):
                displayed += f"  🛡️  Armure >> {self.armor.name} Lv. {self.armor.level} ( Résistance {self.armor.resistance}% - Durabilité {'{:,}'.format(self.armor.durabilite).replace(',', ' ')} / {'{:,}'.format(self.armor.maxDurabilite).replace(',', ' ')} )"
            if(i == 6):
                displayed += f"  🍸 Potions  >> {self.potion.quantity} | 💰 Or >> {'{: }'.format(self.money).replace(',', ' ')} ({item.Potion.price} Or / Potion)"
            res_lines.append(displayed)
        res_lines.append("-"*120)
        return "\n".join(res_lines)

    def loot(self, mob: "mob.Mob") -> None:
        self.arme = mob.arme
        armor = mob.armor
        armor.durabilite = min(self.armor.durabilite, armor.maxDurabilite)
        self.armor = armor

    def buy(self, quantity: int) -> None:
        if(self.money >= item.Potion.price*quantity):
            self.potion.quantity += quantity
            self.money -= item.Potion.price*quantity
        else:
            raise Exception('')

    def heal(self) -> None:
        if(0 < self.potion.quantity):
            self.armor.durabilite = min(self.armor.maxDurabilite, self.armor.durabilite + int(0.1*self.potion.quantity*self.armor.maxDurabilite))
            self.potion.quantity = 0
        else:
            raise Exception('')
    
    def displayFight(self, mob: mob.Mob) -> None:
        res_lines = ["\n"]
        tab = mob.skin.split("\n")
        for i in range(len(tab)):
            displayed = "  "+tab[i]
            healthMob = mob.displayHealth().split("\n")
            if(i == 4):
                displayed += healthMob[0]
            if(i == 5):
                displayed += healthMob[1]
            if(i == 6):
                displayed += healthMob[2]
            if(i == 7):
                displayed += healthMob[3]
            if(i == 8):
                displayed += f"  ⚔️  Arme >> {mob.arme.name} Lv. {mob.arme.level} ( Dégâts {mob.arme.degats} - Chance CC {mob.arme.chance_cc}% - Force CC {mob.arme.force_cc}% )"
            if(i == 9):
                displayed += f"  🛡️  Armure >> {mob.armor.name} Lv. {mob.armor.level} ( Résistance {mob.armor.resistance}% - Durabilité {mob.armor.durabilite} / {mob.armor.maxDurabilite} )"
            healthPlayer = self.displayHealth().split("\n")
            if(i == 15):
                displayed += healthPlayer[0]
            if(i == 16):
                displayed += healthPlayer[1]
            if(i == 17):
                displayed += healthPlayer[2]
            if(i == 18):
                displayed += healthPlayer[3]
            res_lines.append(displayed)
        res_lines.append("\n")
        return "\n".join(res_lines)

    def giveExp(self, mob: mob.Mob) -> None:
        lvl_mob = mob.getLevel()
        exp_of_lvl = utility.Util.SCALE[lvl_mob-1]
        self.exp += int(exp_of_lvl/1)

    def displayExp(self) -> str:
        size = 60
        maxExp = utility.Util.SCALE[self.getLevel()-1]
        exp = self.exp - utility.Util.baseLevel(utility.Util, self.getLevel())+1
        full = int((exp/maxExp)*size)
        percent = int((exp/maxExp)*100)
        return "["+"-"*full+" "*(size-full)+"]"+ f" ( {percent}% )"