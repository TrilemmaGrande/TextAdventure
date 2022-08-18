import random
from Colors import cl
from time import sleep
import Stats
import Inventory
import Enemys
import os




#############################################################################################################################################################################
#-------------------------------------------------------------------------------- ENCOUNTER --------------------------------------------------------------------------------#
#############################################################################################################################################################################


######################################################################### ENCOUNTER (luck + location) #######################################################################
def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    locationIndex = 0
    enemyID = 0
    _locations = [startLocation, "the town", "the forest", "the flatlands", "the mountains", "the castle", "the islands"]
    _locationIndexList = [1,          100,            1,             1,               1,              1,          1]
    enemyLevel = random.randint(playerStats[0]-1, playerStats[0]+2)
    if enemyLevel <= 0:
        enemyLevel = 1
    
    enemyDictEasy = {}
    enemyDictMedium = {}
    enemyDictHard = {}
    enemyDictEasy, enemyDictMedium, enemyDictHard = Enemys.Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard, enemyLevel)

    
    for i in range(0,len(_locations)):
        if location == _locations[i]:
            locationIndex = _locationIndexList[i]
            if locationIndex == 100:
                itemsDict, playerInventoryMoney, playerStats = Inventory.ShopMenu(itemsDict, playerName, playerInventoryMoney, playerStats)
                return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict 
            
                

    luck = random.randint(1,100)                                                    
    if luck >= 98:                                                          
        itemsDict, playerInventoryMoney, playerStats = Inventory.WandererMenu(itemsDict, playerName, playerInventoryMoney, playerStats)
    encounterIndex = round(luck - (luck * (playerStats[0]) * 0.01) - locationIndex)             # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID, selectedDict, selectedDictID = EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard)
    
                         
    
    if enemyID != 0:
                
        enemyMaxHP = (selectedDict[enemyID][2])  
        (selectedDict[enemyID][6]())                                                            # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:           

            UserInputChoose = input(""\
            f"\n{playerName}\t\tLVL {cl.BLUE}{playerStats[0]}{cl.RESET}\tHP {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}\n"\
            f"----------- VS -----------\n"\
            f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET}\t\tLVL {cl.BLUE}{selectedDict[enemyID][1]}{cl.RESET}\tHP {cl.BLUE}{selectedDict[enemyID][2]}/{enemyMaxHP}{cl.RESET}\n\n"\
            f"What do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(0) Flee\n")
            os.system('cls')

            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, location = Fight(
                    playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID)
                break
            
            elif UserInputChoose == "2":
                itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)  

            elif UserInputChoose == "3": 
                playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict )

            elif UserInputChoose == "0": 
                _temp = (playerStats[0] * 2)
                playerInventoryMoney -= (playerStats[0] * 2)
                if playerInventoryMoney - (playerStats[0] * 2) < 0:
                    playerInventoryMoney = 0
                print(f"""\nYou managed to escape the fight, you used up {cl.RED}{round(_temp,2)}{cl.RESET} gold to distract your enemy.
                \nYou have {cl.GREEN}{round(playerStats[2],2)}{cl.RESET} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict

############################################################################# SELECT ENEMY #############################################################################
def EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard):       
    enemyID = 0                                                                                        #Edit this function later to config chances for Encounter
    selectedDict = {}
    _tempList = []
    selectedDictID = 0
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    if encounterIndex <= 10:
        EncounterNothing()

    elif encounterIndex > 11 and encounterIndex <= 20:
        _luck = random.randint(0,len(enemyDictHard)-1)
        for i in enemyDictHard:
            _tempList.append(i)
        enemyID = _tempList[_luck]
        selectedDict = enemyDictHard
        selectedDictID = 3        
    elif encounterIndex > 21 and encounterIndex <= 52:
        _luck = random.randint(0,len(enemyDictMedium)-1)
        for i in enemyDictMedium:
            _tempList.append(i)
        enemyID = _tempList[_luck]
        selectedDict = enemyDictMedium
        selectedDictID = 2
    elif encounterIndex > 53 and encounterIndex <= 100:
        _luck = random.randint(0,len(enemyDictEasy)-1)
        for i in enemyDictEasy:
            _tempList.append(i)
        enemyID = _tempList[_luck]       
        selectedDict = enemyDictEasy
        selectedDictID = 1
    
    if selectedDictID == 3 and playerStats[0] < 20:
        EncounterLowLevel()        
        enemyID = 0
    elif selectedDictID == 2 and playerStats[0] < 10:
        EncounterLowLevel()        
        enemyID = 0

    return enemyID, selectedDict, selectedDictID


############################################################################# ENEMY ITEMS #############################################################################
def EnemyItemSelection(itemsDict, enemyID, selectedDictID):
#Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
#Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic 
    _tempItemList = []
    _tempItemListEasy = []
    _tempItemListMedium = []
    _tempItemListHard = []
    _tempItemListRandom = []
    _itemEnemyItems = []
    itemEnemyItems = []
    itemEnemyAddStats = [0, 0, 0, 0, 0, 0, 0]
    lootItemID = 1
    itemKeyList = [key for key in itemsDict]                                          
    for i in itemKeyList:
        if  itemsDict[i][10] == 7:
            _tempItemListEasy.append(i)
        elif itemsDict[i][10] == 8:
            _tempItemListMedium.append(i)
        elif itemsDict[i][10] == 9:
            _tempItemListHard.append(i)
                                                                             # Choose witch Items (Easy, Medium, Hard)
    if selectedDictID == 1:
        _tempItemList = _tempItemListEasy
    elif selectedDictID == 2:
        _tempItemList = _tempItemListMedium
    elif selectedDictID == 3:
        _tempItemList = _tempItemListHard
    
    j = random.randint(0,len(_tempItemList)-1)
                                                                       # give Random Item from List as Lootitem
    lootItemID = _tempItemList[j]

    for y in range(1,7):                                                                                    
        
        for k in itemsDict:
           
            if itemsDict[k][10] > 0:                                                      # from all choosen Items, append one of every type to enemyItems
                if itemsDict[k][11] == y or itemsDict[k][11] == (y + 10):
                    _tempItemListRandom.append(k)
        if bool(_tempItemListRandom) == True:
            o = random.randint(0,len(_tempItemListRandom)-1)                
            _itemEnemyItems.append(_tempItemListRandom[o])
            _tempItemListRandom = []

    enemyWithoutEquipment = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008] ### chould be changed later after testing

    if enemyID not in enemyWithoutEquipment:
        for s in _itemEnemyItems:                                                   # Values for adding Stats to enemy    
            itemEnemyAddStats[3] += itemsDict[s][3]
            itemEnemyAddStats[4] += itemsDict[s][4]      
                                                                                         # Names of enemy Items
        for t in _itemEnemyItems:
            itemEnemyItems.append(itemsDict[t][2])  

    else: 
        itemEnemyItems = ["Claws", "Body"]
            

    
    return itemEnemyItems, itemEnemyAddStats, lootItemID  



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- FIGHT ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



################################################################################### FIGHT ###################################################################################
def Fight(playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID):
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic   
    _tempMoney = 0.00
    _tempExp = 0.00
    itemAddStats = []
    itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict)
    itemEnemyItems, itemEnemyAddStats, lootItemID  = EnemyItemSelection(itemsDict, enemyID, selectedDictID) 
   
    while True:

        if playerStats[2] <= 0:                                                            	    # if player dead
            sleep(2)
            PicDeath()
            sleep(4)
            PicFairie()
            playerInventoryMoney -= round(playerInventoryMoney * 0.1,2)
            playerStats[5] *= 0.25
            location = "the town"
            playerStats[2] = 1
            break

        elif selectedDict[enemyID][2] <= 0:                                                         # if enemy dead
            print(f"\n--- {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} has been eleminated ---")
            # sleep(2)
            _tempMoney += (round((selectedDict[enemyID][3] + selectedDict[enemyID][2] + selectedDict[enemyID][5]) / 2,2))
            _tempExp += (round(selectedDict[enemyID][5] * 100,2))
            print(f"\nYou received {cl.YELLOW}{itemsDict[lootItemID][2]}{cl.RESET}, {cl.YELLOW}{round(_tempMoney,2)}{cl.RESET} Gold and {cl.YELLOW}{round(_tempExp,2)}{cl.RESET} Experience.")
            playerInventoryMoney += _tempMoney
            playerStats[5] += _tempExp
            itemsDict[lootItemID][8] += 1            
            break
  
        #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
        #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic
        (selectedDict[enemyID][6]())
        UserInputFight = input(""\
        f"\n{cl.BLUE}{playerName}{cl.RESET}\t\tLVL {cl.BLUE}{playerStats[0]}{cl.RESET}\tHP {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}\n"\
        f"----------- VS -----------\n"\
        f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET}\t\tLVL {cl.BLUE}{selectedDict[enemyID][1]}{cl.RESET}\tHP {cl.BLUE}{selectedDict[enemyID][2]}/{enemyMaxHP}{cl.RESET}\nItems: {itemEnemyItems}\n\n"\
        f"(1) Attack\t(2) Inventory\t(3) Stats\t (0) Flee\n")                                             # Fight (P = Player, E = Enemy)
        os.system('cls')

    ################# 1 Attack ###############
        
        if UserInputFight == "1":
            (selectedDict[enemyID][6]())
            blockMessage = ""
            critMessage = ""           
            
            blockChance = (random.randint(75,100))/100
            if blockChance >= 90:
                blockMessage = "(crit)"
            critChance = random.randint(0,100)
            if critChance >= 95:
                critDmg = 1.5
                critMessage = "(crit)"
            else:
                critDmg = 1 
                                                                                          # Player attacks first
            print(f"\nYou attack {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} with {cl.YELLOW}{itemPlayerPrimary}{cl.RESET} and did {cl.BLUE}{round((playerStats[3] + itemAddStats[3]) * critDmg,2)} {cl.YELLOW}{critMessage}{cl.RESET} damage.")
            sleep(0.5)
            print(f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET} defends himself with {cl.YELLOW}{itemEnemyItems[1]}{cl.RESET} and blocks {cl.BLUE}{round((selectedDict[enemyID][4] + itemEnemyAddStats[4]) * blockChance,2)}{cl.RESET} {cl.YELLOW}{blockMessage}{cl.RESET} damage.")
            sleep(0.5)
            if  (round((selectedDict[enemyID][4] + itemEnemyAddStats[4]) * blockChance)) < (round((playerStats[3] + itemAddStats[3]) * critDmg,2)):                               # P_DEF < E_ATK?
                selectedDict[enemyID][2] += (round((selectedDict[enemyID][4]  + itemEnemyAddStats[4]) * blockChance,2) - (round((playerStats[3] + itemAddStats[3]) * critDmg,2))) # E_HP += E_DEF - P_ATK
            else:
                print("Attack blocked")
            if selectedDict[enemyID][2] < 0:                                                                                                                  # HP < 0? Then HP 0
                selectedDict[enemyID][2] = 0
            print(f"{selectedDict[enemyID][0]} has {selectedDict[enemyID][2]} HP left.")
            sleep(1)

            if selectedDict[enemyID][2] > 0:                                                                 # Enemy alive?

                blockChance = (random.randint(75,100))/100
                if blockChance >= 90:
                    blockMessage = "(crit)"
                critChance = random.randint(0,100)
                if critChance >= 95:
                    critDmg = 1.5
                    critMessage = "(crit)"
                else:
                    critDmg = 1 

                print(f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET} attacks you with {cl.YELLOW}{itemEnemyItems[0]}{cl.RESET} and did {cl.RED}{round((selectedDict[enemyID][3] + itemEnemyAddStats[3])  * critDmg),2}{cl.RESET} {cl.YELLOW}{critMessage}{cl.RESET} damage.")  # Enemy attacks second
                sleep(0.5)
                print(f"You defend yourself with {cl.YELLOW}{itemPlayerSecondary}{cl.RESET} and block {cl.BLUE}{(round((playerStats[4] + itemAddStats[4]) * blockChance,2))}{cl.RESET} {cl.YELLOW}{blockMessage}{cl.RESET} damage.")
                sleep(0.5)
                if (round((playerStats[4] + itemAddStats[4]) * blockChance,2)) < (round((selectedDict[enemyID][3] + itemEnemyAddStats[3])  * critDmg),2):                       # E_DEF < P_ATK?
                    playerStats[2] += ((round((playerStats[4] + itemAddStats[4]) * blockChance,2)) - (round((selectedDict[enemyID][3] + itemEnemyAddStats[3]) * critDmg,2)))  # P_HP += P_DEF - E_ATK 
                else:   
                    print("Attack blocked")
                if playerStats[2] < 0:
                    playerStats[2] = 0                                                                                                                  # HP < 0? Then HP 0
                print(f"You have {cl.GREEN}{playerStats[2]}{cl.RESET} HP left.")
                sleep(1)

    ################ 2 Inventory ##############      
                  
        elif UserInputFight == "2":
               itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)

    ################ 3 Stats #################

        elif UserInputFight == "3":
            playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict)

    ################ 4 Flee ################

    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic

        elif UserInputFight == "0":                                                                         # Flee (loose Gold + Enemy
            _temp1 = (playerStats[0] * 2)                                                                   #        hits with 0.5 atk)
            playerInventoryMoney -= (playerStats[0] * 2)
            if playerInventoryMoney - (playerStats[0] * 2) <= 0:
                playerInventoryMoney = 0
            _temp2 = (round((selectedDict[enemyID][3] + itemEnemyAddStats[3]) / 2,2))
            playerStats[2] -= round(_temp2,2)
            if playerStats[2] < 0:
                    playerStats[2] = 0 
            print(f"You managed to flee while you distracted the enemy with {cl.RED}{round(_temp1,2)}{cl.RESET} gold,")
            print(f"but {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} got a hit on you. You received {cl.RED}{round(_temp2,2)}{cl.RESET} dmg!")
            print(f"You have {cl.GREEN}{playerStats[2]}{cl.RESET} HP left.")
            if playerStats[2] <= 0:                                                                        # if player dead (from 1 atk)
                sleep(2)
                PicDeath()
                sleep(4)
                PicFairie()
                playerInventoryMoney -= round(playerInventoryMoney * 0.1,2)
                playerStats[5] *= 0.25
                location = "the town"
                playerStats[2] = 1
                break
            break
        else: 
            print("\nYou can't choose that?!")

    return playerInventoryMoney, playerStats, playerStatPoints, location

################################################################################ NO ENCOUNTER ###############################################################################
def EncounterLowLevel():
    print("'A dangerous sphere approaches you, but as you turn around, it disappears.\nMaybe you escaped your downfall this time.'")

def EncounterNothing():
    print("Phew, nothing happened here.")



#############################################################################################################################################################################
#----------------------------------------------------------------------------------- PICS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################


######################################## Death ##################################################

def PicDeath():
    print("""
           
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................

          ---You have been defeated---

         """)


def PicFairie():
    print("\nYour head feels dizzy.")
    sleep(2) 
    print("A beautiful (fully naked) fairie helps you back to the town.")
    sleep(4)
    print("""
      .--.   _,
  .--;    \ /(_
 /    '.   |   '-._    . ' .
|       \  \    ,-.)  -= * =-
 \ /\_   '. \((` .(    '/. '
  )\ /     \ )\  _/   _/
 /  \\\    .-'   '--. /_\\
|    \\\_.' ,        \/||
\     \_.-';,_) _)'\ \||
 '.       /`\   (   '._/
   `\   .;  |  . '.
     ).'  )/|      \\
     `    ` |  \|   |
             \  |   |
              '.|   |
                 \  '\__
                  `-._  '. _
                     \`;-.` `._
                      \ \ `'-._\\
                       \ |
                        \ )
                         \_\\    
    """)

    print("She thankfully took some of your gold in advance.")
    sleep(2)



