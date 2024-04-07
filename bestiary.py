class Monster:
    def __init__(self, name, stats, gear, loot_table):
        self.name = name
        self.stats = stats
        self.gear = gear
        self.loot_table = loot_table

# Function to create a new monster instance
def create_monster(name, stats, gear, loot_table):
    return Monster(name, stats, gear, loot_table)

# Define monsters and their attributes
goblin_stats = {
    "Strength": 8,
    "Dexterity": 12,
    "Constitution": 10,
    "Intelligence": 6,
    "Wisdom": 6,
    "Charisma": 6
}
goblin_gear = ["Rusty Sword", "Tattered Cloth Armor"]
goblin_loot_table = ["Gold", "Health Potion", "Small Gem"]
goblin = create_monster("Goblin", goblin_stats, goblin_gear, goblin_loot_table)

orc_stats = {
    "Strength": 15,
    "Dexterity": 10,
    "Constitution": 14,
    "Intelligence": 8,
    "Wisdom": 8,
    "Charisma": 8
}
orc_gear = ["Battle Axe", "Chainmail Armor"]
orc_loot_table = ["Gold", "Health Potion", "Large Gem"]
orc = create_monster("Orc", orc_stats, orc_gear, orc_loot_table)

dragon_stats = {
    "Strength": 20,
    "Dexterity": 12,
    "Constitution": 18,
    "Intelligence": 16,
    "Wisdom": 16,
    "Charisma": 14
}
dragon_gear = ["Dragon Scale Armor", "Dragon Tooth Dagger"]
dragon_loot_table = ["Gold", "Dragon Scale", "Dragon Claw"]
dragon = create_monster("Dragon", dragon_stats, dragon_gear, dragon_loot_table)

# Add more monsters as needed...

# Example usage:
print(f"{goblin.name}: {goblin.stats}, Gear: {goblin.gear}, Loot Table: {goblin.loot_table}")
print(f"{orc.name}: {orc.stats}, Gear: {orc.gear}, Loot Table: {orc.loot_table}")
print(f"{dragon.name}: {dragon.stats}, Gear: {dragon.gear}, Loot Table: {dragon.loot_table}")