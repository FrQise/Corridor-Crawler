from monsters.bestiary import Monster

cave_bat_stats = {
    "HP": 100,  # Define HP attribute for Cave Bat
    "Damage": 40,  # Define damage attribute for Cave Bat
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 10,
    "Dexterity": 30,
    "Constitution": 12,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Cave Bat's attack
}
cave_bat_gear = ["Razor-sharp Fangs", "Leathery Wings"]
cave_bat_loot_table = ["Gold", "Bat Wing", "Guano"]
cave_bat_description = "Cave Bats are nocturnal creatures that inhabit the dark recesses of the caves, navigating the labyrinthine passages with ease using their keen echolocation. With their razor-sharp fangs and leathery wings, they are skilled hunters, capable of swooping down from the shadows to snatch up unsuspecting prey. Though individually weak, they can overwhelm their enemies with sheer numbers."
cave_bat_floor_range = (1, 2)
cave_bat_spells = []
cave_bat_spell_probabilities = {}
cave_bat_initial_stats = cave_bat_stats.copy() # Make a copy of the initial stats
cave_bat = Monster("Cave Bat", cave_bat_stats, cave_bat_gear, cave_bat_loot_table, difficulty=20, description=cave_bat_description, floor_range=cave_bat_floor_range, spells=cave_bat_spells, spell_probabilities=cave_bat_spell_probabilities, initial_stats=cave_bat_initial_stats)

cave_spider_stats = {
    "HP": 120,  # Define HP attribute for Cave Spider
    "Damage": 50,  # Define damage attribute for Cave Spider
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 12,
    "Dexterity": 32,
    "Constitution": 14,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "Poison"  # Define elemental attribute of the Cave Spider's attack
}
cave_spider_gear = ["Venomous Fangs", "Silken Webbing"]
cave_spider_loot_table = ["Gold", "Spider Silk", "Venom Sac"]
cave_spider_description = "Cave Spiders are arachnid creatures that lurk in the shadows of the caves, spinning intricate webs to trap their prey. With their venomous fangs and agile movements, they are skilled hunters, capable of ambushing even the most wary adventurers. Though individually small, they can overwhelm their enemies with sheer numbers and deadly poison."
cave_spider_floor_range = (1, 2)
cave_spider_spells = []
cave_spider_spell_probabilities = {}
cave_spider_initial_stats = cave_spider_stats.copy() # Make a copy of the initial stats
cave_spider = Monster("Cave Spider", cave_spider_stats, cave_spider_gear, cave_spider_loot_table, difficulty=30, description=cave_spider_description, floor_range=cave_spider_floor_range, spells=cave_spider_spells, spell_probabilities=cave_spider_spell_probabilities, initial_stats=cave_spider_initial_stats)

luminous_lurkfish_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 20,
    "Dexterity": 28,
    "Constitution": 25,
    "Intelligence": 15,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "Water"
}

luminous_lurkfish_gear = ["Bioluminescent Scales", "Glowing Tentacles"]
luminous_lurkfish_loot_table = ["Luminous Pearl", "Aquatic Essence", "Glowing Fin"]
luminous_lurkfish_description = "Luminous Lurkfish are bioluminescent predators that inhabit underground rivers and pools. Their mesmerizing glow attracts unsuspecting prey, which they ensnare with their tentacles before devouring."
luminous_lurkfish_floor_range = (1, 3)
luminous_lurkfish_spells = []
luminous_lurkfish_spell_probabilities = {}
luminous_lurkfish_initial_stats = luminous_lurkfish_stats.copy()
luminous_lurkfish = Monster("Luminous Lurkfish", luminous_lurkfish_stats, luminous_lurkfish_gear, luminous_lurkfish_loot_table, difficulty=7, description=luminous_lurkfish_description, floor_range=luminous_lurkfish_floor_range, spells=luminous_lurkfish_spells, spell_probabilities=luminous_lurkfish_spell_probabilities, initial_stats=luminous_lurkfish_initial_stats)

darkcrawler_stats = {
    "HP": 180,  # Define HP attribute for Darkcrawler
    "Damage": 70,  # Define damage attribute for Darkcrawler
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 32,
    "Constitution": 24,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "Dark"  # Define elemental attribute of the Darkcrawler's attack
}
darkcrawler_gear = ["Sharp Mandibles", "Chitinous Carapace"]
darkcrawler_loot_table = ["Gold", "Darkcrawler Mandible", "Shadow Essence"]
darkcrawler_description = "Darkcrawlers are nocturnal arthropods that inhabit the deepest, darkest caves, navigating the subterranean passages with their keen senses and razor-sharp mandibles. With their chitinous exoskeletons and agile movements, they are skilled hunters, capable of ambushing prey in the shadows with deadly precision. Though individually small, they can overwhelm their enemies with sheer numbers and their affinity for darkness."
darkcrawler_floor_range = (2, 3)
darkcrawler_spells = []
darkcrawler_spell_probabilities = {}
darkcrawler_initial_stats = darkcrawler_stats.copy() # Make a copy of the initial stats
darkcrawler = Monster("Darkcrawler", darkcrawler_stats, darkcrawler_gear, darkcrawler_loot_table, difficulty=50, description=darkcrawler_description, floor_range=darkcrawler_floor_range, spells=darkcrawler_spells, spell_probabilities=darkcrawler_spell_probabilities, initial_stats=darkcrawler_initial_stats)

deep_gnome_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 18,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}
deep_gnome_gear = ["Underdark Blade", "Shadow Cloak"]
deep_gnome_loot_table = ["Gold", "Gemstone", "Underdark Trinket"]
deep_gnome_description = "Deep Gnomes, also known as Svirfneblin, are a subterranean race that dwell in the depths of the earth. Masters of stealth and subterfuge, they are skilled in navigating the treacherous tunnels of the Underdark and are often wary of outsiders."
deep_gnome_floor_range = (2, 3)
deep_gnome_spells = ["Darkvision"]
deep_gnome_spell_probabilities = {"Darkvision": 1}
deep_gnome_initial_stats = deep_gnome_stats.copy()
deep_gnome = Monster("Deep Gnome", deep_gnome_stats, deep_gnome_gear, deep_gnome_loot_table, difficulty=80, description=deep_gnome_description, floor_range=deep_gnome_floor_range, spells=deep_gnome_spells, spell_probabilities=deep_gnome_spell_probabilities, initial_stats=deep_gnome_initial_stats)

