


#############################################################################################################################################################################
#---------------------------------------------------------------------------------- ITEMS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################

# 1, 2, 3 = Merchant Inv lvl 5, 10, 20+ 
# 4, 5, 6 = Wizard Inv lvl 5, 10, 20+ 
# 7, 8, 9 = Loot Inv lvl 5, 10, 20+ 
# 10,11,12 = Wanderer
# 13,14,15 = Wanderer (with Gems)
# 16,17,18 = Dungeon Loot (not implemented yet)

#For Index 11: Use = 0, Weapon = 1, Secondary = 2, Head = 3, Breast = 4, Feet = 5, Hands = 6, Jewellery = 7 -- if equipped: +10
#              Value Item = 8, Special = 9 

#ItemKeys: 1234 
#          1 = lvl range (0-10, 10-20, 20+)  
#          2 = use/eq (see index 11) 
#          3 + 4 = Numerate

# 
# IF lvl "x" Then itemsDict(10) = itemsDict(9)


def Items(itemsDict):

    itemsDict = {
    
    ########################################## USABLE ITEMS (HP) ##########################################    
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq/Special                           
    #                                                                Max       P                                                     
    1001:[(0),(0),"Apple",          (0),   (0),    (2),  (0.1),    (20),     (2),    (1),    (1),    (0)],
    2001:[(0),(0),"Bottle of Rum",  (0),   (0),    (7),  (0.3),     (5),     (0),    (2),    (0),    (0)],                               
    1002:[(0),(0),"Bandage",        (0),   (0),    (5),  (0.5),     (5),     (2),    (4),    (4),    (0)],                          
    1003:[(0),(0),"10 HP Potion",   (0),   (0),   (10),  (1.5),    (10),     (0),    (4),    (4),    (0)],                       
    2004:[(0),(0),"20 HP Potion",   (0),   (0),   (20),  (2.0),    (10),     (0),    (5),    (0),    (0)],                       
    3005:[(0),(0),"30 HP Potion",   (0),   (0),   (30),  (4.0),    (10),     (0),    (6),    (0),    (0)],                       
    1006:[(0),(0),"Lettuce",        (0),   (0),    (2),  (0.1),    (10),     (0),    (7),    (7),    (0)],                                
    2007:[(0),(0),"Blueberries",    (0),   (0),    (6),  (0.4),    (10),     (0),    (8),    (0),    (0)],
    1008:[(0),(0),"Cabbage",        (0),   (0),    (4),  (0.2),    (10),     (0),    (7),    (7),    (0)],                           
    1009:[(0),(0),"Fish",           (0),   (0),    (5),  (0.3),    (20),     (0),    (7),    (7),    (0)],                          
    2010:[(0),(0),"Chicken",        (0),   (0),    (8),  (0.6),     (5),     (0),    (8),    (0),    (0)],                       
    
    ############################################# ARMOR (DEF) #############################################    
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                             
    1301:[(0),(0),"Leather Cap",    (0),   (8),    (0),   (10),     (5),     (0),    (1),    (1),    (3)],                        
    1402:[(0),(0),"Leather Chest",  (0),  (10),    (0),   (18),     (5),     (0),    (1),    (1),    (4)],                        
    1503:[(0),(0),"Leather Shoes",  (0),   (4),    (0),    (8),     (5),     (0),    (1),    (1),    (5)],                        
    1604:[(0),(0),"Leather Gloves", (0),   (4),    (0),    (8),     (5),     (0),    (1),    (1),    (6)],                        
    2305:[(0),(0),"Steel Helmet",   (0),  (10),    (0),   (14),     (5),     (0),    (2),    (0),    (3)],                        
    2406:[(0),(0),"Steel Plates",   (0),  (14),    (0),   (22),     (5),     (0),    (2),    (0),    (4)],                        
    2507:[(0),(0),"Steel Shoes",    (0),   (8),    (0),   (12),     (5),     (0),    (2),    (0),    (5)],                       
    2608:[(0),(0),"Steel Gloves",   (0),   (8),    (0),   (12),     (5),     (0),    (2),    (0),    (6)],                        
    3309:[(0),(0),"Platin Helmet",  (0),  (12),    (0),   (18),     (5),     (0),    (3),    (0),    (3)],                        
    3410:[(0),(0),"Platin Plates",  (0),  (16),    (0),   (26),     (5),     (0),    (3),    (0),    (4)],                        
    3512:[(0),(0),"Platin Shoes",   (0),  (10),    (0),   (14),     (5),     (0),    (3),    (0),    (5)],                       
    3611:[(0),(0),"Platin Gloves",  (0),  (10),    (0),   (14),     (5),     (0),    (3),    (0),    (6)],                        
    1313:[(0),(0),"Dirty Hat",      (0),   (2),    (0),    (1),     (3),     (0),    (7),    (7),    (3)],                       
    1414:[(0),(0),"Linen Robe",     (0),   (3),    (0),    (2),     (2),     (1),    (7),    (7),   (14)],
    1515:[(0),(0),"Dirty Pants",    (0),   (1),    (0),    (1),     (3),     (1),    (7),    (7),   (15)],                        
    1616:[(0),(0),"Muddy Gloves",   (0),   (1),    (0),    (1),     (3),     (1),    (7),    (7),   (16)],
    1317:[(0),(0),"Cap",            (0),   (3),    (0),    (2),     (3),     (0),    (7),    (7),    (3)],                       
    1418:[(0),(0),"Vest",           (0),   (4),    (0),    (3),     (2),     (0),    (7),    (7),    (4)],
    1519:[(0),(0),"Trousers",       (0),   (2),    (0),    (2),     (3),     (0),    (7),    (7),    (5)],                        
    1620:[(0),(0),"Gloves",         (0),   (2),    (0),    (2),     (3),     (0),    (7),    (7),    (6)],
    1375:[(0),(0),"Dragon Helmet",  (0),  (10),    (0),    (7),     (2),     (0),   (16),   (16),    (3)],                        
    1476:[(0),(0),"Dragon Plates",  (0),  (14),    (0),   (12),     (2),     (0),   (16),   (16),    (4)],                        
    1577:[(0),(0),"Dragon Shoes",   (0),   (8),    (0),    (5),     (2),     (0),   (16),   (16),    (5)],                       
    1678:[(0),(0),"Dragon Gloves",  (0),   (8),    (0),    (5),     (2),     (0),   (16),   (16),    (6)],
    3379:[(0),(0),"Kings Helmet",   (0),  (22),    (0),   (14),     (1),     (0),   (17),    (0),    (3)],
    3480:[(0),(0),"Kings Chest" ,   (0),  (26),    (0),   (20),     (1),     (0),   (17),    (0),    (4)],
    3581:[(0),(0),"Kings Shoes",    (0),  (18),    (0),   (16),     (1),     (0),   (17),    (0),    (5)],
    3682:[(0),(0),"Kings Gloves",   (0),  (20),    (0),   (18),     (1),     (0),   (17),    (0),    (6)],                       
    
    ############################################ SHIELD (DEF) ############################################    
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                            
    1201:[(0),(0),"Leather Shield", (0),   (6),    (0),   (10),     (5),     (0),    (1),    (1),    (2)],                         
    2202:[(0),(0),"Steel Shield",   (0),   (8),    (0),   (17),     (5),     (0),    (2),    (0),    (2)],
    3203:[(0),(0),"Platin Shield",  (0),  (12),    (0),   (18),     (5),     (0),    (3),    (0),    (2)],                        
    3204:[(0),(0),"Knights Shield", (0),  (20),    (0),   (22),     (5),     (0),    (3),    (0),    (2)],                        
    1205:[(0),(0),"Broken Shield",  (0),   (2),    (0),    (2),     (4),     (0),    (7),    (7),    (2)],
    1206:[(0),(0),"Barrel Lid",     (0),   (4),    (0),    (3),     (2),     (0),    (7),    (7),    (2)],
    2207:[(0),(0),"Wood Shield",    (0),   (8),    (0),   (14),     (5),     (0),    (8),    (0),    (2)],
    2208:[(0),(0),"Round Shield",   (0),  (10),    (0),   (16),     (5),     (0),    (8),    (0),    (2)],                            
    3209:[(0),(0),"Bullwark",       (0),  (25),    (0),   (25),     (1),     (0),    (9),    (0),    (2)],                         
    1202:[(0),(0),"Dragon Shield",  (0),  (10),    (0),    (0),     (1),     (0),   (13),   (13),    (2)],
    3210:[(0),(0),"Kings Shield",   (0),  (22),    (0),    (0),     (1),     (0),   (14),    (0),    (2)],

    ############################################ WEAPONS (ATK) ############################################    
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                                                 
    1101:[(0),(0),"Copper Sword", (10.5),  (0),    (0),   (15),     (5),     (0),    (1),    (1),    (1)], 
    2102:[(0),(0),"Steel Sword",  (16.2),  (0),    (0),   (22),     (5),     (0),    (2),    (0),    (1)], 
    3103:[(0),(0),"Knights Sword",(22.0),  (0),    (0),   (36),     (5),     (0),    (3),    (0),    (1)],                        
    1104:[(0),(0),"Big Fish",      (2.3),  (0),    (0),    (1),     (3),     (1),    (7),    (7),   (11)], 
    1105:[(0),(0),"Butcher Knife", (5.4),  (0),    (0),    (2),     (3),     (0),    (7),    (7),    (1)],                       
    1106:[(0),(0),"Falcata",       (6.3),  (0),    (0),    (4),     (1),     (0),    (7),    (7),    (1)],
    1107:[(0),(0),"Fork of Death", (4.4),  (0),    (0),    (1),     (2),     (0),    (7),    (7),    (1)],                                              
    2107:[(0),(0),"Bone Knife",   (10.6),  (0),    (0),   (10),     (1),     (0),    (8),    (0),    (1)], 
    2110:[(0),(0),"Spoon of Dawn", (9.4),  (0),    (0),    (8),     (1),     (0),    (8),    (0),    (1)],                                 
    2108:[(0),(0),"Dark Dagger",  (12.8),  (0),    (0),   (12),     (1),     (0),    (8),    (0),    (1)], 
    1110:[(0),(0),"Dragonslayer", (12.2),  (0),    (0),    (0),     (1),     (0),   (13),   (13),    (1)], 
    2109:[(0),(0),"Kings Sword",  (25.0),  (0),    (0),    (0),     (1),     (0),   (14),    (0),    (1)],
    
    ############################################# VALUE ITEMS #############################################    
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                            
    1801:[(0),(0),"Can of Oil",     (0),   (0),    (0),    (2),     (2),     (0),    (7),    (7),    (8)],
    1802:[(0),(0),"Bronze Nugget",  (0),   (0),    (0),    (4),     (2),     (0),    (7),    (7),    (8)],                         
    1803:[(0),(0),"Bronze Necklace",(0),   (0),    (0),    (8),     (2),     (0),    (8),    (0),    (8)],
    1804:[(0),(0),"Copper Ore",     (0),   (0),    (0),   (11),     (2),     (0),    (8),    (0),    (8)],                        
    2804:[(0),(0),"Golden Goblet",  (0),   (0),    (0),   (14),     (2),     (0),    (8),    (0),    (8)],                        
    2806:[(0),(0),"Silver Ore",     (0),   (0),    (0),   (20),     (2),     (0),    (9),    (0),    (8)],
    3807:[(0),(0),"Gold Nugget",    (0),   (0),    (0),   (25),     (1),     (0),    (9),    (0),    (8)],                            
    1805:[(0),(0),"Emerald",        (0),   (0),    (0),   (20),     (1),     (0),   (16),   (16),    (8)],
    2808:[(0),(0),"Ruby",           (0),   (0),    (0),   (30),     (1),     (0),   (17),    (0),    (8)],                        
    3809:[(0),(0),"Diamond",        (0),   (0),    (0),   (50),     (1),     (0),   (18),    (0),    (8)],

    ############################################### JEWELLERY ###############################################
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                            

    1710:[(0),(0),"Dragons Ring",   (0),   (4),   (10),    (0),     (1),     (0),   (13),    (0),    (7)],
    1711:[(0),(0),"Dragons Earring",(4),   (4),    (0),    (0),     (1),     (0),   (13),    (0),    (7)],
    1712:[(0),(0),"Dragons Brooch", (4),   (0),   (10),    (0),     (1),     (0),   (13),    (0),    (7)],
    1713:[(0),(0),"Dragons Chain",  (0),   (6),    (0),    (0),     (1),     (0),   (13),    (0),    (7)],
    1714:[(0),(0),"Dragons Tooth",  (6),   (0),    (0),    (0),     (1),     (0),   (13),    (0),    (7)],
    1714:[(0),(0),"Dragons Diadem", (0),   (0),   (20),    (0),     (1),     (0),   (13),    (0),    (7)],

    ############################################### SPECIAL ###############################################
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           
    #                                                                Max       P                                                 
    1901:[(0),(0),"Castle Key",     (0),   (0),    (0),   (20),     (1),     (0),   (10),   (10),    (9)],
    2902:[(0),(0),"Slumps Key",     (0),   (0),    (0),  (100),     (1),     (0),   (11),    (0),    (9)],
    3903:[(0),(0),"Cave Key",       (0),   (0),    (0),  (200),     (1),     (0),   (12),    (0),    (9)],
    3904:[(0),(0),"Exp Scroll",     (0),   (0),    (0),   (70),     (1),     (0),   (12),    (0),    (0)],
    1905:[(0),(0),"Map",            (0),   (0),    (0),   (20),     (1),     (0),   (10),   (10),    (0)],
    1906:[(0),(0),"Dragon Gem",     (0),   (0),    (0),    (0),     (0),     (0),   (13),   (13),    (0)],                        
    2907:[(0),(0),"Slayer Gem",     (0),   (0),    (0),    (0),     (0),     (0),   (14),    (0),    (0)],                        
    3908:[(0),(0),"Bloody Gem",     (0),   (0),    (0),    (0),     (0),     (0),   (15),    (0),    (0)]            
    }                          
    
    
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
   
    
    return itemsDict