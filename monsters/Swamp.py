from monsters.bestiary import Monster

dragonfly_stats = {
    "HP": 40,  # Define HP attribute for Dragon Fly
    "Damage": 15,  # Define damage attribute for Dragon Fly
    "Defense": 5,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 6,
    "Dexterity": 18,
    "Constitution": 8,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Air"  # Define elemental attribute of the Dragon Fly's attack
}
dragonfly_gear = ["Razor Wings", "Etheric Scales"]
dragonfly_loot_table = ["Gold", "Etheric Essence", "Dragonfly Wing"]
dragonfly_description = "Dragon Flies are mystical creatures known for their graceful flight and potent magical abilities. Despite their delicate appearance, they are formidable opponents, capable of weaving powerful spells and evading attacks with ease."
dragonfly_floor_range = (3, 6)
dragonfly_spells = ["Etheric Blast", "Wing Gust"]
dragonfly_spell_probabilities = {"Etheric Blast": 0.7, "Wing Gust": 0.3} 
dragonfly_initial_stats = dragonfly_stats.copy() # Make a copy of the initial stats
dragonfly = Monster("Dragon Fly", dragonfly_stats, dragonfly_gear, dragonfly_loot_table, difficulty=3, description=dragonfly_description, floor_range=dragonfly_floor_range, spells=dragonfly_spells, spell_probabilities=dragonfly_spell_probabilities, initial_stats=dragonfly_initial_stats)

basilisk_stats = {
    "HP": 100,  # Define HP attribute for Basilisk
    "Damage": 40,  # Define damage attribute for Basilisk
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 12,
    "Constitution": 16,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Poison"  # Define elemental attribute of the Basilisk's attack
}
basilisk_gear = ["Venomous Fangs", "Scale Armor"]
basilisk_loot_table = ["Gold", "Basilisk Scale", "Basilisk Eye"]
basilisk_description = "Basilisks are fearsome reptilian creatures with the ability to petrify their prey with a single gaze. Their sharp claws and venomous bite make them deadly adversaries, striking fear into the hearts of even the most seasoned adventurers."
basilisk_floor_range = (8, 15)
basilisk_spells = ["Petrifying Gaze"]
basilisk_spell_probabilities = {"Petrifying Gaze": 1} 
basilisk_initial_stats = basilisk_stats.copy() # Make a copy of the initial stats
basilisk = Monster("Basilisk", basilisk_stats, basilisk_gear, basilisk_loot_table, difficulty=8, description=basilisk_description, floor_range=basilisk_floor_range, spells=basilisk_spells, spell_probabilities=basilisk_spell_probabilities, initial_stats=basilisk_initial_stats)

minotaur_stats = {
    "HP": 150,  # Define HP attribute for Minotaur
    "Damage": 50,  # Define damage attribute for Minotaur
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 25,
    "Dexterity": 12,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Minotaur's attack
}
minotaur_gear = ["Bull's Horns", "Thick Hide Armor"]
minotaur_loot_table = ["Gold", "Minotaur Horn", "Minotaur Hide"]
minotaur_description = "Minotaurs are towering beasts with the head of a bull and the body of a muscular humanoid. They are fierce combatants, wielding massive axes with deadly precision. Their ferocity in battle is matched only by their insatiable thirst for glory."
minotaur_floor_range = (15, 30)
minotaur_spells = []
minotaur_spell_probabilities = {}
minotaur_initial_stats = minotaur_stats.copy() # Make a copy of the initial stats
minotaur = Monster("Minotaur", minotaur_stats, minotaur_gear, minotaur_loot_table, difficulty=15, description=minotaur_description, floor_range=minotaur_floor_range, spells=minotaur_spells, spell_probabilities=minotaur_spell_probabilities, initial_stats=minotaur_initial_stats)

crocodile_stats = {
    "HP": 130,  # Define HP attribute for Crocodile
    "Damage": 45,  # Define damage attribute for Crocodile
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 22,
    "Dexterity": 14,
    "Constitution": 20,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Water"  # Define elemental attribute of the Crocodile's attack
}
crocodile_gear = ["Razor-sharp Teeth", "Tough Scales"]
crocodile_loot_table = ["Gold", "Crocodile Tooth", "Crocodile Hide"]
crocodile_description = "Crocodiles are fearsome reptiles that lurk in murky swamps and rivers, waiting patiently to ambush their prey. With powerful jaws and a deadly death roll, they are formidable predators capable of taking down even the largest of creatures."
crocodile_floor_range = (10, 20)
crocodile_spells = []
crocodile_spell_probabilities = {}
crocodile_initial_stats = crocodile_stats.copy() # Make a copy of the initial stats
crocodile = Monster("Crocodile", crocodile_stats, crocodile_gear, crocodile_loot_table, difficulty=10, description=crocodile_description, floor_range=crocodile_floor_range, spells=crocodile_spells, spell_probabilities=crocodile_spell_probabilities, initial_stats=crocodile_initial_stats)

