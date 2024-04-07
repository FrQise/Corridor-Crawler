import random
from enum import Enum
import inquirer
from item_definitions import Weapon, Armor, weapons, armor
from races_classes import Race, Class, human, elf, dwarf, fighter, wizard, rogue, cleric, sorcerer
import importlib

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
    def __init__(self, race=None, char_class=None, starting_gear=None):
        self.race = race
        self.char_class = char_class
        self.stats = {  # Initialize stats attribute
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
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

    def calculate_hp(self):
        return self.stats["Constitution"] * 10 + self.stats["Strength"] * 5

    def calculate_mp(self):
        return self.stats["Intelligence"] * 10 + self.stats["Wisdom"] * 5

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
    print("\nPlayer:")
    print(f"\033[91mHP: {player.calculate_hp()}\033[0m")  # Red color for HP
    print(f"\033[94mMP: {player.calculate_mp()}\033[0m")  # Blue color for MP
    print(f"Race: {player.race.name} | Class: {player.char_class.name}")
    print(f"Holding: {player.get_current_weapon().name if player.get_current_weapon() else 'None'}")

def check_stats(player):
    print("\nPlayer Stats:")
    for stat, value in player.stats.items():
        print(f"{stat}: {value}")

    print("\nProficiencies:")
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
    input("\nPress any key to continue...")

def save_game():
    print("\nSaving game...\n")

def open_treasure_chest(player):
    print("\nYou just entered a treasure room!")
    questions = [
        inquirer.Confirm("open_chest",
                         message="Do you want to open the chest?",
                         default=True)
    ]
    answer = inquirer.prompt(questions)["open_chest"]
    if answer:
        print("\nYou found a Longsword and a Chain Shirt and a Basic Shield!")
        for weapon in weapons:
            if weapon.name == "Longsword":
                player.inventory.append(weapon)
        for armor_piece in armor:
            if armor_piece.name == "Chain Shirt":
                player.inventory.append(armor_piece)
            if armor_piece.name == "Basic Shield":
                player.inventory.append(armor_piece)
        print("\nThe Longsword and Chain Shirt have been added to your inventory.")

def god_altar(player):
    print("\nYou just found a God Altar")
    questions = [inquirer.Confirm("worship_god", message="Do you wish to worship God_Placerholder ?", default=True)]
    answer = inquirer.prompt(questions)["worship_god"]
    if answer:
        print("\nYou decided to worship God_Placeholder")
        print("\nHere are your modifiers: ADD_MODIFIERS")
    else: print("You decided to not worship God_Placeholder, they might take offense of this.")
    wait_for_input()

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
    print(f"\nYou encounter a {enemy.name}")  # Print HP in red color
    print("Prepare for battle!")

    # Combat loop
    while True:
        # Display player's HP and MP in color
        print(f"\033[91mPlayer HP: {player.stats['HP']}\033[0m")  # Print HP in red color
        print(f"\033[94mPlayer MP: {player.stats['MP']}\033[0m")  # Print MP in blue color

        # Display enemy HP before presenting battle options
        print(f"{enemy.name} HP: {enemy.stats['HP']}")

        # Display combat options
        combat_options = [
            inquirer.List("action",
                          message="Choose your action:",
                          choices=["Attack", "Magic", "Use Items"])
        ]
        action = inquirer.prompt(combat_options)["action"]

        if action == "Attack":
            # Implement attack logic
            print("You attacked the enemy!")
        elif action == "Magic":
            # Implement magic usage logic
            print("You cast a spell!")
        elif action == "Use Items":
            # Implement item usage logic
            print("You used an item!")

        # Implement enemy's turn
        enemy_action(player, enemy)

        # Check if the battle is over
        if player.stats['HP'] <= 0:
            print("You have been defeated!")
            break
        elif enemy.stats['HP'] <= 0:
            print(f"{enemy.name} has been defeated!")
            break

    wait_for_input()  # Wait for player input before continuing

import random

def enemy_action(player, enemy):
    if hasattr(enemy, 'stats') and 'Damage' in enemy.stats:
        damage_stat = enemy.stats['Damage']
        damage_modifier = random.uniform(0.8, 1.2)  # Random modifier between 80% to 120%
        damage_dealt = int(damage_stat * damage_modifier)  # Calculate the damage dealt
        player.stats['HP'] -= damage_dealt
        print(f"{enemy.name} attacks and deals {damage_dealt} damage!")
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
                god_altar(self.player)
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
                      message="Choose your race:",
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
                      message="Choose your class:",
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
    selected_race, selected_class = select_character()
    starting_gear = select_starting_gear(selected_class)

    player = Player(selected_race, selected_class, starting_gear)

    game = Game()
    game.player = player  # Assign the player object to the game
    game.main_menu()

if __name__ == "__main__":
    main()