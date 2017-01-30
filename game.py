import random, time

past = ""
player_input = "game help"
health = 100
hunger = 100

trees = 10
logs = 0
saplings = 0
flowers = 0
herbs = 0
apples = 0
seeds = 0
wheat = 0
bread = 0
toast = 0

while True:
    past = player_input
    player_input = input("> ")
    if player_input == "past":
        player_input = past
    
    if "game" in player_input.lower():
        if "game inv" in player_input.lower():
            print("Materials: ")
            print(" Logs: "+str(logs))
                  
            print("\nPlants: ")
            print(" Trees: "+str(trees))
            print(" Saplings: "+str(saplings))
            print(" Flowers: "+str(flowers))
            print(" Herbs: "+str(herbs))
            print(" Seeds: "+str(seeds))
            print(" Wheat: "+str(wheat))

            print("\nFood: ")
            print(" Apples: "+str(apples))
            print(" Bread: "+str(bread))
            print(" Toast: "+str(toast))
            
        if "game help" in player_input.lower():
            print("Use 'past' to run the last input again.")
            print("Use 'game inv' to get the inventory.")
            
    if "player" in player_input.lower():
        if "player health" in player_input.lower():
            print("Health: "+str(health)+"/100")
            
        if "player hunger" in player_input.lower():
            print("Hunger: "+str(hunger)+"/100")        

        print("Health: "+str(health)+"/100")
        print("Hunger: "+str(hunger)+"/100")
        
    if "cut" in player_input.lower():
        if "cut tree" in player_input.lower():
            print("Cutting Tree...")
            if trees > 0:
                trees -= 1
                new_logs = random.randint(2, 5)
                new_saplings = random.randint(1, 3)
                new_apples = random.randint(0, 2)
                apples += new_apples
                if new_apples == 0:
                    apple_text = ""
                else:
                   apple_text = "| Apples: "+str(apples)+" (+"+str(new_apples)+")"
                saplings += new_saplings
                logs += new_logs
                print("Logs: "+str(logs)+" (+"+str(new_logs)+") | Trees: "+str(trees)+" (-1) | Saplings: "+str(saplings)+" (+"+str(new_saplings)+") "+ apple_text)
            else:
                print("Not enough Trees! (Needs: 1 | Has: "+str(trees)+")")

        if "cut logs" in player_input.lower():
            print("Cutting Logs...")
            
    if "plant" in player_input.lower():
        if "plant sapling" in player_input.lower():
            print("Planting Saplings...")
            if saplings > 0:
                saplings -= 1
                trees += 1
                print("Saplings: "+str(saplings)+" (-1) | Trees: "+str(trees)+" (+1)")
            else:
                print("Not enough Saplings! (Needs: 1 | Has: "+str(saplings)+")")
                
        if "plant seeds" in player_input.lower():
            print("Planting Seeds...")
            if seeds > 0:
                seeds -= 5
                wheat += 5
                print("Seeds: "+str(seeds)+" (-5) | Wheat: "+str(wheat)+" (+5)")
            else:
                print("Not enough Seeds! (Needs: 5 | Has: "+str(seeds)+")")

    if "bake" in player_input.lower():
        if "bake bread" in player_input.lower():
            print("Baking Bread...")
            if wheat > 0:
                wheat -= 3
                bread += 1
                print("Wheat: "+str(wheat)+" (-3) | Bread: "+str(bread)+" (+1)")
            else:
                print("Not enough Wheat! (Needs: 3 | Has: "+str(wheat)+")")
                
    if "cook" in player_input.lower():
        if "cook toast" in player_input.lower():
            print("Cooking Toast...")
            if bread > 0:
                bread -= 1
                toast += 2
                print("Bread: "+str(bread)+" (-1) | Toast: "+str(toast)+" (+2)")
            else:
                print("Not enough Bread! (Needs: 1 | Has: "+str(bread)+")")
                
    if "explore" in player_input.lower():
        if "explore plains" in player_input.lower():
            print("Exploring Plains... ")
            new_flowers = random.randint(0, 3)
            if not new_flowers == 0:
                flowers += new_flowers
                print("Flowers: "+str(flowers)+" (+"+str(new_flowers)+")")
                new_flowers = 0
                time.sleep(1)
                
            new_herbs = random.randint(0, 3)
            if not new_herbs == 0:
                herbs += new_herbs
                print("Herbs: "+str(herbs)+" (+"+str(new_herbs)+")")
                new_herbs = 0
                time.sleep(1)
                
            new_seeds = random.randint(1, 8)
            seeds += new_seeds
            print("Seeds: "+str(seeds)+" (+"+str(new_seeds)+")")
            new_seeds = 0
            time.sleep(1)
                
            #TODO: Add more discoveries to plains
    