hydra_stats = {
    "HP": 250,  # Define HP attribute for Hydra
    "Damage": 70,  # Define damage attribute for Hydra
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 25,
    "Dexterity": 18,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Hydra's attack
}
hydra_gear = ["Razor-sharp Fangs", "Tough Scales"]
hydra_loot_table = ["Gold", "Hydra Scale", "Venomous Fang"]
hydra_description = "Hydras are monstrous serpents with multiple heads, each capable of regenerating if severed. They lurk in swamps and marshes, ambushing unsuspecting prey with lightning-fast strikes and toxic venom. Their resilience and adaptability make them a fearsome adversary, as each head grows back stronger than before."
hydra_floor_range = (50, 100)
hydra_spells = ["Toxic Spray", "Regeneration"]
hydra_spell_probabilities = {"Toxic Spray": 0.6, "Regeneration": 0.4} 
hydra_initial_stats = hydra_stats.copy() # Make a copy of the initial stats
hydra = Monster("Hydra", hydra_stats, hydra_gear, hydra_loot_table, difficulty=50, description=hydra_description, floor_range=hydra_floor_range, spells=hydra_spells, spell_probabilities=hydra_spell_probabilities, initial_stats=hydra_initial_stats)

lizardman_stats = {
    "HP": 140,  # Define HP attribute for Lizard Man
    "Damage": 45,  # Define damage attribute for Lizard Man
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Lizard Man's attack
}
lizardman_gear = ["Serrated Spear", "Scaled Armor"]
lizardman_loot_table = ["Gold", "Lizard Scale", "Spearhead"]
lizardman_description = "Lizard Men are humanoid reptiles, skilled hunters and warriors native to swamps and jungles. They are agile and cunning, using their sharp claws and teeth to tear through enemies and their keen senses to track prey. Their thick scales provide natural armor, making them formidable opponents in combat."
lizardman_floor_range = (15, 25)
lizardman_spells = []
lizardman_spell_probabilities = {}
lizardman_initial_stats = lizardman_stats.copy() # Make a copy of the initial stats
lizardman = Monster("Lizard Man", lizardman_stats, lizardman_gear, lizardman_loot_table, difficulty=15, description=lizardman_description, floor_range=lizardman_floor_range, spells=lizardman_spells, spell_probabilities=lizardman_spell_probabilities, initial_stats=lizardman_initial_stats)

naga_stats = {
    "HP": 300,  # Define HP attribute for Naga
    "Damage": 90,  # Define damage attribute for Naga
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 26,
    "Dexterity": 22,
    "Constitution": 28,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 14,
    "Element": "Water"  # Define elemental attribute of the Naga's attack
}
naga_gear = ["Enchanted Trident", "Scale Mail"]
naga_loot_table = ["Gold", "Naga Scale", "Aquamarine"]
naga_description = "Nagas are serpentine creatures that dwell in the depths of lakes and rivers, commanding the power of water with mastery. With their enchanted tridents and agile movements, they are formidable foes both on land and in the water. Known for their cunning and deceit, they lure unsuspecting victims into their domain with promises of treasure, only to strike with deadly precision."
naga_floor_range = (80, 160)
naga_spells = []
naga_spell_probabilities = {}
naga_initial_stats = naga_stats.copy() # Make a copy of the initial stats
naga = Monster("Naga", naga_stats, naga_gear, naga_loot_table, difficulty=80, description=naga_description, floor_range=naga_floor_range, spells=naga_spells, spell_probabilities=naga_spell_probabilities, initial_stats=naga_initial_stats)

redcap_stats = {
    "HP": 140,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
redcap_gear = ["Wicked Sickle", "Redcap Hat"]
redcap_loot_table = ["Gold", "Bloody Boot", "Red Dye"]
redcap_description = "Redcaps are malevolent creatures known for their bloodlust and cruelty. They dwell in dark forests and wear red caps stained with the blood of their victims. Armed with sharp sickles, they delight in hunting and tormenting unwary travelers."
redcap_floor_range = (80, 160)
redcap_spells = []
redcap_spell_probabilities = {}
redcap_initial_stats = redcap_stats.copy()
redcap = Monster("Redcap", redcap_stats, redcap_gear, redcap_loot_table, difficulty=80, description=redcap_description, floor_range=redcap_floor_range, spells=redcap_spells, spell_probabilities=redcap_spell_probabilities, initial_stats=redcap_initial_stats)

sahuagin_glow_priest_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 22,
    "Wisdom": 24,
    "Charisma": 16,
    "Element": "Water"
}
sahuagin_glow_priest_gear = ["Trident of the Depths", "Bioluminescent Robes"]
sahuagin_glow_priest_loot_table = ["Gold", "Glowing Coral", "Oceanic Pearl"]
sahuagin_glow_priest_description = "Sahuagin Glow Priests are revered shamans among their kind, channeling the power of the ocean depths to command water and light. They are surrounded by an aura of bioluminescence, illuminating the darkness of the underwater caverns."
sahuagin_glow_priest_floor_range = (100, 200)
sahuagin_glow_priest_spells = ["Water Jet", "Glowing Shield", "Tidal Surge"]
sahuagin_glow_priest_spell_probabilities = {"Water Jet": 0.4, "Glowing Shield": 0.3, "Tidal Surge": 0.3}
sahuagin_glow_priest_initial_stats = sahuagin_glow_priest_stats.copy()
sahuagin_glow_priest = Monster("Sahuagin Glow Priest", sahuagin_glow_priest_stats, sahuagin_glow_priest_gear, sahuagin_glow_priest_loot_table, difficulty=100, description=sahuagin_glow_priest_description, floor_range=sahuagin_glow_priest_floor_range, spells=sahuagin_glow_priest_spells, spell_probabilities=sahuagin_glow_priest_spell_probabilities, initial_stats=sahuagin_glow_priest_initial_stats)

