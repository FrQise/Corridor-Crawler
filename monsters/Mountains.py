from monsters.bestiary import Monster

harpy_stats = {
    "HP": 100,  # Define HP attribute for Harpy
    "Damage": 40,  # Define damage attribute for Harpy
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 14,
    "Element": "Air"  # Define elemental attribute of the Harpy's attack
}
harpy_gear = ["Talon", "Feathered Cloak"]
harpy_loot_table = ["Gold", "Harpy Feather", "Shiny Trinket"]
harpy_description = "Harpies are vicious creatures with the body of a bird and the torso of a human. They soar through the skies with graceful ease, swooping down to attack their prey with razor-sharp talons and piercing shrieks. Beware their hypnotic song, for those who hear it may fall under their spell."
harpy_floor_range = (15, 25)
harpy_spells = ["Siren Song", "Wing Buffet"]
harpy_spell_probabilities = {"Siren Song": 0.7, "Wing Buffet": 0.3} 
harpy_initial_stats = harpy_stats.copy() # Make a copy of the initial stats
harpy = Monster("Harpy", harpy_stats, harpy_gear, harpy_loot_table, difficulty=15, description=harpy_description, floor_range=harpy_floor_range, spells=harpy_spells, spell_probabilities=harpy_spell_probabilities, initial_stats=harpy_initial_stats)

cockatrice_stats = {
    "HP": 160,  # Define HP attribute for Cockatrice
    "Damage": 50,  # Define damage attribute for Cockatrice
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Cockatrice's attack
}
cockatrice_gear = ["Razor Beak", "Stone Scales"]
cockatrice_loot_table = ["Gold", "Cockatrice Feather", "Petrified Eye"]
cockatrice_description = "Cockatrices are fearsome creatures with the body of a bird and the tail of a serpent. They are known for their petrifying gaze, capable of turning their victims to stone with a single glance. Their razor-sharp beaks and stone scales make them dangerous adversaries, striking fear into the hearts of travelers."
cockatrice_floor_range = (1,5)
cockatrice_spells = []
cockatrice_spell_probabilities = {}
cockatrice_initial_stats = cockatrice_stats.copy() # Make a copy of the initial stats
cockatrice = Monster("Cockatrice", cockatrice_stats, cockatrice_gear, cockatrice_loot_table, difficulty=20, description=cockatrice_description, floor_range=cockatrice_floor_range, spells=cockatrice_spells, spell_probabilities=cockatrice_spell_probabilities, initial_stats=cockatrice_initial_stats)

cyclops_stats = {
    "HP": 350,  # Define HP attribute for Cyclops
    "Damage": 90,  # Define damage attribute for Cyclops
    "Defense": 60,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 35,
    "Dexterity": 16,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Cyclops's attack
}
cyclops_gear = ["Giant Club", "Thick Hide"]
cyclops_loot_table = ["Gold", "Cyclops Eye", "Giant Club"]
cyclops_description = "Cyclopes are towering giants with a single eye in the center of their forehead. They are known for their immense strength and ferocity in battle, wielding massive clubs with devastating force. Despite their brutish appearance, they are cunning fighters, capable of outsmarting their opponents with clever tactics."
cyclops_floor_range = (80, 150)
cyclops_spells = []
cyclops_spell_probabilities = {}
cyclops_initial_stats = cyclops_stats.copy() # Make a copy of the initial stats
cyclops = Monster("Cyclops", cyclops_stats, cyclops_gear, cyclops_loot_table, difficulty=80, description=cyclops_description, floor_range=cyclops_floor_range, spells=cyclops_spells, spell_probabilities=cyclops_spell_probabilities, initial_stats=cyclops_initial_stats)

stone_golem_stats = {
    "HP": 400,  # Define HP attribute for Stone Golem
    "Damage": 100,  # Define damage attribute for Stone Golem
    "Defense": 70,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 35,
    "Dexterity": 10,
    "Constitution": 35,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Earth"  # Define elemental attribute of the Stone Golem's attack
}
stone_golem_gear = ["Massive Fists", "Stone Armor"]
stone_golem_loot_table = ["Gold", "Stone Golem Core", "Cracked Stone"]
stone_golem_description = "Stone Golems are towering constructs sculpted from solid rock and brought to life through ancient rituals. Impervious to all but the most powerful attacks, they are formidable guardians of ancient ruins and secret chambers. With their immense strength and durability, they crush all who dare to trespass upon their domain."
stone_golem_floor_range = (100, 200)
stone_golem_spells = []
stone_golem_spell_probabilities = {}
stone_golem_initial_stats = stone_golem_stats.copy() # Make a copy of the initial stats
stone_golem = Monster("Stone Golem", stone_golem_stats, stone_golem_gear, stone_golem_loot_table, difficulty=100, description=stone_golem_description, floor_range=stone_golem_floor_range, spells=stone_golem_spells, spell_probabilities=stone_golem_spell_probabilities, initial_stats=stone_golem_initial_stats)

griffon_stats = {
    "HP": 320,  # Define HP attribute for Griffon
    "Damage": 85,  # Define damage attribute for Griffon
    "Defense": 55,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 32,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "None"  # Define elemental attribute of the Griffon's attack
}
griffon_gear = ["Razor-sharp Talons", "Feathered Hide"]
griffon_loot_table = ["Gold", "Griffon Feather", "Eagle Eye"]
griffon_description = "Griffons are majestic creatures with the body of a lion and the wings of an eagle. They soar through the skies with unmatched grace and agility, hunting their prey from above. With their razor-sharp talons and powerful beaks, they strike with deadly precision, making them fearsome adversaries to those who dare to challenge them."
griffon_floor_range = (100, 200)
griffon_spells = []
griffon_spell_probabilities = {}
griffon_initial_stats = griffon_stats.copy() # Make a copy of the initial stats
griffon = Monster("Griffon", griffon_stats, griffon_gear, griffon_loot_table, difficulty=100, description=griffon_description, floor_range=griffon_floor_range, spells=griffon_spells, spell_probabilities=griffon_spell_probabilities, initial_stats=griffon_initial_stats)

