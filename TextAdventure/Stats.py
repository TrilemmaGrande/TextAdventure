def StatMenu(playerStats, playerStatPoints, playerName):
    # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    while True:
        nextLevelExp = playerStats[0] * round((100*(playerStats[0]**1.5)),2)
        print(f"\n{playerName}\tLVL {playerStats[0]}\nPoints: {playerStatPoints}\t\t\tEXP: {round(playerStats[5],2)}/{round(nextLevelExp,2)}\n\nHP: {playerStats[2]}/{playerStats[1]}\nATK: {playerStats[3]}\nDEF: {playerStats[4]}")
        if playerStatPoints == 0:  
            userInput = input("\n(1) Return\n")
            if userInput == "1":
                break
            else: print("\nCouldn't understand you?!")
        else: 
            userInput = input(f"\n(1) Edit Stats ({playerStatPoints}P)\t(2) Return\n")
            if userInput == "1":
                playerStats, playerStatPoints = EditStats(playerStats, playerStatPoints, playerName)
            elif userInput == "2":
                break
            else: print("\nCouldn't understand you?!")
    return playerStats, playerStatPoints

def EditStats(playerStats, playerStatPoints, playerName):
     # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    while True:
        if playerStatPoints == 0:
            break
        nextLevelExp = playerStats[0] * round((100*(playerStats[0]**1.5)),2)
        print(f"\n{playerName}\tLVL {playerStats[0]}\nPoints: {playerStatPoints}\t\t\tEXP: {round(playerStats[5],2)}/{round(nextLevelExp,2)}\n\nHP: {playerStats[2]}/{playerStats[1]}\nATK: {playerStats[3]}\nDEF: {playerStats[4]}")
        userInput = input("\n(1) HP +10\t (2) Atk + 1\t (3) Def + 1\t (4) Return\n")
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
        elif userInput == "4":
            break
        else:
            print("\nCouldn't understand you?!")        
           

    return playerStats, playerStatPoints

def LevelUp(playerStats, playerStatPoints, playerName, itemsDict):
    # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    nextLevelExp = playerStats[0] * round((100*(playerStats[0]**1.5)),2)
    if playerStats[5] >= nextLevelExp:
        playerStats[5] -= nextLevelExp
        playerStats[0] += 1
        if playerStats[0] % 5 == 0:
            playerStatPoints += 4
        else:
            playerStatPoints += 2
        print(f"\nYay, {playerName} got a new Level!")

    #### Activate Items ####    
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
    itemKeyList = [key for key in itemsDict]   
    _tempListMidLvl = [2, 5, 8]
    _tempListHighLvl = [3, 6, 9]

    if playerStats[0] == 10:
        for i in itemKeyList:
            if itemsDict[i][9] in _tempListMidLvl:     
                itemsDict[i][10] = itemsDict[i][9]
    if playerStats[0] == 20:
        for i in itemKeyList:
            if itemsDict[i][9] in _tempListHighLvl:
                itemsDict[i][10] = itemsDict[i][9]    
        
    return playerStats, playerStatPoints, itemsDict