sahuagin_warrior_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 22,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Water"
}
sahuagin_warrior_gear = ["Barbed Trident", "Seaweed Armor"]
sahuagin_warrior_loot_table = ["Gold", "Sahuagin Scale", "Aquatic Pearl"]
sahuagin_warrior_description = "Sahuagin Warriors are formidable fighters that patrol the ocean depths, guarding their territory with relentless ferocity. They are armed with barbed tridents and wear armor crafted from seaweed and aquatic materials."
sahuagin_warrior_floor_range = (100, 200)
sahuagin_warrior_spells = []
sahuagin_warrior_spell_probabilities = {}
sahuagin_warrior_initial_stats = sahuagin_warrior_stats.copy()
sahuagin_warrior = Monster("Sahuagin Warrior", sahuagin_warrior_stats, sahuagin_warrior_gear, sahuagin_warrior_loot_table, difficulty=100, description=sahuagin_warrior_description, floor_range=sahuagin_warrior_floor_range, spells=sahuagin_warrior_spells, spell_probabilities=sahuagin_warrior_spell_probabilities, initial_stats=sahuagin_warrior_initial_stats)

sahuagin_trident_master_stats = {
    "HP": 240,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 24,
    "Dexterity": 20,
    "Constitution": 26,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Water"
}
sahuagin_trident_master_gear = ["Mastercrafted Trident", "Aquatic Plate"]
sahuagin_trident_master_loot_table = ["Gold", "Sahuagin Fang", "Trident Shard"]
sahuagin_trident_master_description = "Sahuagin Trident-Masters are elite warriors among their kind, wielding their tridents with deadly precision. They are skilled in both offense and defense, making them formidable adversaries in the underwater realms."
sahuagin_trident_master_floor_range = (120, 240)
sahuagin_trident_master_spells = []
sahuagin_trident_master_spell_probabilities = {}
sahuagin_trident_master_initial_stats = sahuagin_trident_master_stats.copy()
sahuagin_trident_master = Monster("Sahuagin Trident-Master", sahuagin_trident_master_stats, sahuagin_trident_master_gear, sahuagin_trident_master_loot_table, difficulty=120, description=sahuagin_trident_master_description, floor_range=sahuagin_trident_master_floor_range, spells=sahuagin_trident_master_spells, spell_probabilities=sahuagin_trident_master_spell_probabilities, initial_stats=sahuagin_trident_master_initial_stats)

swaysong_naga_stats = {
    "HP": 260,
    "Damage": 60,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 22,
    "Dexterity": 26,
    "Constitution": 24,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Water"
}
swaysong_naga_gear = ["Serpentine Staff", "Enchanted Scales"]
swaysong_naga_loot_table = ["Gold", "Melodic Conch", "Siren's Scale"]
swaysong_naga_description = "Swaysong Nagas are enchanting creatures that lure sailors to their doom with their mesmerizing melodies. They command the power of water and magic, using their songs to manipulate the currents and control the tides."
swaysong_naga_floor_range = (150, 300)
swaysong_naga_spells = ["Siren's Lullaby", "Tidal Wave", "Aquatic Melody"]
swaysong_naga_spell_probabilities = {"Siren's Lullaby": 0.4, "Tidal Wave": 0.3, "Aquatic Melody": 0.3}
swaysong_naga_initial_stats = swaysong_naga_stats.copy()
swaysong_naga = Monster("Swaysong Naga", swaysong_naga_stats, swaysong_naga_gear, swaysong_naga_loot_table, difficulty=150, description=swaysong_naga_description, floor_range=swaysong_naga_floor_range, spells=swaysong_naga_spells, spell_probabilities=swaysong_naga_spell_probabilities, initial_stats=swaysong_naga_initial_stats)

sparkscale_naga_stats = {
    "HP": 320,
    "Damage": 65,
    "Defense": 40,
    "Magic Defense": 45,
    "Strength": 28,
    "Dexterity": 26,
    "Constitution": 24,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 24,
    "Element": "Electric"
}
sparkscale_naga_gear = ["Thunderbolt Trident", "Sparkscale Armor"]
sparkscale_naga_loot_table = ["Gold", "Naga Scale", "Electric Essence"]
sparkscale_naga_description = "Sparkscale Nagas are fearsome serpent warriors who harness the power of electricity in battle. They wield tridents crackling with lightning and wear armor crafted from the scales of electrically-charged serpents."
sparkscale_naga_floor_range = (90, 180)
sparkscale_naga_spells = ["Electric Shock", "Chain Lightning", "Thunderous Roar"]
sparkscale_naga_spell_probabilities = {"Electric Shock": 0.4, "Chain Lightning": 0.3, "Thunderous Roar": 0.3}
sparkscale_naga_initial_stats = sparkscale_naga_stats.copy()
sparkscale_naga = Monster("Sparkscale Naga", sparkscale_naga_stats, sparkscale_naga_gear, sparkscale_naga_loot_table, difficulty=90, description=sparkscale_naga_description, floor_range=sparkscale_naga_floor_range, spells=sparkscale_naga_spells, spell_probabilities=sparkscale_naga_spell_probabilities, initial_stats=sparkscale_naga_initial_stats)

