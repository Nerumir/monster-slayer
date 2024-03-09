# Initialiser le joueur.
# Rentrer dans une boucle qui s'arrête une fois le niveau 99 atteint
# Rentrer dans une boucle qui demande au joueur ce qu'il souhaite faire (buy, heal ou fight)
# Pour le fight, on casse la boucle et on initialise 3 mobs avec des niveaux aléatoires égal ou moins que le niveau du joueur à 5 niveaux près
# Faire choisir le mob au joueur avec 1 2 ou 3.
# Rentrer dans la boucle de combat ou l'on affiche l'interface de combat et on visualise chaque coup porté jusqu'à ce qu'un des deux n'est plus de durabilité sur son armure
# Si défaite, afficher le message de défaite et interrompre le programme. Si victoire, afficher l'affichage de looting et proposer au joueur de looter.
# Ensuite c'est reparti naturellement pour un tour.

#Tester et équilibrer le jeu via le niveau des mobs relativement au joueur et le nombre de potions / money loot

import player
import mob
import utility
import random
import os

if __name__ == '__main__':

    clear = lambda: os.system('cls')
    clear()
    print("\n"*3)
    print(utility.Util.BANNER)
    print("\n"*3)
    playerName = input("Entrer un pseudo : ")
    player = player.Player(playerName)
    while utility.Util.levelOf(utility.Util, player.exp) < 99:
        feedback = ""
        while True:
            clear()
            print(utility.Util.BANNER_LOBBY)
            print(player.displayPlayer())
            print("")
            print(feedback)
            print("")
            action = input("Que souhaite-tu faire ? (rules, buy <qty>, use, fight) : ")
            try:
                if action.startswith("rules"):
                    clear()
                    print(utility.Util.RULES_BANNER)
                    print(utility.Util.RULES)
                    feedback = ""
                    input("Tapez <ENTER> pour revenir au menu.")
                elif action.startswith("buy"):
                    quantity = int(action.split(" ")[1])
                    player.buy(quantity)
                    feedback = f"Achat de {quantity} potion(s) effectué !"
                elif action.startswith("use"):
                    feedback = f"{player.potion.quantity} potion(s) utilisée(s) !"
                    player.heal()
                elif action.startswith("fight"):
                    break
                else:
                    clear()
                    feedback = "Commande non reconnue."
            except:
                clear()
                feedback = "Vous ne pouvez effectuer cette action."

        player.potion.quantity = 0
        player_lvl = player.getLevel()
        mobs = [mob.Mob(random.randint(player_lvl-5, player_lvl)),
                mob.Mob(random.randint(player_lvl-2, player_lvl)), 
                mob.Mob(random.randint(player_lvl-1, player_lvl+2))]
        clear()
        print(utility.Util.BANNER_MOBS)
        print(utility.Util.displayMobChoice(utility.Util, mobs))
        print(player.displayPlayer())
        while True:
            choice = input("Choisi le mob que tu souhaites affronter (1/2/3) : ")
            try:
                if choice.startswith("1"):
                    number = int(choice[0])
                    break
                elif choice.startswith("2"):
                    number = int(choice[0])
                    break
                elif choice.startswith("3"):
                    number = int(choice[0])
                    break
                else:
                    print("Commande non reconnue.")
            except:
                print("Commande non reconnue.")

        mobChoosen = mobs[number-1]
        counter = 0
        while player.armor.durabilite != 0 and mobChoosen.armor.durabilite != 0:
            clear()
            print(player.displayFight(mobChoosen))
            print(player.displayPlayer())
            input("Tapez <ENTER> pour combattre.")
            if counter % 2 == 0:
                player.hit(mobChoosen)
            else:
                mobChoosen.hit(player)
            counter += 1
        if mobChoosen.armor.durabilite == 0:
            player.giveExp(mobChoosen)
            player.potion.quantity += mobChoosen.potion.quantity
            player.money += mobChoosen.money
            clear()
            print("\n")
            print(utility.Util.BANNER_LOOTING)
            print(mobChoosen.displayLoot(player))
            print(player.displayPlayer())
            while True:
                loot = input("Voulez-vous prendre le stuff du mob ? (y/n) : ")
                if loot.startswith("y"):
                    player.loot(mobChoosen)
                    break
                elif loot.startswith("n"):
                    break
                else:
                    print("Commande non reconnue.")
        else:
            clear()
            print("Vous êtes mort.")
            exit()
    clear()
    print("Félicitations ! Vous avez terminé le jeu !")
    exit()