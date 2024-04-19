from monsters.bestiary import Monster

giant_worm_stats = {
    "HP": 160,  # Define HP attribute for Giant Worm
    "Damage": 50,  # Define damage attribute for Giant Worm
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 22,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Giant Worm's attack
}
giant_worm_gear = ["Sharp Mandibles", "Thick Hide"]
giant_worm_loot_table = ["Gold", "Worm Segments", "Digestive Fluid"]
giant_worm_description = "Giant Worms are colossal burrowing creatures that tunnel through earth and rock with ease. They lie in wait beneath the ground, sensing the vibrations of passing prey before erupting from the earth to strike. Their powerful jaws and acidic saliva make short work of their victims, dissolving flesh and bone alike."
giant_worm_floor_range = (15, 30)
giant_worm_spells = []
giant_worm_spell_probabilities = {}
giant_worm_initial_stats = giant_worm_stats.copy() # Make a copy of the initial stats
giant_worm = Monster("Giant Worm", giant_worm_stats, giant_worm_gear, giant_worm_loot_table, difficulty=15, description=giant_worm_description, floor_range=giant_worm_floor_range, spells=giant_worm_spells, spell_probabilities=giant_worm_spell_probabilities, initial_stats=giant_worm_initial_stats)

glowcap_gnome_stats = {
    "HP": 150,  # Define HP attribute for Glowcap Gnome
    "Damage": 50,  # Define damage attribute for Glowcap Gnome
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 15,
    "Dexterity": 25,
    "Constitution": 20,
    "Intelligence": 30,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Nature"  # Define elemental attribute of the Glowcap Gnome's attack
}
glowcap_gnome_gear = ["Glowing Fungi Staff", "Alchemy Pouch"]
glowcap_gnome_loot_table = ["Gold", "Glowing Fungi", "Potion of Growth"]
glowcap_gnome_description = "Glowcap Gnomes are small, humanoid creatures that make their homes among the bioluminescent fungi of the cave. They are skilled alchemists and magic-users, using the natural resources of the cave to create powerful potions and spells. Though small in stature, they are resourceful and cunning opponents."
glowcap_gnome_floor_range = (50, 100)
glowcap_gnome_spells = ["Bioluminescent Blast", "Fungal Growth"]
glowcap_gnome_spell_probabilities = {"Bioluminescent Blast": 0.8, "Fungal Growth": 0.2}
glowcap_gnome_initial_stats = glowcap_gnome_stats.copy() # Make a copy of the initial stats
glowcap_gnome = Monster("Glowcap Gnome", glowcap_gnome_stats, glowcap_gnome_gear, glowcap_gnome_loot_table, difficulty=50, description=glowcap_gnome_description, floor_range=glowcap_gnome_floor_range, spells=glowcap_gnome_spells, spell_probabilities=glowcap_gnome_spell_probabilities, initial_stats=glowcap_gnome_initial_stats)

fungal_fiend_stats = {
    "HP": 220,  # Define HP attribute for Fungal Fiend
    "Damage": 60,  # Define damage attribute for Fungal Fiend
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 35,  # Define magic defense vs spells
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Nature"  # Define elemental attribute of the Fungal Fiend's attack
}
fungal_fiend_gear = ["Moldy Tendrils", "Spore-covered Carapace"]
fungal_fiend_loot_table = ["Gold", "Fungal Spore", "Toxic Mushroom"]
fungal_fiend_description = "Fungal Fiends are grotesque creatures that thrive in the damp, musty environment of caves. Covered in patches of mold and fungi, they emit a foul odor that can sicken even the hardiest adventurers. They attack with spores and tendrils, slowly corroding their prey."
fungal_fiend_floor_range = (120, 180)
fungal_fiend_spells = []
fungal_fiend_spell_probabilities = {}
fungal_fiend_initial_stats = fungal_fiend_stats.copy() # Make a copy of the initial stats
fungal_fiend = Monster("Fungal Fiend", fungal_fiend_stats, fungal_fiend_gear, fungal_fiend_loot_table, difficulty=120, description=fungal_fiend_description, floor_range=fungal_fiend_floor_range, spells=fungal_fiend_spells, spell_probabilities=fungal_fiend_spell_probabilities, initial_stats=fungal_fiend_initial_stats)

fungal_sporeling_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 20,
    "Element": "Nature"
}
fungal_sporeling_gear = ["Spore-covered Cap", "Fungal Fibers"]
fungal_sporeling_loot_table = ["Gold", "Spore Sac", "Mycelium Shard"]
fungal_sporeling_description = "Fungal Sporelings are small, sentient mushrooms that wander the Mushroom Biome, spreading spores and nurturing the growth of new fungi. Though they appear harmless, their spores can cause disorientation and mild hallucinations."
fungal_sporeling_floor_range = (1, 50)
fungal_sporeling_spells = []
fungal_sporeling_spell_probabilities = {}
fungal_sporeling_initial_stats = fungal_sporeling_stats.copy()
fungal_sporeling = Monster("Fungal Sporeling", fungal_sporeling_stats, fungal_sporeling_gear, fungal_sporeling_loot_table, difficulty=1, description=fungal_sporeling_description, floor_range=fungal_sporeling_floor_range, spells=fungal_sporeling_spells, spell_probabilities=fungal_sporeling_spell_probabilities, initial_stats=fungal_sporeling_initial_stats)