cave_goblin_stats = {
    "HP": 80,
    "Damage": 15,
    "Defense": 10,
    "Magic Defense": 10,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 10,
    "Intelligence": 8,
    "Wisdom": 8,
    "Charisma": 8,
    "Element": "Earth"
}
cave_goblin_gear = ["Stone Dagger", "Tattered Cave Cloth"]
cave_goblin_loot_table = ["Gold", "Cave Mushroom", "Goblin Trinket"]
cave_goblin_description = "Cave Goblins are a subterranean species of goblin that make their homes in the darkest depths of underground caverns. They are skilled scavengers and cunning hunters, using their knowledge of the caves to their advantage."
cave_goblin_floor_range = (2, 4)
cave_goblin_spells = []
cave_goblin_spell_probabilities = {}
cave_goblin_initial_stats = cave_goblin_stats.copy()
cave_goblin = Monster("Cave Goblin", cave_goblin_stats, cave_goblin_gear, cave_goblin_loot_table, difficulty=40, description=cave_goblin_description, floor_range=cave_goblin_floor_range, spells=cave_goblin_spells, spell_probabilities=cave_goblin_spell_probabilities, initial_stats=cave_goblin_initial_stats)

kobold_stats = {
    "HP": 80,  # Define HP attribute for Kobold
    "Damage": 25,  # Define damage attribute for Kobold
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 15,  # Define magic defense vs spells
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Kobold's attack
}
kobold_gear = ["Rusty Dagger", "Patchwork Armor"]
kobold_loot_table = ["Gold", "Kobold Tooth", "Shiny Trinket"]
kobold_description = "Kobolds are small, reptilian humanoids known for their cunning and resourcefulness. They inhabit underground caverns and abandoned mines, scavenging for treasure and ambushing unwary travelers. Despite their diminutive size, they are skilled trap makers and adept at coordinating ambushes to overcome larger foes."
kobold_floor_range = (2, 4)
kobold_spells = []
kobold_spell_probabilities = {}
kobold_initial_stats = kobold_stats.copy() # Make a copy of the initial stats
kobold = Monster("Kobold", kobold_stats, kobold_gear, kobold_loot_table, difficulty=10, description=kobold_description, floor_range=kobold_floor_range, spells=kobold_spells, spell_probabilities=kobold_spell_probabilities, initial_stats=kobold_initial_stats)

kobold_wizard_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 25,
    "Strength": 8,
    "Dexterity": 14,
    "Constitution": 10,
    "Intelligence": 18,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "None"
}
kobold_wizard_gear = ["Arcane Staff", "Robes of the Arcanist"]
kobold_wizard_loot_table = ["Gold", "Scroll of Fireball", "Kobold Rune"]
kobold_wizard_description = "Kobold Wizards are cunning spellcasters who wield powerful arcane magic. Despite their small stature, they are skilled in the arcane arts and can unleash devastating spells upon their enemies."
kobold_wizard_floor_range = (2, 4)
kobold_wizard_spells = ["Firebolt", "Magic Missile", "Lightning Bolt"]
kobold_wizard_spell_probabilities = {"Firebolt": 0.4, "Magic Missile": 0.3, "Lightning Bolt": 0.2}
kobold_wizard_initial_stats = kobold_wizard_stats.copy()
kobold_wizard = Monster("Kobold Wizard", kobold_wizard_stats, kobold_wizard_gear, kobold_wizard_loot_table, difficulty=80, description=kobold_wizard_description, floor_range=kobold_wizard_floor_range, spells=kobold_wizard_spells, spell_probabilities=kobold_wizard_spell_probabilities, initial_stats=kobold_wizard_initial_stats)

kobold_archer_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 10,
    "Strength": 8,
    "Dexterity": 16,
    "Constitution": 10,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"
}
kobold_archer_gear = ["Shortbow", "Leather Armor"]
kobold_archer_loot_table = ["Gold", "Arrow Bundle", "Kobold Trinket"]
kobold_archer_description = "Kobold Archers are nimble and cunning creatures skilled in the use of bows. They often serve as scouts and skirmishers for kobold warbands, picking off enemies from a distance with their accurate shots."
kobold_archer_floor_range = (2, 4)
kobold_archer_spells = []
kobold_archer_spell_probabilities = {}
kobold_archer_initial_stats = kobold_archer_stats.copy()
kobold_archer = Monster("Kobold Archer", kobold_archer_stats, kobold_archer_gear, kobold_archer_loot_table, difficulty=40, description=kobold_archer_description, floor_range=kobold_archer_floor_range, spells=kobold_archer_spells, spell_probabilities=kobold_archer_spell_probabilities, initial_stats=kobold_archer_initial_stats)

orcish_archer_stats = {
    "HP": 100,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "None"
}
orcish_archer_gear = ["Orcish Bow", "Studded Leather Armor"]
orcish_archer_loot_table = ["Gold", "Arrow Quiver", "Orcish Helm"]
orcish_archer_description = "Orcish Archers are fierce warriors of the orc tribes, skilled in the use of bows and arrows. They excel in ranged combat, raining down arrows upon their enemies with deadly accuracy."
orcish_archer_floor_range = (4, 6)
orcish_archer_spells = []
orcish_archer_spell_probabilities = {}
orcish_archer_initial_stats = orcish_archer_stats.copy()
orcish_archer = Monster("Orcish Archer", orcish_archer_stats, orcish_archer_gear, orcish_archer_loot_table, difficulty=60, description=orcish_archer_description, floor_range=orcish_archer_floor_range, spells=orcish_archer_spells, spell_probabilities=orcish_archer_spell_probabilities, initial_stats=orcish_archer_initial_stats)

