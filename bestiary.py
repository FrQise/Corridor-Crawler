class Monster:
    def __init__(self, name, stats, gear, loot_table, difficulty):
        self.name = name
        self.stats = stats
        self.gear = gear
        self.loot_table = loot_table
        self.difficulty = difficulty

# Define monsters and their attributes
goblin_stats = {
    "HP": 50,  # Define HP attribute for Goblin
    "Damage": 20,  # Define damage attribute for Goblin
    "Defense": 10,  # Define Defense stat vs attack stat
    "Magic Defense": 0,  # Define magic defense vs spells
    "Strength": 8,
    "Dexterity": 12,
    "Constitution": 10,
    "Intelligence": 6,
    "Wisdom": 6,
    "Charisma": 6,
    "Element": "Fire"  # Define elemental attribute of the goblin's attack
}
goblin_gear = ["Rusty Sword", "Tattered Cloth Armor"]
goblin_loot_table = ["Gold", "Health Potion", "Small Gem"]
goblin = Monster("Goblin", goblin_stats, goblin_gear, goblin_loot_table, difficulty=1)


orc_stats = {
    "HP": 100,  # Define HP attribute for Orc
    "Damage" : 35, #Define damage attribute
    "Defense" : 15, #Define Defense vs attack stat
    "Magic Defense" : 0, #Mdef vs Matk
    "Strength": 15,
    "Dexterity": 10,
    "Constitution": 14,
    "Intelligence": 8,
    "Wisdom": 8,
    "Charisma": 8,
    "Element": "Fire"
}
orc_gear = ["Battle Axe", "Chainmail Armor"]
orc_loot_table = ["Gold", "Health Potion", "Large Gem"]
orc = Monster("Orc", orc_stats, orc_gear, orc_loot_table, difficulty=2)

dragon_stats = {
    "HP": 200,  # Define HP attribute for Dragon
    "Strength": 20,
    "Dexterity": 12,
    "Constitution": 18,
    "Intelligence": 16,
    "Wisdom": 16,
    "Charisma": 14
}
dragon_gear = ["Dragon Scale Armor", "Dragon Tooth Dagger"]
dragon_loot_table = ["Gold", "Dragon Scale", "Dragon Claw"]
dragon = Monster("Dragon", dragon_stats, dragon_gear, dragon_loot_table, difficulty=5)

# Add more monsters as needed...

# Example usage:
#print(f"{goblin.name}: {goblin.stats}, Gear: {goblin.gear}, Loot Table: {goblin.loot_table}")
#print(f"{orc.name}: {orc.stats}, Gear: {orc.gear}, Loot Table: {orc.loot_table}")
#print(f"{dragon.name}: {dragon.stats}, Gear: {dragon.gear}, Loot Table: {dragon.loot_table}")