myconid_sprout_stats = {
    "HP": 100,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 25,
    "Element": "Nature"
}
myconid_sprout_gear = ["Mycelial Vine Whip", "Fungal Armor"]
myconid_sprout_loot_table = ["Gold", "Myconid Essence", "Mycelial Sap"]
myconid_sprout_description = "Myconid Sprouts are young, sapient fungi that dwell in the depths of the Mushroom Biome. They communicate through spores and are capable of controlling other fungal creatures with their telepathic abilities."
myconid_sprout_floor_range = (50, 100)
myconid_sprout_spells = []
myconid_sprout_spell_probabilities = {}
myconid_sprout_initial_stats = myconid_sprout_stats.copy()
myconid_sprout = Monster("Myconid Sprout", myconid_sprout_stats, myconid_sprout_gear, myconid_sprout_loot_table, difficulty=50, description=myconid_sprout_description, floor_range=myconid_sprout_floor_range, spells=myconid_sprout_spells, spell_probabilities=myconid_sprout_spell_probabilities, initial_stats=myconid_sprout_initial_stats)

mushroom_golem_stats = {
    "HP": 400,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 50,
    "Element": "Nature"
}
mushroom_golem_gear = ["Fungal Fist", "Mycelial Plate"]
mushroom_golem_loot_table = ["Gold", "Mushroom Core", "Fungal Residue"]
mushroom_golem_description = "Mushroom Golems are towering constructs made entirely of enchanted fungi and mycelium. They serve as guardians of the Mushroom Biome, protecting its delicate ecosystem from intruders."
mushroom_golem_floor_range = (150, 200)
mushroom_golem_spells = []
mushroom_golem_spell_probabilities = {}
mushroom_golem_initial_stats = mushroom_golem_stats.copy()
mushroom_golem = Monster("Mushroom Golem", mushroom_golem_stats, mushroom_golem_gear, mushroom_golem_loot_table, difficulty=150, description=mushroom_golem_description, floor_range=mushroom_golem_floor_range, spells=mushroom_golem_spells, spell_probabilities=mushroom_golem_spell_probabilities, initial_stats=mushroom_golem_initial_stats)

sporecaster_stats = {
    "HP": 250,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 60,
    "Element": "Nature"
}
sporecaster_gear = ["Spore Staff", "Fungal Robes"]
sporecaster_loot_table = ["Gold", "Spore Wand", "Mycelial Scroll"]
sporecaster_description = "Sporecasters are mystical beings that harness the power of fungal magic to manipulate spores and fungi. They are revered as spiritual leaders and healers within the Mushroom Biome."
sporecaster_floor_range = (100, 150)
sporecaster_spells = []
sporecaster_spell_probabilities = {}
sporecaster_initial_stats = sporecaster_stats.copy()
sporecaster = Monster("Sporecaster", sporecaster_stats, sporecaster_gear, sporecaster_loot_table, difficulty=100, description=sporecaster_description, floor_range=sporecaster_floor_range, spells=sporecaster_spells, spell_probabilities=sporecaster_spell_probabilities, initial_stats=sporecaster_initial_stats)

fungoid_crawler_stats = {
    "HP": 180,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 30,
    "Element": "Nature"
}
fungoid_crawler_gear = ["Fungal Fangs", "Mycelial Hide"]
fungoid_crawler_loot_table = ["Gold", "Crawler Carapace", "Mushroom Fiber"]
fungoid_crawler_description = "Fungoid Crawlers are large arthropods that scuttle through the undergrowth of the Mushroom Biome, feeding on decomposing organic matter and fungal spores. They are essential to the biome's ecosystem, breaking down dead material and recycling nutrients."
fungoid_crawler_floor_range = (50, 100)
fungoid_crawler_spells = []
fungoid_crawler_spell_probabilities = {}
fungoid_crawler_initial_stats = fungoid_crawler_stats.copy()
fungoid_crawler = Monster("Fungoid Crawler", fungoid_crawler_stats, fungoid_crawler_gear, fungoid_crawler_loot_table, difficulty=50, description=fungoid_crawler_description, floor_range=fungoid_crawler_floor_range, spells=fungoid_crawler_spells, spell_probabilities=fungoid_crawler_spell_probabilities, initial_stats=fungoid_crawler_initial_stats)

mycelial_fiend_stats = {
    "HP": 300,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 40,
    "Element": "Nature"
}
mycelial_fiend_gear = ["Fungal Claw", "Mycecial Carapace"]
mycelial_fiend_loot_table = ["Gold", "Mycelial Essence", "Fungus Fragment"]
mycelial_fiend_description = "Mycelial Fiends are malevolent creatures that dwell in the depths of the Mushroom Biome, feeding on the life force of other fungi and creatures. They are shunned by the peaceful denizens of the biome and are known to sow chaos and destruction wherever they roam."
mycelial_fiend_floor_range = (100, 150)
mycelial_fiend_spells = []
mycelial_fiend_spell_probabilities = {}
mycelial_fiend_initial_stats = mycelial_fiend_stats.copy()
mycelial_fiend = Monster("Mycelial Fiend", mycelial_fiend_stats, mycelial_fiend_gear, mycelial_fiend_loot_table, difficulty=100, description=mycelial_fiend_description, floor_range=mycelial_fiend_floor_range, spells=mycelial_fiend_spells, spell_probabilities=mycelial_fiend_spell_probabilities, initial_stats=mycelial_fiend_initial_stats)

