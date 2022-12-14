import os
from Colors import cl



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- STATS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# EDIT STATS #############################################################################
def StatMenu(playerStats, playerStatPoints, playerName, itemsDict):
     # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP    
    itemAddStats = []
    itemAddStats, itemPlayerPrimary, itemPlayerSecondary = AdditionalStats(itemAddStats, itemsDict) 
    while True:
        
        
        nextLevelExp = round(((playerStats[0]**1.25)*200),2)
        print(f"\n{playerName}\tLVL {playerStats[0]}"\
        "\n------------------------------------------------------------------------")    
        print(f"Points: {cl.YELLOW}{playerStatPoints}{cl.RESET}\t\t\tEXP: {cl.YELLOW}{round(playerStats[5],2)}/{round(nextLevelExp,2)}{cl.RESET}\n\n"\
            f"HP: {round(playerStats[2],2)}/{round(playerStats[1],2)}\n"\
            f"ATK: {playerStats[3]} (+{itemAddStats[3]})\n"\
            f"DEF: {playerStats[4]} (+{itemAddStats[4]})"\
            "\n------------------------------------------------------------------------")
        if playerStatPoints == 0:
            userInput = input("\n(0) Return\n")
            if userInput == "0":
                break
            else:
                print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}")
        else:
            userInput = input("\n(1) HP +10\t (2) Atk + 1\t (3) Def + 1\t (0) Return\n")
            os.system('cls')
            if userInput == "1":
                playerStats[1] += 10
                playerStatPoints -= 1
                playerStats[2] = playerStats[1]
            elif userInput == "2":
                playerStats[3] += 1
                playerStatPoints -= 1
            elif userInput == "3":
                playerStats[4] += 1
                playerStatPoints -= 1
            elif userInput == "0":
                break
            else:
                print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}")       
           

    return playerStats, playerStatPoints




#############################################################################################################################################################################
#---------------------------------------------------------------------------------- LEVEL UP -------------------------------------------------------------------------------#
#############################################################################################################################################################################


################################################################################### LEVEL UP ################################################################################
def LevelUp(playerStats, playerStatPoints, playerName, itemsDict):
    # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    nextLevelExp = round(((playerStats[0]**1.25)*200),2)
    if playerStats[5] >= nextLevelExp:
        playerStats[5] -= nextLevelExp
        playerStats[0] += 1
        if playerStats[0] % 5 == 0:
            playerStatPoints += 4
        else:
            playerStatPoints += 2
        print(f"\n{cl.GREEN}Yay, {playerName} got a new Level!{cl.RESET}")

    #### Activate Items ####    
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
    itemKeyList = [key for key in itemsDict]   
    _tempListMidLvl = [2, 5, 8, 11, 14, 17]
    _tempListHighLvl = [3, 6, 9, 12, 15, 18]

    if playerStats[0] == 10:
        for i in itemKeyList:
            if itemsDict[i][9] in _tempListMidLvl:     
                itemsDict[i][10] = itemsDict[i][9]
    if playerStats[0] == 20:
        for i in itemKeyList:
            if itemsDict[i][9] in _tempListHighLvl:
                itemsDict[i][10] = itemsDict[i][9]    
        
    return playerStats, playerStatPoints, itemsDict

################################################################################# ADD ITEM STATS #############################################################################
def AdditionalStats(itemAddStats, itemsDict):   
   # itemAddStats = 0 None,1 None, 2 None, 3 +ATK, 4 +DEF, 5 None 
   # Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq   
    itemAddStats = [0, 0, 0, 0.0, 0.0, 0]
    itemKeyList = [key for key in itemsDict]
    itemPlayerPrimary = "Fists" 
    itemPlayerSecondary = "Your Face"                                         
    for i in itemKeyList:
        if itemsDict[i][11] >= 10:                                                  
            itemAddStats[3] += itemsDict[i][3]
            itemAddStats[4] += itemsDict[i][4]

        if itemsDict[i][11] == 11:
            itemPlayerPrimary = itemsDict[i][2]        
        if itemsDict[i][11] == 12:
            itemPlayerSecondary = itemsDict[i][2]
      

    return itemAddStats, itemPlayerPrimary, itemPlayerSecondary