kobold_bravescale_stats = {
    "HP": 140,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
kobold_bravescale_gear = ["Scaleblade", "Reinforced Scale Armor"]
kobold_bravescale_loot_table = ["Gold", "Kobold Scale", "Bravescale Helm"]
kobold_bravescale_description = "Kobold Bravescales are elite warriors among their kind, clad in sturdy scale armor and wielding razor-sharp blades. They are skilled fighters, fiercely loyal to their tribe and willing to defend their territory at any cost."
kobold_bravescale_floor_range = (4, 6)
kobold_bravescale_spells = []
kobold_bravescale_spell_probabilities = {}
kobold_bravescale_initial_stats = kobold_bravescale_stats.copy()
kobold_bravescale = Monster("Kobold Bravescale", kobold_bravescale_stats, kobold_bravescale_gear, kobold_bravescale_loot_table, difficulty=80, description=kobold_bravescale_description, floor_range=kobold_bravescale_floor_range, spells=kobold_bravescale_spells, spell_probabilities=kobold_bravescale_spell_probabilities, initial_stats=kobold_bravescale_initial_stats)

cave_squid_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 20,
    "Dexterity": 30,
    "Constitution": 28,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "None"
}
cave_squid_gear = ["Inky Tentacles", "Hardened Shell"]
cave_squid_loot_table = ["Gold", "Squid Ink", "Bioluminescent Crystal"]
cave_squid_description = "Cave Squids are mysterious creatures that dwell in the depths of caverns, using their inky tentacles to ensnare unsuspecting prey. Their hardened shell provides protection against predators."
cave_squid_floor_range = (5, 7)
cave_squid_spells = ["Ink Spray", "Tentacle Slam", "Darkness Dive"]
cave_squid_spell_probabilities = {"Ink Spray": 0.4, "Tentacle Slam": 0.3, "Darkness Dive": 0.3}
cave_squid_initial_stats = cave_squid_stats.copy()
cave_squid = Monster("Cave Squid", cave_squid_stats, cave_squid_gear, cave_squid_loot_table, difficulty=60, description=cave_squid_description, floor_range=cave_squid_floor_range, spells=cave_squid_spells, spell_probabilities=cave_squid_spell_probabilities, initial_stats=cave_squid_initial_stats)

cave_crab_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 14,
    "Dexterity": 12,
    "Constitution": 14,
    "Intelligence": 4,
    "Wisdom": 6,
    "Charisma": 6,
    "Element": "Water"
}
cave_crab_gear = []
cave_crab_loot_table = ["Gold", "Crab Shell", "Cave Coral"]
cave_crab_description = "Cave Crabs are crustaceans that inhabit subterranean waterways and underground lakes. With their tough shells and sharp claws, they are adept at hunting prey and defending their territory against intruders."
cave_crab_floor_range = (5, 7)
cave_crab_spells = []
cave_crab_spell_probabilities = {}
cave_crab_initial_stats = cave_crab_stats.copy()
cave_crab = Monster("Cave Crab", cave_crab_stats, cave_crab_gear, cave_crab_loot_table, difficulty=60, description=cave_crab_description, floor_range=cave_crab_floor_range, spells=cave_crab_spells, spell_probabilities=cave_crab_spell_probabilities, initial_stats=cave_crab_initial_stats)

giant_ant_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 12,
    "Intelligence": 2,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "Earth"
}
giant_ant_gear = []
giant_ant_loot_table = ["Gold", "Antenna", "Mandible"]
giant_ant_description = "Giant Ants are formidable insects that dwell in underground tunnels and caverns. They live in complex colonies and are known for their powerful mandibles and organized group attacks."
giant_ant_floor_range = (5, 8)
giant_ant_spells = []
giant_ant_spell_probabilities = {}
giant_ant_initial_stats = giant_ant_stats.copy()
giant_ant = Monster("Giant Ant", giant_ant_stats, giant_ant_gear, giant_ant_loot_table, difficulty=50, description=giant_ant_description, floor_range=giant_ant_floor_range, spells=giant_ant_spells, spell_probabilities=giant_ant_spell_probabilities, initial_stats=giant_ant_initial_stats)

grey_ooze_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 8,
    "Constitution": 14,
    "Intelligence": 2,
    "Wisdom": 6,
    "Charisma": 2,
    "Element": "None"
}
grey_ooze_gear = []
grey_ooze_loot_table = ["Gold", "Ooze Essence", "Acidic Residue"]
grey_ooze_description = "Grey Oozes are amorphous, gelatinous creatures that inhabit the damp, dark recesses of dungeons and caverns. They possess a corrosive acidic touch that can dissolve organic matter, making them a danger to unwary adventurers."
grey_ooze_floor_range = (6, 8)
grey_ooze_spells = []
grey_ooze_spell_probabilities = {}
grey_ooze_initial_stats = grey_ooze_stats.copy()
grey_ooze = Monster("Grey Ooze", grey_ooze_stats, grey_ooze_gear, grey_ooze_loot_table, difficulty=60, description=grey_ooze_description, floor_range=grey_ooze_floor_range, spells=grey_ooze_spells, spell_probabilities=grey_ooze_spell_probabilities, initial_stats=grey_ooze_initial_stats)

troglodyte_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}
troglodyte_gear = ["Stone Club", "Reptilian Hide"]
troglodyte_loot_table = ["Gold", "Troglodyte Tooth", "Cave Fungus"]
troglodyte_description = "Troglodytes are reptilian humanoids that dwell in dark, subterranean caves. With their keen senses and powerful claws, they are formidable hunters and fiercely territorial, defending their underground lairs from intruders."
troglodyte_floor_range = (6, 8)
troglodyte_spells = []
troglodyte_spell_probabilities = {}
troglodyte_initial_stats = troglodyte_stats.copy()
troglodyte = Monster("Troglodyte", troglodyte_stats, troglodyte_gear, troglodyte_loot_table, difficulty=80, description=troglodyte_description, floor_range=troglodyte_floor_range, spells=troglodyte_spells, spell_probabilities=troglodyte_spell_probabilities, initial_stats=troglodyte_initial_stats)

morlock_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 8,
    "Element": "Earth"
}
morlock_gear = ["Crudely Forged Axe", "Ragged Hide Armor"]
morlock_loot_table = ["Gold", "Morlock Fang", "Cave Moss"]
morlock_description = "Morlocks are a primitive and savage race of subterranean humanoids that inhabit the deepest, darkest caves. They are known for their brutish strength and ferocious nature, often ambushing unwary travelers who venture into their domain."
morlock_floor_range = (6, 8)
morlock_spells = []
morlock_spell_probabilities = {}
morlock_initial_stats = morlock_stats.copy()
morlock = Monster("Morlock", morlock_stats, morlock_gear, morlock_loot_table, difficulty=120, description=morlock_description, floor_range=morlock_floor_range, spells=morlock_spells, spell_probabilities=morlock_spell_probabilities, initial_stats=morlock_initial_stats)