toadstool_terror_stats = {
    "HP": 350,
    "Damage": 60,
    "Defense": 35,
    "Magic Defense": 50,
    "Element": "Nature"
}
toadstool_terror_gear = ["Toxic Spore Tentacles", "Venomous Cap"]
toadstool_terror_loot_table = ["Gold", "Toadstool Toxin", "Fungal Spore"]
toadstool_terror_description = "Toadstool Terrors are massive, carnivorous fungi that lie in wait beneath the forest floor of the Mushroom Biome, ambushing unsuspecting prey with their toxic spores and tentacles. They are apex predators within their domain, feared by all who dwell in the biome."
toadstool_terror_floor_range = (150, 200)
toadstool_terror_spells = []
toadstool_terror_spell_probabilities = {}
toadstool_terror_initial_stats = toadstool_terror_stats.copy()
toadstool_terror = Monster("Toadstool Terror", toadstool_terror_stats, toadstool_terror_gear, toadstool_terror_loot_table, difficulty=150, description=toadstool_terror_description, floor_range=toadstool_terror_floor_range, spells=toadstool_terror_spells, spell_probabilities=toadstool_terror_spell_probabilities, initial_stats=toadstool_terror_initial_stats)

sporebat_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 25,
    "Element": "Nature"
}
sporebat_gear = ["Spore-tipped Fangs", "Fungal Wings"]
sporebat_loot_table = ["Gold", "Sporebat Wing", "Fungal Residue"]
sporebat_description = "Sporebats are nocturnal creatures that dwell in the canopy of the Mushroom Biome, flitting between the towering fungi in search of prey. They use their keen senses and echolocation to navigate the dense foliage and hunt down insects and small mammals."
sporebat_floor_range = (50, 100)
sporebat_spells = []
sporebat_spell_probabilities = {}
sporebat_initial_stats = sporebat_stats.copy()
sporebat = Monster("Sporebat", sporebat_stats, sporebat_gear, sporebat_loot_table, difficulty=50, description=sporebat_description, floor_range=sporebat_floor_range, spells=sporebat_spells, spell_probabilities=sporebat_spell_probabilities, initial_stats=sporebat_initial_stats)

fungus_elemental_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 50,
    "Magic Defense": 60,
    "Element": "Nature"
}
fungus_elemental_gear = ["Fungal Staff", "Elemental Fungi"]
fungus_elemental_loot_table = ["Gold", "Fungal Essence", "Elemental Spore"]
fungus_elemental_description = "Fungus Elementals are sentient beings composed entirely of magical fungi and spores. They can manipulate the elements of nature to defend themselves and the Mushroom Biome from threats, harnessing the power of earth, air, water, and fire."
fungus_elemental_floor_range = (200, 250)
fungus_elemental_spells = []
fungus_elemental_spell_probabilities = {}
fungus_elemental_initial_stats = fungus_elemental_stats.copy()
fungus_elemental = Monster("Fungus Elemental", fungus_elemental_stats, fungus_elemental_gear, fungus_elemental_loot_table, difficulty=200, description=fungus_elemental_description, floor_range=fungus_elemental_floor_range, spells=fungus_elemental_spells, spell_probabilities=fungus_elemental_spell_probabilities, initial_stats=fungus_elemental_initial_stats)

mushroom_maniac_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 50,
    "Element": "Nature"
}
mushroom_maniac_gear = ["Mycelial Axe", "Fungal Armor"]
mushroom_maniac_loot_table = ["Gold", "Mushroom Cap", "Fungus Fragment"]
mushroom_maniac_description = "Mushroom Maniacs are frenzied creatures consumed by the spores of the Mushroom Biome, driven to madness by their hallucinogenic effects. They roam the forest floor, hacking and slashing at anything that crosses their path."
mushroom_maniac_floor_range = (150, 200)
mushroom_maniac_spells = []
mushroom_maniac_spell_probabilities = {}
mushroom_maniac_initial_stats = mushroom_maniac_stats.copy()
mushroom_maniac = Monster("Mushroom Maniac", mushroom_maniac_stats, mushroom_maniac_gear, mushroom_maniac_loot_table, difficulty=150, description=mushroom_maniac_description, floor_range=mushroom_maniac_floor_range, spells=mushroom_maniac_spells, spell_probabilities=mushroom_maniac_spell_probabilities, initial_stats=mushroom_maniac_initial_stats)

phosphorescent_mycophage_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Nature"
}
phosphorescent_mycophage_gear = ["Bioluminescent Fangs", "Mycelial Carapace"]
phosphorescent_mycophage_loot_table = ["Gold", "Phosphorescent Spore", "Mycophage Essence"]
phosphorescent_mycophage_description = "Phosphorescent Mycophages are creatures that emit a soft, eerie glow as they roam the Mushroom Biome, feeding on the luminous fungi that grow in the darkness. Their bioluminescent appearance serves both as camouflage and a warning to potential predators."
phosphorescent_mycophage_floor_range = (100, 150)
phosphorescent_mycophage_spells = []
phosphorescent_mycophage_spell_probabilities = {}
phosphorescent_mycophage_initial_stats = phosphorescent_mycophage_stats.copy()
phosphorescent_mycophage = Monster("Phosphorescent Mycophage", phosphorescent_mycophage_stats, phosphorescent_mycophage_gear, phosphorescent_mycophage_loot_table, difficulty=100, description=phosphorescent_mycophage_description, floor_range=phosphorescent_mycophage_floor_range, spells=phosphorescent_mycophage_spells, spell_probabilities=phosphorescent_mycophage_spell_probabilities, initial_stats=phosphorescent_mycophage_initial_stats)

