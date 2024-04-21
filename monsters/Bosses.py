from monsters.bestiary import Monster

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

cow_king_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 40,
    "Dexterity": 35,
    "Constitution": 45,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 35,
    "Element": "Fire"
}
cow_king_gear = ["Infernal Crown", "Burning Hide", "Bardiche"]
cow_king_loot_table = ["Gold", "Hellish Horn", "Charred Hide", "Bardiche", "Infernal Crown"]
cow_king_description = "The Cow King, ruler of the Hell Bovines, is a fearsome monarch from the fiery depths of the underworld. Adorned with an infernal crown and wielding a bardiche, he commands his minions with unmatched strength and authority."
cow_king_floor_range = (100, 200)
cow_king_spells = ["Infernal Roar", "Stampede of Flame", "Bovine Fury"]
cow_king_spell_probabilities = {"Infernal Roar": 0.4, "Stampede of Flame": 0.3, "Bovine Fury": 0.3}
cow_king_initial_stats = cow_king_stats.copy()
cow_king = Monster("Cow King", cow_king_stats, cow_king_gear, cow_king_loot_table, difficulty=100, description=cow_king_description, floor_range=cow_king_floor_range, spells=cow_king_spells, spell_probabilities=cow_king_spell_probabilities, initial_stats=cow_king_initial_stats)
