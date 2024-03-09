import utility
import item
import entity
import random
import player

class Mob(entity.Entity):

    def __init__(self, lvl: int) -> None:
        
        arme = item.Arme(lvl)
        armor = item.Armor(lvl)
        potion = item.Potion(random.randint(1, 5))
        money = random.randint(35, 100)
        super().__init__(lvl, "name", arme, armor, potion, money)
        mob = random.choice(utility.Util.MOBS)
        self.name = mob["name"]
        self.skin = mob["skin"]

    def displayLoot(self, player: "player.Player") -> str:
        res_lines = ["\n"]
        tab = utility.Util.CHEST_SKIN.split("\n")
        for i in range(len(tab)):
            displayed = "  "+tab[i]
            if(i == 4):
                displayed += f"  ⚔️  Arme >> {self.arme.name} Lv. {self.arme.level} ( Dégâts {self.arme.degats} - Chance CC {self.arme.chance_cc}% - Force CC {self.arme.force_cc}% )"
            if(i == 6):
                displayed += f"  🛡️  Armure >> {self.armor.name} Lv. {self.armor.level} ( Résistance {self.armor.resistance}% - Durabilité {min(player.armor.durabilite, self.armor.maxDurabilite)} / {self.armor.maxDurabilite} )"
            res_lines.append(displayed)
        res_lines.append("\n")
        return "\n".join(res_lines)