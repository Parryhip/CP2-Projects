#Samuel Andelin, Battle Simulator



#moster ded function
def monsterloser(enemy, placeholder):
    if placeholder <= 0 or placeholder == 0:
        print("You killed the monster!")
        return True
    else:
        return False
  

#lose function
def loser(plyr):
    if plyr["hp"] <= 0:
        print("Sadly, it seems as though your journey ends here, because the mosnters have killed you.")
        return True
    else:
        return False
    
#lose function
def loser(plyr):
    if plyr["hp"] <= 0:
        print("Sadly, it seems as though your journey ends here, because the mosnters have killed you.")
        return True
    else:
        return False