yeti_stats = {
    "HP": 350,  # Define HP attribute for Yeti
    "Damage": 100,  # Define damage attribute for Yeti
    "Defense": 60,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 32,
    "Dexterity": 18,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Ice"  # Define elemental attribute of the Yeti's attack
}
yeti_gear = ["Icy Claws", "Thick Fur"]
yeti_loot_table = ["Gold", "Yeti Claw", "Frost Gem"]
yeti_description = "Yetis are formidable creatures that inhabit the frozen wastelands of the north, towering over their prey with immense size and strength. Covered in thick fur to withstand the biting cold, they are skilled hunters capable of tracking their quarry for miles across the snow-covered terrain. With their icy claws and freezing breath, they strike fear into the hearts of those who venture into their domain."
yeti_floor_range = (100, 200)
yeti_spells = []
yeti_spell_probabilities = {}
yeti_initial_stats = yeti_stats.copy() # Make a copy of the initial stats
yeti = Monster("Yeti", yeti_stats, yeti_gear, yeti_loot_table, difficulty=100, description=yeti_description, floor_range=yeti_floor_range, spells=yeti_spells, spell_probabilities=yeti_spell_probabilities, initial_stats=yeti_initial_stats)

rock_elemental_stats = {
    "HP": 400,  # Define HP attribute for Rock Elemental
    "Damage": 80,  # Define damage attribute for Rock Elemental
    "Defense": 70,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 35,
    "Dexterity": 10,
    "Constitution": 35,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Earth"  # Define elemental attribute of the Rock Elemental's attack
}
rock_elemental_gear = ["Rocky Fists", "Stone Armor"]
rock_elemental_loot_table = ["Gold", "Rock Elemental Core", "Polished Stone"]
rock_elemental_description = "Rock Elementals are massive creatures formed from animated boulders and earth. They roam the mountainous terrain, blending in with the rocky landscape. With their immense strength and durability, they are nearly indestructible, shrugging off all but the most powerful attacks. Their rocky fists pummel foes into submission, leaving nothing but rubble in their wake."
rock_elemental_floor_range = (120, 240)
rock_elemental_spells = []
rock_elemental_spell_probabilities = {}
rock_elemental_initial_stats = rock_elemental_stats.copy() # Make a copy of the initial stats
rock_elemental = Monster("Rock Elemental", rock_elemental_stats, rock_elemental_gear, rock_elemental_loot_table, difficulty=120, description=rock_elemental_description, floor_range=rock_elemental_floor_range, spells=rock_elemental_spells, spell_probabilities=rock_elemental_spell_probabilities, initial_stats=rock_elemental_initial_stats)

mountain_lion_stats = {
    "HP": 180,  # Define HP attribute for Mountain Lion
    "Damage": 60,  # Define damage attribute for Mountain Lion
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 30,
    "Constitution": 18,
    "Intelligence": 6,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Mountain Lion's attack
}
mountain_lion_gear = ["Razor-sharp Claws", "Thick Fur"]
mountain_lion_loot_table = ["Gold", "Mountain Lion Pelt", "Sharp Claw"]
mountain_lion_description = "Mountain Lions are sleek and agile predators that stalk the rocky slopes and craggy cliffs of the mountains. With their keen senses and lightning-fast reflexes, they are skilled hunters capable of ambushing their prey with deadly precision. Their razor-sharp claws and powerful jaws make short work of any unfortunate enough to cross their path."
mountain_lion_floor_range = (60, 120)
mountain_lion_spells = []
mountain_lion_spell_probabilities = {}
mountain_lion_initial_stats = mountain_lion_stats.copy() # Make a copy of the initial stats
mountain_lion = Monster("Mountain Lion", mountain_lion_stats, mountain_lion_gear, mountain_lion_loot_table, difficulty=60, description=mountain_lion_description, floor_range=mountain_lion_floor_range, spells=mountain_lion_spells, spell_probabilities=mountain_lion_spell_probabilities, initial_stats=mountain_lion_initial_stats)

mountain_goat_stats = {
    "HP": 200,  # Define HP attribute for Mountain Goat
    "Damage": 50,  # Define damage attribute for Mountain Goat
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 22,
    "Dexterity": 28,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Mountain Goat's attack
}
mountain_goat_gear = ["Horns", "Thick Hide"]
mountain_goat_loot_table = ["Gold", "Mountain Goat Horn", "Wool"]
mountain_goat_description = "Mountain Goats are sure-footed creatures that inhabit the rugged slopes and sheer cliffs of the mountains. With their powerful legs and sharp horns, they navigate treacherous terrain with ease, leaping from rock to rock in search of food. Though they may appear docile, they are fiercely territorial and will not hesitate to defend themselves if threatened."
mountain_goat_floor_range = (80, 160)
mountain_goat_spells = []
mountain_goat_spell_probabilities = {}
mountain_goat_initial_stats = mountain_goat_stats.copy() # Make a copy of the initial stats
mountain_goat = Monster("Mountain Goat", mountain_goat_stats, mountain_goat_gear, mountain_goat_loot_table, difficulty=80, description=mountain_goat_description, floor_range=mountain_goat_floor_range, spells=mountain_goat_spells, spell_probabilities=mountain_goat_spell_probabilities, initial_stats=mountain_goat_initial_stats)

giant_eagle_stats = {
    "HP": 280,  # Define HP attribute for Giant Eagle
    "Damage": 75,  # Define damage attribute for Giant Eagle
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 26,
    "Dexterity": 30,
    "Constitution": 24,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "Air"  # Define elemental attribute of the Giant Eagle's attack
}
giant_eagle_gear = ["Razor-sharp Talons", "Feathered Wings"]
giant_eagle_loot_table = ["Gold", "Giant Eagle Feather", "Wind Essence"]
giant_eagle_description = "Giant Eagles are majestic birds of prey that soar high above the mountain peaks, scanning the landscape for signs of food. With their keen eyesight and swift flight, they are skilled hunters, capable of swooping down from the sky to snatch up unsuspecting prey. With their razor-sharp talons and powerful beaks, they strike with deadly precision, making them fearsome adversaries to those who dare to challenge them."
giant_eagle_floor_range = (100, 200)
giant_eagle_spells = []
giant_eagle_spell_probabilities = {}
giant_eagle_initial_stats = giant_eagle_stats.copy() # Make a copy of the initial stats
giant_eagle = Monster("Giant Eagle", giant_eagle_stats, giant_eagle_gear, giant_eagle_loot_table, difficulty=100, description=giant_eagle_description, floor_range=giant_eagle_floor_range, spells=giant_eagle_spells, spell_probabilities=giant_eagle_spell_probabilities, initial_stats=giant_eagle_initial_stats)