sahuagin_mutant_stats = {
    "HP": 300,
    "Damage": 65,
    "Defense": 45,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 28,
    "Constitution": 26,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Water"
}
sahuagin_mutant_gear = ["Mutated Trident", "Toxic Slime Coating"]
sahuagin_mutant_loot_table = ["Gold", "Mutant Scale", "Toxic Essence"]
sahuagin_mutant_description = "Sahuagin Mutants are grotesque hybrids created through twisted experiments. They possess mutated features and secrete toxic slime, making them formidable adversaries in both land and water."
sahuagin_mutant_floor_range = (80, 160)
sahuagin_mutant_spells = ["Toxic Barrage", "Aqua Surge", "Mutagenic Burst"]
sahuagin_mutant_spell_probabilities = {"Toxic Barrage": 0.4, "Aqua Surge": 0.3, "Mutagenic Burst": 0.3}
sahuagin_mutant_initial_stats = sahuagin_mutant_stats.copy()
sahuagin_mutant = Monster("Sahuagin Mutant", sahuagin_mutant_stats, sahuagin_mutant_gear, sahuagin_mutant_loot_table, difficulty=80, description=sahuagin_mutant_description, floor_range=sahuagin_mutant_floor_range, spells=sahuagin_mutant_spells, spell_probabilities=sahuagin_mutant_spell_probabilities, initial_stats=sahuagin_mutant_initial_stats)

manafang_naga_stats = {
    "HP": 300,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 28,
    "Dexterity": 30,
    "Constitution": 26,
    "Intelligence": 24,
    "Wisdom": 26,
    "Charisma": 22,
    "Element": "Water"
}
manafang_naga_gear = ["Serpentine Trident", "Abyssal Robes"]
manafang_naga_loot_table = ["Gold", "Manafang Fang", "Arcane Coral"]
manafang_naga_description = "Manafang Nagas are guardians of the mystical waters, wielding tridents infused with arcane energy. They are adorned with abyssal robes that shimmer with otherworldly power."
manafang_naga_floor_range = (80, 160)
manafang_naga_spells = ["Aqua Sphere", "Arcane Torrent", "Tidal Surge"]
manafang_naga_spell_probabilities = {"Aqua Sphere": 0.4, "Arcane Torrent": 0.3, "Tidal Surge": 0.3}
manafang_naga_initial_stats = manafang_naga_stats.copy()
manafang_naga = Monster("Manafang Naga", manafang_naga_stats, manafang_naga_gear, manafang_naga_loot_table, difficulty=80, description=manafang_naga_description, floor_range=manafang_naga_floor_range, spells=manafang_naga_spells, spell_probabilities=manafang_naga_spell_probabilities, initial_stats=manafang_naga_initial_stats)

elder_swaysong_naga_stats = {
    "HP": 400,
    "Damage": 75,
    "Defense": 55,
    "Magic Defense": 60,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 32,
    "Intelligence": 30,
    "Wisdom": 35,
    "Charisma": 30,
    "Element": "Water"
}
elder_swaysong_naga_gear = ["Ancient Trident", "Siren's Mantle"]
elder_swaysong_naga_loot_table = ["Gold", "Elder Scales", "Melodic Gem"]
elder_swaysong_naga_description = "Elder Swaysong Nagas are revered guardians of the ocean depths, wielding ancient tridents imbued with mystical melodies. Their enchanting songs lure sailors to their doom while their powerful strikes crush their foes."
elder_swaysong_naga_floor_range = (100, 200)
elder_swaysong_naga_spells = ["Siren's Lament", "Tidal Harmony", "Oceanic Fury"]
elder_swaysong_naga_spell_probabilities = {"Siren's Lament": 0.4, "Tidal Harmony": 0.3, "Oceanic Fury": 0.3}
elder_swaysong_naga_initial_stats = elder_swaysong_naga_stats.copy()
elder_swaysong_naga = Monster("Elder Swaysong Naga", elder_swaysong_naga_stats, elder_swaysong_naga_gear, elder_swaysong_naga_loot_table, difficulty=100, description=elder_swaysong_naga_description, floor_range=elder_swaysong_naga_floor_range, spells=elder_swaysong_naga_spells, spell_probabilities=elder_swaysong_naga_spell_probabilities, initial_stats=elder_swaysong_naga_initial_stats)

siren_stats = {
    "HP": 280,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 45,
    "Strength": 20,
    "Dexterity": 35,
    "Constitution": 28,
    "Intelligence": 30,
    "Wisdom": 32,
    "Charisma": 38,
    "Element": "Water"
}
siren_gear = ["Enchanted Harp", "Seashell Necklace"]
siren_loot_table = ["Gold", "Siren Song Crystal", "Pearl Necklace"]
siren_description = "Sirens are enchanting creatures that lure sailors to their doom with their mesmerizing songs. They wield enchanted harps and seashell necklaces, using their charisma to captivate their victims."
siren_floor_range = (80, 160)
siren_spells = ["Siren's Song", "Aqua Blast", "Tidal Wave"]
siren_spell_probabilities = {"Siren's Song": 0.4, "Aqua Blast": 0.3, "Tidal Wave": 0.3}
siren_initial_stats = siren_stats.copy()
siren = Monster("Siren", siren_stats, siren_gear, siren_loot_table, difficulty=80, description=siren_description, floor_range=siren_floor_range, spells=siren_spells, spell_probabilities=siren_spell_probabilities, initial_stats=siren_initial_stats)