giant_bloodworm_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 10,
    "Strength": 16,
    "Dexterity": 12,
    "Constitution": 16,
    "Intelligence": 2,
    "Wisdom": 6,
    "Charisma": 4,
    "Element": "None"
}
giant_bloodworm_gear = []
giant_bloodworm_loot_table = ["Gold", "Bloody Fang", "Worm Secretion"]
giant_bloodworm_description = "Giant Bloodworms are massive, carnivorous worms that inhabit underground tunnels and caverns. They ambush their prey with lightning-fast strikes and consume them with their razor-sharp teeth."
giant_bloodworm_floor_range = (6, 8)
giant_bloodworm_spells = []
giant_bloodworm_spell_probabilities = {}
giant_bloodworm_initial_stats = giant_bloodworm_stats.copy()
giant_bloodworm = Monster("Giant Bloodworm", giant_bloodworm_stats, giant_bloodworm_gear, giant_bloodworm_loot_table, difficulty=80, description=giant_bloodworm_description, floor_range=giant_bloodworm_floor_range, spells=giant_bloodworm_spells, spell_probabilities=giant_bloodworm_spell_probabilities, initial_stats=giant_bloodworm_initial_stats)

cave_bear_stats = {
    "HP": 200,  # Define HP attribute for Cave Bear
    "Damage": 60,  # Define damage attribute for Cave Bear
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 25,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Cave Bear's attack
}
cave_bear_gear = ["Claws", "Thick Fur"]
cave_bear_loot_table = ["Gold", "Bear Claw", "Bear Pelt"]
cave_bear_description = "Cave Bears are formidable predators that dwell in dark caverns and deep forests. They are known for their immense size and strength, capable of overpowering almost any foe. With razor-sharp claws and a thick coat of fur, they are well adapted to hunting in the harsh environments of their underground lairs."
cave_bear_floor_range = (7, 9)
cave_bear_spells = []
cave_bear_spell_probabilities = {}
cave_bear_initial_stats = cave_bear_stats.copy() # Make a copy of the initial stats
cave_bear = Monster("Cave Bear", cave_bear_stats, cave_bear_gear, cave_bear_loot_table, difficulty=30, description=cave_bear_description, floor_range=cave_bear_floor_range, spells=cave_bear_spells, spell_probabilities=cave_bear_spell_probabilities, initial_stats=cave_bear_initial_stats)

spectral_stalagmite_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 45,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 35,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Earth"
}

spectral_stalagmite_gear = ["Ethereal Crystals", "Phantom Spikes"]
spectral_stalagmite_loot_table = ["Spectral Shard", "Ghostly Fragment", "Hollow Gem"]
spectral_stalagmite_description = "Spectral Stalagmites are haunting formations that come to life in the depths of caves. They possess the ability to extend spectral tendrils to ensnare and drain the life force of their prey."
spectral_stalagmite_floor_range = (7, 9)
spectral_stalagmite_spells = ["Spectral Grasp", "Ethereal Drain"]
spectral_stalagmite_spell_probabilities = {"Spectral Grasp": 0.6, "Ethereal Drain": 0.4}
spectral_stalagmite_initial_stats = spectral_stalagmite_stats.copy()
spectral_stalagmite = Monster("Spectral Stalagmite", spectral_stalagmite_stats, spectral_stalagmite_gear, spectral_stalagmite_loot_table, difficulty=8, description=spectral_stalagmite_description, floor_range=spectral_stalagmite_floor_range, spells=spectral_stalagmite_spells, spell_probabilities=spectral_stalagmite_spell_probabilities, initial_stats=spectral_stalagmite_initial_stats)

earth_elemental_stats = {
    "HP": 200,  # Define HP attribute for Earth Elemental
    "Damage": 60,  # Define damage attribute for Earth Elemental
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 14,
    "Constitution": 30,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"  # Define elemental attribute of the Earth Elemental's attack
}
earth_elemental_gear = ["Rocky Form", "Earthen Armor"]
earth_elemental_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
earth_elemental_description = "Earth Elementals are beings of solid stone and earth, animated by ancient magic. They wield the power of the earth itself, crushing their enemies beneath massive boulders and summoning earthquakes to shake the ground. Their sturdy form makes them nearly impervious to physical harm."
earth_elemental_floor_range = (7, 9)
earth_elemental_spells = ["Stone Barrage", "Quake"]
earth_elemental_spell_probabilities = {"Stone Barrage": 0.6, "Quake": 0.4} 
earth_elemental_initial_stats = earth_elemental_stats.copy() # Make a copy of the initial stats
earth_elemental = Monster("Earth Elemental", earth_elemental_stats, earth_elemental_gear, earth_elemental_loot_table, difficulty=25, description=earth_elemental_description, floor_range=earth_elemental_floor_range, spells=earth_elemental_spells, spell_probabilities=earth_elemental_spell_probabilities, initial_stats=earth_elemental_initial_stats)

dark_elf_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 20,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Shadow"
}
dark_elf_gear = ["Shadowblade", "Dark Cloak"]
dark_elf_loot_table = ["Gold", "Dark Essence", "Shadow Shard"]
dark_elf_description = "Dark Elves, also known as Drow, are a sinister and cunning race that dwell in the depths of the Underdark. Masters of stealth and deception, they excel in the arts of assassination and dark magic, wielding shadowy blades and weaving spells of darkness to strike fear into the hearts of their enemies."
dark_elf_floor_range = (7, 9)
dark_elf_spells = ["Shadow Step", "Dark Bolt"]
dark_elf_spell_probabilities = {"Shadow Step": 0.5, "Dark Bolt": 0.3}
dark_elf_initial_stats = dark_elf_stats.copy()
dark_elf = Monster("Dark Elf", dark_elf_stats, dark_elf_gear, dark_elf_loot_table, difficulty=100, description=dark_elf_description, floor_range=dark_elf_floor_range, spells=dark_elf_spells, spell_probabilities=dark_elf_spell_probabilities, initial_stats=dark_elf_initial_stats)