snow_leopard_stats = {
    "HP": 240,  # Define HP attribute for Snow Leopard
    "Damage": 70,  # Define damage attribute for Snow Leopard
    "Defense": 45,  # Define Defense stat vs attack stat
    "Magic Defense": 35,  # Define magic defense vs spells
    "Strength": 24,
    "Dexterity": 28,
    "Constitution": 22,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "None"  # Define elemental attribute of the Snow Leopard's attack
}
snow_leopard_gear = ["Razor-sharp Claws", "Snowy Coat"]
snow_leopard_loot_table = ["Gold", "Snow Leopard Pelt", "Sharp Claw"]
snow_leopard_description = "Snow Leopards are elusive predators that prowl the snowy peaks and icy crevasses of the mountains. With their stealthy movements and fur-lined coats, they blend seamlessly into their wintry surroundings, making them difficult to spot until it's too late. With their razor-sharp claws and lightning-fast reflexes, they are skilled hunters capable of taking down prey much larger than themselves."
snow_leopard_floor_range = (80, 160)
snow_leopard_spells = []
snow_leopard_spell_probabilities = {}
snow_leopard_initial_stats = snow_leopard_stats.copy() # Make a copy of the initial stats
snow_leopard = Monster("Snow Leopard", snow_leopard_stats, snow_leopard_gear, snow_leopard_loot_table, difficulty=80, description=snow_leopard_description, floor_range=snow_leopard_floor_range, spells=snow_leopard_spells, spell_probabilities=snow_leopard_spell_probabilities, initial_stats=snow_leopard_initial_stats)

mountain_troll_stats = {
    "HP": 380,  # Define HP attribute for Mountain Troll
    "Damage": 110,  # Define damage attribute for Mountain Troll
    "Defense": 65,  # Define Defense stat vs attack stat
    "Magic Defense": 55,  # Define magic defense vs spells
    "Strength": 34,
    "Dexterity": 20,
    "Constitution": 32,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Mountain Troll's attack
}
mountain_troll_gear = ["Club", "Rugged Hide"]
mountain_troll_loot_table = ["Gold", "Troll Tooth", "Stone Club"]
mountain_troll_description = "Mountain Trolls are brutish creatures that dwell in the deep caverns and rugged peaks of the mountains. With their massive size and strength, they are capable of crushing boulders with their bare hands and tearing through solid rock with their sharp claws. Though not the most intelligent of creatures, they make up for it with sheer brute force, overpowering their enemies with relentless ferocity."
mountain_troll_floor_range = (120, 240)
mountain_troll_spells = []
mountain_troll_spell_probabilities = {}
mountain_troll_initial_stats = mountain_troll_stats.copy() # Make a copy of the initial stats
mountain_troll = Monster("Mountain Troll", mountain_troll_stats, mountain_troll_gear, mountain_troll_loot_table, difficulty=120, description=mountain_troll_description, floor_range=mountain_troll_floor_range, spells=mountain_troll_spells, spell_probabilities=mountain_troll_spell_probabilities, initial_stats=mountain_troll_initial_stats)

frost_wyrm_stats = {
    "HP": 420,  # Define HP attribute for Frost Wyrm
    "Damage": 130,  # Define damage attribute for Frost Wyrm
    "Defense": 75,  # Define Defense stat vs attack stat
    "Magic Defense": 65,  # Define magic defense vs spells
    "Strength": 36,
    "Dexterity": 20,
    "Constitution": 38,
    "Intelligence": 14,
    "Wisdom": 18,
    "Charisma": 14,
    "Element": "Ice"  # Define elemental attribute of the Frost Wyrm's attack
}
frost_wyrm_gear = ["Frozen Fangs", "Icy Scales"]
frost_wyrm_loot_table = ["Gold", "Frost Wyrm Scale", "Frozen Heart"]
frost_wyrm_description = "Frost Wyrms are ancient dragons that inhabit the highest peaks of the mountains, ruling over the frozen wastelands with icy breath and razor-sharp claws. With their immense size and power, they are nearly unbeatable in combat, freezing their enemies solid with a single blast of their icy breath. Only the bravest and most skilled warriors dare to challenge them, knowing that defeat means certain death."
frost_wyrm_floor_range = (200, 400)
frost_wyrm_spells = []
frost_wyrm_spell_probabilities = {}
frost_wyrm_initial_stats = frost_wyrm_stats.copy() # Make a copy of the initial stats
frost_wyrm = Monster("Frost Wyrm", frost_wyrm_stats, frost_wyrm_gear, frost_wyrm_loot_table, difficulty=200, description=frost_wyrm_description, floor_range=frost_wyrm_floor_range, spells=frost_wyrm_spells, spell_probabilities=frost_wyrm_spell_probabilities, initial_stats=frost_wyrm_initial_stats)

glacial_bear_stats = {
    "HP": 350,  # Define HP attribute for Glacial Bear
    "Damage": 100,  # Define damage attribute for Glacial Bear
    "Defense": 60,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 34,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Ice"  # Define elemental attribute of the Glacial Bear's attack
}
glacial_bear_gear = ["Frozen Claws", "Thick Fur"]
glacial_bear_loot_table = ["Gold", "Glacial Bear Fur", "Ice Crystal"]
glacial_bear_description = "Glacial Bears are massive creatures that roam the frozen tundra and icy caverns of the mountains. With their thick fur and powerful limbs, they are well-adapted to the harsh conditions of their environment, shrugging off cold temperatures and blizzard winds with ease. Though they may appear slow and lumbering, they are surprisingly agile and deadly in combat, capable of tearing apart prey with their razor-sharp claws."
glacial_bear_floor_range = (150, 300)
glacial_bear_spells = []
glacial_bear_spell_probabilities = {}
glacial_bear_initial_stats = glacial_bear_stats.copy() # Make a copy of the initial stats
glacial_bear = Monster("Glacial Bear", glacial_bear_stats, glacial_bear_gear, glacial_bear_loot_table, difficulty=150, description=glacial_bear_description, floor_range=glacial_bear_floor_range, spells=glacial_bear_spells, spell_probabilities=glacial_bear_spell_probabilities, initial_stats=glacial_bear_initial_stats)