fungoid_arcanist_stats = {
    "HP": 300,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Nature"
}
fungoid_arcanist_gear = ["Spore Staff", "Arcane Fungal Robes"]
fungoid_arcanist_loot_table = ["Gold", "Arcane Spore", "Fungoid Scroll"]
fungoid_arcanist_description = "Fungoid Arcanists are masters of fungal magic, wielding the power of spores and mushrooms to cast potent spells and control the elements within the Mushroom Biome. They are revered as wise elders and guardians of ancient knowledge."
fungoid_arcanist_floor_range = (150, 200)
fungoid_arcanist_spells = []
fungoid_arcanist_spell_probabilities = {}
fungoid_arcanist_initial_stats = fungoid_arcanist_stats.copy()
fungoid_arcanist = Monster("Fungoid Arcanist", fungoid_arcanist_stats, fungoid_arcanist_gear, fungoid_arcanist_loot_table, difficulty=150, description=fungoid_arcanist_description, floor_range=fungoid_arcanist_floor_range, spells=fungoid_arcanist_spells, spell_probabilities=fungoid_arcanist_spell_probabilities, initial_stats=fungoid_arcanist_initial_stats)

shrieking_shroomling_stats = {
    "HP": 120,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Nature"
}
shrieking_shroomling_gear = ["Razorcap Claws", "Fungal Hide"]
shrieking_shroomling_loot_table = ["Gold", "Shrieking Spore", "Fungal Fragment"]
shrieking_shroomling_description = "Shrieking Shroomlings are small, aggressive fungi that emit piercing cries as they attack their prey. Their shrill screams can disorient and frighten even the most seasoned adventurers, making them formidable opponents in the Mushroom Biome."
shrieking_shroomling_floor_range = (50, 100)
shrieking_shroomling_spells = []
shrieking_shroomling_spell_probabilities = {}
shrieking_shroomling_initial_stats = shrieking_shroomling_stats.copy()
shrieking_shroomling = Monster("Shrieking Shroomling", shrieking_shroomling_stats, shrieking_shroomling_gear, shrieking_shroomling_loot_table, difficulty=50, description=shrieking_shroomling_description, floor_range=shrieking_shroomling_floor_range, spells=shrieking_shroomling_spells, spell_probabilities=shrieking_shroomling_spell_probabilities, initial_stats=shrieking_shroomling_initial_stats)

fungaloid_creeper_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 12,
    "Intelligence": 10,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "Earth"
}
fungaloid_creeper_gear = ["Vine Whip", "Fungal Spores"]
fungaloid_creeper_loot_table = ["Gold", "Fungal Essence", "Mushroom Cap"]
fungaloid_creeper_description = "Fungaloid Creepers are sinister plant-like creatures that lurk in dark, damp environments. They ambush unsuspecting prey, ensnaring them with their vine-like tendrils and releasing toxic spores that induce paralysis."
fungaloid_creeper_floor_range = (60, 120)
fungaloid_creeper_spells = []
fungaloid_creeper_spell_probabilities = {}
fungaloid_creeper_initial_stats = fungaloid_creeper_stats.copy()
fungaloid_creeper = Monster("Fungaloid Creeper", fungaloid_creeper_stats, fungaloid_creeper_gear, fungaloid_creeper_loot_table, difficulty=60, description=fungaloid_creeper_description, floor_range=fungaloid_creeper_floor_range, spells=fungaloid_creeper_spells, spell_probabilities=fungaloid_creeper_spell_probabilities, initial_stats=fungaloid_creeper_initial_stats)

elder_spore_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 18,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "None"
}
elder_spore_gear = ["Toxic Tentacles", "Fungal Armor"]
elder_spore_loot_table = ["Gold", "Spore Essence", "Toxic Spore Cap"]
elder_spore_description = "Elder Spores are ancient fungal entities that dwell deep within damp caverns. They spread their toxic spores throughout their surroundings, poisoning all who come near. Their tentacles are capable of ensnaring prey with ease."
elder_spore_floor_range = (100, 200)
elder_spore_spells = []
elder_spore_spell_probabilities = {}
elder_spore_initial_stats = elder_spore_stats.copy()
elder_spore = Monster("Elder Spore", elder_spore_stats, elder_spore_gear, elder_spore_loot_table, difficulty=100, description=elder_spore_description, floor_range=elder_spore_floor_range, spells=elder_spore_spells, spell_probabilities=elder_spore_spell_probabilities, initial_stats=elder_spore_initial_stats)