water_elemental_stats = {
    "HP": 150,  # Define HP attribute for Water Elemental
    "Damage": 50,  # Define damage attribute for Water Elemental
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Water"  # Define elemental attribute of the Water Elemental's attack
}
water_elemental_gear = ["Watery Form", "Aqua Shield"]
water_elemental_loot_table = ["Gold", "Water Essence", "Aquamarine"]
water_elemental_description = "Water Elementals are beings of pure water summoned from the depths of the ocean. They wield the power of the tides, unleashing devastating waves and torrents upon their foes. Their liquid form makes them difficult to damage, and they can reform from even the smallest droplets."
water_elemental_floor_range = (20, 40)
water_elemental_spells = ["Aqua Jet", "Tidal Wave"]
water_elemental_spell_probabilities = {"Aqua Jet": 0.6, "Tidal Wave": 0.4} 
water_elemental_initial_stats = water_elemental_stats.copy() # Make a copy of the initial stats
water_elemental = Monster("Water Elemental", water_elemental_stats, water_elemental_gear, water_elemental_loot_table, difficulty=20, description=water_elemental_description, floor_range=water_elemental_floor_range, spells=water_elemental_spells, spell_probabilities=water_elemental_spell_probabilities, initial_stats=water_elemental_initial_stats)

redcap_grimsnap_stats = {
    "HP": 60,
    "Damage": 15,
    "Defense": 10,
    "Magic Defense": 8,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 10,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Dark"
}
redcap_grimsnap_gear = ["Grim Blade", "Tattered Hood"]
redcap_grimsnap_loot_table = ["Gold", "Redcap Tooth", "Torn Cloak"]
redcap_grimsnap_description = "Redcap Grimsnaps are vicious little creatures, their sharp teeth and malevolent grins striking fear into the hearts of travelers."
redcap_grimsnap_floor_range = (1, 3)
redcap_grimsnap_spells = ["Shadow Leap"]
redcap_grimsnap_spell_probabilities = {"Shadow Leap": 1.0}
redcap_grimsnap_initial_stats = redcap_grimsnap_stats.copy()
redcap_grimsnap = Monster("Redcap Grimsnap", redcap_grimsnap_stats, redcap_grimsnap_gear, redcap_grimsnap_loot_table, difficulty=1, description=redcap_grimsnap_description, floor_range=redcap_grimsnap_floor_range, spells=redcap_grimsnap_spells, spell_probabilities=redcap_grimsnap_spell_probabilities, initial_stats=redcap_grimsnap_initial_stats)

redcap_vilegrin_stats = {
    "HP": 65,
    "Damage": 14,
    "Defense": 11,
    "Magic Defense": 9,
    "Strength": 11,
    "Dexterity": 15,
    "Constitution": 11,
    "Intelligence": 9,
    "Wisdom": 11,
    "Charisma": 7,
    "Element": "Dark"
}
redcap_vilegrin_gear = ["Vile Dagger", "Wicked Smile"]
redcap_vilegrin_loot_table = ["Gold", "Redcap Grin", "Tainted Garb"]
redcap_vilegrin_description = "Redcap Vilegrins are known for their cruel laughter and sinister intentions, reveling in the misery they cause to unsuspecting wanderers."
redcap_vilegrin_floor_range = (1, 3)
redcap_vilegrin_spells = ["Shadow Step"]
redcap_vilegrin_spell_probabilities = {"Shadow Step": 1.0}
redcap_vilegrin_initial_stats = redcap_vilegrin_stats.copy()
redcap_vilegrin = Monster("Redcap Vilegrin", redcap_vilegrin_stats, redcap_vilegrin_gear, redcap_vilegrin_loot_table, difficulty=1, description=redcap_vilegrin_description, floor_range=redcap_vilegrin_floor_range, spells=redcap_vilegrin_spells, spell_probabilities=redcap_vilegrin_spell_probabilities, initial_stats=redcap_vilegrin_initial_stats)

redcap_shadowtooth_stats = {
    "HP": 70,
    "Damage": 16,
    "Defense": 12,
    "Magic Defense": 10,
    "Strength": 13,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Shadow"
}
redcap_shadowtooth_gear = ["Shadow Blade", "Tooth Necklace"]
redcap_shadowtooth_loot_table = ["Gold", "Redcap Claw", "Dark Cloak"]
redcap_shadowtooth_description = "Redcap Shadowtooths lurk in the darkness, their sharp teeth and cunning nature making them deadly adversaries to any who cross their path."
redcap_shadowtooth_floor_range = (1, 3)
redcap_shadowtooth_spells = ["Shadow Slash"]
redcap_shadowtooth_spell_probabilities = {"Shadow Slash": 1.0}
redcap_shadowtooth_initial_stats = redcap_shadowtooth_stats.copy()
redcap_shadowtooth = Monster("Redcap Shadowtooth", redcap_shadowtooth_stats, redcap_shadowtooth_gear, redcap_shadowtooth_loot_table, difficulty=1, description=redcap_shadowtooth_description, floor_range=redcap_shadowtooth_floor_range, spells=redcap_shadowtooth_spells, spell_probabilities=redcap_shadowtooth_spell_probabilities, initial_stats=redcap_shadowtooth_initial_stats)

