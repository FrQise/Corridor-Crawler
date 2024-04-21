from monsters.bestiary import Monster

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
goblin_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
goblin_description = "Goblins are small, agile creatures known for their mischief and love of shiny objects. Despite their size, they can be formidable opponents in combat, relying on their speed and cunning to outmaneuver their foes."
goblin_floor_range = (1,2)
goblin_spells = ["Smelly feet"]
goblin_spell_probabilities = {goblin_spells[0]: 1} 
goblin_initial_stats = goblin_stats.copy() #Make a copy of the initial stats
goblin = Monster("Goblin", goblin_stats, goblin_gear, goblin_loot_table, difficulty=1, description=goblin_description, floor_range=goblin_floor_range, spells=goblin_spells, spell_probabilities=goblin_spell_probabilities, initial_stats=goblin_initial_stats)

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

boar_stats = {
    "HP": 100,  # Define HP attribute for Boar
    "Damage": 35,  # Define damage attribute for Boar
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 14,
    "Constitution": 18,
    "Intelligence": 4,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Boar's attack
}
boar_gear = ["Tusks", "Thick Hide"]
boar_loot_table = ["Gold", "Boar Tusk", "Boar Hide"]
boar_description = "Boars are aggressive wild pigs known for their sharp tusks and ferocious charges. They are fiercely territorial and will aggressively defend their territory from any intruders. Their powerful attacks can easily overpower unsuspecting adventurers."
boar_floor_range = (1,5)
boar_spells = []
boar_spell_probabilities = {}
boar_initial_stats = boar_stats.copy() # Make a copy of the initial stats
boar = Monster("Boar", boar_stats, boar_gear, boar_loot_table, difficulty=5, description=boar_description, floor_range=boar_floor_range, spells=boar_spells, spell_probabilities=boar_spell_probabilities, initial_stats=boar_initial_stats)

gargoyle_stats = {
    "HP": 180,  # Define HP attribute for Gargoyle
    "Damage": 55,  # Define damage attribute for Gargoyle
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Gargoyle's attack
}
gargoyle_gear = ["Stone Claws", "Obsidian Armor"]
gargoyle_loot_table = ["Gold", "Gargoyle Horn", "Obsidian Shard"]
gargoyle_description = "Gargoyles are fearsome stone guardians crafted to protect ancient tombs and sacred places. Animated by dark magic, they swoop down from their perches to strike at intruders with razor-sharp claws and powerful wings. Their stone bodies make them highly resilient to physical attacks."
gargoyle_floor_range = (30, 60)
gargoyle_spells = ["Stone Skin", "Wing Buffet"]
gargoyle_spell_probabilities = {"Stone Skin": 0.6, "Wing Buffet": 0.4} 
gargoyle_initial_stats = gargoyle_stats.copy() # Make a copy of the initial stats
gargoyle = Monster("Gargoyle", gargoyle_stats, gargoyle_gear, gargoyle_loot_table, difficulty=30, description=gargoyle_description, floor_range=gargoyle_floor_range, spells=gargoyle_spells, spell_probabilities=gargoyle_spell_probabilities, initial_stats=gargoyle_initial_stats)

hobgoblin_stats = {
    "HP": 120,  # Define HP attribute for Hobgoblin
    "Damage": 35,  # Define damage attribute for Hobgoblin
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 12,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Hobgoblin's attack
}
hobgoblin_gear = ["Serrated Sword", "Chainmail Armor"]
hobgoblin_loot_table = ["Gold", "Hobgoblin Ear", "Broken Shield"]
hobgoblin_description = "Hobgoblins are disciplined warriors renowned for their martial prowess and tactical cunning. They form organized warbands, employing strategic maneuvers and coordinated attacks to overwhelm their enemies. With their razor-sharp blades and sturdy armor, they are formidable opponents on the battlefield."
hobgoblin_floor_range = (10, 20)
hobgoblin_spells = []
hobgoblin_spell_probabilities = {}
hobgoblin_initial_stats = hobgoblin_stats.copy() # Make a copy of the initial stats
hobgoblin = Monster("Hobgoblin", hobgoblin_stats, hobgoblin_gear, hobgoblin_loot_table, difficulty=10, description=hobgoblin_description, floor_range=hobgoblin_floor_range, spells=hobgoblin_spells, spell_probabilities=hobgoblin_spell_probabilities, initial_stats=hobgoblin_initial_stats)

dire_rat_stats = {
    "HP": 80,  # Define HP attribute for Dire Rat
    "Damage": 25,  # Define damage attribute for Dire Rat
    "Defense": 15,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Dire Rat's attack
}
dire_rat_gear = ["Razor-sharp Teeth", "Fur"]
dire_rat_loot_table = ["Gold", "Rat Tail", "Foul Meat"]
dire_rat_description = "Dire Rats are larger and more aggressive cousins of common rats, infesting dungeons and sewers with their filthy presence. They swarm their prey with overwhelming numbers, their sharp teeth and claws tearing through flesh with ease. Despite their small size, they are tenacious predators, capable of delivering deadly bites."
dire_rat_floor_range = (1, 5)
dire_rat_spells = []
dire_rat_spell_probabilities = {}
dire_rat_initial_stats = dire_rat_stats.copy() # Make a copy of the initial stats
dire_rat = Monster("Dire Rat", dire_rat_stats, dire_rat_gear, dire_rat_loot_table, difficulty=1, description=dire_rat_description, floor_range=dire_rat_floor_range, spells=dire_rat_spells, spell_probabilities=dire_rat_spell_probabilities, initial_stats=dire_rat_initial_stats)

