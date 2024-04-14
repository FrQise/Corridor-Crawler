import random
from enum import Enum
import inquirer
import importlib
import sys
from item_definitions import Weapon, Armor, weapons, armor
from races_classes import Race, Class, human, elf, dwarf, fighter, wizard, rogue, cleric, sorcerer
from itertools import zip_longest
from pantheon import gods

class CorridorEventType(Enum):
    ENEMY_ENCOUNTER = "Enemy Encounter"
    TREASURE_CHEST = "Treasure Chest"
    TRAP = "Trap"
    EMPTY_CORRIDOR = "Empty Corridor"
    GOD_ALTAR = "God Altar"

class CorridorEvent:
    def __init__(self, description):
        self.description = description

class CorridorDungeon:
    def __init__(self, corridor_length):
        self.corridor_length = corridor_length
        self.corridor = []

    def generate_corridor(self):
        self.corridor.append(CorridorEvent("Starting Room - Welcome to the Dungeon!"))
        for _ in range(self.corridor_length - 1):
            event = self.generate_event()
            self.corridor.append(event)

    def generate_event(self):
        event_types = [event_type.value for event_type in CorridorEventType]
        return CorridorEvent(random.choice(event_types))

    def display_corridor(self):
        for i, event in enumerate(self.corridor):
            print(f"Corridor Position {i+1}: {event.description}")