redcap_bloodclaw_stats = {
    "HP": 75,
    "Damage": 17,
    "Defense": 13,
    "Magic Defense": 11,
    "Strength": 14,
    "Dexterity": 17,
    "Constitution": 13,
    "Intelligence": 11,
    "Wisdom": 13,
    "Charisma": 9,
    "Element": "Dark"
}
redcap_bloodclaw_gear = ["Bloodied Dagger", "Clawed Gauntlets"]
redcap_bloodclaw_loot_table = ["Gold", "Redcap Fang", "Bloody Tunic"]
redcap_bloodclaw_description = "Redcap Bloodclaws are ferocious fighters, their razor-sharp claws dripping with the blood of their victims as they roam the forests in search of fresh prey."
redcap_bloodclaw_floor_range = (1, 3)
redcap_bloodclaw_spells = ["Bloodlust"]
redcap_bloodclaw_spell_probabilities = {"Bloodlust": 1.0}
redcap_bloodclaw_initial_stats = redcap_bloodclaw_stats.copy()
redcap_bloodclaw = Monster("Redcap Bloodclaw", redcap_bloodclaw_stats, redcap_bloodclaw_gear, redcap_bloodclaw_loot_table, difficulty=1, description=redcap_bloodclaw_description, floor_range=redcap_bloodclaw_floor_range, spells=redcap_bloodclaw_spells, spell_probabilities=redcap_bloodclaw_spell_probabilities, initial_stats=redcap_bloodclaw_initial_stats)

redcap_grimlaugh_stats = {
    "HP": 80,
    "Damage": 18,
    "Defense": 14,
    "Magic Defense": 12,
    "Strength": 15,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Dark"
}
redcap_grimlaugh_gear = ["Grim Laughing Blade", "Gnarled Staff"]
redcap_grimlaugh_loot_table = ["Gold", "Redcap Grin", "Cursed Charm"]
redcap_grimlaugh_description = "Redcap Grimlaughs are known for their sinister cackles and wicked sense of humor, often luring unsuspecting travelers into their traps with promises of treasure."
redcap_grimlaugh_floor_range = (1, 3)
redcap_grimlaugh_spells = ["Cackle of Madness"]
redcap_grimlaugh_spell_probabilities = {"Cackle of Madness": 1.0}
redcap_grimlaugh_initial_stats = redcap_grimlaugh_stats.copy()
redcap_grimlaugh = Monster("Redcap Grimlaugh", redcap_grimlaugh_stats, redcap_grimlaugh_gear, redcap_grimlaugh_loot_table, difficulty=1, description=redcap_grimlaugh_description, floor_range=redcap_grimlaugh_floor_range, spells=redcap_grimlaugh_spells, spell_probabilities=redcap_grimlaugh_spell_probabilities, initial_stats=redcap_grimlaugh_initial_stats)

redcap_fangsnarl_stats = {
    "HP": 85,
    "Damage": 19,
    "Defense": 15,
    "Magic Defense": 13,
    "Strength": 16,
    "Dexterity": 19,
    "Constitution": 15,
    "Intelligence": 13,
    "Wisdom": 15,
    "Charisma": 11,
    "Element": "Dark"
}
redcap_fangsnarl_gear = ["Snarling Fangs", "Twisted Horns"]
redcap_fangsnarl_loot_table = ["Gold", "Redcap Fang", "Tattered Mantle"]
redcap_fangsnarl_description = "Redcap Fangsnarls are relentless hunters, their savage snarls and razor-sharp teeth striking fear into the hearts of those who dare to enter their territory."
redcap_fangsnarl_floor_range = (1, 3)
redcap_fangsnarl_spells = ["Ferocious Assault"]
redcap_fangsnarl_spell_probabilities = {"Ferocious Assault": 1.0}
redcap_fangsnarl_initial_stats = redcap_fangsnarl_stats.copy()
redcap_fangsnarl = Monster("Redcap Fangsnarl", redcap_fangsnarl_stats, redcap_fangsnarl_gear, redcap_fangsnarl_loot_table, difficulty=1, description=redcap_fangsnarl_description, floor_range=redcap_fangsnarl_floor_range, spells=redcap_fangsnarl_spells, spell_probabilities=redcap_fangsnarl_spell_probabilities, initial_stats=redcap_fangsnarl_initial_stats)

redcap_dreadsmir_stats = {
    "HP": 90,
    "Damage": 20,
    "Defense": 16,
    "Magic Defense": 14,
    "Strength": 17,
    "Dexterity": 20,
    "Constitution": 16,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Dark"
}
redcap_dreadsmir_gear = ["Dreadful Blade", "Cursed Amulet"]
redcap_dreadsmir_loot_table = ["Gold", "Redcap Dread", "Tattered Hood"]
redcap_dreadsmir_description = "Redcap Dreadsmirs are the most feared among their kind, their relentless pursuit of their prey and their eerie presence striking terror into the hearts of even the bravest adventurers."
redcap_dreadsmir_floor_range = (1, 3)
redcap_dreadsmir_spells = ["Dreadful Howl"]
redcap_dreadsmir_spell_probabilities = {"Dreadful Howl": 1.0}
redcap_dreadsmir_initial_stats = redcap_dreadsmir_stats.copy()
redcap_dreadsmir = Monster("Redcap Dreadsmir", redcap_dreadsmir_stats, redcap_dreadsmir_gear, redcap_dreadsmir_loot_table, difficulty=1, description=redcap_dreadsmir_description, floor_range=redcap_dreadsmir_floor_range, spells=redcap_dreadsmir_spells, spell_probabilities=redcap_dreadsmir_spell_probabilities, initial_stats=redcap_dreadsmir_initial_stats)