giant_spider_stats = {
    "HP": 140,  # Define HP attribute for Giant Spider
    "Damage": 45,  # Define damage attribute for Giant Spider
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 25,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Giant Spider's attack
}
giant_spider_gear = ["Venomous Fangs", "Silken Webbing"]
giant_spider_loot_table = ["Gold", "Spider Silk", "Venom Gland"]
giant_spider_description = "Giant Spiders are arachnids of enormous size, lurking in dark corners and dank caves. They ensnare their prey in sticky webs, injecting them with paralyzing venom before draining them of their vital fluids. Their eight legs and razor-sharp fangs make them agile predators, striking fear into the hearts of adventurers."
giant_spider_floor_range = (10, 20)
giant_spider_spells = []
giant_spider_spell_probabilities = {}
giant_spider_initial_stats = giant_spider_stats.copy() # Make a copy of the initial stats
giant_spider = Monster("Giant Spider", giant_spider_stats, giant_spider_gear, giant_spider_loot_table, difficulty=10, description=giant_spider_description, floor_range=giant_spider_floor_range, spells=giant_spider_spells, spell_probabilities=giant_spider_spell_probabilities, initial_stats=giant_spider_initial_stats)

bugbear_stats = {
    "HP": 220,  # Define HP attribute for Bugbear
    "Damage": 65,  # Define damage attribute for Bugbear
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 35,  # Define magic defense vs spells
    "Strength": 24,
    "Dexterity": 16,
    "Constitution": 22,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Bugbear's attack
}
bugbear_gear = ["Spiked Club", "Fur Armor"]
bugbear_loot_table = ["Gold", "Bugbear Claw", "Fur"]
bugbear_description = "Bugbears are large and brutish humanoid creatures, known for their savagery and ferocity in battle. They roam the wilderness in roving bands, preying on travelers and raiding settlements for food and plunder. With their spiked clubs and thick fur, they strike fear into the hearts of those who dare to cross their path."
bugbear_floor_range = (30, 60)
bugbear_spells = []
bugbear_spell_probabilities = {}
bugbear_initial_stats = bugbear_stats.copy() # Make a copy of the initial stats
bugbear = Monster("Bugbear", bugbear_stats, bugbear_gear, bugbear_loot_table, difficulty=30, description=bugbear_description, floor_range=bugbear_floor_range, spells=bugbear_spells, spell_probabilities=bugbear_spell_probabilities, initial_stats=bugbear_initial_stats)

gorgon_stats = {
    "HP": 280,  # Define HP attribute for Gorgon
    "Damage": 75,  # Define damage attribute for Gorgon
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 45,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 18,
    "Constitution": 28,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "None"  # Define elemental attribute of the Gorgon's attack
}
gorgon_gear = ["Petrifying Gaze", "Iron Scales"]
gorgon_loot_table = ["Gold", "Gorgon Scale", "Petrified Eye"]
gorgon_description = "Gorgons are fearsome creatures with the body of a bull and the head of a woman, wreathed in serpentine hair. They possess a petrifying gaze capable of turning their victims to stone with a single glance. With their razor-sharp horns and iron-hard scales, they are formidable adversaries, striking terror into the hearts of those who cross their path."
gorgon_floor_range = (80, 160)
gorgon_spells = []
gorgon_spell_probabilities = {}
gorgon_initial_stats = gorgon_stats.copy() # Make a copy of the initial stats
gorgon = Monster("Gorgon", gorgon_stats, gorgon_gear, gorgon_loot_table, difficulty=80, description=gorgon_description, floor_range=gorgon_floor_range, spells=gorgon_spells, spell_probabilities=gorgon_spell_probabilities, initial_stats=gorgon_initial_stats)

cycloptopus_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 30,
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Water"
}
cycloptopus_gear = ["Tentacle Whip", "Suction Cup Shield"]
cycloptopus_loot_table = ["Gold", "Cycloptopus Eye", "Seaweed Necklace"]
cycloptopus_description = "A fearsome aquatic creature with the body of an octopus and the eye of a cyclops. It lurks in dark underwater caves, ambushing unsuspecting prey with its powerful tentacles and deadly gaze."
cycloptopus_floor_range = (100, 200)
cycloptopus_spells = ["Ink Cloud", "Water Jet"]
cycloptopus_spell_probabilities = {"Ink Cloud": 0.5, "Water Jet": 0.3}
cycloptopus_initial_stats = cycloptopus_stats.copy()
cycloptopus = Monster("Cycloptopus", cycloptopus_stats, cycloptopus_gear, cycloptopus_loot_table, difficulty=100, description=cycloptopus_description, floor_range=cycloptopus_floor_range, spells=cycloptopus_spells, spell_probabilities=cycloptopus_spell_probabilities, initial_stats=cycloptopus_initial_stats)

thief_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 18,
    "Constitution": 12,
    "Intelligence": 14,
    "Wisdom": 12,
    "Charisma": 16,
    "Element": "None"
}
thief_gear = ["Dagger", "Leather Armor"]
thief_loot_table = ["Gold", "Stolen Jewel", "Lockpick Set"]
thief_description = "Thieves are agile and cunning individuals who excel in stealth, lockpicking, and pickpocketing. They use their speed and wit to outmaneuver their opponents and make off with valuable treasures."
thief_floor_range = (1,5)
thief_spells = []
thief_spell_probabilities = {}
thief_initial_stats = thief_stats.copy()
thief = Monster("Thief", thief_stats, thief_gear, thief_loot_table, difficulty=80, description=thief_description, floor_range=thief_floor_range, spells=thief_spells, spell_probabilities=thief_spell_probabilities, initial_stats=thief_initial_stats)

troll_berserker_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 22,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"
}
troll_berserker_gear = ["Greatclub", "Trollhide Armor"]
troll_berserker_loot_table = ["Gold", "Troll Fang", "Berserker Charm"]
troll_berserker_description = "Troll Berserkers are massive and ferocious warriors known for their incredible strength and resilience. In battle, they enter a frenzy, disregarding pain and fear as they unleash devastating attacks upon their enemies."
troll_berserker_floor_range = (150, 250)
troll_berserker_spells = []
troll_berserker_spell_probabilities = {}
troll_berserker_initial_stats = troll_berserker_stats.copy()
troll_berserker = Monster("Troll Berserker", troll_berserker_stats, troll_berserker_gear, troll_berserker_loot_table, difficulty=150, description=troll_berserker_description, floor_range=troll_berserker_floor_range, spells=troll_berserker_spells, spell_probabilities=troll_berserker_spell_probabilities, initial_stats=troll_berserker_initial_stats)