class Player:
    def __init__(self, name, race=None, char_class=None, starting_gear=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.stats = {  
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10,
            "HP": 0,  # Placeholder for HP calculation
            "MP": 0,  # Placeholder for MP calculation
            "Fire Resistance": 0,  # New elemental resistance stats
            "Ice Resistance": 0,
            "Earth Resistance": 0,
            "Water Resistance": 0,
            "Electricity Resistance": 0,
            "Poison Resistance": 0,
            "Darkness Resistance": 0
        }
        self.god = None
        self.equipment = Equipment()
        self.inventory = []
        self.apply_race_modifiers()
        if char_class:
            char_class.apply_class_modifiers(self.stats)
        if starting_gear:
            self.equip_starting_gear(starting_gear)

        # Calculate HP after initializing stats
        self.stats["HP"] = self.calculate_hp()
        self.stats["MP"] = self.calculate_mp()

    def equip_starting_gear(self, starting_gear):
        for slot, item_name in starting_gear.items():
            if item_name:
                item = None
                if slot == "Right Hand" or slot == "Left Hand":
                    item = next((weapon for weapon in weapons if weapon.name == item_name), None)
                else:
                    item = next((armor_piece for armor_piece in armor if armor_piece.name == item_name), None)
                if item:
                    self.equipment.equip_item(slot, item)
                else:
                    print(f"Starting gear item '{item_name}' not found in inventory.")


    def apply_race_modifiers(self):
        if self.race:
            self.stats['Strength'] += self.race.strength
            self.stats['Dexterity'] += self.race.dexterity
            self.stats['Constitution'] += self.race.constitution
            self.stats['Intelligence'] += self.race.intelligence
            self.stats['Wisdom'] += self.race.wisdom
            self.stats['Charisma'] += self.race.charisma

            # Apply elemental resistance modifiers based on race if they exist
            if hasattr(self.race, 'fire_resistance'):
                self.stats['Fire Resistance'] += self.race.fire_resistance
            if hasattr(self.race, 'ice_resistance'):
                self.stats['Ice Resistance'] += self.race.ice_resistance
            if hasattr(self.race, 'earth_resistance'):
                self.stats['Earth Resistance'] += self.race.earth_resistance
            if hasattr(self.race, 'water_resistance'):
                self.stats['Water Resistance'] += self.race.water_resistance
            if hasattr(self.race, 'electricity_resistance'):
                self.stats['Electricity Resistance'] += self.race.electricity_resistance
            if hasattr(self.race, 'poison_resistance'):
                self.stats['Poison Resistance'] += self.race.poison_resistance
            if hasattr(self.race, 'darkness_resistance'):
                self.stats['Darkness Resistance'] += self.race.darkness_resistance

    def calculate_hp(self):
        return round(self.stats["Constitution"] * 2 + self.stats["Strength"] * 0.5)

    def calculate_mp(self):
        return round(self.stats["Intelligence"] * 2 + self.stats["Wisdom"] * 0.5)

    def get_current_weapon(self):
        if self.equipment:
            return self.equipment.get_equipped_item("Right Hand")
        else:
            return None

    def check_weapon_proficiency(self, weapon):
        return self.char_class.check_weapon_proficiency(weapon)

    def check_armor_proficiency(self, armor):
        return self.char_class.check_armor_proficiency(armor)

class Equipment:
    def __init__(self):
        self.slots = {
            "Right Hand": None,
            "Left Hand": None,
            "Head": None,
            "Chest": None,
            "Back": None,
            "Gloves": None,
            "Legs": None,
            "Boots": None,
            "Accessory 1": None,
            "Accessory 2": None
        }

    def equip_item(self, slot, item):
        if slot in self.slots:
            self.slots[slot] = item
            return True
        else:
            print("Invalid equipment slot.")
            return False

    def get_equipped_item(self, slot):
        return self.slots[slot]

def move_forward(position):
    print("\nMoving forward...\n")
    return position + 1

def check_room(player):
    print("\n" + player.name + ":")  # Print the player's chosen name
    print(f"Race: {player.race.name} | Class: {player.char_class.name}\n")
    print(f"\033[91mHP: {player.stats['HP']}\033[0m")  # Red color for HP
    print(f"\033[94mMP: {player.stats['MP']}\033[0m\n")  # Blue color for MP
    print(f"Holding: {player.get_current_weapon().name if player.get_current_weapon() else 'None'}")

def check_stats(player):
    print("\n\033[1m\033[4mPlayer Stats:\033[0m")

    # Exclude HP and MP stats from printing
    stats_to_exclude = ["HP", "MP"]

    # Calculate maximum width for stats and resistances
    stats_width = max(len(stat.split(":")[0]) for stat in player.stats.keys() if not stat.endswith("Resistance") and stat not in stats_to_exclude)
    resistance_width = max(len(stat.split(":")[0]) for stat in player.stats.keys() if stat.endswith("Resistance"))

    # Collect stats and resistances into separate lists
    stats_column = []
    resistances_column = []

    for stat, value in player.stats.items():
        if not stat.endswith("Resistance") and stat not in stats_to_exclude:
            stats_column.append(f"{stat}: {value}")  # Collect stats
        elif stat.endswith("Resistance"):
            resistances_column.append(f"{stat}: {value}")  # Collect resistances

    # Calculate the total width for the two columns
    total_width = max(stats_width, resistance_width) + 1  # Add 1 for spacing

    # Print stats and resistances side by side with proper alignment
    for stat, resistance in zip_longest(stats_column, resistances_column, fillvalue=""):
        print(f"{stat:<{total_width}}{resistance}")

    # Print god if it exists
    if hasattr(player, 'god'):
        print(f"\n\033[1m\033[4mGod:\033[0m {player.god}")

    # Print proficiencies
    print("\n\033[1m\033[4mProficiencies:\033[0m")
    print(f"Weapon Proficiencies: {', '.join(player.char_class.weapon_proficiencies)}")
    print(f"Armor Proficiencies: {', '.join(player.char_class.armor_proficiencies)}")
    wait_for_input()

def check_equipment(player):
    print("\nPlayer Equipment:")
    equipment_slots = player.equipment.slots
    for slot, item in equipment_slots.items():
        if item:
            print(f"{slot}: {item.name}")
        else:
            print(f"{slot}: Empty")

    questions = [
        inquirer.List("equipment_action",
                      message="[?] Equipment Options:",
                      choices=["View Details", "Back"])
    ]
    answer = inquirer.prompt(questions)["equipment_action"]

    if answer == "View Details":
        view_equipment_details(player)

def view_equipment_details(player):
    print("\nSelect an item to view details:")
    equipped_items = [item.name for item in player.equipment.slots.values() if item]
    equipped_items.append("Back")

    questions = [
        inquirer.List("item_action",
                      message="[?] Select Item:",
                      choices=equipped_items)
    ]
    answer = inquirer.prompt(questions)["item_action"]

    if answer != "Back":
        for slot, item in player.equipment.slots.items():
            if item and item.name == answer:
                print(f"\nName: {item.name}")
                print(f"Description: {item.description}")
                print("Modifiers:")
                for stat, value in item.stats.items():
                    print(f"{stat}: {value}")
                wait_for_input()
                return

        print("\nInvalid item selection.")

def check_inventory(player):
    print("\nPlayer Inventory:")
    for i, item in enumerate(player.inventory):
        print(f"{i + 1}. {item.name}")

    questions = [
        inquirer.List("inventory_action",
                      message="[?] Inventory Options:",
                      choices=["Equip Item", "Use Item", "View Details", "Back"])
    ]
    answer = inquirer.prompt(questions)["inventory_action"]

    if answer == "Equip Item":
        equip_item(player)
    elif answer == "Use Item":
        use_item(player)
    elif answer == "View Details":
        view_item_details(player)

def view_item_details(player):
    choice = input("\nEnter the number of the item you want to view details for (or 'b' to go back): ").strip().lower()

    if choice == 'b':
        return
    elif choice.isdigit():
        item_index = int(choice) - 1

        if 0 <= item_index < len(player.inventory):
            item = player.inventory[item_index]
            print(f"\nName: {item.name}")
            print(f"Description: {item.description}")
            print("Modifiers:")
            for stat, value in item.stats.items():
                print(f"{stat}: {value}")
            wait_for_input()
        else:
            print("\nInvalid item index. Please enter a valid number.")
    else:
        print("\nInvalid input. Please enter a number or 'b' to go back.")

def equip_item(player):
    if not player.inventory:
        print("\nYour inventory is empty. There are no items to equip.")
        wait_for_input()
        return

    while True:
        print("\nSelect an item to equip (or 'b' to go back):")
        for i, item in enumerate(player.inventory):
            print(f"{i + 1}. {item.name}")
        print("b. Back")

        choice = input("\nEnter the number of the item you want to equip: ").strip().lower()

        if choice == 'b':
            return
        elif choice.isdigit():
            item_index = int(choice) - 1

            if 0 <= item_index < len(player.inventory):
                item = player.inventory[item_index]

                # Check if the player has proficiency in using the item
                if isinstance(item, Weapon):
                    if player.check_weapon_proficiency(item.category.name):
                        # Equip the item
                        player.equipment.equip_item("Right Hand", item)
                        print(f"\nEquipped {item.name} in the Right Hand.")
                    else:
                        print(f"\nYou are not proficient in using {item.name}.")
                elif isinstance(item, Armor):
                    if player.check_armor_proficiency(item.name):
                        # Equip the item
                        slot = item.slot
                        if player.equipment.equip_item(slot, item):
                            print(f"\nEquipped {item.name} in the {slot}.")
                    else:
                        print(f"\nYou are not proficient in wearing {item.name}.")

                # Update player's stats based on the equipped item
                for stat, value in item.stats.items():
                    if stat in player.stats:
                        player.stats[stat] += value
                    else:
                        # Add the stat to the player's stats if it doesn't exist
                        player.stats[stat] = value

                # Remove the item from the inventory
                del player.inventory[item_index]
                wait_for_input()
                return
            else:
                print("\nInvalid item index. Please enter a valid number.")
        else:
            print("\nInvalid input. Please enter a number or 'b' to go back.")

def use_item(player):
    # Implement item usage logic here
    pass

def wait_for_input():
    input("\nPress Enter to continue...")
    # Move the cursor to the beginning of the line and clear it
    sys.stdout.write("\033[F\033[K")

def save_game():
    print("\nSaving game...\n")

def open_treasure_chest(player):
    print("\nYou just entered a treasure room!")
    questions = [
        inquirer.List("open_chest",
                      message="Do you want to open the chest?",
                      choices=["Yes", "No"],
                      default="Yes")
    ]
    answer = inquirer.prompt(questions)["open_chest"]
    if answer == "Yes":
        print("\nYou found a Longsword, a Chain Shirt, and a Basic Shield!")
        for item in weapons + armor:
            if item.name in ["Longsword", "Chain Shirt", "Basic Shield"]:
                player.inventory.append(item)
        print("\nThe Longsword, Chain Shirt, and Basic Shield have been added to your inventory.")
        wait_for_input()


def god_altar(player, altar_description):
    print("\n\nYou just found the Altar of", end=" ")

    # Randomly select a god
    selected_god = random.choice(gods)
    print(selected_god.name)

    print("\nDescription:", selected_god.description,"\n")

    current_god = player.stats.get('God', None)
    if current_god:
        if current_god == selected_god.name:
            print("This is the altar of your current god.")
            wait_for_input()
            return

        print(f"\nYou are currently worshiping {current_god}.")
        betray_question = [inquirer.List("betray_current_god", 
                                         message="Do you want to betray your current god and worship a new one?", 
                                         choices=["Yes", "No"], 
                                         default="No")]
        betray_answer = inquirer.prompt(betray_question)["betray_current_god"]
        if betray_answer:
            print(f"\nYou decided to betray {current_god}.")
            player.stats.pop('God')
        else:
            print("\nYou decided to remain loyal to your current god.")
            wait_for_input()
            return
    
    # Ask the player if they want to worship the selected god
    questions = [
        inquirer.List("worship_confirm",
                      message=f"Do you want to worship {selected_god.name}?",
                      choices=["Yes", "No"],
                      default="No")
    ]
    worship_confirm = inquirer.prompt(questions)["worship_confirm"]

    if worship_confirm == "Yes":
        print(f"\nYou decided to worship {selected_god.name}.")
        # Apply buffs to the player based on the selected god
        for stat, value in selected_god.buffs.items():
            player.stats[stat] += value
        player.stats['God'] = selected_god.name
    else:
        print("\nYou decided not to worship any god at this time.")

    wait_for_input()

def game_over():
    print("GAME OVER")
    input("Press any key to quit the game...")
    exit()

def check_player_hp(player):
    if player.stats['HP'] <= 0:
        game_over()

def handle_hp_reduction(player, hp_reduction_amount):
    player.stats['HP'] -= hp_reduction_amount
    check_player_hp(player)

def calculate_encounter_difficulty(current_position):
    # Calculate difficulty based on the current position
    # For example, you might want the difficulty to increase as the player progresses deeper into the dungeon
    # You can define your own formula here based on your game design
    return min(current_position // 2 + 1, 5)  # Example formula, capped at difficulty level 5

def handle_enemy_encounter(player, current_position):
    # Calculate encounter difficulty
    encounter_difficulty = calculate_encounter_difficulty(current_position)

    # Dynamically import the bestiary module
    bestiary = importlib.import_module('bestiary')

    # Filter enemies based on difficulty level
    possible_enemies = [enemy for enemy in [bestiary.goblin, bestiary.orc, bestiary.dragon] if enemy.difficulty <= encounter_difficulty]

    # Choose a random enemy from the list of possible enemies
    enemy = random.choice(possible_enemies)

    # Display initial enemy encounter
    print(f"\n\033[1;33mYou encounter a {enemy.name}\033[0m")
    print("Prepare for battle!")

    # Combat loop
    while True:
        # Check if the player is defeated
        if player.stats['HP'] <= 0:
            print("You have been defeated!")
            check_player_hp(player)
            return  # Exit the combat loop if the player is defeated

        # Display player's HP and MP in color
        print(f"\n\033[91mPlayer HP: {player.stats['HP']}\033[0m")  # Print HP in red color
        print(f"\033[94mPlayer MP: {player.stats['MP']}\033[0m\n")  # Print MP in blue color

        # Display enemy HP before presenting battle options if enemy is alive
        if enemy.stats['HP'] > 0:
            print(f"{enemy.name} HP: {enemy.stats['HP']}\n")

        # Display combat options only if player's HP is above 0
        if player.stats['HP'] > 0:
            # Combat options
            combat_options = [
                inquirer.List("action",
                              message="Choose your action:",
                              choices=["Attack", "Spells", "Use Items", "Block"])
            ]
            action = inquirer.prompt(combat_options)["action"]

            if action == "Attack":
                # Implement attack logic
                attack(player, enemy)
            elif action == "Spells":
                # Implement magic usage logic
                use_spells(player, enemy)
            elif action == "Use Items":
                # Implement item usage logic
                use_items(player)
            elif action == "Block":
                # Implement blocking logic
                block(player, enemy)

        # Check if the enemy is defeated
        if enemy.stats['HP'] <= 0:
            print(f"\n{enemy.name} has been defeated!")
            break  # Exit the combat loop if the enemy is defeated

        # Check if the player is defeated after taking action
        if player.stats['HP'] <= 0:
            print("You have been defeated!")
            return  # Exit the combat loop if the player is defeated

        # Implement enemy's turn only if it's alive
        if enemy.stats['HP'] > 0:
            enemy_action(player, enemy)

    wait_for_input()  # Wait for player input before continuing

def attack(player, enemy):
    # Get the equipped weapon of the player
    equipped_weapon = player.get_current_weapon()
    
    if equipped_weapon:
        # Calculate player's attack power based on strength and weapon's attack
        attack_power = player.stats['Strength'] + equipped_weapon.stats.get('Attack', 0)
        
        # Calculate damage dealt by subtracting enemy's defense from player's attack power
        damage = max(0, attack_power - enemy.stats.get('Defense', 0))
        
        # Reduce enemy's HP by damage
        enemy.stats['HP'] -= damage
        
        print(f"You attacked the {enemy.name} with {equipped_weapon.name} and dealt {damage} damage!\n")

    else:
        print("You have no weapon equipped!")
    
    # Check if the enemy is still alive before allowing it to attack
    if enemy.stats.get('HP', 0) > 0:
        if 'Attack' in enemy.stats:
            print(f"{enemy.name} attacks and deals {enemy.stats['Attack']} damage!")
            player.stats['HP'] -= enemy.stats['Attack']
            if player.stats['HP'] <= 0:
                print("You have been defeated!")
                # Add any other game over logic here

def use_spells(player, enemy):
    # Implement spell usage logic here
    pass

def use_items(player):
    # Implement item usage logic here
    pass

def block(player, enemy):
    # Calculate damage reduction based on player's defense stats
    damage_reduction = player.stats.get('Defense', 0)
    # Reduce the enemy's damage by the player's defense
    enemy_damage = max(0, enemy.stats.get('Damage', 0) - damage_reduction)
    # Reduce player's HP by the enemy's damage
    player.stats['HP'] -= enemy_damage
    print(f"You blocked the {enemy.name}'s attack and received {enemy_damage} damage!")

def enemy_action(player, enemy):
    if hasattr(enemy, 'stats') and 'Damage' in enemy.stats:
        damage_stat = enemy.stats['Damage']
        damage_modifier = random.uniform(0.8, 1.2)  # Random modifier between 80% to 120%
        damage_dealt = int(damage_stat * damage_modifier)  # Calculate the damage dealt
        
        # Check if the enemy's attack is elemental
        if 'Element' in enemy.stats:
            element = enemy.stats['Element']
            # Check if the player has resistance to the elemental attack
            if f"{element} Resistance" in player.stats:
                resistance = player.stats[f"{element} Resistance"]
                # Calculate the damage reduction based on elemental resistance
                damage_reduction_percentage = resistance / 100
                damage_dealt -= int(damage_dealt * damage_reduction_percentage)
                print(f"{enemy.name} attacks with {element} and deals {damage_dealt} damage!")
        else:
            print(f"{enemy.name} attacks and deals {damage_dealt} damage!")
        
        player.stats['HP'] -= damage_dealt
        if player.stats['HP'] <= 0:
            print("You have been defeated!")
            # Add any other game over logic here
    else:
        print(f"{enemy.name} attacks! Unable to determine the outcome of the attack.")


class GameState:
    def __init__(self, menu_function):
        self.menu_function = menu_function

class Game:
    def __init__(self):
        self.corridor_dungeon = CorridorDungeon(corridor_length=10)
        self.corridor_dungeon.generate_corridor()
        self.player = None  # Player object will be initialized later
        self.current_position = 0  # Initialize player's position
        self.states = []
        self.opened_treasure_chests = []  # Track opened treasure chests

    def push_state(self, state):
        self.states.append(state)

    def pop_state(self):
        if self.states:
            return self.states.pop()
        else:
            return None

    def current_state(self):
        return self.states[-1]

    def current_event(self):
        return self.corridor_dungeon.corridor[self.current_position]

    def main_menu(self):
        self.push_state(GameState(self.main_menu))
        while self.current_position < self.corridor_dungeon.corridor_length:
            current_event = self.current_event()
            print("\nCurrent Corridor Event:")
            print(current_event.description)
            print("Current position :", self.current_position)
            check_room(self.player)

            # Handle treasure room event only if it hasn't been opened yet
            if current_event.description == CorridorEventType.TREASURE_CHEST.value and self.current_position not in self.opened_treasure_chests:
                open_treasure_chest(self.player)
                self.opened_treasure_chests.append(self.current_position)
            elif current_event.description == CorridorEventType.GOD_ALTAR.value:
                god_altar(self.player, self.current_event().description)
            elif current_event.description == CorridorEventType.ENEMY_ENCOUNTER.value:
                handle_enemy_encounter(self.player, self.current_position)

            # Player options
            questions = [
                inquirer.List("action",
                              message="[?] What would you like to do?",
                              choices=["Move forward", "Check Stats", "Check Equipment", "Check Inventory", "Save"])]
            answer = inquirer.prompt(questions)["action"]

            if answer == "Move forward":
                self.current_position = move_forward(self.current_position)  # Update player's position
            elif answer == "Check Stats":
                check_stats(self.player)
                self.pop_state()  # After finishing the submenu, pop the state to return to the previous state
            elif answer == "Check Equipment":
                check_equipment(self.player)
                self.pop_state()  # After finishing the submenu, pop the state to return to the previous state
            elif answer == "Check Inventory":
                check_inventory(self.player)
                self.pop_state()  # After finishing the submenu, pop the state to return to the previous state
            elif answer == "Save":
                save_game()

            # Check if the game ends
            if self.current_position == self.corridor_dungeon.corridor_length:
                print("\nYou reached the end of the corridor!")
                self.pop_state()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_character():
    races = [human, elf, dwarf]
    classes = [fighter, wizard, rogue, cleric, sorcerer]

    # Select race
    race_questions = [
        inquirer.List("race",
                      message="Choose your race",
                      choices=[race.name for race in races])
    ]
    selected_race = Race("Human", "Adaptable and versatile")  # Default to Human
    race_answer = inquirer.prompt(race_questions)["race"]
    for race in races:
        if race.name == race_answer:
            selected_race = race
            break

    # Select class
    class_questions = [
        inquirer.List("class",
                      message="Choose your class",
                      choices=[char_class.name for char_class in classes])
    ]
    selected_class = None
    while selected_class is None:
        class_answer = inquirer.prompt(class_questions)["class"]
        for char_class in classes:
            if char_class.name == class_answer:
                selected_class = char_class
                break
        else:
            print("Invalid class selection. Please choose from the available classes.")

    return selected_race, selected_class

def select_starting_gear(selected_class):
    starting_gear = {
        "Right Hand": None,
        "Left Hand": None,
        "Chest": None,
        "Boots": None,        
        "Head": None,
        "Chest": None,
        "Back": None,
        "Gloves": None,
        "Legs": None,
        "Accessory 1": None,
        "Accessory 2": None
    }

    if selected_class == fighter:
        starting_gear["Right Hand"] = "Short Sword"
        starting_gear["Chest"] = "Leather Armor"
        starting_gear["Left Hand"] = "Basic Shield"
        # Add other starting gear for fighter if needed

    return starting_gear

def main():
    print("""                   
        _____         ____     ___________      ___________        ____________  ____________          ____     ___________                     _____  ___________          _____           _______     _______  _____               _____\    \ ___________       
   _____\    \_   ____\_  \__  \          \     \          \      /            \ \           \     ____\_  \__  \          \               _____\    \_\          \       /      |_        /      /|   |\      \|\    \             /    / |    |\          \      
  /     /|     | /     /     \  \    /\    \     \    /\    \    |\___/\  \\___/| \           \   /     /     \  \    /\    \             /     /|     |\    /\    \     /         \      /      / |   | \      \\\    \           /    /  /___/| \    /\    \     
 /     / /____/|/     /\      |  |   \_\    |     |   \_\    |    \|____\  \___|/  |    /\     | /     /\      |  |   \_\    |           /     / /____/| |   \_\    |   |     /\    \    |      /  |___|  \      |\\    \         |    |__ |___|/  |   \_\    |    
|     | |____|/|     |  |     |  |      ___/      |      ___/           |  |       |   |  |    ||     |  |     |  |      ___/           |     | |____|/  |      ___/    |    |  |    \   |      |  |   |  |      | \|    | ______ |       \        |      ___/     
|     |  _____ |     |  |     |  |      \  ____   |      \  ____   __  /   / __    |    \/     ||     |  |     |  |      \  ____        |     |  _____   |      \  ____ |     \/      \  |       \ \   / /       |  |    |/      \|     __/ __     |      \  ____  
|\     \|\    \|     | /     /| /     /\ \/    \ /     /\ \/    \ /  \/   /_/  |  /           /||     | /     /| /     /\ \/    \       |\     \|\    \ /     /\ \/    \|\      /\     \ |      |\\/   \//|      |  /            ||\    \  /  \   /     /\ \/    \ 
| \_____\|    ||\     \_____/ |/_____/ |\______|/_____/ |\______||____________/| /___________/ ||\     \_____/ |/_____/ |\______|       | \_____\|    |/_____/ |\______|| \_____\ \_____\|\_____\|\_____/|/_____/| /_____/\_____/|| \____\/    | /_____/ |\______| 
| |     /____/|| \_____\   | / |     | | |     ||     | | |     ||           | /|           | / | \_____\   | / |     | | |     |       | |     /____/||     | | |     || |     | |     || |     | |   | |     | ||      | |    ||| |    |____/| |     | | |     | 
 \|_____|    || \ |    |___|/  |_____|/ \|_____||_____|/ \|_____||___________|/ |___________|/   \ |    |___|/  |_____|/ \|_____|        \|_____|    |||_____|/ \|_____| \|_____|\|_____| \|_____|\|___|/|_____|/ |______|/|____|/ \|____|   | | |_____|/ \|_____| 
        |____|/  \|____|                                                                          \|____|                                       |____|/                                                                                  |___|/                    
    """)
    wait_for_input()
    while True:
        print("\nMain Menu:")
        menu_choices = [
            inquirer.List("choice",
                          message="Select an option:",
                          choices=[
                              "Start a new game",
                              "Load",
                              "About",
                              "Exit"
                          ])
        ]
        choice = inquirer.prompt(menu_choices)["choice"]

        if choice == "Start a new game":
            start_new_game()
        elif choice == "Load":
            load_game()
        elif choice == "About":
            show_about()
        elif choice == "Exit":
            print("Exiting the game. Goodbye!")
            break

def get_valid_player_name():
    while True:
        player_name = input("Enter your character's name (up to 15 characters): ").strip()
        if not player_name:
            print("Please enter a non-empty name.")
        elif len(player_name) > 15:
            print("Name cannot exceed 15 characters.")
        else:
            return player_name

def start_new_game():
    player_name = get_valid_player_name()
    selected_race, selected_class = select_character()
    starting_gear = select_starting_gear(selected_class)

    player = Player(player_name, selected_race, selected_class, starting_gear)

    game = Game()
    game.player = player  # Assign the player object to the game
    game.main_menu()

def load_game():
    # Implement loading saved game logic here
    print("Load function is under construction.")

def show_about():
    # Display information about the game
    print("This is a text-based adventure game.")
    print("Developed by FrQise.")
    print("Version : Very pas finished")
    wait_for_input()

if __name__ == "__main__":
    main()