myconid_sporecaster_stats = {
    "HP": 80,
    "Damage": 15,
    "Defense": 12,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 8,
    "Constitution": 14,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 8,
    "Element": "Poison"
}
myconid_sporecaster_gear = ["Mycelium Staff", "Fungal Robes"]
myconid_sporecaster_loot_table = ["Gold", "Mushroom Potion", "Spore Orb"]
myconid_sporecaster_description = "Myconid Sporecasters are mystics among the fungal folk, adept at manipulating spores to control the battlefield and inflict debilitating effects on their enemies."
myconid_sporecaster_floor_range = (2, 4)
myconid_sporecaster_spells = ["Spore Burst", "Fungal Growth"]
myconid_sporecaster_spell_probabilities = {"Spore Burst": 0.7, "Fungal Growth": 0.3}
myconid_sporecaster_initial_stats = myconid_sporecaster_stats.copy()
myconid_sporecaster = Monster("Myconid Sporecaster", myconid_sporecaster_stats, myconid_sporecaster_gear, myconid_sporecaster_loot_table, difficulty=2, description=myconid_sporecaster_description, floor_range=myconid_sporecaster_floor_range, spells=myconid_sporecaster_spells, spell_probabilities=myconid_sporecaster_spell_probabilities, initial_stats=myconid_sporecaster_initial_stats)

myconid_fungomancer_stats = {
    "HP": 90,
    "Damage": 18,
    "Defense": 10,
    "Magic Defense": 20,
    "Strength": 8,
    "Dexterity": 10,
    "Constitution": 16,
    "Intelligence": 14,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "Earth"
}
myconid_fungomancer_gear = ["Spore Staff", "Fungal Robes"]
myconid_fungomancer_loot_table = ["Gold", "Mycelium Elixir", "Fungal Tome"]
myconid_fungomancer_description = "Myconid Fungomancers are powerful spellcasters within fungal communities, wielding magic to shape the environment and control their adversaries."
myconid_fungomancer_floor_range = (3, 5)
myconid_fungomancer_spells = ["Fungal Burst", "Spore Cloud"]
myconid_fungomancer_spell_probabilities = {"Fungal Burst": 0.6, "Spore Cloud": 0.4}
myconid_fungomancer_initial_stats = myconid_fungomancer_stats.copy()
myconid_fungomancer = Monster("Myconid Fungomancer", myconid_fungomancer_stats, myconid_fungomancer_gear, myconid_fungomancer_loot_table, difficulty=3, description=myconid_fungomancer_description, floor_range=myconid_fungomancer_floor_range, spells=myconid_fungomancer_spells, spell_probabilities=myconid_fungomancer_spell_probabilities, initial_stats=myconid_fungomancer_initial_stats)

myconid_sporebrute_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 16,
    "Dexterity": 8,
    "Constitution": 20,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Physical"
}
myconid_sporebrute_gear = ["Fungal Club", "Thick Mycelium Armor"]
myconid_sporebrute_loot_table = ["Gold", "Spore-Encrusted Shield", "Fungal Spores"]
myconid_sporebrute_description = "Myconid Sporebrutes are towering brutes, heavily armored and wielding massive clubs imbued with spores, capable of crushing anything in their path."
myconid_sporebrute_floor_range = (4, 6)
myconid_sporebrute_spells = ["Fungal Rage"]
myconid_sporebrute_spell_probabilities = {"Fungal Rage": 1.0}
myconid_sporebrute_initial_stats = myconid_sporebrute_stats.copy()
myconid_sporebrute = Monster("Myconid Sporebrute", myconid_sporebrute_stats, myconid_sporebrute_gear, myconid_sporebrute_loot_table, difficulty=4, description=myconid_sporebrute_description, floor_range=myconid_sporebrute_floor_range, spells=myconid_sporebrute_spells, spell_probabilities=myconid_sporebrute_spell_probabilities, initial_stats=myconid_sporebrute_initial_stats)

myconid_sporeclaw_stats = {
    "HP": 70,
    "Damage": 20,
    "Defense": 12,
    "Magic Defense": 10,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Physical"
}
myconid_sporeclaw_gear = ["Spore-Infused Claws", "Fungal Hide"]
myconid_sporeclaw_loot_table = ["Gold", "Spore Vial", "Fungal Spine"]
myconid_sporeclaw_description = "Myconid Sporeclaws are agile hunters, using their sharp claws and stealth to ambush prey within the fungal depths."
myconid_sporeclaw_floor_range = (2, 4)
myconid_sporeclaw_spells = ["Spore Burst"]
myconid_sporeclaw_spell_probabilities = {"Spore Burst": 1.0}
myconid_sporeclaw_initial_stats = myconid_sporeclaw_stats.copy()
myconid_sporeclaw = Monster("Myconid Sporeclaw", myconid_sporeclaw_stats, myconid_sporeclaw_gear, myconid_sporeclaw_loot_table, difficulty=2, description=myconid_sporeclaw_description, floor_range=myconid_sporeclaw_floor_range, spells=myconid_sporeclaw_spells, spell_probabilities=myconid_sporeclaw_spell_probabilities, initial_stats=myconid_sporeclaw_initial_stats)