human_thug_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 10,
    "Charisma": 10,
    "Element": "None"
}
human_thug_gear = ["Bludgeon", "Leather Vest"]
human_thug_loot_table = ["Gold", "Stolen Purse", "Brass Knuckles"]
human_thug_description = "Human Thugs are rough and violent individuals who make a living through intimidation, theft, and extortion. Armed with crude weapons and a lack of scruples, they roam the streets looking for easy marks to prey upon."
human_thug_floor_range = (60, 120)
human_thug_spells = []
human_thug_spell_probabilities = {}
human_thug_initial_stats = human_thug_stats.copy()
human_thug = Monster("Human Thug", human_thug_stats, human_thug_gear, human_thug_loot_table, difficulty=60, description=human_thug_description, floor_range=human_thug_floor_range, spells=human_thug_spells, spell_probabilities=human_thug_spell_probabilities, initial_stats=human_thug_initial_stats)

goblin_shaman_stats = {
    "HP": 120,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 25,
    "Strength": 10,
    "Dexterity": 12,
    "Constitution": 12,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "None"
}
goblin_shaman_gear = ["Staff of the Spirits", "Shaman Robes"]
goblin_shaman_loot_table = ["Gold", "Shaman Totem", "Goblin Potion"]
goblin_shaman_description = "Goblin Shamans are spiritual leaders among goblin tribes, wielding powerful magic to aid their kin in battle. They commune with the spirits of nature, calling upon them to unleash curses and blessings upon their enemies and allies."
goblin_shaman_floor_range = (60, 120)
goblin_shaman_spells = ["Hex", "Healing Wave", "Spiritual Bolt"]
goblin_shaman_spell_probabilities = {"Hex": 0.4, "Healing Wave": 0.3, "Spiritual Bolt": 0.2}
goblin_shaman_initial_stats = goblin_shaman_stats.copy()
goblin_shaman = Monster("Goblin Shaman", goblin_shaman_stats, goblin_shaman_gear, goblin_shaman_loot_table, difficulty=60, description=goblin_shaman_description, floor_range=goblin_shaman_floor_range, spells=goblin_shaman_spells, spell_probabilities=goblin_shaman_spell_probabilities, initial_stats=goblin_shaman_initial_stats)

orc_shaman_stats = {
    "HP": 140,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 14,
    "Dexterity": 12,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "None"
}
orc_shaman_gear = ["Staff of the Elements", "Shamanic Robes"]
orc_shaman_loot_table = ["Gold", "Shamanic Totem", "Orcish Brew"]
orc_shaman_description = "Orc Shamans are revered spellcasters within orcish society, wielding potent magic to serve their tribes. They draw upon the elemental forces of nature, calling forth storms, earthquakes, and other natural phenomena to aid their kin in battle."
orc_shaman_floor_range = (80, 160)
orc_shaman_spells = ["Fireball", "Earthquake", "Chain Lightning"]
orc_shaman_spell_probabilities = {"Fireball": 0.4, "Earthquake": 0.3, "Chain Lightning": 0.2}
orc_shaman_initial_stats = orc_shaman_stats.copy()
orc_shaman = Monster("Orc Shaman", orc_shaman_stats, orc_shaman_gear, orc_shaman_loot_table, difficulty=80, description=orc_shaman_description, floor_range=orc_shaman_floor_range, spells=orc_shaman_spells, spell_probabilities=orc_shaman_spell_probabilities, initial_stats=orc_shaman_initial_stats)

orc_berserker_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "None"
}
orc_berserker_gear = ["Battle Axe", "Toughened Hide"]
orc_berserker_loot_table = ["Gold", "Orcish Trophy", "Battle Axe Shard"]
orc_berserker_description = "Orc Berserkers are fearsome warriors known for their ferocious strength and unrelenting aggression. They charge into battle with reckless abandon, wielding massive axes and shrugging off all but the most devastating blows."
orc_berserker_floor_range = (80, 160)
orc_berserker_spells = []
orc_berserker_spell_probabilities = {}
orc_berserker_initial_stats = orc_berserker_stats.copy()
orc_berserker = Monster("Orc Berserker", orc_berserker_stats, orc_berserker_gear, orc_berserker_loot_table, difficulty=80, description=orc_berserker_description, floor_range=orc_berserker_floor_range, spells=orc_berserker_spells, spell_probabilities=orc_berserker_spell_probabilities, initial_stats=orc_berserker_initial_stats)

wererat_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
wererat_gear = ["Rusty Dagger", "Tattered Cloak"]
wererat_loot_table = ["Gold", "Wererat Fang", "Torn Cloth"]
wererat_description = "Wererats are cursed creatures, once human but transformed into rat-like monstrosities under the light of the full moon. Agile and cunning, they stalk the shadows of city streets and sewers, preying on unsuspecting victims with their sharp teeth and claws."
wererat_floor_range = (60, 120)
wererat_spells = []
wererat_spell_probabilities = {}
wererat_initial_stats = wererat_stats.copy()
wererat = Monster("Wererat", wererat_stats, wererat_gear, wererat_loot_table, difficulty=60, description=wererat_description, floor_range=wererat_floor_range, spells=wererat_spells, spell_probabilities=wererat_spell_probabilities, initial_stats=wererat_initial_stats)