gelatinous_glutton_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 10,
    "Constitution": 22,
    "Intelligence": 5,
    "Wisdom": 8,
    "Charisma": 5,
    "Element": "Acid"
}
gelatinous_glutton_gear = ["Acidic Pseudopods", "Dissolving Membrane"]
gelatinous_glutton_loot_table = ["Gold", "Slime Core", "Corroded Armor"]
gelatinous_glutton_description = "The Gelatinous Glutton is a massive blob of acidic slime, its insatiable appetite dissolving anything unfortunate enough to come into contact with it."
gelatinous_glutton_floor_range = (6, 8)
gelatinous_glutton_spells = ["Acidic Barrage", "Engulf"]
gelatinous_glutton_spell_probabilities = {"Acidic Barrage": 0.7, "Engulf": 0.3}
gelatinous_glutton_initial_stats = gelatinous_glutton_stats.copy()
gelatinous_glutton = Monster("Gelatinous Glutton", gelatinous_glutton_stats, gelatinous_glutton_gear, gelatinous_glutton_loot_table, difficulty=6, description=gelatinous_glutton_description, floor_range=gelatinous_glutton_floor_range, spells=gelatinous_glutton_spells, spell_probabilities=gelatinous_glutton_spell_probabilities, initial_stats=gelatinous_glutton_initial_stats)

blobby_behemoth_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 5,
    "Constitution": 25,
    "Intelligence": 5,
    "Wisdom": 10,
    "Charisma": 5,
    "Element": "Slime"
}
blobby_behemoth_gear = ["Amorphous Appendages", "Sticky Residue"]
blobby_behemoth_loot_table = ["Gold", "Slime Essence", "Corrupted Gem"]
blobby_behemoth_description = "The Blobby Behemoth is a colossal mass of slime, its gelatinous form undulating and shifting as it moves, leaving a trail of sticky residue in its wake."
blobby_behemoth_floor_range = (8, 10)
blobby_behemoth_spells = ["Slime Wave", "Engulfing Strike"]
blobby_behemoth_spell_probabilities = {"Slime Wave": 0.6, "Engulfing Strike": 0.4}
blobby_behemoth_initial_stats = blobby_behemoth_stats.copy()
blobby_behemoth = Monster("Blobby Behemoth", blobby_behemoth_stats, blobby_behemoth_gear, blobby_behemoth_loot_table, difficulty=8, description=blobby_behemoth_description, floor_range=blobby_behemoth_floor_range, spells=blobby_behemoth_spells, spell_probabilities=blobby_behemoth_spell_probabilities, initial_stats=blobby_behemoth_initial_stats)

quagmire_marauder_stats = {
    "HP": 100,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "Water"
}
quagmire_marauder_gear = ["Quagmire Scales", "Mud-crusted Teeth"]
quagmire_marauder_loot_table = ["Gold", "Quagmire Pearl", "Bogweed Necklace"]
quagmire_marauder_description = "The Quagmire Marauder is a formidable predator that lurks in the murky depths of the swamp, its massive jaws capable of tearing through anything that crosses its path."
quagmire_marauder_floor_range = (7, 9)
quagmire_marauder_spells = ["Mudslide", "Aqua Assault"]
quagmire_marauder_spell_probabilities = {"Mudslide": 0.7, "Aqua Assault": 0.3}
quagmire_marauder_initial_stats = quagmire_marauder_stats.copy()
quagmire_marauder = Monster("Quagmire Marauder", quagmire_marauder_stats, quagmire_marauder_gear, quagmire_marauder_loot_table, difficulty=7, description=quagmire_marauder_description, floor_range=quagmire_marauder_floor_range, spells=quagmire_marauder_spells, spell_probabilities=quagmire_marauder_spell_probabilities, initial_stats=quagmire_marauder_initial_stats)

sludgegill_predator_stats = {
    "HP": 120,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 25,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Water"
}
sludgegill_predator_gear = ["Sludgegill Scales", "Toxic Fangs"]
sludgegill_predator_loot_table = ["Gold", "Sludgegill Eye", "Putrid Scale"]
sludgegill_predator_description = "The Sludgegill Predator is a fearsome hunter that prowls the fetid waters of the swamp, its slimy scales blending seamlessly with the murky environment as it stalks its prey."
sludgegill_predator_floor_range = (8, 10)
sludgegill_predator_spells = ["Toxic Wave", "Venomous Strike"]
sludgegill_predator_spell_probabilities = {"Toxic Wave": 0.6, "Venomous Strike": 0.4}
sludgegill_predator_initial_stats = sludgegill_predator_stats.copy()
sludgegill_predator = Monster("Sludgegill Predator", sludgegill_predator_stats, sludgegill_predator_gear, sludgegill_predator_loot_table, difficulty=8, description=sludgegill_predator_description, floor_range=sludgegill_predator_floor_range, spells=sludgegill_predator_spells, spell_probabilities=sludgegill_predator_spell_probabilities, initial_stats=sludgegill_predator_initial_stats)