cave_lurker_stats = {
    "HP": 250,  # Define HP attribute for Cave Lurker
    "Damage": 90,  # Define damage attribute for Cave Lurker
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 45,  # Define magic defense vs spells
    "Strength": 24,
    "Dexterity": 28,
    "Constitution": 28,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "Dark"  # Define elemental attribute of the Cave Lurker's attack
}
cave_lurker_gear = ["Sharp Claws", "Thick Hide"]
cave_lurker_loot_table = ["Gold", "Lurker Fang", "Shadow Orb"]
cave_lurker_description = "Cave Lurkers are large, predatory creatures that lurk in the depths of the caves, waiting patiently for unsuspecting prey to wander into their territory. With their razor-sharp claws and thick hide, they are well-equipped for hunting in the darkness, relying on their keen senses to detect even the slightest movement. Though not the most agile of creatures, they make up for it with brute strength and tenacity."
cave_lurker_floor_range = (8, 10)
cave_lurker_spells = []
cave_lurker_spell_probabilities = {}
cave_lurker_initial_stats = cave_lurker_stats.copy() # Make a copy of the initial stats
cave_lurker = Monster("Cave Lurker", cave_lurker_stats, cave_lurker_gear, cave_lurker_loot_table, difficulty=80, description=cave_lurker_description, floor_range=cave_lurker_floor_range, spells=cave_lurker_spells, spell_probabilities=cave_lurker_spell_probabilities, initial_stats=cave_lurker_initial_stats)

deathweb_spider_stats = {
    "HP": 300,
    "Damage": 70,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
deathweb_spider_gear = ["Venomous Fangs", "Shadow Silk Webs"]
deathweb_spider_loot_table = ["Gold", "Spider Silk", "Dark Essence"]
deathweb_spider_description = "Deathweb Spiders are monstrous arachnids that haunt the darkest corners of the underground. Their webs are woven from shadow itself, ensnaring their prey and draining them of their life force. They are swift and deadly predators, striking fear into the hearts of adventurers."
deathweb_spider_floor_range = (8, 10)
deathweb_spider_spells = []
deathweb_spider_spell_probabilities = {}
deathweb_spider_initial_stats = deathweb_spider_stats.copy()
deathweb_spider = Monster("Deathweb Spider", deathweb_spider_stats, deathweb_spider_gear, deathweb_spider_loot_table, difficulty=100, description=deathweb_spider_description, floor_range=deathweb_spider_floor_range, spells=deathweb_spider_spells, spell_probabilities=deathweb_spider_spell_probabilities, initial_stats=deathweb_spider_initial_stats)

stygian_crawler_stats = {
    "HP": 300,  # Define HP attribute for Stygian Crawler
    "Damage": 80,  # Define damage attribute for Stygian Crawler
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 12,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "Dark"  # Define elemental attribute of the Stygian Crawler's attack
}
stygian_crawler_gear = ["Barbed Appendages", "Shadowed Carapace"]
stygian_crawler_loot_table = ["Gold", "Crawler Fang", "Shadow Essence"]
stygian_crawler_description = "Stygian Crawlers are sinister creatures that skulk in the shadows of the underground tunnels and caverns, their twisted forms blending seamlessly with the darkness. With their sharp appendages and venomous bite, they are skilled hunters, capable of ambushing prey with deadly precision. Though individually small, they often hunt in packs, overwhelming their enemies with their sheer numbers and cunning tactics."
stygian_crawler_floor_range = (8, 10)
stygian_crawler_spells = []
stygian_crawler_spell_probabilities = {}
stygian_crawler_initial_stats = stygian_crawler_stats.copy() # Make a copy of the initial stats
stygian_crawler = Monster("Stygian Crawler", stygian_crawler_stats, stygian_crawler_gear, stygian_crawler_loot_table, difficulty=100, description=stygian_crawler_description, floor_range=stygian_crawler_floor_range, spells=stygian_crawler_spells, spell_probabilities=stygian_crawler_spell_probabilities, initial_stats=stygian_crawler_initial_stats)

kobold_skyclaw_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Air"
}
kobold_skyclaw_gear = ["Windblade", "Feathered Cloak"]
kobold_skyclaw_loot_table = ["Gold", "Sky Crystal", "Feathered Charm"]
kobold_skyclaw_description = "Kobold Skyclaws are agile warriors who have formed a bond with the element of air. They soar through the skies on their feathered wings, swooping down on unsuspecting foes with deadly precision."
kobold_skyclaw_floor_range = (8, 10)
kobold_skyclaw_spells = []
kobold_skyclaw_spell_probabilities = {}
kobold_skyclaw_initial_stats = kobold_skyclaw_stats.copy()
kobold_skyclaw = Monster("Kobold Skyclaw", kobold_skyclaw_stats, kobold_skyclaw_gear, kobold_skyclaw_loot_table, difficulty=60, description=kobold_skyclaw_description, floor_range=kobold_skyclaw_floor_range, spells=kobold_skyclaw_spells, spell_probabilities=kobold_skyclaw_spell_probabilities, initial_stats=kobold_skyclaw_initial_stats)

venomous_chasmfiend_stats = {
    "HP": 400,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Poison"
}
venomous_chasmfiend_gear = ["Toxic Barb Stingers", "Chitin Carapace"]
venomous_chasmfiend_loot_table = ["Gold", "Venom Sac", "Corrosive Fang"]
venomous_chasmfiend_description = "Venomous Chasmfiends are vicious arachnid-like creatures that lurk in the depths of underground chasms. Their bodies are covered in toxic venom, and they can ensnare their prey with their razor-sharp stingers. Their venom is potent enough to paralyze even the hardiest of adventurers."
venomous_chasmfiend_floor_range = (9, 11)
venomous_chasmfiend_spells = []
venomous_chasmfiend_spell_probabilities = {}
venomous_chasmfiend_initial_stats = venomous_chasmfiend_stats.copy()
venomous_chasmfiend = Monster("Venomous Chasmfiend", venomous_chasmfiend_stats, venomous_chasmfiend_gear, venomous_chasmfiend_loot_table, difficulty=150, description=venomous_chasmfiend_description, floor_range=venomous_chasmfiend_floor_range, spells=venomous_chasmfiend_spells, spell_probabilities=venomous_chasmfiend_spell_probabilities, initial_stats=venomous_chasmfiend_initial_stats)