death_plague_orc_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
death_plague_orc_gear = ["Corrupted Axe", "Plague-infested Armor"]
death_plague_orc_loot_table = ["Gold", "Corrupted Flesh", "Plague-ridden Helm"]
death_plague_orc_description = "Death-Plague Orcs are warriors tainted by dark necromantic energies and the virulent plague that ravages their lands. They wield corrupted weapons and wear armor infused with the disease, spreading death and decay wherever they go."
death_plague_orc_floor_range = (100, 200)
death_plague_orc_spells = []
death_plague_orc_spell_probabilities = {}
death_plague_orc_initial_stats = death_plague_orc_stats.copy()
death_plague_orc = Monster("Death-Plague Orc", death_plague_orc_stats, death_plague_orc_gear, death_plague_orc_loot_table, difficulty=100, description=death_plague_orc_description, floor_range=death_plague_orc_floor_range, spells=death_plague_orc_spells, spell_probabilities=death_plague_orc_spell_probabilities, initial_stats=death_plague_orc_initial_stats)

goblin_bat_mage_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 30,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 12,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "Air"
}
goblin_bat_mage_gear = ["Winged Staff", "Mage Robes"]
goblin_bat_mage_loot_table = ["Gold", "Bat Wing Staff", "Aerial Scroll"]
goblin_bat_mage_description = "Goblin Bat Mages are spellcasters who have formed a pact with the element of air, granting them the ability to command the winds and summon swarms of bats. They glide through the skies on leathery wings, unleashing powerful magic upon their enemies."
goblin_bat_mage_floor_range = (80, 160)
goblin_bat_mage_spells = ["Gust", "Summon Bat Swarm", "Aerial Blast"]
goblin_bat_mage_spell_probabilities = {"Gust": 0.4, "Summon Bat Swarm": 0.3, "Aerial Blast": 0.2}
goblin_bat_mage_initial_stats = goblin_bat_mage_stats.copy()
goblin_bat_mage = Monster("Goblin Bat Mage", goblin_bat_mage_stats, goblin_bat_mage_gear, goblin_bat_mage_loot_table, difficulty=80, description=goblin_bat_mage_description, floor_range=goblin_bat_mage_floor_range, spells=goblin_bat_mage_spells, spell_probabilities=goblin_bat_mage_spell_probabilities, initial_stats=goblin_bat_mage_initial_stats)

hobgoblin_captain_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 18,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 16,
    "Element": "None"
}
hobgoblin_captain_gear = ["Commander's Sword", "Heavy Plate Armor"]
hobgoblin_captain_loot_table = ["Gold", "Hobgoblin Insignia", "Captain's Helm"]
hobgoblin_captain_description = "Hobgoblin Captains are fearsome leaders among their kind, renowned for their tactical acumen and martial prowess. They inspire loyalty in their troops and lead from the front lines, wielding their heavy swords with deadly precision."
hobgoblin_captain_floor_range = (100, 200)
hobgoblin_captain_spells = []
hobgoblin_captain_spell_probabilities = {}
hobgoblin_captain_initial_stats = hobgoblin_captain_stats.copy()
hobgoblin_captain = Monster("Hobgoblin Captain", hobgoblin_captain_stats, hobgoblin_captain_gear, hobgoblin_captain_loot_table, difficulty=100, description=hobgoblin_captain_description, floor_range=hobgoblin_captain_floor_range, spells=hobgoblin_captain_spells, spell_probabilities=hobgoblin_captain_spell_probabilities, initial_stats=hobgoblin_captain_initial_stats)

half_orc_legionnaire_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 24,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
half_orc_legionnaire_gear = ["Legionnaire Sword", "Heavy Legionnaire Armor"]
half_orc_legionnaire_loot_table = ["Gold", "Half-Orc Medallion", "Legionnaire Helm"]
half_orc_legionnaire_description = "Half-Orc Legionnaires are disciplined soldiers trained in the art of war. They serve with honor and loyalty in the ranks of their legion, wielding their swords with skill and determination."
half_orc_legionnaire_floor_range = (100, 200)
half_orc_legionnaire_spells = []
half_orc_legionnaire_spell_probabilities = {}
half_orc_legionnaire_initial_stats = half_orc_legionnaire_stats.copy()
half_orc_legionnaire = Monster("Half-Orc Legionnaire", half_orc_legionnaire_stats, half_orc_legionnaire_gear, half_orc_legionnaire_loot_table, difficulty=100, description=half_orc_legionnaire_description, floor_range=half_orc_legionnaire_floor_range, spells=half_orc_legionnaire_spells, spell_probabilities=half_orc_legionnaire_spell_probabilities, initial_stats=half_orc_legionnaire_initial_stats)

barbarous_bugbear_stats = {
    "HP": 240,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 24,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "None"
}
barbarous_bugbear_gear = ["Savage Axe", "Fur Armor"]
barbarous_bugbear_loot_table = ["Gold", "Barbarous Trophy", "Bloody Pelt"]
barbarous_bugbear_description = "Barbarous Bugbears are fearsome warriors known for their savage brutality in battle. They revel in chaos and bloodshed, wielding their axes with deadly precision as they charge into the fray."
barbarous_bugbear_floor_range = (120, 240)
barbarous_bugbear_spells = []
barbarous_bugbear_spell_probabilities = {}
barbarous_bugbear_initial_stats = barbarous_bugbear_stats.copy()
barbarous_bugbear = Monster("Barbarous Bugbear", barbarous_bugbear_stats, barbarous_bugbear_gear, barbarous_bugbear_loot_table, difficulty=120, description=barbarous_bugbear_description, floor_range=barbarous_bugbear_floor_range, spells=barbarous_bugbear_spells, spell_probabilities=barbarous_bugbear_spell_probabilities, initial_stats=barbarous_bugbear_initial_stats)

