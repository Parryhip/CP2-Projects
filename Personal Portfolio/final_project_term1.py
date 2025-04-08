#Samuel Andelin, FINAL PROJECT!!!
import random
import time
listofanamotopoeia = ["Bang!", "Whack!", "Kapow!", "Kazoinks!", "Bonk!", "Bazingha!", "Yooooowch!", "Oowie", "Boom! Shackalackalacka!"]
room1 = {
    'monster_probability' : 0,
    'final_boss' : False,
    'room_accesses' : [2, 3],
    'common_chest_prob' : 100,
    'rare_chest_prob' : 0,
    'legendary_chest_prob' : 0
}
room2 = {
    'monster_probability' : 50,
    'final_boss' : False,
    'room_accesses' : [4, 1],
    'common_chest_prob' : 70,
    'rare_chest_prob' : 100,
    'legendary_chest_prob' : 0
}
room3 = {
    'monster_probability' : 60,
    'final_boss' : False,
    'room_accesses' : [1, 6, 9],
    'common_chest_prob' : 40,
    'rare_chest_prob' : 80,
    'legendary_chest_prob' : 100
}
room4 = {
    'monster_probability': 60,
    'final_boss' : False,
    'room_accesses' : [2, 5],
    'common_chest_prob' : 60,
    'rare_chest_prob' : 100,
    'legendary_chest_prob' : 0
}
room5 = {
    'monster_probability' : 70,
    'final_boss' : False,
    'room_accesses' : [4, 7, 9],
    'common_chest_prob' : 49,
    'rare_chest_prob' : 99,
    'legendary_chest_prob' : 100
}
room6 = {
    'monster_probability' : 100,
    'final_boss' : False,
    'room_accesses' : [3],
    'common_chest_prob' : 10,
    'rare_chest_prob' : 30,
    'legendary_chest_prob' : 100
}
room7 = {
    'monster_probability' : 80,
    'final_boss' : False,
    'room_accesses' : [5, 8],
    'common_chest_prob' : 10,
    'rare_chest_prob' : 70,
    'legendary_chest_prob' : 100
}
room8 = {
    'monster_probability' : 90,
    'final_boss' : False,
    'room_accesses' : [7, 9],
    'common_chest_prob' : 0,
    'rare_chest_prob' : 50,
    'legendary_chest_prob' : 100
}
room9 = {
    'monster_probability' : 100,
    'final_boss' : True,
    'room_accesses' : [3,5,8],
    'common_chest_prob' : 0,
    'rare_chest_prob' : 0,
    'legendary_chest_prob' : 100
}
plyrstats = {
    'hp' : 50,
    'strength' : 13,
    'speed' : 13,
    'potioninventory' : [],
    'spellinventory' : [],
    'weaponinventory' : [],
    'weaponcurrentlyequipped' : "dagger",
}
normal_enemy = {
    'hp' : 30,
    'strength' : 10,
    'speed' : 10
}
final_boss = {
    'hp' : 100,
    'strength' : 18,
    'speed' : 18,
    'spellinventory' : ['fireball', 'slow spell'],
    'potioninventory' : ['health potion', 'strength potion', 'speed potion']
}
common_chest ={
    'spellinventory' : [],
    'potioninventory' : ['health potion'],
    'weaponinventory' : ['dagger']
}
rare_chest ={
    'spellinventory' : ['slow spell'],
    'potioninventory' : ['health potion'],
    'weaponinventory' : ['shortsword']
}
legendary_chest ={
    'spellinventory' : ['fireball', 'slow spell'],
    'potioninventory' : ['health potion', 'strength potion', 'speed potion'],
    'weaponinventory' : ['longsword']
}
current_room = "room1"
def play_again():
    while True:
        playagain = input("Do you want to play again?(y/n)")
        if playagain.lower() == "y":
            return True
        elif playagain.lower() == "n":
            return False
        else:
            print("Invalid input.")
            time.sleep(1.5)
            continue