minotaur_lancer_stats = {
    "HP": 220,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 26,
    "Dexterity": 16,
    "Constitution": 22,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
minotaur_lancer_gear = ["Lance of Horns", "Reinforced Minotaur Armor"]
minotaur_lancer_loot_table = ["Gold", "Minotaur Horn", "Lancer's Shield"]
minotaur_lancer_description = "Minotaur Lancers are renowned for their skill and ferocity in battle. Mounted atop mighty beasts, they charge into combat with their lances held high, skewering their enemies with deadly precision."
minotaur_lancer_floor_range = (9, 11)
minotaur_lancer_spells = []
minotaur_lancer_spell_probabilities = {}
minotaur_lancer_initial_stats = minotaur_lancer_stats.copy()
minotaur_lancer = Monster("Minotaur Lancer", minotaur_lancer_stats, minotaur_lancer_gear, minotaur_lancer_loot_table, difficulty=100, description=minotaur_lancer_description, floor_range=minotaur_lancer_floor_range, spells=minotaur_lancer_spells, spell_probabilities=minotaur_lancer_spell_probabilities, initial_stats=minotaur_lancer_initial_stats)

dark_elf_spider_sorceress_stats = {
    "HP": 280,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 50,
    "Strength": 16,
    "Dexterity": 24,
    "Constitution": 20,
    "Intelligence": 26,
    "Wisdom": 28,
    "Charisma": 24,
    "Element": "Dark"
}
dark_elf_spider_sorceress_gear = ["Spiderweb Staff", "Arachnid Robes"]
dark_elf_spider_sorceress_loot_table = ["Gold", "Dark Elf Silk", "Spider Fang"]
dark_elf_spider_sorceress_description = "Dark Elf Spider-Sorceresses are formidable spellcasters who have formed a symbiotic bond with spiders. They wield staffs woven from spider silk and wear robes infused with dark magic, allowing them to control and manipulate arachnids to do their bidding."
dark_elf_spider_sorceress_floor_range = (9, 11)
dark_elf_spider_sorceress_spells = ["Web of Darkness", "Venomous Blast", "Arachnid Swarm"]
dark_elf_spider_sorceress_spell_probabilities = {"Web of Darkness": 0.4, "Venomous Blast": 0.3, "Arachnid Swarm": 0.3}
dark_elf_spider_sorceress_initial_stats = dark_elf_spider_sorceress_stats.copy()
dark_elf_spider_sorceress = Monster("Dark Elf Spider-Sorceress", dark_elf_spider_sorceress_stats, dark_elf_spider_sorceress_gear, dark_elf_spider_sorceress_loot_table, difficulty=80, description=dark_elf_spider_sorceress_description, floor_range=dark_elf_spider_sorceress_floor_range, spells=dark_elf_spider_sorceress_spells, spell_probabilities=dark_elf_spider_sorceress_spell_probabilities, initial_stats=dark_elf_spider_sorceress_initial_stats)

phase_spider_stats = {
    "HP": 280,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 45,
    "Strength": 26,
    "Dexterity": 32,
    "Constitution": 28,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "None"
}
phase_spider_gear = ["Ethereal Fangs", "Phase Silk"]
phase_spider_loot_table = ["Gold", "Spider Essence", "Ethereal Webbing"]
phase_spider_description = "Phase Spiders are elusive arachnids capable of phasing in and out of reality. They attack with ethereal fangs and ensnare their prey with webs that transcend dimensions."
phase_spider_floor_range = (10, 12)
phase_spider_spells = ["Phase Shift", "Ethereal Strike", "Web of Shadows"]
phase_spider_spell_probabilities = {"Phase Shift": 0.4, "Ethereal Strike": 0.3, "Web of Shadows": 0.3}
phase_spider_initial_stats = phase_spider_stats.copy()
phase_spider = Monster("Phase Spider", phase_spider_stats, phase_spider_gear, phase_spider_loot_table, difficulty=70, description=phase_spider_description, floor_range=phase_spider_floor_range, spells=phase_spider_spells, spell_probabilities=phase_spider_spell_probabilities, initial_stats=phase_spider_initial_stats)

kobold_shadow_warrior_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Shadow"
}
kobold_shadow_warrior_gear = ["Shadowblade", "Cloak of Shadows"]
kobold_shadow_warrior_loot_table = ["Gold", "Shadow Shard", "Cloak Fragment"]
kobold_shadow_warrior_description = "Kobold Shadow-Warriors are skilled assassins who move with uncanny stealth and strike from the shadows. They are masters of deception and subterfuge, using their shadowy abilities to outmaneuver and ambush their enemies."
kobold_shadow_warrior_floor_range = (10, 12)
kobold_shadow_warrior_spells = []
kobold_shadow_warrior_spell_probabilities = {}
kobold_shadow_warrior_initial_stats = kobold_shadow_warrior_stats.copy()
kobold_shadow_warrior = Monster("Kobold Shadow-Warrior", kobold_shadow_warrior_stats, kobold_shadow_warrior_gear, kobold_shadow_warrior_loot_table, difficulty=80, description=kobold_shadow_warrior_description, floor_range=kobold_shadow_warrior_floor_range, spells=kobold_shadow_warrior_spells, spell_probabilities=kobold_shadow_warrior_spell_probabilities, initial_stats=kobold_shadow_warrior_initial_stats)

cave_troll_stats = {
    "HP": 400,  # Define HP attribute for Cave Troll
    "Damage": 120,  # Define damage attribute for Cave Troll
    "Defense": 70,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 36,
    "Dexterity": 18,
    "Constitution": 34,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Cave Troll's attack
}
cave_troll_gear = ["Club", "Rugged Hide"]
cave_troll_loot_table = ["Gold", "Troll Tooth", "Stone Club"]
cave_troll_description = "Cave Trolls are brutish creatures that dwell in the dark depths of the caves, emerging only to hunt for food or defend their territory. With their massive size and strength, they can crush boulders with their bare hands and tear through solid rock with their sharp claws. Though not the most intelligent of creatures, they make up for it with sheer brute force, overpowering their enemies with relentless ferocity."
cave_troll_floor_range = (10, 12)
cave_troll_spells = []
cave_troll_spell_probabilities = {}
cave_troll_initial_stats = cave_troll_stats.copy() # Make a copy of the initial stats
cave_troll = Monster("Cave Troll", cave_troll_stats, cave_troll_gear, cave_troll_loot_table, difficulty=120, description=cave_troll_description, floor_range=cave_troll_floor_range, spells=cave_troll_spells, spell_probabilities=cave_troll_spell_probabilities, initial_stats=cave_troll_initial_stats)

dragger_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 35,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