hobgoblin_warmage_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 35,
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 22,
    "Wisdom": 18,
    "Charisma": 14,
    "Element": "Fire"
}
hobgoblin_warmage_gear = ["Flamestaff", "Enchanted Robes"]
hobgoblin_warmage_loot_table = ["Gold", "Arcane Scroll", "Fire Essence"]
hobgoblin_warmage_description = "Hobgoblin Warmages are powerful spellcasters trained in the arcane arts. They wield fiery magic with deadly precision, raining down flames upon their enemies from a safe distance."
hobgoblin_warmage_floor_range = (120, 240)
hobgoblin_warmage_spells = ["Fireball", "Flame Burst", "Inferno"]
hobgoblin_warmage_spell_probabilities = {"Fireball": 0.5, "Flame Burst": 0.3, "Inferno": 0.2}
hobgoblin_warmage_initial_stats = hobgoblin_warmage_stats.copy()
hobgoblin_warmage = Monster("Hobgoblin Warmage", hobgoblin_warmage_stats, hobgoblin_warmage_gear, hobgoblin_warmage_loot_table, difficulty=120, description=hobgoblin_warmage_description, floor_range=hobgoblin_warmage_floor_range, spells=hobgoblin_warmage_spells, spell_probabilities=hobgoblin_warmage_spell_probabilities, initial_stats=hobgoblin_warmage_initial_stats)

half_orc_champion_stats = {
    "HP": 350,
    "Damage": 70,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 32,
    "Dexterity": 18,
    "Constitution": 28,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 22,
    "Element": "None"
}
half_orc_champion_gear = ["Tribal War Axe", "Heavy Tribal Armor"]
half_orc_champion_loot_table = ["Gold", "Tribal Pendant", "Champion's Trophy"]
half_orc_champion_description = "Half-Orc Tribal Champions are revered leaders among their clans, possessing immense strength and skill in battle. They wield massive war axes and wear heavy armor adorned with tribal markings, inspiring fear and respect in their foes."
half_orc_champion_floor_range = (70, 140)
half_orc_champion_spells = []
half_orc_champion_spell_probabilities = {}
half_orc_champion_initial_stats = half_orc_champion_stats.copy()
half_orc_champion = Monster("Half-Orc Tribal Champion", half_orc_champion_stats, half_orc_champion_gear, half_orc_champion_loot_table, difficulty=70, description=half_orc_champion_description, floor_range=half_orc_champion_floor_range, spells=half_orc_champion_spells, spell_probabilities=half_orc_champion_spell_probabilities, initial_stats=half_orc_champion_initial_stats)

ogre_mage_knight_stats = {
    "HP": 400,
    "Damage": 80,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 35,
    "Dexterity": 25,
    "Constitution": 32,
    "Intelligence": 28,
    "Wisdom": 26,
    "Charisma": 30,
    "Element": "None"
}
ogre_mage_knight_gear = ["Arcane Battleaxe", "Enchanted Plate Armor"]
ogre_mage_knight_loot_table = ["Gold", "Ogre Mage Rune", "Knight's Crest"]
ogre_mage_knight_description = "Ogre Mage Knights are elite warriors skilled in both martial combat and arcane magic. They wield enchanted battleaxes and wear heavy plate armor adorned with magical runes."
ogre_mage_knight_floor_range = (100, 200)
ogre_mage_knight_spells = ["Arcane Blast", "Shield of Magic", "Teleport Strike"]
ogre_mage_knight_spell_probabilities = {"Arcane Blast": 0.4, "Shield of Magic": 0.3, "Teleport Strike": 0.3}
ogre_mage_knight_initial_stats = ogre_mage_knight_stats.copy()
ogre_mage_knight = Monster("Ogre Mage Knight", ogre_mage_knight_stats, ogre_mage_knight_gear, ogre_mage_knight_loot_table, difficulty=100, description=ogre_mage_knight_description, floor_range=ogre_mage_knight_floor_range, spells=ogre_mage_knight_spells, spell_probabilities=ogre_mage_knight_spell_probabilities, initial_stats=ogre_mage_knight_initial_stats)

ogre_mage_stats = {
    "HP": 350,
    "Damage": 70,
    "Defense": 50,
    "Magic Defense": 60,
    "Strength": 32,
    "Dexterity": 28,
    "Constitution": 30,
    "Intelligence": 26,
    "Wisdom": 24,
    "Charisma": 28,
    "Element": "None"
}
ogre_mage_gear = ["Arcane Staff", "Enchanted Robes"]
ogre_mage_loot_table = ["Gold", "Ogre Mage Rune", "Arcane Essence"]
ogre_mage_description = "Ogre Mages are powerful spellcasters with immense physical strength. They wield arcane staffs and wear enchanted robes, channeling raw magic to devastating effect in battle."
ogre_mage_floor_range = (90, 180)
ogre_mage_spells = ["Arcane Bolt", "Mana Shield", "Thunderstorm"]
ogre_mage_spell_probabilities = {"Arcane Bolt": 0.4, "Mana Shield": 0.3, "Thunderstorm": 0.3}
ogre_mage_initial_stats = ogre_mage_stats.copy()
ogre_mage = Monster("Ogre Mage", ogre_mage_stats, ogre_mage_gear, ogre_mage_loot_table, difficulty=90, description=ogre_mage_description, floor_range=ogre_mage_floor_range, spells=ogre_mage_spells, spell_probabilities=ogre_mage_spell_probabilities, initial_stats=ogre_mage_initial_stats)

orc_rager_stats = {
    "HP": 320,
    "Damage": 65,
    "Defense": 45,
    "Magic Defense": 35,
    "Strength": 30,
    "Dexterity": 28,
    "Constitution": 28,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 20,
    "Element": "None"
}
orc_rager_gear = ["Furious Greataxe", "Rage-Forged Armor"]
orc_rager_loot_table = ["Gold", "Orcish Trophy", "Rage Shard"]
orc_rager_description = "Orc Ragers are ferocious warriors fueled by uncontrollable rage. They wield massive greataxes with reckless abandon, carving through their enemies with savage fury."
orc_rager_floor_range = (80, 160)
orc_rager_spells = ["Berserker Fury", "Rage Strike", "Bloodlust"]
orc_rager_spell_probabilities = {"Berserker Fury": 0.4, "Rage Strike": 0.3, "Bloodlust": 0.3}
orc_rager_initial_stats = orc_rager_stats.copy()
orc_rager = Monster("Orc Rager", orc_rager_stats, orc_rager_gear, orc_rager_loot_table, difficulty=80, description=orc_rager_description, floor_range=orc_rager_floor_range, spells=orc_rager_spells, spell_probabilities=orc_rager_spell_probabilities, initial_stats=orc_rager_initial_stats)