myconid_fungoid_sentinel_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 10,
    "Constitution": 18,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Earth"
}
myconid_fungoid_sentinel_gear = ["Fungal Halberd", "Reinforced Fungal Plate"]
myconid_fungoid_sentinel_loot_table = ["Gold", "Ancient Fungal Relic", "Myconid Spore Pod"]
myconid_fungoid_sentinel_description = "Myconid Fungoid Sentinels are stalwart guardians of the fungal realm, wielding their immense strength and sturdy armor to protect their kin from threats."
myconid_fungoid_sentinel_floor_range = (5, 7)
myconid_fungoid_sentinel_spells = ["Fungal Shield", "Rooted Grasp"]
myconid_fungoid_sentinel_spell_probabilities = {"Fungal Shield": 0.6, "Rooted Grasp": 0.4}
myconid_fungoid_sentinel_initial_stats = myconid_fungoid_sentinel_stats.copy()
myconid_fungoid_sentinel = Monster("Myconid Fungoid Sentinel", myconid_fungoid_sentinel_stats, myconid_fungoid_sentinel_gear, myconid_fungoid_sentinel_loot_table, difficulty=5, description=myconid_fungoid_sentinel_description, floor_range=myconid_fungoid_sentinel_floor_range, spells=myconid_fungoid_sentinel_spells, spell_probabilities=myconid_fungoid_sentinel_spell_probabilities, initial_stats=myconid_fungoid_sentinel_initial_stats)

myconid_sporeborn_shaman_stats = {
    "HP": 100,
    "Damage": 18,
    "Defense": 12,
    "Magic Defense": 25,
    "Strength": 10,
    "Dexterity": 12,
    "Constitution": 14,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 12,
    "Element": "Nature"
}
myconid_sporeborn_shaman_gear = ["Scepter of Spores", "Mycelium Robes"]
myconid_sporeborn_shaman_loot_table = ["Gold", "Spore-Infused Totem", "Fungal Trinket"]
myconid_sporeborn_shaman_description = "Myconid Sporeborn Shamans commune with the spirits of the fungal realm, channeling their wisdom and power to aid their brethren in times of need."
myconid_sporeborn_shaman_floor_range = (4, 6)
myconid_sporeborn_shaman_spells = ["Sporeburst", "Nature's Embrace"]
myconid_sporeborn_shaman_spell_probabilities = {"Sporeburst": 0.8, "Nature's Embrace": 0.2}
myconid_sporeborn_shaman_initial_stats = myconid_sporeborn_shaman_stats.copy()
myconid_sporeborn_shaman = Monster("Myconid Sporeborn Shaman", myconid_sporeborn_shaman_stats, myconid_sporeborn_shaman_gear, myconid_sporeborn_shaman_loot_table, difficulty=4, description=myconid_sporeborn_shaman_description, floor_range=myconid_sporeborn_shaman_floor_range, spells=myconid_sporeborn_shaman_spells, spell_probabilities=myconid_sporeborn_shaman_spell_probabilities, initial_stats=myconid_sporeborn_shaman_initial_stats)

myconid_fungus_fiend_stats = {
    "HP": 110,
    "Damage": 22,
    "Defense": 14,
    "Magic Defense": 15,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Dark"
}
myconid_fungus_fiend_gear = ["Fungal Scythe", "Spore-Infused Cloak"]
myconid_fungus_fiend_loot_table = ["Gold", "Fungal Essence", "Shadowcap Mushroom"]
myconid_fungus_fiend_description = "Myconid Fungus Fiends are corrupted by dark energies, wielding twisted fungal weapons and spreading decay wherever they roam."
myconid_fungus_fiend_floor_range = (5, 7)
myconid_fungus_fiend_spells = ["Fungal Corruption", "Dark Sporeburst"]
myconid_fungus_fiend_spell_probabilities = {"Fungal Corruption": 0.7, "Dark Sporeburst": 0.3}
myconid_fungus_fiend_initial_stats = myconid_fungus_fiend_stats.copy()
myconid_fungus_fiend = Monster("Myconid Fungus Fiend", myconid_fungus_fiend_stats, myconid_fungus_fiend_gear, myconid_fungus_fiend_loot_table, difficulty=5, description=myconid_fungus_fiend_description, floor_range=myconid_fungus_fiend_floor_range, spells=myconid_fungus_fiend_spells, spell_probabilities=myconid_fungus_fiend_spell_probabilities, initial_stats=myconid_fungus_fiend_initial_stats)

myconid_sporewalker_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 18,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 16,
    "Charisma": 8,
    "Element": "Shadow"
}
myconid_sporewalker_gear = ["Shadowy Staff", "Cloak of Spores"]
myconid_sporewalker_loot_table = ["Gold", "Shadow Fungus", "Void Spore"]
myconid_sporewalker_description = "Myconid Sporewalkers lurk in the depths, blending with the shadows and unleashing dark spores upon unsuspecting prey."
myconid_sporewalker_floor_range = (4, 6)
myconid_sporewalker_spells = ["Shadowstep", "Void Eruption"]
myconid_sporewalker_spell_probabilities = {"Shadowstep": 0.6, "Void Eruption": 0.4}
myconid_sporewalker_initial_stats = myconid_sporewalker_stats.copy()
myconid_sporewalker = Monster("Myconid Sporewalker", myconid_sporewalker_stats, myconid_sporewalker_gear, myconid_sporewalker_loot_table, difficulty=4, description=myconid_sporewalker_description, floor_range=myconid_sporewalker_floor_range, spells=myconid_sporewalker_spells, spell_probabilities=myconid_sporewalker_spell_probabilities, initial_stats=myconid_sporewalker_initial_stats)