dragger_gear = ["Rock-hard Carapace", "Stone Crusher"]
dragger_loot_table = ["Earthen Shard", "Tunneling Claw", "Cavern Core"]
dragger_description = "Draggers are formidable creatures often encountered in natural caverns and underground passageways. Resembling boulders with appendages. Their immense strength and ability to move through stone make them formidable adversaries."
dragger_floor_range = (11, 13)
dragger_spells = []
dragger_spell_probabilities = {}
dragger_initial_stats = dragger_stats.copy()
dragger = Monster("Dragger", dragger_stats, dragger_gear, dragger_loot_table, difficulty=8, description=dragger_description, floor_range=dragger_floor_range, spells=dragger_spells, spell_probabilities=dragger_spell_probabilities, initial_stats=dragger_initial_stats)

gloombeast_stats = {
    "HP": 250,
    "Damage": 60,
    "Defense": 45,
    "Magic Defense": 50,
    "Strength": 35,
    "Dexterity": 20,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 15,
    "Element": "Dark"
}

gloombeast_gear = ["Shadowy Fur", "Voidborn Claws"]
gloombeast_loot_table = ["Umbral Essence", "Darkened Hide", "Void Fang"]
gloombeast_description = "Gloombeasts are massive creatures adorned with bioluminescent patterns that emit an eerie glow in the darkness of the caves. They hunt by luring prey with their glow before ambushing them with their razor-sharp claws."
gloombeast_floor_range = (11, 13)
gloombeast_spells = []
gloombeast_spell_probabilities = {}
gloombeast_initial_stats = gloombeast_stats.copy()
gloombeast = Monster("Gloombeast", gloombeast_stats, gloombeast_gear, gloombeast_loot_table, difficulty=8, description=gloombeast_description, floor_range=gloombeast_floor_range, spells=gloombeast_spells, spell_probabilities=gloombeast_spell_probabilities, initial_stats=gloombeast_initial_stats)

fangtooth_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 28,
    "Dexterity": 30,
    "Constitution": 30,
    "Intelligence": 12,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "Ice"
}

fangtooth_gear = ["Frostbite Scales", "Glacial Fangs"]
fangtooth_loot_table = ["Icy Tooth", "Frozen Claw", "Chilled Essence"]
fangtooth_description = "Fangtooths are icy predators that lurk in the depths of caverns. Their razor-sharp teeth and keen senses make them formidable hunters, able to navigate through the darkness with ease."
fangtooth_floor_range = (11, 13)
fangtooth_spells = []
fangtooth_spell_probabilities = {}
fangtooth_initial_stats = fangtooth_stats.copy()
fangtooth = Monster("Fangtooth", fangtooth_stats, fangtooth_gear, fangtooth_loot_table, difficulty=7, description=fangtooth_description, floor_range=fangtooth_floor_range, spells=fangtooth_spells, spell_probabilities=fangtooth_spell_probabilities, initial_stats=fangtooth_initial_stats)

abyssal_amalgam_stats = {
    "HP": 300,
    "Damage": 70,
    "Defense": 55,
    "Magic Defense": 60,
    "Strength": 40,
    "Dexterity": 30,
    "Constitution": 50,
    "Intelligence": 25,
    "Wisdom": 28,
    "Charisma": 15,
    "Element": "Dark"
}

abyssal_amalgam_gear = ["Twisted Flesh", "Corrupted Claws"]
abyssal_amalgam_loot_table = ["Abyssal Essence", "Darkened Core", "Eldritch Fragment"]
abyssal_amalgam_description = "Abyssal Amalgams are grotesque fusion creatures formed from the dark energies of the depths. Composed of various cave-dwelling creatures, they are twisted and formidable foes."
abyssal_amalgam_floor_range = (12, 15)
abyssal_amalgam_spells = ["Shadow Nova", "Corrupting Touch"]
abyssal_amalgam_spell_probabilities = {"Shadow Nova": 0.6, "Corrupting Touch": 0.4}
abyssal_amalgam_initial_stats = abyssal_amalgam_stats.copy()
abyssal_amalgam = Monster("Abyssal Amalgam", abyssal_amalgam_stats, abyssal_amalgam_gear, abyssal_amalgam_loot_table, difficulty=10, description=abyssal_amalgam_description, floor_range=abyssal_amalgam_floor_range, spells=abyssal_amalgam_spells, spell_probabilities=abyssal_amalgam_spell_probabilities, initial_stats=abyssal_amalgam_initial_stats)

chittering_chasmcrawler_stats = {
    "HP": 120,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 12,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "Earth"
}

chittering_chasmcrawler_gear = ["Razor Mandibles", "Chitinous Carapace"]
chittering_chasmcrawler_loot_table = ["Chasmcrawler Fang", "Chitinous Shell", "Venom Sac"]
chittering_chasmcrawler_description = "Chittering Chasmcrawlers are insectoid creatures that scuttle through the caverns with incredible speed. Their sharp mandibles can tear through rock and flesh alike, making them formidable adversaries."
chittering_chasmcrawler_floor_range = (12, 15)
chittering_chasmcrawler_spells = []
chittering_chasmcrawler_spell_probabilities = {}
chittering_chasmcrawler_initial_stats = chittering_chasmcrawler_stats.copy()
chittering_chasmcrawler = Monster("Chittering Chasmcrawler", chittering_chasmcrawler_stats, chittering_chasmcrawler_gear, chittering_chasmcrawler_loot_table, difficulty=7, description=chittering_chasmcrawler_description, floor_range=chittering_chasmcrawler_floor_range, spells=chittering_chasmcrawler_spells, spell_probabilities=chittering_chasmcrawler_spell_probabilities, initial_stats=chittering_chasmcrawler_initial_stats)

luminiferous_lurker_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 45,
    "Strength": 30,
    "Dexterity": 35,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Light"
}