def plyrturn():
    while True:
        plyraction = input("What do you want to do? 1 for attack with sword, 2 for use potion, 3 for cast spell, 4 for switch weapon, and 5 for run away.")
        if plyraction == "1":
            if current_room == "room9":
                print("You attack with your sword.")
                time.sleep(1.5)
                print("Rolling die for attack...")
                time.sleep(1.5)
                attack = random.randint(1,20)
                print("You got a " + str(attack) + ".")
                time.sleep(1.5)
                overall_attack = str((plyrstats['strength']//3)+attack)
                print("With your +"+ str(plyrstats['strength']//3) +" modifier means that you end with a "+overall_attack+".")
                time.sleep(1.5)
                print(random.choice(listofanamotopoeia))
                time.sleep(1.5)
                print("You hit the final boss for "+overall_attack+".")
                final_boss['hp'] -= int(overall_attack)
                time.sleep(1.5)
                print("The final_boss's hp is now "+str(final_boss['hp']) +".")
                time.sleep(1.5)
                if final_boss['hp'] <= 0:
                    print("You killed the final boss!")
                    return 'theywon'
                else:
                    print("Enemy's turn!")
                    return 'enemynotdead'
            else:
                print("You attack with your sword.")
                time.sleep(1.5)
                print("Rolling die for attack...")
                time.sleep(1.5)
                attack = random.randint(1,20)
                print("You got a " + str(attack) + ".")
                time.sleep(1.5)
                overall_attack = str((plyrstats['strength']//3)+attack)
                print("With your +"+ str(plyrstats['strength']//3) +" modifier means that you end with a "+overall_attack+".")
                time.sleep(1.5)
                print(random.choice(listofanamotopoeia))
                time.sleep(1.5)
                print("You hit the monster for "+overall_attack+".")
                normal_enemy['hp'] -= int(overall_attack)
                time.sleep(1.5)
                print("The monster's hp is now "+str(normal_enemy['hp']) +".")
                time.sleep(1.5)
                if normal_enemy['hp'] <= 0:
                    print("You killed the enemy!")
                    return 'enemydead'
                else:
                    print("Enemy's turn!")
                    return 'enemynotdead'
        elif plyraction == "2":
            print("These are the potions that you have:")
            time.sleep(1.5)
            print(plyrstats['potioninventory'])
            time.sleep(1.5)
            while True:
                potiontouse = input("What potion do you want to use?(use the exact name of the item) or type exit to exit the potion menu.")
                if potiontouse in plyrstats['potioninventory']:
                    print("You use your" + potiontouse + ".")
                    if potiontouse == "speed potion":
                        speedpotionindex = plyrstats['potioninventory'].index("speed potion")
                        plyrstats['potioninventory'].pop(speedpotionindex)
                        plyrstats['speed'] += 5
                        return 'enemynotdead'
                    elif potiontouse == "strength potion":
                        strengthpotionindex = plyrstats['potioninventory'].index("strength potion")
                        plyrstats['potioninventory'].pop(strengthpotionindex)
                        plyrstats['strength'] += 5
                        return 'enemynotdead'
                    elif potiontouse == "health potion":
                        healthpotionindex = plyrstats['potioninventory'].index("health potion")
                        plyrstats['potioninventory'].pop(healthpotionindex)
                        plyrstats['hp'] += 20
                        return 'enemynotdead'
                elif potiontouse == "exit":
                    break
                else:
                    print("You do not have that potion!")
                    time.sleep(1.5)
        elif plyraction == "3":
            print("These are the spells that you have:")
            time.sleep(1.5)
            print(plyrstats['spellinventory'])
            time.sleep(1.5)
            while True:
                spelltouse = input("What spell do you want to use?(use the exact name of the item) or type exit to exit the spell menu.")
                if spelltouse in plyrstats['spellinventory']:
                    print("You use your" + spelltouse + ".")
                    if spelltouse == "fireball":
                        fireballspellindex = plyrstats['spellinventory'].index("fireball")
                        plyrstats['spellinventory'].pop(fireballspellindex)
                        if current_room == "room9":
                            final_boss['hp'] -= 20
                            print("You hit the final boss for 20.")
                            time.sleep(1.5)
                            print("The final boss's hp is now "+str(final_boss['hp'] +"."))
                            if final_boss['hp'] <= 0:
                                print("You killed the final_boss!")
                                return 'theywon'
                            else:
                                print("Final boss's turn!")
                                return 'enemynotdead'                                 
                        else:
                            normal_enemy['hp'] -= 20
                            print("You hit the monster for 20.")
                            time.sleep(1.5)
                            print("The monster's hp is now "+str(normal_enemy['hp'] +"."))
                            time.sleep(1.5)
                            if normal_enemy['hp'] <= 0:
                                print("You killed the enemy!")
                                return 'enemydead'
                            else:
                                print("Enemy's turn!")
                                return 'enemynotdead'
                    elif spelltouse == "slow spell":
                        slowspellspellindex = plyrstats['spellinventory'].index("slow spell")
                        plyrstats['spellinventory'].pop(slowspellspellindex)
                        if current_room == "room9":
                            final_boss['speed'] -= 10
                            print("You decrease the final boss's speed by 10.")
                            time.sleep(1.5)
                            print("The final boss's speed is now "+str(final_boss['speed'] +"."))
                            return 'enemynotdead'
                        else:
                            normal_enemy['speed'] -= 10
                            print("You decrease the monster's speed by 10.")
                            time.sleep(1.5)
                            print("The monster's speed is now "+str(normal_enemy['speed'] +"."))
                            time.sleep(1.5)
                            return 'enemynotdead'
                elif spelltouse == "exit":
                    break
                else:
                    print("You do not have that spell!")
                    time.sleep(1.5)
        elif plyraction == "4":
            print("These are the weapons that you have:")
            print(plyrstats['weaponinventory'])
            time.sleep(1.5)
            print("The weapon currently equipped is your "+ plyrstats['weaponcurrentlyequipped']+".")
            time.sleep(1.5)
            while True:
                weapontoequip = input("What weapon do you want to equip?(use the exact name of the item) or type exit to exit the weapon menu.")
                if weapontoequip in plyrstats['weaponinventory']:
                    print("You equip your" + weapontoequip + ".")
                    if weapontoequip == "longsword":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "longsword"
                        plyrstats['strength'] += 6
                    elif weapontoequip == "longsword":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "shortsword"
                        plyrstats['strength'] += 4
                    elif weapontoequip == "dagger":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "dagger"
                        plyrstats['strength'] += 2
                elif weapontoequip == "exit":
                    break
                else:
                    print("You do not have that weapon!")
                    time.sleep(1.5)
        elif plyraction == "5":
            print("You try to run away.")
            monsterwantstoblock = random.randint(0,1)
            if monsterwantstoblock == 1:
                if current_room == "room9":
                    print("The final boss is trying to block you.")
                    time.sleep(1.5)
                    print("Rolling die for final boss...")
                    time.sleep(1.5)
                    monsterrolltoblock = random.randint(1,20)
                    print("The final boss got a "+str(monsterrolltoblock)+".")
                    time.sleep(1.5)
                    print("With the final boss's modifier of +"+str(final_boss['speed']//3)+" means that the final boss got a "+str(monsterrolltoblock+normal_enemy['speed']//3))
                    time.sleep(1.5)
                    print("Rolling die for you...")
                    time.sleep(1.5)
                    plyrrolltorunaway = random.randint(1,20)
                    print("You got a "+str(plyrrolltorunaway))
                    time.sleep(1.5)
                    print("With your modifier of +"+str(plyrstats['speed']//3)+" means that you got a "+ str(plyrrolltorunaway+plyrstats['speed']//3))
                    if (plyrrolltorunaway+plyrstats['speed']//3) > (monsterrolltoblock+normal_enemy['speed']//3):
                        print("You got away!")
                        return "exitcombat"
                    else:
                        print("The final boss successfully blocked you.")
                        return "enemynotdead"
                else:
                    print("The monster is trying to block you.")
                    time.sleep(1.5)
                    print("Rolling die for monster...")
                    time.sleep(1.5)
                    monsterrolltoblock = random.randint(1,20)
                    print("The monster got a "+str(monsterrolltoblock)+".")
                    time.sleep(1.5)
                    print("With the monster's modifier of +"+str(normal_enemy['speed']//3)+" means that the monster got a "+str(monsterrolltoblock+normal_enemy['speed']//3))
                    time.sleep(1.5)
                    print("Rolling die for you...")
                    time.sleep(1.5)
                    plyrrolltorunaway = random.randint(1,20)
                    print("You got a "+str(plyrrolltorunaway))
                    time.sleep(1.5)
                    print("With your modifier of +"+str(plyrstats['speed']//3)+" means that you got a "+ str(plyrrolltorunaway+plyrstats['speed']//3))
                    if (plyrrolltorunaway+plyrstats['speed']//3) > (monsterrolltoblock+normal_enemy['speed']//3):
                        print("You got away!")
                        return "exitcombat"
                    else:
                        print("The monster successfully blocked you.")
                        return "enemynotdead"
            else:
                print("The enemy doesn't want to block you!")
                print("You escape!")
                return "exitcombat"
        else:
            print("Not a valid input.")
def monsterturn():
    global current_room
    if current_room == "room9":
        finalbossincombat = True
    else:
        finalbossincombat = False
    if finalbossincombat:
        monsteraction = str(random.randint(1,3))
        if monsteraction == "1":
            print("The final boss is attacking with their greatsword!")
            time.sleep(1.5)
            print("Rolling die for attack...")
            time.sleep(1.5)
            attack = random.randint(1,20)
            print("The final boss got a " + str(attack) + ".")
            time.sleep(1.5)
            overall_attack = str((final_boss['strength']//3)+attack)
            print("With their +"+ str(final_boss['strength']//3) +" modifier means that the final boss ends with a "+overall_attack+".")
            time.sleep(1.5)
            print(random.choice(listofanamotopoeia))
            time.sleep(1.5)
            print("The final boss hits you for "+overall_attack+".")
            plyrstats['hp'] -= int(overall_attack)
            time.sleep(1.5)
            print("Your hp is now "+str(plyrstats['hp'] +"."))
            time.sleep(1.5)
            if plyrstats['hp'] <= 0:
                print("Sadly, you have died to the final boss, ruler of all the dungeon.")
                return 'playerdead'
            else:
                print("Your turn!")
                return 'playernotdead'
        elif monsteraction == "2":
            potiontousemonster = random.choice(final_boss['potioninventory'])
            print("The final boss is using their" + potiontousemonster + ".")
            if potiontousemonster == "speed potion":
                final_boss['speed'] += 5
                return 'playernotdead'
            elif potiontousemonster == "strength potion":
                final_boss['strength'] += 5
                return 'playernotdead'
            elif potiontousemonster == "health potion":
                final_boss['hp'] += 20
                return 'playernotdead'
        elif monsteraction == "3":
            while True:
                spelltousemonster = random.choice(final_boss['spellinventory'])
                print("The final boss is using their " + spelltousemonster + ".")
                if spelltousemonster == "fireball":
                    plyrstats['hp'] -= 20
                    print("The final boss hits you for 20.")
                    time.sleep(1.5)
                    print("Your hp is now "+str(plyrstats['hp']) +".")
                    time.sleep(1.5)
                    if plyrstats['hp'] <= 0:
                        print("Sadly, you have died to the final boss, ruler of all the dungeon.")
                        return 'playerdead'
                    else:
                        print("Your turn!")
                        return 'playernotdead'
                elif spelltousemonster == "slow spell":
                    plyrstats['speed'] -= 10
                    print("The final boss decreases your speed by 10.")
                    time.sleep(1.5)
                    print("Your speed is now "+str(plyrstats['speed']) +".")
                    time.sleep(1.5)
                    return 'playernotdead'
    else:
        if normal_enemy['hp'] <= 5:
            monsterwantstorunaway = random.randint(0,1)
            if monsterwantstorunaway == 0:
                print("The monster wants to run away.")
                plyrwantstoblock = input("Do you want to block the monster")
                if plyrwantstoblock.lower() == "y":
                    print("You try to block the monster")
                    time.sleep(1.5)
                    print("Rolling die for you...")
                    time.sleep(1.5)
                    plyrrolltorunaway = random.randint(1,20)
                    print("You got a "+str(plyrrolltorunaway))
                    time.sleep(1.5)
                    print("With your modifier of +"+str(plyrstats['speed']//3)+" means that you got a "+ str(plyrrolltorunaway+plyrstats['speed']//3))
                    print("Rolling die for monster...")
                    time.sleep(1.5)
                    monsterrolltoblock = random.randint(1,20)
                    print("The monster got a "+str(monsterrolltoblock)+".")
                    time.sleep(1.5)
                    print("With the monster's modifier of +"+str(normal_enemy['speed']//3)+" means that the monster got a "+str(monsterrolltoblock+normal_enemy['speed']//3))
                    time.sleep(1.5)
                    if (plyrrolltorunaway+plyrstats['speed']//3) < (monsterrolltoblock+normal_enemy['speed']//3):
                        print("The monster got away!")
                        return "exitcombat"
                    else:
                        print("You successfully blocked the monster!")
                        return "playernotdead"
                elif plyrwantstoblock.lower() == "n":
                    print("The monster gets away.")
                    return "exitcombat"
                else:
                    print("While you were considering your grammar usage, the monster got away.")
                    return "exitcombat"
            else:
                pass
        else:
            print("The monster is attacking!")
            time.sleep(1.5)
            print("Rolling die for attack...")
            time.sleep(1.5)
            attack = random.randint(1,20)
            print("The monster got a " + str(attack) + ".")
            time.sleep(1.5)
            overall_attack = str((normal_enemy['strength']//3)+attack)
            print("With their +"+ str(normal_enemy['strength']//3) +" modifier means that the monster ends with a "+overall_attack+".")
            time.sleep(1.5)
            print(random.choice(listofanamotopoeia))
            time.sleep(1.5)
            print("The monster hits you for "+overall_attack+".")
            plyrstats['hp'] -= int(overall_attack)
            time.sleep(1.5)
            print("Your hp is now "+str(plyrstats['hp']) +".")
            time.sleep(1.5)
            if plyrstats['hp'] <= 0:
                print("Sadly, you have died.")
                return 'playerdead'
            else:
                print("Your turn!")
                return 'playernotdead'
def loot():
    normal_enemy['hp'] = 30
    if current_room == "room1":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room1['common_chest_prob']
        roomlootprobrare = room1['rare_chest_prob']
        roomlootproblegendary = room1['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room2":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room2['common_chest_prob']
        roomlootprobrare = room2['rare_chest_prob']
        roomlootproblegendary = room2['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room3":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room3['common_chest_prob']
        roomlootprobrare = room3['rare_chest_prob']
        roomlootproblegendary = room3['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room4":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room4['common_chest_prob']
        roomlootprobrare = room4['rare_chest_prob']
        roomlootproblegendary = room4['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room5":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room5['common_chest_prob']
        roomlootprobrare = room5['rare_chest_prob']
        roomlootproblegendary = room5['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room6":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room6['common_chest_prob']
        roomlootprobrare = room6['rare_chest_prob']
        roomlootproblegendary = room6['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room7":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room7['common_chest_prob']
        roomlootprobrare = room7['rare_chest_prob']
        roomlootproblegendary = room7['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room8":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room8['common_chest_prob']
        roomlootprobrare = room8['rare_chest_prob']
        roomlootproblegendary = room8['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    elif current_room == "room9":
        chestrarity = random.randint(1,100)
        roomlootprobcommon = room9['common_chest_prob']
        roomlootprobrare = room9['rare_chest_prob']
        roomlootproblegendary = room9['legendary_chest_prob']
        if chestrarity <= roomlootprobcommon:
            chest = 'common'
        elif roomlootprobcommon < chestrarity <= roomlootprobrare:
            chest = 'rare'
        elif roomlootprobrare < chestrarity <= roomlootproblegendary:
            chest = 'legendary'
    if chest == "common":
        print("The chest in the room is a common chest!")
        time.sleep(1.5)
        commonloottype = random.randint(1,2)
        if commonloottype == 1:
            commonchestitem = random.choice(common_chest['potioninventory'])
            plyrstats['potioninventory'].append(commonchestitem)
        elif commonloottype == 2:
            commonchestitem = random.choice(common_chest['weaponinventory'])
            plyrstats['weaponinventory'].append(commonchestitem)
        print("You got a "+commonchestitem+"!")
    elif chest == "rare":
        print("The chest in the room is a rare chest!")
        time.sleep(1.5)
        rareloottype = random.randint(1,3)
        if rareloottype == 1:
            rarechestitem = random.choice(rare_chest['potioninventory'])
            plyrstats['potioninventory'].append(rarechestitem)
        elif rareloottype == 2:
            rarechestitem = random.choice(rare_chest['spellinventory'])
            plyrstats['spellinventory'].append(rarechestitem)
        elif rareloottype == 3:
            rarechestitem = random.choice(rare_chest['weaponinventory'])
            plyrstats['weaponinventory'].append(rarechestitem)
        print("You got a "+rarechestitem+"!")
    elif chest == "legendary":
        print("The chest in the room is a legendary chest!")
        time.sleep(1.5)
        legendaryloottype = random.randint(1,3)
        if legendaryloottype == 1:
            legendarychestitem = random.choice(legendary_chest['potioninventory'])
            plyrstats['potioninventory'].append(legendarychestitem)
        elif legendaryloottype == 2:
            legendarychestitem = random.choice(legendary_chest['spellinventory'])
            plyrstats['spellinventory'].append(legendarychestitem)
        elif legendaryloottype == 3:
            legendarychestitem = random.choice(legendary_chest['weaponinventory'])
            plyrstats['weaponinventory'].append(legendarychestitem)
        print("You got a "+legendarychestitem+"!")
def combat():
    print("Rolling dice for who goes first in combat...")
    time.sleep(1.5)
    global current_room
    if current_room == "room9":
        finalbossincombat = True
    else:
        finalbossincombat = False
    if finalbossincombat:
        plyrrollforcombat = random.randint(1,20)
        overallrollplyr = plyrrollforcombat + plyrstats['speed']//3
        print("You rolled a "+str(plyrrollforcombat)+".")
        time.sleep(1.5)
        print("With your +"+str(plyrstats['speed']//3)+" modifier it means that you got a "+str(overallrollplyr)+".")
        time.sleep(1.5)
        final_bossrollforcombat = random.randint(1,20)
        overallrollenemy = final_bossrollforcombat + final_boss['speed']//3
        print("The final boss rolled a "+str(final_bossrollforcombat)+".")
        time.sleep(1.5)
        print("With their +"+str(final_boss['speed']//3)+" modifier it means that they got a "+str(overallrollenemy)+".")
        time.sleep(1.5)
        if overallrollenemy > overallrollplyr:
            enemygoesfirst = True
            plyrgoesfirst = False
        elif overallrollenemy < overallrollplyr:
            enemygoesfirst = False
            plyrgoesfirst = True
        else:
            enemygoesfirst = True
            plyrgoesfirst = False

    else:
        plyrrollforcombat = random.randint(1,20)
        overallrollplyr = plyrrollforcombat + plyrstats['speed']//3
        print("You rolled a "+str(plyrrollforcombat)+".")
        time.sleep(1.5)
        print("With your +"+str(plyrstats['speed']//3)+" means that you got a "+str(overallrollplyr)+".")
        time.sleep(1.5)
        enemyrollforcombat = random.randint(1,20)
        overallrollenemy = enemyrollforcombat + normal_enemy['speed']//3
        print("The monster rolled a "+str(enemyrollforcombat)+".")
        time.sleep(1.5)
        print("With their +"+str(normal_enemy['speed']//3)+" means that they got a "+str(overallrollenemy)+".")
        time.sleep(1.5)
        if overallrollenemy > overallrollplyr:
            enemygoesfirst = True
            plyrgoesfirst = False
        elif overallrollenemy > overallrollplyr:
            enemygoesfirst = False
            plyrgoesfirst = True
        else:
            enemygoesfirst = True
            plyrgoesfirst = False
    if enemygoesfirst:
        while True:
            resultsofmonsterturn = monsterturn()
            if resultsofmonsterturn == 'playerdead':
                return 'playerdead'
            elif resultsofmonsterturn == 'exitcombat':
                return 'exitcombat'
            elif resultsofmonsterturn == 'playernotdead':
                resultsofplyrturn = plyrturn()
                if resultsofplyrturn == 'enemydead':
                    loot()
                    return 'exitcombat'
                elif resultsofplyrturn == 'enemynotdead':
                    continue
                elif resultsofplyrturn == 'exitcombat':
                    return 'exitcombat'
    elif plyrgoesfirst:
        while True:
            resultsofplyrturn = plyrturn()
            if resultsofplyrturn == 'enemynotdead':
                continue
            elif resultsofplyrturn == 'exitcombat':
                return 'exitcombat'
            elif resultsofplyrturn == 'theywon':
                return 'theywon'
            elif resultsofplyrturn == 'playernotdead':
                resultsofmonsterturn = monsterturn()
                if resultsofmonsterturn == 'enemydead':
                    loot()
                    return 'exitcombat'
                elif resultsofmonsterturn == 'playerdead':
                    return 'playerdead'
                elif resultsofmonsterturn == 'exitcombat':
                    return 'exitcombat'
def room_details():
    global current_room
    if current_room == "room1":
        if room1['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room1['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room1['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room2":
        if room2['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room2['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room2['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room3":
        if room3['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room3['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room3['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room4":
        if room4['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room4['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room4['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room5":
        if room5['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room5['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room5['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room6":
        if room6['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room6['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room6['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room7":
        if room7['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room7['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room7['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room8":
        if room8['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room8['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room8['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
    elif current_room == "room9":
        if room9['monster_probability'] > random.randint(1,100):
            print("There is a monster in this room!")
            time.sleep(1.5)
            is_monster = True
            if room9['final_boss'] == True:
                print("You are facing the final boss!")
                time.sleep(1.5)
            else:
                print("You are facing a normal monster!")
                time.sleep(1.5)
        else:
            print("There is not a monster in this room.")
            time.sleep(1.5)
            is_monster = False
        print("You can access these rooms:")
        time.sleep(1.5)
        for i in room9['room_accesses']:
            print(str(i)+",", end="")
        return is_monster
def main():
    global current_room
    while True:
        if room_details() == True:
            print("\n")
            print("Since there is a monster, you enter combat.")
            if combat() == 'exitcombat':
                pass
            elif combat() == 'playerdead':
                return 'playerdead'
            elif combat() == 'theywon':
                return 'plyrwon'
        else:
            pass
        while True:
            print("\n")
            roomtomoveto = input("What room do you want to move to?(Use only the number of the room)")
            if current_room == "room1":
                if int(roomtomoveto) in room1['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room2":
                if int(roomtomoveto) in room2['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room3":
                if int(roomtomoveto) in room3['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room4":
                if int(roomtomoveto) in room4['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room5":
                if int(roomtomoveto) in room5['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room6":
                if int(roomtomoveto) in room6['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room7":
                if int(roomtomoveto) in room7['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room8":
                if int(roomtomoveto) in room8['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
            elif current_room == "room9":
                if int(roomtomoveto) in room9['room_accesses']:
                    current_room = "room"+roomtomoveto
                    break
                else:
                    print("Not a valid room!")
        print("You move to room"+roomtomoveto)
def play():
    print("Welcome to the dungeon! fight monsters, go through rooms, and face the final boss to win the game.")
    time.sleep(3)
    while True:
        if main() == 'playerdead':
            print("You have lost!")
            if play_again() == False:
                break
            else:
                main()
        elif main() == 'plyrwon':
            print("You won!")
            if play_again() == False:
                break
            else:
                plyrstats['hp'] = 50
                current_room = "room1"
                main()
play()

    
        