frost_giant_stats = {
    "HP": 500,  # Define HP attribute for Frost Giant
    "Damage": 150,  # Define damage attribute for Frost Giant
    "Defense": 80,  # Define Defense stat vs attack stat
    "Magic Defense": 70,  # Define magic defense vs spells
    "Strength": 40,
    "Dexterity": 18,
    "Constitution": 40,
    "Intelligence": 14,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Ice"  # Define elemental attribute of the Frost Giant's attack
}
frost_giant_gear = ["Ice Hammer", "Glacial Armor"]
frost_giant_loot_table = ["Gold", "Frost Giant's Heart", "Frozen Axe"]
frost_giant_description = "Frost Giants are towering behemoths that inhabit the icy peaks and frozen valleys of the mountains. With their massive size and strength, they wield enormous ice-covered weapons, capable of shattering even the toughest armor with a single blow. Despite their brutish appearance, they possess a cunning intellect, making them formidable opponents in battle."
frost_giant_floor_range = (200, 400)
frost_giant_spells = []
frost_giant_spell_probabilities = {}
frost_giant_initial_stats = frost_giant_stats.copy() # Make a copy of the initial stats
frost_giant = Monster("Frost Giant", frost_giant_stats, frost_giant_gear, frost_giant_loot_table, difficulty=200, description=frost_giant_description, floor_range=frost_giant_floor_range, spells=frost_giant_spells, spell_probabilities=frost_giant_spell_probabilities, initial_stats=frost_giant_initial_stats)

mountain_drake_stats = {
    "HP": 480,  # Define HP attribute for Mountain Drake
    "Damage": 140,  # Define damage attribute for Mountain Drake
    "Defense": 75,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 38,
    "Dexterity": 22,
    "Constitution": 36,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "Earth"  # Define elemental attribute of the Mountain Drake's attack
}
mountain_drake_gear = ["Razor-sharp Claws", "Scaled Hide"]
mountain_drake_loot_table = ["Gold", "Mountain Drake Scale", "Dragon Fang"]
mountain_drake_description = "Mountain Drakes are formidable dragon-like creatures that make their nests in the highest peaks of the mountains. With their powerful wings and razor-sharp claws, they soar through the skies, hunting for prey to feed their insatiable appetites. Known for their fiery breath and formidable strength, they are feared by all who dwell in the shadow of the mountains."
mountain_drake_floor_range = (180, 360)
mountain_drake_spells = []
mountain_drake_spell_probabilities = {}
mountain_drake_initial_stats = mountain_drake_stats.copy() # Make a copy of the initial stats
mountain_drake = Monster("Mountain Drake", mountain_drake_stats, mountain_drake_gear, mountain_drake_loot_table, difficulty=180, description=mountain_drake_description, floor_range=mountain_drake_floor_range, spells=mountain_drake_spells, spell_probabilities=mountain_drake_spell_probabilities, initial_stats=mountain_drake_initial_stats)

mountain_djinn_stats = {
    "HP": 420,  # Define HP attribute for Mountain Djinn
    "Damage": 130,  # Define damage attribute for Mountain Djinn
    "Defense": 70,  # Define Defense stat vs attack stat
    "Magic Defense": 80,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 26,
    "Constitution": 32,
    "Intelligence": 18,
    "Wisdom": 22,
    "Charisma": 20,
    "Element": "Air"  # Define elemental attribute of the Mountain Djinn's attack
}
mountain_djinn_gear = ["Gust Staff", "Ether Robes"]
mountain_djinn_loot_table = ["Gold", "Djinn's Essence", "Storm Crystal"]
mountain_djinn_description = "Mountain Djinns are ancient spirits of the air that dwell among the highest peaks of the mountains. With their mastery over wind and weather, they are capable of summoning powerful storms and gusts of wind to defend their territory. Though they may appear ethereal and insubstantial, they possess great wisdom and arcane knowledge, making them formidable foes in battle."
mountain_djinn_floor_range = (250, 500)
mountain_djinn_spells = []
mountain_djinn_spell_probabilities = {}
mountain_djinn_initial_stats = mountain_djinn_stats.copy() # Make a copy of the initial stats
mountain_djinn = Monster("Mountain Djinn", mountain_djinn_stats, mountain_djinn_gear, mountain_djinn_loot_table, difficulty=250, description=mountain_djinn_description, floor_range=mountain_djinn_floor_range, spells=mountain_djinn_spells, spell_probabilities=mountain_djinn_spell_probabilities, initial_stats=mountain_djinn_initial_stats)

snow_wraith_stats = {
    "HP": 320,  # Define HP attribute for Snow Wraith
    "Damage": 100,  # Define damage attribute for Snow Wraith
    "Defense": 60,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 26,
    "Dexterity": 30,
    "Constitution": 28,
    "Intelligence": 14,
    "Wisdom": 18,
    "Charisma": 16,
    "Element": "Ice"  # Define elemental attribute of the Snow Wraith's attack
}
snow_wraith_gear = ["Icy Claws", "Frozen Mist"]
snow_wraith_loot_table = ["Gold", "Wraith Essence", "Frost Crystal"]
snow_wraith_description = "Snow Wraiths are ghostly apparitions that haunt the frozen peaks and icy caves of the mountains. With their chilling touch and freezing breath, they can drain the warmth from living creatures, leaving them frozen solid. Though they may be incorporeal, they are no less deadly, striking fear into the hearts of those who encounter them."
snow_wraith_floor_range = (150, 300)
snow_wraith_spells = []
snow_wraith_spell_probabilities = {}
snow_wraith_initial_stats = snow_wraith_stats.copy() # Make a copy of the initial stats
snow_wraith = Monster("Snow Wraith", snow_wraith_stats, snow_wraith_gear, snow_wraith_loot_table, difficulty=150, description=snow_wraith_description, floor_range=snow_wraith_floor_range, spells=snow_wraith_spells, spell_probabilities=snow_wraith_spell_probabilities, initial_stats=snow_wraith_initial_stats)

