import random, time

global campfire_dur
iteration = 0
past = ""
past2 = ""
player_input = "game help"
health = 100
hunger = 100

trees = 15
logs = 0
planks = 0
sticks = 0
saplings = 0
flowers = 0
herbs = 0
apples = 0
seeds = 0
wheat = 0
bread = 0
toast = 0
wool = 0
mutton = 0
cooked_mutton = 0
driftwood = 0

campfire = 0
campfire_dur = 0

def check_camp_durability(input_camp_dur):
    if campfire_dur < input_camp_dur:
        return False
    else:
        return True
  
while True:
    #checks on loop
    if campfire_dur < 1:
        campfire -= 0
    elif campfire > 1:
        campfire = 1
        
    if "game" in player_input.lower():
        if "game help" in player_input.lower():
            print("Use 'player inv' to get the inventory.")
            print("Use 'game help' to show this again.")
            
    if "player" in player_input.lower():
        if "player health" in player_input.lower():
            print("Health: "+str(health)+"/100")
            
        if "player hunger" in player_input.lower():
            print("Hunger: "+str(hunger)+"/100")
    
        if "player inv" in player_input.lower():
            print("Buildings: ")
            print(" Campfire: "+str(campfire)+"/1")
            
            print("\nMaterials: ")
            print(" Logs: "+str(logs))
            print(" Planks: "+str(planks))
            print(" Sticks: "+str(sticks))
                  
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
            print(" Mutton: "+str(mutton))
            print(" Cooked Mutton: "+str(cooked_mutton))
        
    if "cut" in player_input.lower():
        if "cut tree" in player_input.lower():
            print("Cutting Tree...")
            if trees > 0:
                trees -= 1
                new_logs = random.randint(2, 5)
                new_saplings = random.randint(1, 3)
                new_sticks = random.randint(1, 3)
                new_apples = random.randint(0, 2)
                if new_apples == 0:
                    apple_text = ""
                else:
                    apples += new_apples
                    apple_text = "| Apples: "+str(apples)+" (+"+str(new_apples)+")"
                saplings += new_saplings
                logs += new_logs
                sticks += new_sticks
                print("Logs: "+str(logs)+" (+"+str(new_logs)+") | Trees: "+str(trees)+" (-1) | Saplings: "+str(saplings)+" (+"+str(new_saplings)+") | Sticks: "+str(sticks)+" (+"+str(new_sticks)+")" + apple_text)
            else:
                print("Not enough Trees! (Needs: 1 | Has: "+str(trees)+")")
                
        if "cut logs" in player_input.lower():
            print("Cutting Logs...")
            if logs > 1:
                logs -= 2
                planks += 6
                print("Logs: "+str(logs)+" (-2) | Planks: "+str(planks)+" (+2)")
            else:
                print("Not enough Logs! (Needs: 2 | Has: "+str(logs)+")")
                      
        if "cut driftwood" in player_input.lower():
            print("Cutting Driftwood...")
            if driftwood > 1:
                driftwood -= 2
                planks += 1
                print("Driftwood: "+str(driftwood)+" (-2) | Planks: "+str(planks)+" (+1)")
            else:
                print("Not enough Driftwood! (Needs: 2 | Has: "+str(driftwood)+")")                
                        
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
                cook_dur = 3
                if check_camp_durability(cook_dur) == False:
                    print("Not enough fire durability! (Have: "+str(campfire_dur)+"/100 | Need: "+str(cook_dur)+")")
                else:
                    campfire_dur -= cook_dur
                    bread -= 1
                    toast += 2
                    print("Bread: "+str(bread)+" (-1) | Toast: "+str(toast)+" (+2)")
                    print("Campfire Dur.: "+str(campfire_dur)+"/100) (-"+str(cook_dur)+")")
            else:
                print("Not enough Bread! (Needs: 1 | Has: "+str(bread)+")")
                
        if "cook mutton" in player_input.lower():
            print("Cooking Mutton...")
            if mutton > 0:
                cook_dur = 4
                if check_camp_durability(cook_dur) == False:
                    print("Not enough fire durability! (Have: "+str(campfire_dur)+"/100 | Need: "+str(cook_dur)+")")
                else:
                    campfire_dur -= cook_dur
                    mutton -= 1
                    cooked_mutton += 1
                    print("Mutton: "+str(mutton)+" (-1) | Cooked Mutton: "+str(cooked_mutton)+" (+1)")
                    print("Campfire Dur.: ("+str(campfire_dur)+"/100) (-"+str(cook_dur)+")")
            else:
                print("Not enough Mutton! (Needs: 1 | Has: "+str(mutton)+")")
                
    if "explore" in player_input.lower():
        if "explore plains" in player_input.lower():
            print("Exploring Plains... ")
            new_flowers = random.randint(0, 3)
            if not new_flowers == 0:
                flowers += new_flowers
                print("Flowers: "+str(flowers)+" (+"+str(new_flowers)+")")
                new_flowers = 0
                time.sleep(0.5)
                
            new_herbs = random.randint(0, 3)
            if not new_herbs == 0:
                herbs += new_herbs
                print("Herbs: "+str(herbs)+" (+"+str(new_herbs)+")")
                new_herbs = 0
                time.sleep(0.5)
                
            new_seeds = random.randint(1, 8)
            seeds += new_seeds
            print("Seeds: "+str(seeds)+" (+"+str(new_seeds)+")")
            new_seeds = 0
            time.sleep(0.5)

            find_sheep = random.randint(1, 10)
            if find_sheep > 6:
                ask_sheep = input("You have found a sheep. Kill it? (Y/N)\n> ")
                if ask_sheep.lower() == "y":
                    kill_sheep = random.randint(1, 100)
                    if kill_sheep > 15:
                        print("[SUCCESS] The sheep was killed.")
                        new_wool = random.randint(1, 3)
                        wool += new_wool
                        new_mutton = random.randint(2, 4)
                        mutton += new_mutton
                        print("Wool: "+str(wool)+" (+"+str(new_wool)+") | Mutton: "+str(mutton)+" (+"+str(new_mutton)+")")
                    else:
                        print("[FAILED] The sheep managed to escape from you, making you look like an idiot.")
                else:
                    print("You've decided not to kill the sheep.")
                      
        if "explore beach" in player_input.lower():
            print("Exploring Beach... ")
            new_driftwood = random.randint(1, 3)
            driftwood += new_driftwood
            print("Driftwood: "+str(driftwood)+" (+"+str(new_driftwood)+")")
            new_driftwood = 0
            time.sleep(0.5)
                
    if "build" in player_input:
        if "build campfire" in player_input:
            print("Building Campfire...")
            if campfire > 0:
                print("You already have a campfire!")
            elif sticks >= 5 or logs >= 3:
                sticks -= 5
                logs -= 3
                campfire += 1
                campfire_dur = 100
                print("Campfire: "+str(campfire)+" (Dur.: "+str(campfire_dur)+"/100) (+1) | Logs: "+str(logs)+" (-3) | Sticks: "+str(sticks)+" (-5)")
            else:
                print("Not enough Sticks/Logs! (Logs: Needs: 3 | Has: "+str(logs)+") (Sticks: Needs: 5 | Has: "+str(sticks)+")")

    if "destroy" in player_input:
        if "destroy campfire" in player_input:
            print("Destroying Campfire...")
            campfire_dur = 0
            campfire -= 1
            print("Campfire: "+str(campfire)+" (-1)")

    
    if "building" in player_input:
        if "building info" in player_input:
            print("Building Information")
            print(" Campfire: (Have: "+str(campfire)+") (Dur.: "+str(campfire_dur)+"/100)") 
            
    time.sleep(0.1)
    if past == "auto past":
        if iteration == 0:
            iteration == 1
            past = player_input
            player_input = past2
            
        if iteration == 10:
            player_input = input("> ")
            iteration = 0
            past = ""
            
        else:
            iteration += 1
            
    elif iteration == 0:
        past2 = player_input
        player_input = input("> ")
        if player_input == "past":
            player_input = past 
        past = player_input
