from monsters.bestiary import Monster

chest_mimic_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 25,
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
chest_mimic_gear = []
chest_mimic_loot_table = ["Gold", "Rare Item", "Treasure Key"]
chest_mimic_description = "Chest Mimics are cunning creatures that disguise themselves as treasure chests to lure unsuspecting adventurers. When approached, they reveal their true form and attack with sharp teeth and tentacles, eager to devour their prey."
chest_mimic_floor_range = (80, 160)
chest_mimic_spells = []
chest_mimic_spell_probabilities = {}
chest_mimic_initial_stats = chest_mimic_stats.copy()
chest_mimic = Monster("Chest Mimic", chest_mimic_stats, chest_mimic_gear, chest_mimic_loot_table, difficulty=80, description=chest_mimic_description, floor_range=chest_mimic_floor_range, spells=chest_mimic_spells, spell_probabilities=chest_mimic_spell_probabilities, initial_stats=chest_mimic_initial_stats)

hell_bovine_stats = {
    "HP": 320,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 30,
    "Dexterity": 28,
    "Constitution": 32,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Fire"
}
hell_bovine_gear = ["Infernal Horns", "Burning Hide", "Bardiche"]
hell_bovine_loot_table = ["Gold", "Hellish Horn", "Charred Hide", "Bardiche"]
hell_bovine_description = "Hell Bovines are demonic cattle from the fiery depths of the underworld. With their infernal horns and burning hide, they trample through the inferno, leaving destruction in their wake."
hell_bovine_floor_range = (80, 160)
hell_bovine_spells = ["Infernal Charge", "Fiery Stampede", "Hellfire Breath"]
hell_bovine_spell_probabilities = {"Infernal Charge": 0.4, "Fiery Stampede": 0.3, "Hellfire Breath": 0.3}
hell_bovine_initial_stats = hell_bovine_stats.copy()
hell_bovine = Monster("Hell Bovine", hell_bovine_stats, hell_bovine_gear, hell_bovine_loot_table, difficulty=80, description=hell_bovine_description, floor_range=hell_bovine_floor_range, spells=hell_bovine_spells, spell_probabilities=hell_bovine_spell_probabilities, initial_stats=hell_bovine_initial_stats)