ice_serpent_stats = {
    "HP": 380,  # Define HP attribute for Ice Serpent
    "Damage": 120,  # Define damage attribute for Ice Serpent
    "Defense": 70,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 32,
    "Dexterity": 26,
    "Constitution": 34,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "Ice"  # Define elemental attribute of the Ice Serpent's attack
}
ice_serpent_gear = ["Frozen Fangs", "Icy Scales"]
ice_serpent_loot_table = ["Gold", "Ice Serpent Scale", "Frozen Fang"]
ice_serpent_description = "Ice Serpents are massive reptilian creatures that slither through the snow and ice of the mountainous terrain. With their icy breath and razor-sharp fangs, they can freeze their prey solid in a matter of seconds. Though they may appear slow and sluggish, they are surprisingly agile and can strike with lightning-fast speed, making them formidable predators in their icy domain."
ice_serpent_floor_range = (180, 360)
ice_serpent_spells = []
ice_serpent_spell_probabilities = {}
ice_serpent_initial_stats = ice_serpent_stats.copy() # Make a copy of the initial stats
ice_serpent = Monster("Ice Serpent", ice_serpent_stats, ice_serpent_gear, ice_serpent_loot_table, difficulty=180, description=ice_serpent_description, floor_range=ice_serpent_floor_range, spells=ice_serpent_spells, spell_probabilities=ice_serpent_spell_probabilities, initial_stats=ice_serpent_initial_stats)

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
earth_elemental_loot_table = ["Gold", "Earth Essence", "Crystal Shard"]
earth_elemental_description = "Earth Elementals are beings of solid stone and earth, animated by ancient magic. They wield the power of the earth itself, crushing their enemies beneath massive boulders and summoning earthquakes to shake the ground. Their sturdy form makes them nearly impervious to physical harm."
earth_elemental_floor_range = (25, 50)
earth_elemental_spells = ["Stone Barrage", "Quake"]
earth_elemental_spell_probabilities = {"Stone Barrage": 0.6, "Quake": 0.4} 
earth_elemental_initial_stats = earth_elemental_stats.copy() # Make a copy of the initial stats
earth_elemental = Monster("Earth Elemental", earth_elemental_stats, earth_elemental_gear, earth_elemental_loot_table, difficulty=25, description=earth_elemental_description, floor_range=earth_elemental_floor_range, spells=earth_elemental_spells, spell_probabilities=earth_elemental_spell_probabilities, initial_stats=earth_elemental_initial_stats)