half_orc_commander_stats = {
    "HP": 380,
    "Damage": 70,
    "Defense": 50,
    "Magic Defense": 45,
    "Strength": 34,
    "Dexterity": 28,
    "Constitution": 32,
    "Intelligence": 24,
    "Wisdom": 26,
    "Charisma": 30,
    "Element": "None"
}
half_orc_commander_gear = ["Commander's Warhammer", "Tactical Plate Armor"]
half_orc_commander_loot_table = ["Gold", "Half-Orc Medal", "Tactical Map"]
half_orc_commander_description = "Half-Orc Commanders are seasoned leaders on the battlefield, wielding warhammers with tactical precision. Clad in heavy plate armor, they inspire their troops with strategic prowess and unmatched ferocity."
half_orc_commander_floor_range = (90, 180)
half_orc_commander_spells = ["War Cry", "Tactical Strike", "Rallying Banner"]
half_orc_commander_spell_probabilities = {"War Cry": 0.4, "Tactical Strike": 0.3, "Rallying Banner": 0.3}
half_orc_commander_initial_stats = half_orc_commander_stats.copy()
half_orc_commander = Monster("Half-Orc Commander", half_orc_commander_stats, half_orc_commander_gear, half_orc_commander_loot_table, difficulty=90, description=half_orc_commander_description, floor_range=half_orc_commander_floor_range, spells=half_orc_commander_spells, spell_probabilities=half_orc_commander_spell_probabilities, initial_stats=half_orc_commander_initial_stats)

high_orc_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 40,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Physical"
}

high_orc_gear = ["Orcish Battleaxe", "Iron Armor"]
high_orc_loot_table = ["Orcish Charm", "Trophy Tusk", "Brutal Bone"]
high_orc_description = "High Orcs are formidable warriors known for their brute strength and ferocity in battle. They often lead orcish tribes and are feared for their relentless aggression."
high_orc_floor_range = (40, 45)
high_orc_spells = []
high_orc_spell_probabilities = {}
high_orc_initial_stats = high_orc_stats.copy()
high_orc = Monster("High Orc", high_orc_stats, high_orc_gear, high_orc_loot_table, difficulty=6, description=high_orc_description, floor_range=high_orc_floor_range, spells=high_orc_spells, spell_probabilities=high_orc_spell_probabilities, initial_stats=high_orc_initial_stats)
high_orc_archer_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 20,
    "Element": "Physical"
}

high_orc_archer_gear = ["Orcish Longbow", "Leather Armor"]
high_orc_archer_loot_table = ["Orcish Arrow", "Sharpshooter's Eye", "Bowstring Fiber"]
high_orc_archer_description = "High Orc Archers are skilled marksmen among orcish tribes. They rain down arrows upon their enemies with deadly accuracy, often serving as scouts and ranged support."
high_orc_archer_floor_range = (41, 46)
high_orc_archer_spells = []
high_orc_archer_spell_probabilities = {}
high_orc_archer_initial_stats = high_orc_archer_stats.copy()
high_orc_archer = Monster("High Orc Archer", high_orc_archer_stats, high_orc_archer_gear, high_orc_archer_loot_table, difficulty=6, description=high_orc_archer_description, floor_range=high_orc_archer_floor_range, spells=high_orc_archer_spells, spell_probabilities=high_orc_archer_spell_probabilities, initial_stats=high_orc_archer_initial_stats)
high_orc_berserker_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 45,
    "Dexterity": 28,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 20,
    "Element": "Physical"
}

high_orc_berserker_gear = ["Orcish Greataxe", "Bloodied Armor"]
high_orc_berserker_loot_table = ["Berserker Rage", "Frenzied Horn", "Savage Skull"]
high_orc_berserker_description = "High Orc Berserkers are fierce warriors fueled by rage and adrenaline. They charge into battle with reckless abandon, striking fear into the hearts of their foes."
high_orc_berserker_floor_range = (42, 47)
high_orc_berserker_spells = []
high_orc_berserker_spell_probabilities = {}
high_orc_berserker_initial_stats = high_orc_berserker_stats.copy()
high_orc_berserker = Monster("High Orc Berserker", high_orc_berserker_stats, high_orc_berserker_gear, high_orc_berserker_loot_table, difficulty=7, description=high_orc_berserker_description, floor_range=high_orc_berserker_floor_range, spells=high_orc_berserker_spells, spell_probabilities=high_orc_berserker_spell_probabilities, initial_stats=high_orc_berserker_initial_stats)

goblin_tinkerer_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 25,
    "Intelligence": 28,
    "Wisdom": 30,
    "Charisma": 28,
    "Element": "Physical"
}

goblin_tinkerer_gear = ["Goblin Wrench", "Mechanical Gadgets"]
goblin_tinkerer_loot_table = ["Tinkerer's Blueprint", "Ingenious Contraption", "Scrap Metal"]
goblin_tinkerer_description = "Goblin Tinkerers are inventive engineers skilled at crafting mechanical contraptions and traps. They use their intellect to outsmart enemies and protect their lairs."
goblin_tinkerer_floor_range = (38, 43)
goblin_tinkerer_spells = []
goblin_tinkerer_spell_probabilities = {}
goblin_tinkerer_initial_stats = goblin_tinkerer_stats.copy()
goblin_tinkerer = Monster("Goblin Tinkerer", goblin_tinkerer_stats, goblin_tinkerer_gear, goblin_tinkerer_loot_table, difficulty=5, description=goblin_tinkerer_description, floor_range=goblin_tinkerer_floor_range, spells=goblin_tinkerer_spells, spell_probabilities=goblin_tinkerer_spell_probabilities, initial_stats=goblin_tinkerer_initial_stats)