luminiferous_lurker_gear = ["Radiant Core", "Ethereal Aura"]
luminiferous_lurker_loot_table = ["Luminous Essence", "Radiant Shard", "Etheric Crystal"]
luminiferous_lurker_description = "Luminiferous Lurkers are creatures composed of pure light, their radiant forms both captivating and deadly. They stalk the darkest caverns, illuminating their surroundings with their ethereal glow."
luminiferous_lurker_floor_range = (12, 15)
luminiferous_lurker_spells = ["Radiant Burst", "Luminous Beam"]
luminiferous_lurker_spell_probabilities = {"Radiant Burst": 0.6, "Luminous Beam": 0.4}
luminiferous_lurker_initial_stats = luminiferous_lurker_stats.copy()
luminiferous_lurker = Monster("Luminiferous Lurker", luminiferous_lurker_stats, luminiferous_lurker_gear, luminiferous_lurker_loot_table, difficulty=8, description=luminiferous_lurker_description, floor_range=luminiferous_lurker_floor_range, spells=luminiferous_lurker_spells, spell_probabilities=luminiferous_lurker_spell_probabilities, initial_stats=luminiferous_lurker_initial_stats)

vorpal_veilstalker_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 25,
    "Dexterity": 40,
    "Constitution": 30,
    "Intelligence": 22,
    "Wisdom": 28,
    "Charisma": 15,
    "Element": "Shadow"
}

vorpal_veilstalker_gear = ["Phasing Cloak", "Shadow Blade"]
vorpal_veilstalker_loot_table = ["Veil Fragment", "Shadow Essence", "Ethereal Blade"]
vorpal_veilstalker_description = "Vorpal Veilstalkers are creatures that phase in and out of reality, their attacks striking from unexpected angles. They haunt the shadows of the caves, blending seamlessly with the darkness."
vorpal_veilstalker_floor_range = (13, 16)
vorpal_veilstalker_spells = ["Shadowstep", "Ethereal Strike"]
vorpal_veilstalker_spell_probabilities = {"Shadowstep": 0.6, "Ethereal Strike": 0.4}
vorpal_veilstalker_initial_stats = vorpal_veilstalker_stats.copy()
vorpal_veilstalker = Monster("Vorpal Veilstalker", vorpal_veilstalker_stats, vorpal_veilstalker_gear, vorpal_veilstalker_loot_table, difficulty=8, description=vorpal_veilstalker_description, floor_range=vorpal_veilstalker_floor_range, spells=vorpal_veilstalker_spells, spell_probabilities=vorpal_veilstalker_spell_probabilities, initial_stats=vorpal_veilstalker_initial_stats)

obsidian_golem_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 60,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
obsidian_golem_gear = ["Obsidian Shard Fists", "Molten Core Armor"]
obsidian_golem_loot_table = ["Gold", "Obsidian Shard", "Earthen Gem"]
obsidian_golem_description = "Obsidian Golems are massive constructs formed from the darkest depths of the earth. Their bodies are composed of solid obsidian, making them nearly indestructible. They are relentless guardians of the underground, crushing anything that dares to trespass into their domain."
obsidian_golem_floor_range = (13, 16)
obsidian_golem_spells = []
obsidian_golem_spell_probabilities = {}
obsidian_golem_initial_stats = obsidian_golem_stats.copy()
obsidian_golem = Monster("Obsidian Golem", obsidian_golem_stats, obsidian_golem_gear, obsidian_golem_loot_table, difficulty=200, description=obsidian_golem_description, floor_range=obsidian_golem_floor_range, spells=obsidian_golem_spells, spell_probabilities=obsidian_golem_spell_probabilities, initial_stats=obsidian_golem_initial_stats)

mossy_goliath_stats = {
    "HP": 600,  # Define HP attribute for Mossy Goliath
    "Damage": 150,  # Define damage attribute for Mossy Goliath
    "Defense": 80,  # Define Defense stat vs attack stat
    "Magic Defense": 70,  # Define magic defense vs spells
    "Strength": 45,
    "Dexterity": 30,
    "Constitution": 50,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Earth"  # Define elemental attribute of the Mossy Goliath's attack
}
mossy_goliath_gear = ["Vine Whip", "Mossy Armor"]
mossy_goliath_loot_table = ["Gold", "Ancient Vine", "Mossy Stone"]
mossy_goliath_description = "Mossy Goliaths are colossal creatures camouflaged with thick layers of moss and vines, making them nearly indistinguishable from the cave walls. Despite their immense size, they move with surprising agility, ambushing their prey with powerful vine lashes and crushing blows. They are formidable opponents, capable of overpowering even the most skilled adventurers with their sheer strength and tenacity."
mossy_goliath_floor_range = (14, 17)
mossy_goliath_spells = []
mossy_goliath_spell_probabilities = {}
mossy_goliath_initial_stats = mossy_goliath_stats.copy() # Make a copy of the initial stats
mossy_goliath = Monster("Mossy Goliath", mossy_goliath_stats, mossy_goliath_gear, mossy_goliath_loot_table, difficulty=200, description=mossy_goliath_description, floor_range=mossy_goliath_floor_range, spells=mossy_goliath_spells, spell_probabilities=mossy_goliath_spell_probabilities, initial_stats=mossy_goliath_initial_stats)

cave_abomination_stats = {
    "HP": 600,  # Define HP attribute for Cave Abomination
    "Damage": 150,  # Define damage attribute for Cave Abomination
    "Defense": 80,  # Define Defense stat vs attack stat
    "Magic Defense": 70,  # Define magic defense vs spells
    "Strength": 40,
    "Dexterity": 40,
    "Constitution": 50,
    "Intelligence": 20,
    "Wisdom": 30,
    "Charisma": 20,
    "Element": "Dark"  # Define elemental attribute of the Cave Abomination's attack
}
cave_abomination_gear = ["Twisted Limbs", "Obsidian Hide"]
cave_abomination_loot_table = ["Gold", "Abomination Essence", "Dark Crystal"]
cave_abomination_description = "Cave Abominations are grotesque monstrosities that dwell in the deepest, most inhospitable caverns, their twisted forms a testament to the corruption of the darkness. With their immense strength and ferocious appetite, they rampage through the underground tunnels, leaving destruction and chaos in their wake. Though slow-moving, they are nearly unstoppable once they have their sights set on their prey."
cave_abomination_floor_range = (14, 17)
cave_abomination_spells = []
cave_abomination_spell_probabilities = {}
cave_abomination_initial_stats = cave_abomination_stats.copy() # Make a copy of the initial stats
cave_abomination = Monster("Cave Abomination", cave_abomination_stats, cave_abomination_gear, cave_abomination_loot_table, difficulty=200, description=cave_abomination_description, floor_range=cave_abomination_floor_range, spells=cave_abomination_spells, spell_probabilities=cave_abomination_spell_probabilities, initial_stats=cave_abomination_initial_stats)