class Monster:
    def __init__(self, name, stats, gear, loot_table, difficulty, description, floor_range):
        self.name = name
        self.stats = stats
        self.initial_stats = stats.copy()
        self.gear = gear
        self.loot_table = loot_table
        self.difficulty = difficulty
        self.floor_range = floor_range
        self.description = description
        self.initial_hp = stats["HP"] #Initialize initial HP attribute

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
goblin_description = "Goblins are small, agile creatures known for their mischief and love of shiny objects. Despite their size, they can be formidable opponents in combat, relying on their speed and cunning to outmaneuver their foes."
goblin_floor_range = (1,2)
goblin = Monster("Goblin", goblin_stats, goblin_gear, goblin_loot_table, difficulty=1, description=goblin_description, floor_range=goblin_floor_range)


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
orc_description = "Orcs are fierce warriors, towering in stature and wielding massive weapons with ease. They are known for their strength, ferocity, and cunning tactics in battle. Loyalty to their clans drives them to protect their territory at any cost."
orc_floor_range = (3,5)
orc = Monster("Orc", orc_stats, orc_gear, orc_loot_table, difficulty=2, description=orc_description, floor_range=orc_floor_range)

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
dragon_description = "Dragons are majestic creatures, feared and revered for their immense power and intelligence. With scales as tough as armor and breath as deadly as fire, they rule the skies and dominate the land. Their hoards glitter with treasure, attracting both adventurers and those seeking their favor."
dragon_floor_range = (5,10)
dragon = Monster("Dragon", dragon_stats, dragon_gear, dragon_loot_table, difficulty=5, description=dragon_description, floor_range=dragon_floor_range)


edouard_stats = {
    "HP": 200,
    "Damage" : 1, #Define damage attribute
    "Defense" : 3, #Define Defense vs attack stat
    "Magic Defense" : 0, #Mdef vs Matk
    "Strength": 1,
    "Dexterity": 1,
    "Constitution": 18,
    "Intelligence": 1,
    "Wisdom": 1,
    "Charisma": 5
}
# Need to add description. He'll try to rob merchant that we encounter, everytime he'll flee before dying, 
# the first time we'll cut his left ear, the second time his right ear, if we meet him a 3rd time he'll give us good loot he stole from his rich parents

edouard_gear = ["Butter knife"]
edouard_loot_table = ["Gold", "Edouard's ears"]
edouard_description = "Edouard is a strange young half-elf wearing a fierce butter knife in his right hand"
edouard_floor_range = (10,20)
edouard = Monster("Edouard", edouard_stats, edouard_gear, edouard_loot_table, difficulty=1, description=edouard_description, floor_range=edouard_floor_range)


torgorak_stats = {
    "HP": 200,
    "Damage" : 50, #Define damage attribute
    "Defense" : 35, #Define Defense vs attack stat
    "Magic Defense" : 45, #Mdef vs Matk
    "Strength": 17,
    "Dexterity": 15,
    "Constitution": 18,
    "Intelligence": 13,
    "Wisdom": 12,
    "Charisma": 14
}
# Need to add description. Torgorak can cast a spell that will devour the reality, teleporting the player into a new biome, difficulty for every floor go +1.
# If the player let Torgorak use this spell : Torgorak will flee, not looting anything but you'll have access to the new biome (to define)
# If the player kill Torgorak before he cast the devour spell, he'll have the loot

torgorak_gear = [""]
torgorak_loot_table = ["Gold", "Torgorak's Tooth"]
torgorak_description = "Torgorak is... a small hamster wearing a cape"
#Torgorak's Tooth is a dagger made from a tooth of Torgorak. To define
torgorak_floor_range = (12,20)
torgorak = Monster("Torgorak, devour of world", torgorak_stats, torgorak_gear, torgorak_loot_table, difficulty=12,description=torgorak_description,floor_range=torgorak_floor_range)

# Add more monsters as needed...

# Example usage:
#print(f"{goblin.name}: {goblin.stats}, Gear: {goblin.gear}, Loot Table: {goblin.loot_table}")
#print(f"{orc.name}: {orc.stats}, Gear: {orc.gear}, Loot Table: {orc.loot_table}")
#print(f"{dragon.name}: {dragon.stats}, Gear: {dragon.gear}, Loot Table: {dragon.loot_table}")