goblin_bomber_stats = {
    "HP": 80,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 15,
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "None"
}
goblin_bomber_gear = ["Explosive Pouches", "Dagger"]
goblin_bomber_loot_table = ["Bomb Components", "Scorched Coin", "Gold"]
goblin_bomber_description = "Goblin Bombers are pyromaniacs, specializing in crafting and hurling makeshift explosives at their enemies. They revel in chaos and destruction, often giggling maniacally as they rain fiery destruction down upon their foes."
goblin_bomber_floor_range = (10, 30)
goblin_bomber_spells = []
goblin_bomber_spell_probabilities = {}
goblin_bomber_initial_stats = goblin_bomber_stats.copy()
goblin_bomber = Monster("Goblin Bomber", goblin_bomber_stats, goblin_bomber_gear, goblin_bomber_loot_table, difficulty=10, description=goblin_bomber_description, floor_range=goblin_bomber_floor_range, spells=goblin_bomber_spells, spell_probabilities=goblin_bomber_spell_probabilities, initial_stats=goblin_bomber_initial_stats)

goblin_sharpshooter_stats = {
    "HP": 90,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
goblin_sharpshooter_gear = ["Longbow", "Leather Armor"]
goblin_sharpshooter_loot_table = ["Sharpened Arrow", "Pierced Coin", "Gold"]
goblin_sharpshooter_description = "Goblin Sharpshooters are deadly marksmen, picking off their enemies from afar with remarkable accuracy. They favor hit-and-run tactics, using their agility and cunning to outmaneuver larger opponents while raining down arrows upon them."
goblin_sharpshooter_floor_range = (10, 30)
goblin_sharpshooter_spells = []
goblin_sharpshooter_spell_probabilities = {}
goblin_sharpshooter_initial_stats = goblin_sharpshooter_stats.copy()
goblin_sharpshooter = Monster("Goblin Sharpshooter", goblin_sharpshooter_stats, goblin_sharpshooter_gear, goblin_sharpshooter_loot_table, difficulty=10, description=goblin_sharpshooter_description, floor_range=goblin_sharpshooter_floor_range, spells=goblin_sharpshooter_spells, spell_probabilities=goblin_sharpshooter_spell_probabilities, initial_stats=goblin_sharpshooter_initial_stats)

goblin_trickster_stats = {
    "HP": 70,
    "Damage": 20,
    "Defense": 12,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 14,
    "Wisdom": 12,
    "Charisma": 16,
    "Element": "None"
}
goblin_trickster_gear = ["Dagger", "Illusionist's Cloak"]
goblin_trickster_loot_table = ["Trickster's Charm", "Deceptive Coin", "Gold"]
goblin_trickster_description = "Goblin Tricksters are mischievous rogues, using their cunning and deception to confound their enemies. They excel at stealthy maneuvers and dirty tricks, often employing illusions and traps to outsmart their foes."
goblin_trickster_floor_range = (10, 30)
goblin_trickster_spells = []
goblin_trickster_spell_probabilities = {}
goblin_trickster_initial_stats = goblin_trickster_stats.copy()
goblin_trickster = Monster("Goblin Trickster", goblin_trickster_stats, goblin_trickster_gear, goblin_trickster_loot_table, difficulty=10, description=goblin_trickster_description, floor_range=goblin_trickster_floor_range, spells=goblin_trickster_spells, spell_probabilities=goblin_trickster_spell_probabilities, initial_stats=goblin_trickster_initial_stats)

cave_goblin_hunter_stats = {
    "HP": 100,
    "Damage": 35,
    "Defense": 18,
    "Magic Defense": 12,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
cave_goblin_hunter_gear = ["Hunting Bow", "Stalker's Garb"]
cave_goblin_hunter_loot_table = ["Trophy Pelt", "Hunting Arrow", "Gold"]
cave_goblin_hunter_description = "Cave Goblin Hunters are skilled trackers and marksmen, navigating the dark caverns of their home with ease. They rely on stealth and precision to take down their prey, using their keen senses to ambush unwary travelers."
cave_goblin_hunter_floor_range = (10, 30)
cave_goblin_hunter_spells = []
cave_goblin_hunter_spell_probabilities = {}
cave_goblin_hunter_initial_stats = cave_goblin_hunter_stats.copy()
cave_goblin_hunter = Monster("Cave Goblin Hunter", cave_goblin_hunter_stats, cave_goblin_hunter_gear, cave_goblin_hunter_loot_table, difficulty=10, description=cave_goblin_hunter_description, floor_range=cave_goblin_hunter_floor_range, spells=cave_goblin_hunter_spells, spell_probabilities=cave_goblin_hunter_spell_probabilities, initial_stats=cave_goblin_hunter_initial_stats)

high_orc_skirmisher_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 22,
    "Magic Defense": 18,
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
high_orc_skirmisher_gear = ["Skirmisher's Axe", "Chainmail"]
high_orc_skirmisher_loot_table = ["High Orc Tusk", "Battle Trophy", "Gold"]
high_orc_skirmisher_description = "High Orc Skirmishers are agile and aggressive fighters, specializing in hit-and-run tactics on the battlefield. They excel at harassing enemy lines, darting in and out of combat to sow chaos and confusion among their foes."
high_orc_skirmisher_floor_range = (30, 60)
high_orc_skirmisher_spells = []
high_orc_skirmisher_spell_probabilities = {}
high_orc_skirmisher_initial_stats = high_orc_skirmisher_stats.copy()
high_orc_skirmisher = Monster("High Orc Skirmisher", high_orc_skirmisher_stats, high_orc_skirmisher_gear, high_orc_skirmisher_loot_table, difficulty=30, description=high_orc_skirmisher_description, floor_range=high_orc_skirmisher_floor_range, spells=high_orc_skirmisher_spells, spell_probabilities=high_orc_skirmisher_spell_probabilities, initial_stats=high_orc_skirmisher_initial_stats)

high_orc_firebrand_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 22,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Fire"
}
high_orc_firebrand_gear = ["Flaming Warhammer", "Fireproof Plate"]
high_orc_firebrand_loot_table = ["High Orc Horn", "Charred Relic", "Gold"]
high_orc_firebrand_description = "High Orc Firebrands are fearsome warriors, wielding weapons wreathed in flames and armor resistant to heat. They charge into battle with unmatched ferocity, leaving a trail of scorched earth and smoldering enemies in their wake."
high_orc_firebrand_floor_range = (30, 60)
high_orc_firebrand_spells = []
high_orc_firebrand_spell_probabilities = {}
high_orc_firebrand_initial_stats = high_orc_firebrand_stats.copy()
high_orc_firebrand = Monster("High Orc Firebrand", high_orc_firebrand_stats, high_orc_firebrand_gear, high_orc_firebrand_loot_table, difficulty=30, description=high_orc_firebrand_description, floor_range=high_orc_firebrand_floor_range, spells=high_orc_firebrand_spells, spell_probabilities=high_orc_firebrand_spell_probabilities, initial_stats=high_orc_firebrand_initial_stats)

savage_orc_brute_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 14,
    "Constitution": 22,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"
}
savage_orc_brute_gear = ["Giant Club", "Fur Loincloth"]
savage_orc_brute_loot_table = ["Orcish Trophy", "Savage Relic", "Gold"]
savage_orc_brute_description = "Savage Orc Brutes are towering behemoths, wielding massive clubs with devastating force. They revel in primal rage, tearing through their enemies with raw strength and ferocity, leaving nothing but destruction in their wake."
savage_orc_brute_floor_range = (60, 90)
savage_orc_brute_spells = []
savage_orc_brute_spell_probabilities = {}
savage_orc_brute_initial_stats = savage_orc_brute_stats.copy()
savage_orc_brute = Monster("Savage Orc Brute", savage_orc_brute_stats, savage_orc_brute_gear, savage_orc_brute_loot_table, difficulty=60, description=savage_orc_brute_description, floor_range=savage_orc_brute_floor_range, spells=savage_orc_brute_spells, spell_probabilities=savage_orc_brute_spell_probabilities, initial_stats=savage_orc_brute_initial_stats)