hag_stats = {
    "HP": 240,  # Define HP attribute for Hag
    "Damage": 70,  # Define damage attribute for Hag
    "Defense": 45,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 22,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 20,
    "Element": "Dark"  # Define elemental attribute of the Hag's attack
}
hag_gear = ["Cursed Staff", "Tattered Robes"]
hag_loot_table = ["Gold", "Hag's Eye", "Cursed Talisman"]
hag_description = "Hags are malevolent witches with a knack for dark magic and deceit. They lurk in shadowy swamps and haunted forests, luring unsuspecting travelers into their clutches with promises of power and fortune. With their cursed staffs and wicked spells, they ensnare their victims in their web of deception, feasting on their souls to sustain their unnaturally long lives."
hag_floor_range = (60, 120)
hag_spells = ["Hex", "Dark Pact"]
hag_spell_probabilities = {"Hex": 0.7, "Dark Pact": 0.3} 
hag_initial_stats = hag_stats.copy() # Make a copy of the initial stats
hag = Monster("Hag", hag_stats, hag_gear, hag_loot_table, difficulty=60, description=hag_description, floor_range=hag_floor_range, spells=hag_spells, spell_probabilities=hag_spell_probabilities, initial_stats=hag_initial_stats)

spider_golem_stats = {
    "HP": 250,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 50,
    "Dexterity": 40,
    "Constitution": 60,
    "Intelligence": 20,
    "Wisdom": 30,
    "Charisma": 10,
    "Element": "Earth"
}
spider_golem_gear = ["Steel Exoskeleton", "Venomous Fangs"]
spider_golem_loot_table = ["Gold", "Spider Golem Core", "Webbed Silk"]
spider_golem_description = "The Spider Golem is a formidable construct crafted in the likeness of a giant arachnid, its mechanical limbs and venomous fangs making it a terrifying opponent on the battlefield."
spider_golem_floor_range = (12, 14)
spider_golem_spells = ["Web Shot", "Venomous Bite"]
spider_golem_spell_probabilities = {"Web Shot": 0.6, "Venomous Bite": 0.4}
spider_golem_initial_stats = spider_golem_stats.copy()
spider_golem = Monster("Spider Golem", spider_golem_stats, spider_golem_gear, spider_golem_loot_table, difficulty=12, description=spider_golem_description, floor_range=spider_golem_floor_range, spells=spider_golem_spells, spell_probabilities=spider_golem_spell_probabilities, initial_stats=spider_golem_initial_stats)

hangman_tree_stats = {
    "HP": 300,
    "Damage": 70,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 60,
    "Dexterity": 30,
    "Constitution": 70,
    "Intelligence": 20,
    "Wisdom": 40,
    "Charisma": 10,
    "Element": "Nature"
}
hangman_tree_gear = ["Twisted Branches", "Noose Vines"]
hangman_tree_loot_table = ["Gold", "Hangman's Bark", "Entangled Rope"]
hangman_tree_description = "The Hangman Tree is a malevolent tree-like creature with twisted branches that resemble hangman's nooses, its eerie presence and deadly grip striking fear into those who dare to approach."
hangman_tree_floor_range = (13, 15)
hangman_tree_spells = ["Strangle", "Grasping Roots"]
hangman_tree_spell_probabilities = {"Strangle": 0.7, "Grasping Roots": 0.3}
hangman_tree_initial_stats = hangman_tree_stats.copy()
hangman_tree = Monster("Hangman Tree", hangman_tree_stats, hangman_tree_gear, hangman_tree_loot_table, difficulty=13, description=hangman_tree_description, floor_range=hangman_tree_floor_range, spells=hangman_tree_spells, spell_probabilities=hangman_tree_spell_probabilities, initial_stats=hangman_tree_initial_stats)

giant_leech_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 30,
    "Dexterity": 40,
    "Constitution": 35,
    "Intelligence": 10,
    "Wisdom": 20,
    "Charisma": 5,
    "Element": "Water"
}
giant_leech_gear = ["Slimy Skin", "Razor Teeth"]
giant_leech_loot_table = ["Gold", "Leech Essence", "Bloated Blood"]
giant_leech_description = "The Giant Leech is a massive aquatic predator, its slimy skin and razor-sharp teeth allowing it to latch onto its prey and drain them of their life force."
giant_leech_floor_range = (8, 10)
giant_leech_spells = ["Leech Bite", "Aqua Slime"]
giant_leech_spell_probabilities = {"Leech Bite": 0.6, "Aqua Slime": 0.4}
giant_leech_initial_stats = giant_leech_stats.copy()
giant_leech = Monster("Giant Leech", giant_leech_stats, giant_leech_gear, giant_leech_loot_table, difficulty=8, description=giant_leech_description, floor_range=giant_leech_floor_range, spells=giant_leech_spells, spell_probabilities=giant_leech_spell_probabilities, initial_stats=giant_leech_initial_stats)