myconid_fungusflayer_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 16,
    "Magic Defense": 16,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Psychic"
}
myconid_fungusflayer_gear = ["Psionic Blade", "Mycelium Armor"]
myconid_fungusflayer_loot_table = ["Gold", "Psionic Spore", "Fungal Brain"]
myconid_fungusflayer_description = "Myconid Fungusflayers possess psychic abilities, using their mental powers to manipulate foes and control the battlefield."
myconid_fungusflayer_floor_range = (6, 8)
myconid_fungusflayer_spells = ["Mind Blast", "Psychic Distortion"]
myconid_fungusflayer_spell_probabilities = {"Mind Blast": 0.7, "Psychic Distortion": 0.3}
myconid_fungusflayer_initial_stats = myconid_fungusflayer_stats.copy()
myconid_fungusflayer = Monster("Myconid Fungusflayer", myconid_fungusflayer_stats, myconid_fungusflayer_gear, myconid_fungusflayer_loot_table, difficulty=6, description=myconid_fungusflayer_description, floor_range=myconid_fungusflayer_floor_range, spells=myconid_fungusflayer_spells, spell_probabilities=myconid_fungusflayer_spell_probabilities, initial_stats=myconid_fungusflayer_initial_stats)

myconid_sporewretch_stats = {
    "HP": 60,
    "Damage": 15,
    "Defense": 10,
    "Magic Defense": 12,
    "Strength": 8,
    "Dexterity": 10,
    "Constitution": 12,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Toxic"
}
myconid_sporewretch_gear = ["Putrid Claw", "Rotting Garb"]
myconid_sporewretch_loot_table = ["Gold", "Toxic Spore Sac", "Decayed Mushroom"]
myconid_sporewretch_description = "Myconid Sporewretches are diseased and decrepit, exuding toxic spores that corrode flesh and sicken the unwary."
myconid_sporewretch_floor_range = (1, 3)
myconid_sporewretch_spells = ["Noxious Cloud"]
myconid_sporewretch_spell_probabilities = {"Noxious Cloud": 1.0}
myconid_sporewretch_initial_stats = myconid_sporewretch_stats.copy()
myconid_sporewretch = Monster("Myconid Sporewretch", myconid_sporewretch_stats, myconid_sporewretch_gear, myconid_sporewretch_loot_table, difficulty=1, description=myconid_sporewretch_description, floor_range=myconid_sporewretch_floor_range, spells=myconid_sporewretch_spells, spell_probabilities=myconid_sporewretch_spell_probabilities, initial_stats=myconid_sporewretch_initial_stats)

fungusbeast_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 18,
    "Dexterity": 12,
    "Constitution": 16,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "Poison"
}
fungusbeast_gear = ["Fungal Claws", "Molded Hide"]
fungusbeast_loot_table = ["Gold", "Fungal Essence", "Decayed Bone"]
fungusbeast_description = "Fungusbeasts are massive creatures lurking within the depths of fungal forests, their bodies infused with toxic spores and their claws dripping with decay."
fungusbeast_floor_range = (4, 6)
fungusbeast_spells = ["Toxic Slam", "Fungal Burst"]
fungusbeast_spell_probabilities = {"Toxic Slam": 0.6, "Fungal Burst": 0.4}
fungusbeast_initial_stats = fungusbeast_stats.copy()
fungusbeast = Monster("Fungusbeast", fungusbeast_stats, fungusbeast_gear, fungusbeast_loot_table, difficulty=4, description=fungusbeast_description, floor_range=fungusbeast_floor_range, spells=fungusbeast_spells, spell_probabilities=fungusbeast_spell_probabilities, initial_stats=fungusbeast_initial_stats)

gloomcap_assassin_stats = {
    "HP": 80,
    "Damage": 25,
    "Defense": 12,
    "Magic Defense": 12,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 12,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Shadow"
}
gloomcap_assassin_gear = ["Shadowed Blades", "Cloak of Gloom"]
gloomcap_assassin_loot_table = ["Gold", "Shadowcap Mushroom", "Tenebrous Shard"]
gloomcap_assassin_description = "Gloomcap Assassins are stealthy hunters, moving silently through the shadows of the fungal undergrowth to strike down their prey with deadly precision."
gloomcap_assassin_floor_range = (3, 5)
gloomcap_assassin_spells = ["Shadowstep", "Venomous Strike"]
gloomcap_assassin_spell_probabilities = {"Shadowstep": 0.7, "Venomous Strike": 0.3}
gloomcap_assassin_initial_stats = gloomcap_assassin_stats.copy()
gloomcap_assassin = Monster("Gloomcap Assassin", gloomcap_assassin_stats, gloomcap_assassin_gear, gloomcap_assassin_loot_table, difficulty=3, description=gloomcap_assassin_description, floor_range=gloomcap_assassin_floor_range, spells=gloomcap_assassin_spells, spell_probabilities=gloomcap_assassin_spell_probabilities, initial_stats=gloomcap_assassin_initial_stats)