orc_grunt_stats = {
    "HP": 120,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
orc_grunt_gear = ["Orcish Axe", "Rough Iron Armor"]
orc_grunt_loot_table = ["Orcish Trophy", "Grunt's Token", "Gold"]
orc_grunt_description = "Orc Grunts are the foot soldiers of orcish armies, wielding axes and wearing crude armor into battle. Though lacking in finesse, they make up for it with sheer brute strength and unrelenting aggression."
orc_grunt_floor_range = (30, 60)
orc_grunt_spells = []
orc_grunt_spell_probabilities = {}
orc_grunt_initial_stats = orc_grunt_stats.copy()
orc_grunt = Monster("Orc Grunt", orc_grunt_stats, orc_grunt_gear, orc_grunt_loot_table, difficulty=30, description=orc_grunt_description, floor_range=orc_grunt_floor_range, spells=orc_grunt_spells, spell_probabilities=orc_grunt_spell_probabilities, initial_stats=orc_grunt_initial_stats)

hobgoblin_battlemage_stats = {
    "HP": 150,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 18,
    "Intelligence": 18,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "None"
}
hobgoblin_battlemage_gear = ["Arcane Staff", "Robes of Power"]
hobgoblin_battlemage_loot_table = ["Arcane Essence", "Mage's Grimoire", "Gold"]
hobgoblin_battlemage_description = "Hobgoblin Battlemages are formidable spellcasters, blending martial prowess with arcane magic on the battlefield. They unleash devastating spells upon their enemies, turning the tide of battle with thunderous blasts and fiery explosions."
hobgoblin_battlemage_floor_range = (30, 60)
hobgoblin_battlemage_spells = ["Fireball", "Thunderbolt", "Arcane Barrage"]
hobgoblin_battlemage_spell_probabilities = {"Fireball": 0.4, "Thunderbolt": 0.3, "Arcane Barrage": 0.3}
hobgoblin_battlemage_initial_stats = hobgoblin_battlemage_stats.copy()
hobgoblin_battlemage = Monster("Hobgoblin Battlemage", hobgoblin_battlemage_stats, hobgoblin_battlemage_gear, hobgoblin_battlemage_loot_table, difficulty=30, description=hobgoblin_battlemage_description, floor_range=hobgoblin_battlemage_floor_range, spells=hobgoblin_battlemage_spells, spell_probabilities=hobgoblin_battlemage_spell_probabilities, initial_stats=hobgoblin_battlemage_initial_stats)

hobgoblin_sentinel_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"
}
hobgoblin_sentinel_gear = ["Tower Shield", "Halberd"]
hobgoblin_sentinel_loot_table = ["Hobgoblin Insignia", "Sentinel's Badge", "Gold"]
hobgoblin_sentinel_description = "Hobgoblin Sentinels are stalwart defenders, wielding tower shields and halberds to guard key positions on the battlefield. They stand resolute against enemy attacks, their disciplined formations acting as an impenetrable barrier against all who would oppose them."
hobgoblin_sentinel_floor_range = (30, 60)
hobgoblin_sentinel_spells = []
hobgoblin_sentinel_spell_probabilities = {}
hobgoblin_sentinel_initial_stats = hobgoblin_sentinel_stats.copy()
hobgoblin_sentinel = Monster("Hobgoblin Sentinel", hobgoblin_sentinel_stats, hobgoblin_sentinel_gear, hobgoblin_sentinel_loot_table, difficulty=30, description=hobgoblin_sentinel_description, floor_range=hobgoblin_sentinel_floor_range, spells=hobgoblin_sentinel_spells, spell_probabilities=hobgoblin_sentinel_spell_probabilities, initial_stats=hobgoblin_sentinel_initial_stats)