mountain_goblin_warrior_stats = {
    "HP": 80,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 20,
    "Dexterity": 15,
    "Constitution": 18,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_goblin_warrior_gear = ["Crude Sword", "Scrap Shield"]
mountain_goblin_warrior_loot_table = ["Goblin Tooth", "Rusty Armor", "Mountain Ore"]
mountain_goblin_warrior_description = "The Mountain Goblin Warriors are fierce fighters native to the rocky peaks. Armed with crude swords and scrap shields, they defend their territory with unwavering determination."
mountain_goblin_warrior_floor_range = (50, 52)
mountain_goblin_warrior_initial_stats = mountain_goblin_warrior_stats.copy()
mountain_goblin_warrior = Monster("Mountain Goblin Warrior", mountain_goblin_warrior_stats, mountain_goblin_warrior_gear, mountain_goblin_warrior_loot_table, difficulty=5, description=mountain_goblin_warrior_description, floor_range=mountain_goblin_warrior_floor_range, initial_stats=mountain_goblin_warrior_initial_stats)

mountain_goblin_ranger_stats = {
    "HP": 70,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 15,
    "Dexterity": 20,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_goblin_ranger_gear = ["Rugged Bow", "Leather Quiver"]
mountain_goblin_ranger_loot_table = ["Goblin Ear", "Tattered Cloak", "Forest Arrow"]
mountain_goblin_ranger_description = "The Mountain Goblin Rangers are expert archers, adept at hunting prey across the rocky slopes. With rugged bows and leather quivers, they strike from a distance with deadly accuracy."
mountain_goblin_ranger_floor_range = (50, 52)
mountain_goblin_ranger_initial_stats = mountain_goblin_ranger_stats.copy()
mountain_goblin_ranger = Monster("Mountain Goblin Ranger", mountain_goblin_ranger_stats, mountain_goblin_ranger_gear, mountain_goblin_ranger_loot_table, difficulty=5, description=mountain_goblin_ranger_description, floor_range=mountain_goblin_ranger_floor_range, initial_stats=mountain_goblin_ranger_initial_stats)

mountain_goblin_shaman_stats = {
    "HP": 60,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 25,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 14,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Earth"
}

mountain_goblin_shaman_gear = ["Tribal Staff", "Woven Robes"]
mountain_goblin_shaman_loot_table = ["Goblin Skull", "Mystic Totem", "Earthen Root"]
mountain_goblin_shaman_description = "The Mountain Goblin Shamans wield the primal forces of nature to aid their kin. With tribal staffs and woven robes, they channel earth magic, bolstering their allies and wreaking havoc upon intruders."
mountain_goblin_shaman_floor_range = (50, 52)
mountain_goblin_shaman_initial_stats = mountain_goblin_shaman_stats.copy()
mountain_goblin_shaman = Monster("Mountain Goblin Shaman", mountain_goblin_shaman_stats, mountain_goblin_shaman_gear, mountain_goblin_shaman_loot_table, difficulty=5, description=mountain_goblin_shaman_description, floor_range=mountain_goblin_shaman_floor_range, initial_stats=mountain_goblin_shaman_initial_stats)

mountain_goblin_brawler_stats = {
    "HP": 90,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_goblin_brawler_gear = ["Heavy Fists", "Reinforced Bracers"]
mountain_goblin_brawler_loot_table = ["Goblin Knuckle", "Broken Gauntlet", "Mountain Brew"]
mountain_goblin_brawler_description = "The Mountain Goblin Brawlers are known for their brute strength and ferocious combat style. With heavy fists and reinforced bracers, they charge into battle, unleashing devastating blows upon their foes."
mountain_goblin_brawler_floor_range = (50, 52)
mountain_goblin_brawler_initial_stats = mountain_goblin_brawler_stats.copy()
mountain_goblin_brawler = Monster("Mountain Goblin Brawler", mountain_goblin_brawler_stats, mountain_goblin_brawler_gear, mountain_goblin_brawler_loot_table, difficulty=5, description=mountain_goblin_brawler_description, floor_range=mountain_goblin_brawler_floor_range, initial_stats=mountain_goblin_brawler_initial_stats)

mountain_goblin_berserker_stats = {
    "HP": 100,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 10,
    "Strength": 28,
    "Dexterity": 15,
    "Constitution": 22,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_goblin_berserker_gear = ["Savage Axe", "Ragged Hide"]
mountain_goblin_berserker_loot_table = ["Goblin Claw", "Torn Pelt", "Berserker Brew"]
mountain_goblin_berserker_description = "The Mountain Goblin Berserkers are feared for their uncontrollable rage and savage attacks. With savage axes and ragged hides, they charge into battle, heedless of danger, seeking only bloodshed and victory."
mountain_goblin_berserker_floor_range = (50, 52)
mountain_goblin_berserker_initial_stats = mountain_goblin_berserker_stats.copy()
mountain_goblin_berserker = Monster("Mountain Goblin Berserker", mountain_goblin_berserker_stats, mountain_goblin_berserker_gear, mountain_goblin_berserker_loot_table, difficulty=5, description=mountain_goblin_berserker_description, floor_range=mountain_goblin_berserker_floor_range, initial_stats=mountain_goblin_berserker_initial_stats)

mountain_goblin_sapper_stats = {
    "HP": 70,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "Earth"
}

mountain_goblin_sapper_gear = ["Explosive Charge", "Detonator Device"]
mountain_goblin_sapper_loot_table = ["Goblin Gadget", "Singed Wire", "Mountain Brew"]
mountain_goblin_sapper_description = "The Mountain Goblin Sappers specialize in explosives and traps, making them deadly adversaries on the battlefield. With explosive charges and detonator devices, they wreak havoc and chaos upon their enemies."
mountain_goblin_sapper_floor_range = (50, 52)
mountain_goblin_sapper_initial_stats = mountain_goblin_sapper_stats.copy()
mountain_goblin_sapper = Monster("Mountain Goblin Sapper", mountain_goblin_sapper_stats, mountain_goblin_sapper_gear, mountain_goblin_sapper_loot_table, difficulty=5, description=mountain_goblin_sapper_description, floor_range=mountain_goblin_sapper_floor_range, initial_stats=mountain_goblin_sapper_initial_stats)

mountain_orc_warrior_stats = {
    "HP": 100,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 10,
    "Strength": 28,
    "Dexterity": 15,
    "Constitution": 22,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_orc_warrior_gear = ["Rugged Axe", "Iron Shield"]
mountain_orc_warrior_loot_table = ["Orc Tooth", "Tattered Armor", "Mountain Ore"]
mountain_orc_warrior_description = "Mountain Orc Warriors are fierce and battle-hardened fighters, renowned for their strength and resilience. Armed with rugged axes and iron shields, they charge into battle with fearless determination."
mountain_orc_warrior_floor_range = (50, 52)
mountain_orc_warrior_initial_stats = mountain_orc_warrior_stats.copy()
mountain_orc_warrior = Monster("Mountain Orc Warrior", mountain_orc_warrior_stats, mountain_orc_warrior_gear, mountain_orc_warrior_loot_table, difficulty=5, description=mountain_orc_warrior_description, floor_range=mountain_orc_warrior_floor_range, initial_stats=mountain_orc_warrior_initial_stats)

mountain_orc_sentinel_stats = {
    "HP": 110,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_orc_sentinel_gear = ["Stone Maul", "Heavy Plate Armor"]
mountain_orc_sentinel_loot_table = ["Orc Crest", "Reinforced Armor", "Mountain Ore"]
mountain_orc_sentinel_description = "Mountain Orc Sentinels stand guard over their territories with unwavering resolve. Clad in heavy plate armor and wielding stone mauls, they are formidable defenders of their mountain strongholds."
mountain_orc_sentinel_floor_range = (50, 52)
mountain_orc_sentinel_initial_stats = mountain_orc_sentinel_stats.copy()
mountain_orc_sentinel = Monster("Mountain Orc Sentinel", mountain_orc_sentinel_stats, mountain_orc_sentinel_gear, mountain_orc_sentinel_loot_table, difficulty=6, description=mountain_orc_sentinel_description, floor_range=mountain_orc_sentinel_floor_range, initial_stats=mountain_orc_sentinel_initial_stats)

mountain_orc_tracker_stats = {
    "HP": 90,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 25,
    "Constitution": 22,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Earth"
}

mountain_orc_tracker_gear = ["Hunting Bow", "Camouflaged Cloak"]
mountain_orc_tracker_loot_table = ["Orc Eye", "Tattered Camouflage", "Forest Arrow"]
mountain_orc_tracker_description = "Mountain Orc Trackers are skilled hunters, adept at stalking prey through the rugged terrain. With hunting bows and camouflaged cloaks, they excel at ambushing unsuspecting foes."
mountain_orc_tracker_floor_range = (50, 52)
mountain_orc_tracker_initial_stats = mountain_orc_tracker_stats.copy()
mountain_orc_tracker = Monster("Mountain Orc Tracker", mountain_orc_tracker_stats, mountain_orc_tracker_gear, mountain_orc_tracker_loot_table, difficulty=6, description=mountain_orc_tracker_description, floor_range=mountain_orc_tracker_floor_range, initial_stats=mountain_orc_tracker_initial_stats)

mountain_orc_brute_stats = {
    "HP": 120,
    "Damage": 40,
    "Defense": 35,
    "Magic Defense": 10,
    "Strength": 35,
    "Dexterity": 15,
    "Constitution": 28,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_orc_brute_gear = ["Orcish Club", "Heavy Hide Armor"]
mountain_orc_brute_loot_table = ["Orc Tusk", "Torn Hide", "Mountain Brew"]
mountain_orc_brute_description = "Mountain Orc Brutes are imposing warriors known for their raw strength and ferocity in battle. With orcish clubs and heavy hide armor, they smash through enemy lines with brutal force."
mountain_orc_brute_floor_range = (50, 52)
mountain_orc_brute_initial_stats = mountain_orc_brute_stats.copy()
mountain_orc_brute = Monster("Mountain Orc Brute", mountain_orc_brute_stats, mountain_orc_brute_gear, mountain_orc_brute_loot_table, difficulty=6, description=mountain_orc_brute_description, floor_range=mountain_orc_brute_floor_range, initial_stats=mountain_orc_brute_initial_stats)

mountain_orc_scout_stats = {
    "HP": 80,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 20,
    "Dexterity": 25,
    "Constitution": 20,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Earth"
}

mountain_orc_scout_gear = ["Dual Daggers", "Stealth Cloak"]
mountain_orc_scout_loot_table = ["Orc Claw", "Shadow Cloak", "Forest Dagger"]
mountain_orc_scout_description = "Mountain Orc Scouts are expert infiltrators, skilled at navigating the treacherous mountain terrain unseen. With dual daggers and stealth cloaks, they excel at gathering intelligence and ambushing enemy targets."
mountain_orc_scout_floor_range = (50, 52)
mountain_orc_scout_initial_stats = mountain_orc_scout_stats.copy()
mountain_orc_scout = Monster("Mountain Orc Scout", mountain_orc_scout_stats, mountain_orc_scout_gear, mountain_orc_scout_loot_table, difficulty=6, description=mountain_orc_scout_description, floor_range=mountain_orc_scout_floor_range, initial_stats=mountain_orc_scout_initial_stats)

mountain_orc_raider_stats = {
    "HP": 100,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 22,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_orc_raider_gear = ["Serrated Axe", "Reinforced Leather Armor"]
mountain_orc_raider_loot_table = ["Orc Horn", "Bloodied Leather", "Mountain Brew"]
mountain_orc_raider_description = "Mountain Orc Raiders are swift and ruthless attackers, known for their lightning-fast strikes and hit-and-run tactics. With serrated axes and reinforced leather armor, they plunder and pillage with reckless abandon."
mountain_orc_raider_floor_range = (50, 52)
mountain_orc_raider_initial_stats = mountain_orc_raider_stats.copy()
mountain_orc_raider = Monster("Mountain Orc Raider", mountain_orc_raider_stats, mountain_orc_raider_gear, mountain_orc_raider_loot_table, difficulty=6, description=mountain_orc_raider_description, floor_range=mountain_orc_raider_floor_range, initial_stats=mountain_orc_raider_initial_stats)

mountain_ogre_crusher_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 20,
    "Strength": 40,
    "Dexterity": 15,
    "Constitution": 35,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_ogre_crusher_gear = ["Massive Club", "Thick Hide Armor"]
mountain_ogre_crusher_loot_table = ["Ogre Tooth", "Crushed Armor Plate", "Mountain Rock"]
mountain_ogre_crusher_description = "Mountain Ogre Crushers are towering brutes, known for their immense strength and devastating blows. Armed with massive clubs and thick hide armor, they crush anything that stands in their way."
mountain_ogre_crusher_floor_range = (55, 58)
mountain_ogre_crusher_initial_stats = mountain_ogre_crusher_stats.copy()
mountain_ogre_crusher = Monster("Mountain Ogre Crusher", mountain_ogre_crusher_stats, mountain_ogre_crusher_gear, mountain_ogre_crusher_loot_table, difficulty=8, description=mountain_ogre_crusher_description, floor_range=mountain_ogre_crusher_floor_range, initial_stats=mountain_ogre_crusher_initial_stats)

mountain_ogre_mauler_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 30,
    "Magic Defense": 15,
    "Strength": 35,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_ogre_mauler_gear = ["Mighty Maul", "Reinforced Bracers"]
mountain_ogre_mauler_loot_table = ["Ogre Nail", "Torn Bracers", "Mountain Brew"]
mountain_ogre_mauler_description = "Mountain Ogre Maulers are relentless in their assault, wielding mighty mauls to pulverize their foes. With reinforced bracers, they shrug off attacks while delivering bone-crushing blows."
mountain_ogre_mauler_floor_range = (55, 58)
mountain_ogre_mauler_initial_stats = mountain_ogre_mauler_stats.copy()
mountain_ogre_mauler = Monster("Mountain Ogre Mauler", mountain_ogre_mauler_stats, mountain_ogre_mauler_gear, mountain_ogre_mauler_loot_table, difficulty=8, description=mountain_ogre_mauler_description, floor_range=mountain_ogre_mauler_floor_range, initial_stats=mountain_ogre_mauler_initial_stats)

mountain_ogre_smasher_stats = {
    "HP": 220,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 38,
    "Dexterity": 18,
    "Constitution": 38,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_ogre_smasher_gear = ["Great Hammer", "Sturdy Plate Mail"]
mountain_ogre_smasher_loot_table = ["Ogre Knuckle", "Dented Armor Plate", "Mountain Brew"]
mountain_ogre_smasher_description = "Mountain Ogre Smashers are known for their unmatched power and resilience. Armed with great hammers and sturdy plate mail, they bring destruction upon their enemies with every earth-shattering strike."
mountain_ogre_smasher_floor_range = (55, 58)
mountain_ogre_smasher_initial_stats = mountain_ogre_smasher_stats.copy()
mountain_ogre_smasher = Monster("Mountain Ogre Smasher", mountain_ogre_smasher_stats, mountain_ogre_smasher_gear, mountain_ogre_smasher_loot_table, difficulty=8, description=mountain_ogre_smasher_description, floor_range=mountain_ogre_smasher_floor_range, initial_stats=mountain_ogre_smasher_initial_stats)

mountain_ogre_brute_stats = {
    "HP": 240,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 15,
    "Strength": 42,
    "Dexterity": 16,
    "Constitution": 40,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_ogre_brute_gear = ["Massive Cleaver", "Iron Plated Armor"]
mountain_ogre_brute_loot_table = ["Ogre Horn", "Battered Armor Piece", "Mountain Brew"]
mountain_ogre_brute_description = "Mountain Ogre Brutes are towering giants, feared for their immense strength and brutal fighting style. With massive cleavers and iron-plated armor, they charge into battle, leaving destruction in their wake."
mountain_ogre_brute_floor_range = (55, 58)
mountain_ogre_brute_initial_stats = mountain_ogre_brute_stats.copy()
mountain_ogre_brute = Monster("Mountain Ogre Brute", mountain_ogre_brute_stats, mountain_ogre_brute_gear, mountain_ogre_brute_loot_table, difficulty=8, description=mountain_ogre_brute_description, floor_range=mountain_ogre_brute_floor_range, initial_stats=mountain_ogre_brute_initial_stats)

mountain_ogre_ravager_stats = {
    "HP": 260,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 20,
    "Strength": 45,
    "Dexterity": 20,
    "Constitution": 42,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 8,
    "Element": "Earth"
}

mountain_ogre_ravager_gear = ["War Maul", "Steel Plate Armor"]
mountain_ogre_ravager_loot_table = ["Ogre Fist", "Cracked Armor Plate", "Mountain Brew"]
mountain_ogre_ravager_description = "Mountain Ogre Ravagers are relentless juggernauts on the battlefield, known for their unyielding strength and indomitable spirit. With war mauls and steel plate armor, they crush all who dare to oppose them."
mountain_ogre_ravager_floor_range = (55, 58)
mountain_ogre_ravager_initial_stats = mountain_ogre_ravager_stats.copy()
mountain_ogre_ravager = Monster("Mountain Ogre Ravager", mountain_ogre_ravager_stats, mountain_ogre_ravager_gear, mountain_ogre_ravager_loot_table, difficulty=8, description=mountain_ogre_ravager_description, floor_range=mountain_ogre_ravager_floor_range, initial_stats=mountain_ogre_ravager_initial_stats)

mountain_ogre_behemoth_stats = {
    "HP": 300,
    "Damage": 60,
    "Defense": 45,
    "Magic Defense": 25,
    "Strength": 50,
    "Dexterity": 25,
    "Constitution": 48,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_ogre_behemoth_gear = ["Giant Warclub", "Adamantine Armor"]
mountain_ogre_behemoth_loot_table = ["Ogre Boulder", "Shattered Armor Plate", "Mountain Brew"]
mountain_ogre_behemoth_description = "Mountain Ogre Behemoths are titans of destruction, towering over the battlefield with unmatched power and resilience. Armed with giant warclubs and adamantine armor, they crush everything in their path with relentless fury."
mountain_ogre_behemoth_floor_range = (55, 58)
mountain_ogre_behemoth_initial_stats = mountain_ogre_behemoth_stats.copy()
mountain_ogre_behemoth = Monster("Mountain Ogre Behemoth", mountain_ogre_behemoth_stats, mountain_ogre_behemoth_gear, mountain_ogre_behemoth_loot_table, difficulty=8, description=mountain_ogre_behemoth_description, floor_range=mountain_ogre_behemoth_floor_range, initial_stats=mountain_ogre_behemoth_initial_stats)

mountain_ogre_juggernaut_stats = {
    "HP": 280,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 20,
    "Strength": 48,
    "Dexterity": 22,
    "Constitution": 45,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_ogre_juggernaut_gear = ["Titanic Mace", "Obsidian Plated Armor"]
mountain_ogre_juggernaut_loot_table = ["Ogre Fist", "Cracked Armor Plate", "Mountain Brew"]
mountain_ogre_juggernaut_description = "Mountain Ogre Juggernauts are unstoppable forces of destruction, trampling their enemies beneath their massive feet. With titanic maces and obsidian plated armor, they crush all who dare to stand in their path."
mountain_ogre_juggernaut_floor_range = (55, 58)
mountain_ogre_juggernaut_initial_stats = mountain_ogre_juggernaut_stats.copy()
mountain_ogre_juggernaut = Monster("Mountain Ogre Juggernaut", mountain_ogre_juggernaut_stats, mountain_ogre_juggernaut_gear, mountain_ogre_juggernaut_loot_table, difficulty=8, description=mountain_ogre_juggernaut_description, floor_range=mountain_ogre_juggernaut_floor_range, initial_stats=mountain_ogre_juggernaut_initial_stats)

mountain_ogre_colossus_stats = {
    "HP": 320,
    "Damage": 65,
    "Defense": 50,
    "Magic Defense": 30,
    "Strength": 55,
    "Dexterity": 28,
    "Constitution": 50,
    "Intelligence": 14,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Earth"
}

mountain_ogre_colossus_gear = ["Gigantic Warhammer", "Legendary Plate Armor"]
mountain_ogre_colossus_loot_table = ["Ogre Heart", "Shattered Legendary Armor Plate", "Mountain Brew"]
mountain_ogre_colossus_description = "Mountain Ogre Colossi are ancient giants of unparalleled might, feared and revered by all who behold them. Armed with gigantic warhammers and legendary plate armor, they stride across the battlefield as living legends, crushing all who oppose them."
mountain_ogre_colossus_floor_range = (55, 58)
mountain_ogre_colossus_initial_stats = mountain_ogre_colossus_stats.copy()
mountain_ogre_colossus = Monster("Mountain Ogre Colossus", mountain_ogre_colossus_stats, mountain_ogre_colossus_gear, mountain_ogre_colossus_loot_table, difficulty=8, description=mountain_ogre_colossus_description, floor_range=mountain_ogre_colossus_floor_range, initial_stats=mountain_ogre_colossus_initial_stats)

mountain_ogre_boulderfist_stats = {
    "HP": 280,
    "Damage": 60,
    "Defense": 45,
    "Magic Defense": 25,
    "Strength": 50,
    "Dexterity": 25,
    "Constitution": 45,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Earth"
}

mountain_ogre_boulderfist_gear = ["Boulder-Crusher Gauntlets", "Adamantine Plated Armor"]
mountain_ogre_boulderfist_loot_table = ["Ogre Boulder", "Shattered Armor Plate", "Mountain Brew"]
mountain_ogre_boulderfist_description = "Mountain Ogre Boulderfists are known for their ability to hurl massive boulders at their enemies, crushing them from afar. With boulder-crusher gauntlets and adamantine plated armor, they are unstoppable forces of destruction on the battlefield."
mountain_ogre_boulderfist_floor_range = (55, 58)
mountain_ogre_boulderfist_initial_stats = mountain_ogre_boulderfist_stats.copy()
mountain_ogre_boulderfist = Monster("Mountain Ogre Boulderfist", mountain_ogre_boulderfist_stats, mountain_ogre_boulderfist_gear, mountain_ogre_boulderfist_loot_table, difficulty=8, description=mountain_ogre_boulderfist_description, floor_range=mountain_ogre_boulderfist_floor_range, initial_stats=mountain_ogre_boulderfist_initial_stats)