gloomcap_sporemancer_stats = {
    "HP": 90,
    "Damage": 18,
    "Defense": 14,
    "Magic Defense": 18,
    "Strength": 10,
    "Dexterity": 12,
    "Constitution": 14,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Dark"
}
gloomcap_sporemancer_gear = ["Staff of Shadows", "Robes of Obscurity"]
gloomcap_sporemancer_loot_table = ["Gold", "Darkspore Fungus", "Eclipse Crystal"]
gloomcap_sporemancer_description = "Gloomcap Sporemancers are masters of shadow and decay, wielding dark magic to command the fungi and spores of the forest to do their bidding."
gloomcap_sporemancer_floor_range = (4, 6)
gloomcap_sporemancer_spells = ["Shadowbolt", "Decay Aura"]
gloomcap_sporemancer_spell_probabilities = {"Shadowbolt": 0.6, "Decay Aura": 0.4}
gloomcap_sporemancer_initial_stats = gloomcap_sporemancer_stats.copy()
gloomcap_sporemancer = Monster("Gloomcap Sporemancer", gloomcap_sporemancer_stats, gloomcap_sporemancer_gear, gloomcap_sporemancer_loot_table, difficulty=4, description=gloomcap_sporemancer_description, floor_range=gloomcap_sporemancer_floor_range, spells=gloomcap_sporemancer_spells, spell_probabilities=gloomcap_sporemancer_spell_probabilities, initial_stats=gloomcap_sporemancer_initial_stats)

gloomcap_thornheart_stats = {
    "HP": 90,
    "Damage": 22,
    "Defense": 16,
    "Magic Defense": 14,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Nature"
}
gloomcap_thornheart_gear = ["Thorned Vine Whip", "Bark Armor"]
gloomcap_thornheart_loot_table = ["Gold", "Thornheart Seed", "Entangled Vine"]
gloomcap_thornheart_description = "Gloomcap Thornhearts are guardians of the forest, their bodies intertwined with thorny vines and their hearts pulsing with the essence of nature."
gloomcap_thornheart_floor_range = (4, 6)
gloomcap_thornheart_spells = ["Nature's Wrath", "Thorn Shield"]
gloomcap_thornheart_spell_probabilities = {"Nature's Wrath": 0.7, "Thorn Shield": 0.3}
gloomcap_thornheart_initial_stats = gloomcap_thornheart_stats.copy()
gloomcap_thornheart = Monster("Gloomcap Thornheart", gloomcap_thornheart_stats, gloomcap_thornheart_gear, gloomcap_thornheart_loot_table, difficulty=4, description=gloomcap_thornheart_description, floor_range=gloomcap_thornheart_floor_range, spells=gloomcap_thornheart_spells, spell_probabilities=gloomcap_thornheart_spell_probabilities, initial_stats=gloomcap_thornheart_initial_stats)

gloomcap_sporeweaver_stats = {
    "HP": 80,
    "Damage": 18,
    "Defense": 12,
    "Magic Defense": 18,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 14,
    "Intelligence": 16,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Earth"
}
gloomcap_sporeweaver_gear = ["Weaver's Staff", "Sporecloak Robes"]
gloomcap_sporeweaver_loot_table = ["Gold", "Mycelium Thread", "Sporeweaver Tome"]
gloomcap_sporeweaver_description = "Gloomcap Sporeweavers are master manipulators of fungal energies, spinning threads of spores to ensnare their foes and control the battlefield."
gloomcap_sporeweaver_floor_range = (1,5)
gloomcap_sporeweaver_spells = ["Fungal Bind", "Sporeblast"]
gloomcap_sporeweaver_spell_probabilities = {"Fungal Bind": 0.6, "Sporeblast": 0.4}
gloomcap_sporeweaver_initial_stats = gloomcap_sporeweaver_stats.copy()
gloomcap_sporeweaver = Monster("Gloomcap Sporeweaver", gloomcap_sporeweaver_stats, gloomcap_sporeweaver_gear, gloomcap_sporeweaver_loot_table, difficulty=3, description=gloomcap_sporeweaver_description, floor_range=gloomcap_sporeweaver_floor_range, spells=gloomcap_sporeweaver_spells, spell_probabilities=gloomcap_sporeweaver_spell_probabilities, initial_stats=gloomcap_sporeweaver_initial_stats)

gloomcap_frostbramble_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 14,
    "Magic Defense": 16,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 14,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Ice"
}
gloomcap_frostbramble_gear = ["Frostbriar Whip", "Glacial Bark Armor"]
gloomcap_frostbramble_loot_table = ["Gold", "Frostbloom Petal", "Icicle Shard"]
gloomcap_frostbramble_description = "Gloomcap Frostbrambles are ice-cursed guardians, their veins frozen with frost and their thorny branches coated in icy spikes."
gloomcap_frostbramble_floor_range = (1,5)
gloomcap_frostbramble_spells = ["Frostbite", "Icicle Barrage"]
gloomcap_frostbramble_spell_probabilities = {"Frostbite": 0.7, "Icicle Barrage": 0.3}
gloomcap_frostbramble_initial_stats = gloomcap_frostbramble_stats.copy()
gloomcap_frostbramble = Monster("Gloomcap Frostbramble", gloomcap_frostbramble_stats, gloomcap_frostbramble_gear, gloomcap_frostbramble_loot_table, difficulty=4, description=gloomcap_frostbramble_description, floor_range=gloomcap_frostbramble_floor_range, spells=gloomcap_frostbramble_spells, spell_probabilities=gloomcap_frostbramble_spell_probabilities, initial_stats=gloomcap_frostbramble_initial_stats)

