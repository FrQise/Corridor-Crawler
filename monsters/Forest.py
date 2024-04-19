from monsters.bestiary import Monster

wolf_stats = {
    "HP": 60,  # Define HP attribute for Wolf
    "Damage": 25,  # Define damage attribute for Wolf
    "Defense": 15,  # Define Defense stat vs attack stat
    "Magic Defense": 5,  # Define magic defense vs spells
    "Strength": 10,
    "Dexterity": 15,
    "Constitution": 12,
    "Intelligence": 4,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Wolf's attack
}
wolf_gear = ["Sharp Fangs", "Thick Fur"]
wolf_loot_table = ["Gold", "Meat", "Wolf Pelt"]
wolf_description = "Wolves are fierce predators that roam in packs. Known for their agility and ferocity, they can swiftly take down prey much larger than themselves."
wolf_floor_range = (1,4)
wolf_spells = []
wolf_spell_probabilities = {}
wolf_initial_stats = wolf_stats.copy() # Make a copy of the initial stats
wolf = Monster("Wolf", wolf_stats, wolf_gear, wolf_loot_table, difficulty=2, description=wolf_description, floor_range=wolf_floor_range, spells=wolf_spells, spell_probabilities=wolf_spell_probabilities, initial_stats=wolf_initial_stats)


troll_stats = {
    "HP": 120,  # Define HP attribute for Troll
    "Damage": 35,  # Define damage attribute for Troll
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 15,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 8,
    "Constitution": 18,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 4,
    "Element": "Earth"  # Define elemental attribute of the Troll's attack
}
troll_gear = ["Club", "Thick Hide Armor"]
troll_loot_table = ["Gold", "Troll Tooth", "Troll Hide"]
troll_description = "Trolls are massive, brutish creatures with regenerative abilities. They wield crude weapons and rely on their immense strength to overpower their foes. Beware their ferocious roars, for they can strike fear into the hearts of even the bravest adventurers."
troll_floor_range = (5, 10)
troll_spells = ["Regeneration"]
troll_spell_probabilities = {"Regeneration": 0.2} 
troll_initial_stats = troll_stats.copy() # Make a copy of the initial stats
troll = Monster("Troll", troll_stats, troll_gear, troll_loot_table, difficulty=5, description=troll_description, floor_range=troll_floor_range, spells=troll_spells, spell_probabilities=troll_spell_probabilities, initial_stats=troll_initial_stats)

snake_stats = {
    "HP": 40,  # Define HP attribute for Snake
    "Damage": 15,  # Define damage attribute for Snake
    "Defense": 10,  # Define Defense stat vs attack stat
    "Magic Defense": 5,  # Define magic defense vs spells
    "Strength": 8,
    "Dexterity": 15,
    "Constitution": 10,
    "Intelligence": 4,
    "Wisdom": 6,
    "Charisma": 4,
    "Element": "Poison"  # Define elemental attribute of the Snake's attack
}
snake_gear = ["Venomous Fangs", "Scales"]
snake_loot_table = ["Gold", "Snake Skin", "Venom Sac"]
snake_description = "Snakes are stealthy predators known for their lethal venom and lightning-fast strikes. Despite their small size, they can deliver deadly blows with their venomous fangs, making them a dangerous foe to encounter."
snake_floor_range = (1, 3)
snake_spells = []
snake_spell_probabilities = {}
snake_initial_stats = snake_stats.copy() # Make a copy of the initial stats
snake = Monster("Snake", snake_stats, snake_gear, snake_loot_table, difficulty=1, description=snake_description, floor_range=snake_floor_range, spells=snake_spells, spell_probabilities=snake_spell_probabilities, initial_stats=snake_initial_stats)

ogre_stats = {
    "HP": 200,  # Define HP attribute for Ogre
    "Damage": 60,  # Define damage attribute for Ogre
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 25,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 10,
    "Constitution": 25,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 4,
    "Element": "None"  # Define elemental attribute of the Ogre's attack
}
ogre_gear = ["Massive Club", "Thick Hide Armor"]
ogre_loot_table = ["Gold", "Ogre Bone", "Ogre Hide"]
ogre_description = "Ogres are hulking brutes with a penchant for violence. They roam the wilderness in search of prey, crushing anything that stands in their way with their immense strength. Despite their lumbering gait, they are surprisingly agile in combat, making them a formidable opponent."
ogre_floor_range = (20, 40)
ogre_spells = []
ogre_spell_probabilities = {}
ogre_initial_stats = ogre_stats.copy() # Make a copy of the initial stats
ogre = Monster("Ogre", ogre_stats, ogre_gear, ogre_loot_table, difficulty=20, description=ogre_description, floor_range=ogre_floor_range, spells=ogre_spells, spell_probabilities=ogre_spell_probabilities, initial_stats=ogre_initial_stats)

bear_stats = {
    "HP": 120,  # Define HP attribute for Bear
    "Damage": 40,  # Define damage attribute for Bear
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 22,
    "Dexterity": 12,
    "Constitution": 20,
    "Intelligence": 4,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Bear's attack
}
bear_gear = ["Claws", "Thick Fur"]
bear_loot_table = ["Gold", "Bear Claw", "Bear Pelt"]
bear_description = "Bears are massive, formidable predators with powerful claws and jaws capable of tearing through flesh and bone. They are known for their strength and resilience, often dominating their territory with sheer brute force."
bear_floor_range = (10, 20)
bear_spells = []
bear_spell_probabilities = {}
bear_initial_stats = bear_stats.copy() # Make a copy of the initial stats
bear = Monster("Bear", bear_stats, bear_gear, bear_loot_table, difficulty=10, description=bear_description, floor_range=bear_floor_range, spells=bear_spells, spell_probabilities=bear_spell_probabilities, initial_stats=bear_initial_stats)

giant_stats = {
    "HP": 300,  # Define HP attribute for Giant
    "Damage": 80,  # Define damage attribute for Giant
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 18,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Giant's attack
}
giant_gear = ["Massive Club", "Heavy Armor"]
giant_loot_table = ["Gold", "Giant Tooth", "Giant Club"]
giant_description = "Giants are colossal beings towering over the landscape with brute strength and raw power. They wield massive clubs and hurl boulders at their foes, crushing anything that stands in their way. Their sheer size and ferocity make them a force to be reckoned with."
giant_floor_range = (1,5)
giant_spells = []
giant_spell_probabilities = {}
giant_initial_stats = giant_stats.copy() # Make a copy of the initial stats
giant = Monster("Giant", giant_stats, giant_gear, giant_loot_table, difficulty=40, description=giant_description, floor_range=giant_floor_range, spells=giant_spells, spell_probabilities=giant_spell_probabilities, initial_stats=giant_initial_stats)

gnoll_stats = {
    "HP": 100,  # Define HP attribute for Gnoll
    "Damage": 30,  # Define damage attribute for Gnoll
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 15,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Gnoll's attack
}
gnoll_gear = ["Rusty Axe", "Patchwork Armor"]
gnoll_loot_table = ["Gold", "Gnoll Tooth", "Torn Pelt"]
gnoll_description = "Gnolls are savage hyena-like humanoids known for their brutal raids and ferocious pack mentality. They swarm their enemies with overwhelming numbers, wielding crude weapons and tearing into flesh with their razor-sharp teeth. Their lust for blood drives them to pursue their prey relentlessly."
gnoll_floor_range = (5, 15)
gnoll_spells = []
gnoll_spell_probabilities = {}
gnoll_initial_stats = gnoll_stats.copy() # Make a copy of the initial stats
gnoll = Monster("Gnoll", gnoll_stats, gnoll_gear, gnoll_loot_table, difficulty=5, description=gnoll_description, floor_range=gnoll_floor_range, spells=gnoll_spells, spell_probabilities=gnoll_spell_probabilities, initial_stats=gnoll_initial_stats)

giant_snake_stats = {
    "HP": 120,  # Define HP attribute for Giant Snake
    "Damage": 40,  # Define damage attribute for Giant Snake
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 18,
    "Intelligence": 6,
    "Wisdom": 12,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Giant Snake's attack
}
giant_snake_gear = ["Venomous Fangs", "Serpentine Scales"]
giant_snake_loot_table = ["Gold", "Snake Skin", "Venom Sac"]
giant_snake_description = "Giant Snakes are massive reptiles, lurking in the depths of forests and swamps, waiting to ambush unsuspecting prey. With lightning-fast strikes and deadly venom, they coil around their victims, squeezing the life out of them before devouring them whole. Their sinuous bodies and keen senses make them formidable hunters."
giant_snake_floor_range = (10, 20)
giant_snake_spells = []
giant_snake_spell_probabilities = {}
giant_snake_initial_stats = giant_snake_stats.copy() # Make a copy of the initial stats
giant_snake = Monster("Giant Snake", giant_snake_stats, giant_snake_gear, giant_snake_loot_table, difficulty=10, description=giant_snake_description, floor_range=giant_snake_floor_range, spells=giant_snake_spells, spell_probabilities=giant_snake_spell_probabilities, initial_stats=giant_snake_initial_stats)

giant_ape_stats = {
    "HP": 280,  # Define HP attribute for Giant Ape
    "Damage": 75,  # Define damage attribute for Giant Ape
    "Defense": 45,  # Define Defense stat vs attack stat
    "Magic Defense": 35,  # Define magic defense vs spells
    "Strength": 28,
    "Dexterity": 16,
    "Constitution": 28,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Giant Ape's attack
}
giant_ape_gear = ["Mighty Fists", "Thick Fur"]
giant_ape_loot_table = ["Gold", "Giant Ape Tooth", "Banana"]
giant_ape_description = "Giant Apes are massive primates of incredible strength and ferocity. They roam through dense jungles and mountainous regions, pounding their chests and unleashing deafening roars to assert dominance over their territory. In combat, they rely on their powerful fists and sheer brute force to crush their opponents."
giant_ape_floor_range = (50, 100)
giant_ape_spells = []
giant_ape_spell_probabilities = {}
giant_ape_initial_stats = giant_ape_stats.copy() # Make a copy of the initial stats
giant_ape = Monster("Giant Ape", giant_ape_stats, giant_ape_gear, giant_ape_loot_table, difficulty=50, description=giant_ape_description, floor_range=giant_ape_floor_range, spells=giant_ape_spells, spell_probabilities=giant_ape_spell_probabilities, initial_stats=giant_ape_initial_stats)

dire_bear_stats = {
    "HP": 300,  # Define HP attribute for Dire Bear
    "Damage": 80,  # Define damage attribute for Dire Bear
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 30,
    "Dexterity": 16,
    "Constitution": 30,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"  # Define elemental attribute of the Dire Bear's attack
}
dire_bear_gear = ["Razor-sharp Claws", "Thick Hide"]
dire_bear_loot_table = ["Gold", "Dire Bear Claw", "Bear Pelt"]
dire_bear_description = "Dire Bears are massive predators, towering over their smaller kin with raw strength and ferocity. They roam through the wilderness, hunting for prey to sate their insatiable hunger. With razor-sharp claws and thick fur, they are formidable adversaries, capable of shrugging off all but the most powerful attacks."
dire_bear_floor_range = (60, 120)
dire_bear_spells = []
dire_bear_spell_probabilities = {}
dire_bear_initial_stats = dire_bear_stats.copy() # Make a copy of the initial stats
dire_bear = Monster("Dire Bear", dire_bear_stats, dire_bear_gear, dire_bear_loot_table, difficulty=60, description=dire_bear_description, floor_range=dire_bear_floor_range, spells=dire_bear_spells, spell_probabilities=dire_bear_spell_probabilities, initial_stats=dire_bear_initial_stats)

carnivorous_plant_stats = {
    "HP": 120,  # Define HP attribute for Carnivorous Plant
    "Damage": 40,  # Define damage attribute for Carnivorous Plant
    "Defense": 25,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Carnivorous Plant's attack
}
carnivorous_plant_gear = ["Venomous Thorns", "Vicious Vines"]
carnivorous_plant_loot_table = ["Gold", "Plant Essence", "Venomous Thorn"]
carnivorous_plant_description = "Carnivorous Plants are deceptive predators that lure unsuspecting prey with the promise of nectar, only to ensnare them in their deadly embrace. With venomous thorns and grasping vines, they entangle their victims, draining them of their life force. Their seductive appearance masks their true nature as merciless killers."
carnivorous_plant_floor_range = (10, 20)
carnivorous_plant_spells = []
carnivorous_plant_spell_probabilities = {}
carnivorous_plant_initial_stats = carnivorous_plant_stats.copy() # Make a copy of the initial stats
carnivorous_plant = Monster("Carnivorous Plant", carnivorous_plant_stats, carnivorous_plant_gear, carnivorous_plant_loot_table, difficulty=10, description=carnivorous_plant_description, floor_range=carnivorous_plant_floor_range, spells=carnivorous_plant_spells, spell_probabilities=carnivorous_plant_spell_probabilities, initial_stats=carnivorous_plant_initial_stats)

elf_raider_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "None"
}
elf_raider_gear = ["Elven Longbow", "Leather Armor"]
elf_raider_loot_table = ["Gold", "Elven Arrow", "Silver Bracelet"]
elf_raider_description = "Elf Raiders are skilled archers and swordsmen who roam the forests in search of plunder and glory. They are adept at guerrilla tactics and can strike swiftly and silently from the shadows."
elf_raider_floor_range = (120, 220)
elf_raider_spells = []
elf_raider_spell_probabilities = {}
elf_raider_initial_stats = elf_raider_stats.copy()
elf_raider = Monster("Elf Raider", elf_raider_stats, elf_raider_gear, elf_raider_loot_table, difficulty=120, description=elf_raider_description, floor_range=elf_raider_floor_range, spells=elf_raider_spells, spell_probabilities=elf_raider_spell_probabilities, initial_stats=elf_raider_initial_stats)

awakened_tree_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 28,
    "Dexterity": 10,
    "Constitution": 30,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
awakened_tree_gear = ["Branch Club", "Thick Bark Armor"]
awakened_tree_loot_table = ["Gold", "Ent Sap", "Wooden Splinter"]
awakened_tree_description = "Awakened Trees are ancient guardians of the forest, imbued with life by powerful druidic magic. Towering over their surroundings, they are formidable opponents in battle, wielding massive branches with surprising speed and strength."
awakened_tree_floor_range = (120, 240)
awakened_tree_spells = []
awakened_tree_spell_probabilities = {}
awakened_tree_initial_stats = awakened_tree_stats.copy()
awakened_tree = Monster("Awakened Tree", awakened_tree_stats, awakened_tree_gear, awakened_tree_loot_table, difficulty=120, description=awakened_tree_description, floor_range=awakened_tree_floor_range, spells=awakened_tree_spells, spell_probabilities=awakened_tree_spell_probabilities, initial_stats=awakened_tree_initial_stats)

common_treant_stats = {
    "HP": 300,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Earth"
}
common_treant_gear = ["Branch Club", "Wooden Bark Armor"]
common_treant_loot_table = ["Gold", "Treant Sap", "Ancient Wood"]
common_treant_description = "Common Treants are ancient guardians of the forests, towering over the treetops with their massive forms. They are peaceful beings by nature, but will fiercely defend their home against any threat with their powerful limbs and roots."
common_treant_floor_range = (200, 400)
common_treant_spells = []
common_treant_spell_probabilities = {}
common_treant_initial_stats = common_treant_stats.copy()
common_treant = Monster("Common Treant", common_treant_stats, common_treant_gear, common_treant_loot_table, difficulty=200, description=common_treant_description, floor_range=common_treant_floor_range, spells=common_treant_spells, spell_probabilities=common_treant_spell_probabilities, initial_stats=common_treant_initial_stats)

poison_dandelion_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 14,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Poison"
}
poison_dandelion_gear = ["Toxic Thorns", "Pollen Cloud"]
poison_dandelion_loot_table = ["Gold", "Poisonous Petal", "Dandelion Essence"]
poison_dandelion_description = "Poison Dandelions are deceptively innocent-looking plants that conceal deadly toxins within their petals. They release clouds of poisonous pollen and shoot toxic thorns at unsuspecting prey."
poison_dandelion_floor_range = (40, 80)
poison_dandelion_spells = ["Toxic Pollen", "Venomous Thorns", "Petal Storm"]
poison_dandelion_spell_probabilities = {"Toxic Pollen": 0.4, "Venomous Thorns": 0.3, "Petal Storm": 0.3}
poison_dandelion_initial_stats = poison_dandelion_stats.copy()
poison_dandelion = Monster("Poison Dandelion", poison_dandelion_stats, poison_dandelion_gear, poison_dandelion_loot_table, difficulty=40, description=poison_dandelion_description, floor_range=poison_dandelion_floor_range, spells=poison_dandelion_spells, spell_probabilities=poison_dandelion_spell_probabilities, initial_stats=poison_dandelion_initial_stats)

dire_flea_stats = {
    "HP": 150,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 25,
    "Constitution": 18,
    "Intelligence": 5,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"
}
dire_flea_gear = ["Razor Fangs", "Tough Exoskeleton"]
dire_flea_loot_table = ["Gold", "Flea Carapace", "Venomous Stinger"]
dire_flea_description = "Dire Fleas are bloodthirsty parasites that infest dark and damp environments. With razor-sharp fangs and a tough exoskeleton, they pose a threat to any unfortunate traveler who crosses their path."
dire_flea_floor_range = (40, 80)
dire_flea_spells = []
dire_flea_spell_probabilities = {}
dire_flea_initial_stats = dire_flea_stats.copy()
dire_flea = Monster("Dire Flea", dire_flea_stats, dire_flea_gear, dire_flea_loot_table, difficulty=40, description=dire_flea_description, floor_range=dire_flea_floor_range, spells=dire_flea_spells, spell_probabilities=dire_flea_spell_probabilities, initial_stats=dire_flea_initial_stats)

mosskin_druid_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 30,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Nature"
}
mosskin_druid_gear = ["Oak Staff", "Mossy Robes"]
mosskin_druid_loot_table = ["Druidic Relic", "Verdant Tome", "Gold"]
mosskin_druid_description = "Mosskin Druids are guardians of the forest, wielding powerful nature magic to heal allies, manipulate the environment, and summon the forces of the wilderness against intruders."
mosskin_druid_floor_range = (30, 60)
mosskin_druid_spells = ["Entangling Roots", "Healing Touch", "Nature's Wrath"]
mosskin_druid_spell_probabilities = {"Entangling Roots": 0.4, "Healing Touch": 0.3, "Nature's Wrath": 0.3}
mosskin_druid_initial_stats = mosskin_druid_stats.copy()
mosskin_druid = Monster("Mosskin Druid", mosskin_druid_stats, mosskin_druid_gear, mosskin_druid_loot_table, difficulty=30, description=mosskin_druid_description, floor_range=mosskin_druid_floor_range, spells=mosskin_druid_spells, spell_probabilities=mosskin_druid_spell_probabilities, initial_stats=mosskin_druid_initial_stats)

mosskin_warrior_stats = {
    "HP": 150,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 14,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Nature"
}
mosskin_warrior_gear = ["Thick Vine Club", "Bark Armor"]
mosskin_warrior_loot_table = ["Warrior's Token", "Battered Shield", "Gold"]
mosskin_warrior_description = "Mosskin Warriors are fierce defenders of the forest, clad in thick bark armor and wielding mighty vine clubs. They stand resolute against any who would threaten their woodland home, using brute strength and ferocity to crush their enemies."
mosskin_warrior_floor_range = (30, 60)
mosskin_warrior_spells = []
mosskin_warrior_spell_probabilities = {}
mosskin_warrior_initial_stats = mosskin_warrior_stats.copy()
mosskin_warrior = Monster("Mosskin Warrior", mosskin_warrior_stats, mosskin_warrior_gear, mosskin_warrior_loot_table, difficulty=30, description=mosskin_warrior_description, floor_range=mosskin_warrior_floor_range, spells=mosskin_warrior_spells, spell_probabilities=mosskin_warrior_spell_probabilities, initial_stats=mosskin_warrior_initial_stats)

mosskin_shaman_stats = {
    "HP": 130,
    "Damage": 20,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Nature"
}
mosskin_shaman_gear = ["Thornwood Staff", "Nature's Robes"]
mosskin_shaman_loot_table = ["Shamanic Relic", "Forest Talisman", "Gold"]
mosskin_shaman_description = "Mosskin Shamans are spiritual leaders of the forest, channeling the ancient energies of nature to heal allies, curse enemies, and commune with the spirits of the wilderness."
mosskin_shaman_floor_range = (30, 60)
mosskin_shaman_spells = ["Nature's Blessing", "Curse of Thorns", "Spiritual Guidance"]
mosskin_shaman_spell_probabilities = {"Nature's Blessing": 0.4, "Curse of Thorns": 0.3, "Spiritual Guidance": 0.3}
mosskin_shaman_initial_stats = mosskin_shaman_stats.copy()
mosskin_shaman = Monster("Mosskin Shaman", mosskin_shaman_stats, mosskin_shaman_gear, mosskin_shaman_loot_table, difficulty=30, description=mosskin_shaman_description, floor_range=mosskin_shaman_floor_range, spells=mosskin_shaman_spells, spell_probabilities=mosskin_shaman_spell_probabilities, initial_stats=mosskin_shaman_initial_stats)

mosskin_ranger_stats = {
    "HP": 110,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "Nature"
}
mosskin_ranger_gear = ["Enchanted Longbow", "Silent Boots"]
mosskin_ranger_loot_table = ["Ranger's Mark", "Forest Arrow", "Gold"]
mosskin_ranger_description = "Mosskin Rangers are elite archers and trackers, skilled in the art of stealth and camouflage. They patrol the forest depths, hunting down intruders with deadly accuracy and precision."
mosskin_ranger_floor_range = (30, 60)
mosskin_ranger_spells = []
mosskin_ranger_spell_probabilities = {}
mosskin_ranger_initial_stats = mosskin_ranger_stats.copy()
mosskin_ranger = Monster("Mosskin Ranger", mosskin_ranger_stats, mosskin_ranger_gear, mosskin_ranger_loot_table, difficulty=30, description=mosskin_ranger_description, floor_range=mosskin_ranger_floor_range, spells=mosskin_ranger_spells, spell_probabilities=mosskin_ranger_spell_probabilities, initial_stats=mosskin_ranger_initial_stats)

mosskin_sentinel_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 18,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Nature"
}
mosskin_sentinel_gear = ["Ancient Shield", "Thorned Spear"]
mosskin_sentinel_loot_table = ["Sentinel's Crest", "Forest Relic", "Gold"]
mosskin_sentinel_description = "Mosskin Sentinels are stalwart defenders of the forest, clad in heavy armor and wielding towering shields. They stand guard at the forest's borders, ready to repel any who would threaten their woodland home."
mosskin_sentinel_floor_range = (30, 60)
mosskin_sentinel_spells = []
mosskin_sentinel_spell_probabilities = {}
mosskin_sentinel_initial_stats = mosskin_sentinel_stats.copy()
mosskin_sentinel = Monster("Mosskin Sentinel", mosskin_sentinel_stats, mosskin_sentinel_gear, mosskin_sentinel_loot_table, difficulty=30, description=mosskin_sentinel_description, floor_range=mosskin_sentinel_floor_range, spells=mosskin_sentinel_spells, spell_probabilities=mosskin_sentinel_spell_probabilities, initial_stats=mosskin_sentinel_initial_stats)

mosskin_scout_stats = {
    "HP": 100,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Nature"
}
mosskin_scout_gear = ["Forest Bow", "Cloak of Shadows"]
mosskin_scout_loot_table = ["Scout's Mark", "Forest Arrow", "Gold"]
mosskin_scout_description = "Mosskin Scouts are swift and agile forest runners, skilled in reconnaissance and hit-and-run tactics. They traverse the woodland terrain with unmatched speed and agility, gathering information and ambushing unwary travelers."
mosskin_scout_floor_range = (30, 60)
mosskin_scout_spells = []
mosskin_scout_spell_probabilities = {}
mosskin_scout_initial_stats = mosskin_scout_stats.copy()
mosskin_scout = Monster("Mosskin Scout", mosskin_scout_stats, mosskin_scout_gear, mosskin_scout_loot_table, difficulty=30, description=mosskin_scout_description, floor_range=mosskin_scout_floor_range, spells=mosskin_scout_spells, spell_probabilities=mosskin_scout_spell_probabilities, initial_stats=mosskin_scout_initial_stats)

mosskin_sporecaster_stats = {
    "HP": 140,
    "Damage": 20,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "Nature"
}
mosskin_sporecaster_gear = ["Fungal Staff", "Spore-infused Robes"]
mosskin_sporecaster_loot_table = ["Sporecaster's Spore Pouch", "Fungal Essence", "Gold"]
mosskin_sporecaster_description = "Mosskin Sporecasters are masters of fungal magic, harnessing the power of spores and toxins found within the forest. They unleash clouds of noxious gases and debilitating spores upon their enemies, spreading chaos and confusion on the battlefield."
mosskin_sporecaster_floor_range = (30, 60)
mosskin_sporecaster_spells = ["Spore Cloud", "Toxic Blast", "Fungal Growth"]
mosskin_sporecaster_spell_probabilities = {"Spore Cloud": 0.4, "Toxic Blast": 0.3, "Fungal Growth": 0.3}
mosskin_sporecaster_initial_stats = mosskin_sporecaster_stats.copy()
mosskin_sporecaster = Monster("Mosskin Sporecaster", mosskin_sporecaster_stats, mosskin_sporecaster_gear, mosskin_sporecaster_loot_table, difficulty=30, description=mosskin_sporecaster_description, floor_range=mosskin_sporecaster_floor_range, spells=mosskin_sporecaster_spells, spell_probabilities=mosskin_sporecaster_spell_probabilities, initial_stats=mosskin_sporecaster_initial_stats)

mosskin_berserker_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 20,
    "Dexterity": 14,
    "Constitution": 22,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Nature"
}
mosskin_berserker_gear = ["Enchanted Thorn Club", "Frenzied Hide"]
mosskin_berserker_loot_table = ["Berserker's Trophy", "Bloodied Hide", "Gold"]
mosskin_berserker_description = "Mosskin Berserkers are fearsome warriors driven into frenzied rage by the primal energies of the forest. They charge into battle with reckless abandon, tearing through enemies with their bare hands and savage strength."
mosskin_berserker_floor_range = (60, 90)
mosskin_berserker_spells = []
mosskin_berserker_spell_probabilities = {}
mosskin_berserker_initial_stats = mosskin_berserker_stats.copy()
mosskin_berserker = Monster("Mosskin Berserker", mosskin_berserker_stats, mosskin_berserker_gear, mosskin_berserker_loot_table, difficulty=60, description=mosskin_berserker_description, floor_range=mosskin_berserker_floor_range, spells=mosskin_berserker_spells, spell_probabilities=mosskin_berserker_spell_probabilities, initial_stats=mosskin_berserker_initial_stats)

mosskin_thornweaver_stats = {
    "HP": 130,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "Nature"
}
mosskin_thornweaver_gear = ["Thorned Vine Whip", "Bark Armor"]
mosskin_thornweaver_loot_table = ["Thornweaver's Vine", "Briar Essence", "Gold"]
mosskin_thornweaver_description = "Mosskin Thornweavers are masters of botanical warfare, wielding sharp thorns and entangling vines to ensnare and immobilize their foes. They command the flora of the forest to lash out against intruders with lethal precision."
mosskin_thornweaver_floor_range = (30, 60)
mosskin_thornweaver_spells = ["Entangling Vines", "Thorn Barrage", "Blossoming Fury"]
mosskin_thornweaver_spell_probabilities = {"Entangling Vines": 0.4, "Thorn Barrage": 0.3, "Blossoming Fury": 0.3}
mosskin_thornweaver_initial_stats = mosskin_thornweaver_stats.copy()
mosskin_thornweaver = Monster("Mosskin Thornweaver", mosskin_thornweaver_stats, mosskin_thornweaver_gear, mosskin_thornweaver_loot_table, difficulty=30, description=mosskin_thornweaver_description, floor_range=mosskin_thornweaver_floor_range, spells=mosskin_thornweaver_spells, spell_probabilities=mosskin_thornweaver_spell_probabilities, initial_stats=mosskin_thornweaver_initial_stats)

viperling_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 10,
    "Strength": 12,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Poison"
}
viperling_gear = ["Venomous Fangs", "Slippery Scales"]
viperling_loot_table = ["Viperling Scale", "Toxic Venom", "Gold"]
viperling_description = "Venomous Viperlings are small but deadly serpents that lurk in the shadows of the forest, striking swiftly with their poisonous fangs. Their venom can incapacitate even the largest of prey, making them a formidable threat to any who dare to venture into their territory."
viperling_floor_range = (10, 30)
viperling_spells = []
viperling_spell_probabilities = {}
viperling_initial_stats = viperling_stats.copy()
viperling = Monster("Venomous Viperling", viperling_stats, viperling_gear, viperling_loot_table, difficulty=10, description=viperling_description, floor_range=viperling_floor_range, spells=viperling_spells, spell_probabilities=viperling_spell_probabilities, initial_stats=viperling_initial_stats)

brambleback_stats = {
    "HP": 150,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 12,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Nature"
}
brambleback_gear = ["Thorny Club", "Tough Bark Armor"]
brambleback_loot_table = ["Brambleback Thorn", "Tangled Vine", "Gold"]
brambleback_description = "Brambleback Bruisers are hulking creatures covered in thick, thorny armor, resembling living fortresses of tangled vegetation. They charge into battle with brute strength, using their spiked clubs to crush anything foolish enough to oppose them."
brambleback_floor_range = (30, 60)
brambleback_spells = []
brambleback_spell_probabilities = {}
brambleback_initial_stats = brambleback_stats.copy()
brambleback = Monster("Brambleback Bruiser", brambleback_stats, brambleback_gear, brambleback_loot_table, difficulty=30, description=brambleback_description, floor_range=brambleback_floor_range, spells=brambleback_spells, spell_probabilities=brambleback_spell_probabilities, initial_stats=brambleback_initial_stats)

grove_goliath_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 22,
    "Dexterity": 12,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 8,
    "Element": "Nature"
}
grove_goliath_gear = ["Ancient Oak Maul", "Living Bark Plate"]
grove_goliath_loot_table = ["Goliath's Heartwood", "Forest Relic", "Gold"]
grove_goliath_description = "Grove Goliaths are titanic guardians of the ancient forests, towering over the treetops with their massive size and formidable strength. They are revered as living embodiments of nature's fury, capable of single-handedly felling entire armies with their earth-shaking blows."
grove_goliath_floor_range = (60, 90)
grove_goliath_spells = []
grove_goliath_spell_probabilities = {}
grove_goliath_initial_stats = grove_goliath_stats.copy()
grove_goliath = Monster("Grove Goliath", grove_goliath_stats, grove_goliath_gear, grove_goliath_loot_table, difficulty=60, description=grove_goliath_description, floor_range=grove_goliath_floor_range, spells=grove_goliath_spells, spell_probabilities=grove_goliath_spell_probabilities, initial_stats=grove_goliath_initial_stats)

grove_guardian_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 14,
    "Constitution": 22,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Nature"
}
grove_guardian_gear = ["Forest Guardian Halberd", "Ancient Bark Shield"]
grove_guardian_loot_table = ["Guardian's Emblem", "Forest Relic", "Gold"]
grove_guardian_description = "Grove Guardians are ancient spirits of the forest, bound to towering suits of enchanted armor and wielding weapons crafted from the heartwood of the oldest trees. They stand as eternal sentinels, protecting the woodland realms from all who would seek to despoil them."
grove_guardian_floor_range = (30, 60)
grove_guardian_spells = []
grove_guardian_spell_probabilities = {}
grove_guardian_initial_stats = grove_guardian_stats.copy()
grove_guardian = Monster("Grove Guardian", grove_guardian_stats, grove_guardian_gear, grove_guardian_loot_table, difficulty=30, description=grove_guardian_description, floor_range=grove_guardian_floor_range, spells=grove_guardian_spells, spell_probabilities=grove_guardian_spell_probabilities, initial_stats=grove_guardian_initial_stats)

grove_spirit_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Nature"
}
grove_spirit_gear = ["Spiritual Essence", "Wisps of the Forest"]
grove_spirit_loot_table = ["Ancient Grove Sigil", "Essence of Nature", "Gold"]
grove_spirit_description = "Grove Spirits are ethereal entities born from the heart of ancient forests, embodying the wisdom and vitality of the woodland realms. They manifest as shimmering apparitions, wielding the magic of nature to protect their sacred groves from harm."
grove_spirit_floor_range = (30, 60)
grove_spirit_spells = ["Ethereal Blessing", "Spiritual Renewal", "Forest's Wrath"]
grove_spirit_spell_probabilities = {"Ethereal Blessing": 0.4, "Spiritual Renewal": 0.3, "Forest's Wrath": 0.3}
grove_spirit_initial_stats = grove_spirit_stats.copy()
grove_spirit = Monster("Grove Spirit", grove_spirit_stats, grove_spirit_gear, grove_spirit_loot_table, difficulty=30, description=grove_spirit_description, floor_range=grove_spirit_floor_range, spells=grove_spirit_spells, spell_probabilities=grove_spirit_spell_probabilities, initial_stats=grove_spirit_initial_stats)

grove_warden_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 14,
    "Constitution": 22,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Nature"
}
grove_warden_gear = ["Warden's Oak Spear", "Guardian's Plate"]
grove_warden_loot_table = ["Warden's Crest", "Ancient Grove Relic", "Gold"]
grove_warden_description = "Grove Wardens are elite protectors of the ancient forests, clad in enchanted armor crafted from the heartwood of the oldest trees. They wield spears imbued with the power of the woodland spirits, striking down any who would threaten the sanctity of their groves."
grove_warden_floor_range = (30, 60)
grove_warden_spells = []
grove_warden_spell_probabilities = {}
grove_warden_initial_stats = grove_warden_stats.copy()
grove_warden = Monster("Grove Warden", grove_warden_stats, grove_warden_gear, grove_warden_loot_table, difficulty=30, description=grove_warden_description, floor_range=grove_warden_floor_range, spells=grove_warden_spells, spell_probabilities=grove_warden_spell_probabilities, initial_stats=grove_warden_initial_stats)

grove_symbiote_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Nature"
}
grove_symbiote_gear = ["Symbiotic Vines", "Wooden Claws"]
grove_symbiote_loot_table = ["Symbiotic Seed", "Forest Essence", "Gold"]
grove_symbiote_description = "Grove Symbiotes are parasitic creatures that infest the heart of ancient trees, corrupting their hosts with their twisted influence. They emerge from the shadows to defend their arboreal homes, lashing out with venomous vines and razor-sharp claws."
grove_symbiote_floor_range = (10, 30)
grove_symbiote_spells = []
grove_symbiote_spell_probabilities = {}
grove_symbiote_initial_stats = grove_symbiote_stats.copy()
grove_symbiote = Monster("Grove Symbiote", grove_symbiote_stats, grove_symbiote_gear, grove_symbiote_loot_table, difficulty=10, description=grove_symbiote_description, floor_range=grove_symbiote_floor_range, spells=grove_symbiote_spells, spell_probabilities=grove_symbiote_spell_probabilities, initial_stats=grove_symbiote_initial_stats)

grove_howler_stats = {
    "HP": 140,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Nature"
}
grove_howler_gear = ["Howling Bark", "Fur Cloak"]
grove_howler_loot_table = ["Howler's Fang", "Ancient Wood Essence", "Gold"]
grove_howler_description = "Grove Howlers are primal beasts that roam the depths of the forest, their eerie cries echoing through the trees. They are fierce predators, using their razor-sharp claws and powerful jaws to tear apart their prey with ruthless efficiency."
grove_howler_floor_range = (30, 60)
grove_howler_spells = []
grove_howler_spell_probabilities = {}
grove_howler_initial_stats = grove_howler_stats.copy()
grove_howler = Monster("Grove Howler", grove_howler_stats, grove_howler_gear, grove_howler_loot_table, difficulty=30, description=grove_howler_description, floor_range=grove_howler_floor_range, spells=grove_howler_spells, spell_probabilities=grove_howler_spell_probabilities, initial_stats=grove_howler_initial_stats)

treant_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 20,
    "Dexterity": 12,
    "Constitution": 25,
    "Intelligence": 14,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Nature"
}
treant_gear = ["Branch Club", "Bark Armor"]
treant_loot_table = ["Treant's Heartwood", "Ancient Oak Branch", "Gold"]
treant_description = "Thorned Treants are ancient guardians of the forest, towering over the canopy with their massive forms and limbs adorned with razor-sharp thorns. They protect the woodland realms with stoic resolve, using their immense strength to crush any who would threaten the sanctity of their domain."
treant_floor_range = (50, 80)
treant_spells = []
treant_spell_probabilities = {}
treant_initial_stats = treant_stats.copy()
treant = Monster("Thorned Treant", treant_stats, treant_gear, treant_loot_table, difficulty=50, description=treant_description, floor_range=treant_floor_range, spells=treant_spells, spell_probabilities=treant_spell_probabilities, initial_stats=treant_initial_stats)

wisp_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 30,
    "Strength": 8,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Light"
}
wisp_gear = ["Ethereal Glow", "Misty Veil"]
wisp_loot_table = ["Wisp Essence", "Ghostly Orb", "Gold"]
wisp_description = "Will-o'-Wisps are mystical spirits that flicker and dance amidst the shadows of the forest, leading unwary travelers astray with their enchanting glow. They are elusive and ethereal, luring their prey deeper into the heart of the woods before vanishing without a trace."
wisp_floor_range = (20, 40)
wisp_spells = ["Ethereal Bolt", "Phantom Mirage", "Ghostly Whispers"]
wisp_spell_probabilities = {"Ethereal Bolt": 0.4, "Phantom Mirage": 0.3, "Ghostly Whispers": 0.3}
wisp_initial_stats = wisp_stats.copy()
wisp = Monster("Will-o'-Wisp", wisp_stats, wisp_gear, wisp_loot_table, difficulty=20, description=wisp_description, floor_range=wisp_floor_range, spells=wisp_spells, spell_probabilities=wisp_spell_probabilities, initial_stats=wisp_initial_stats)

huntsman_stats = {
    "HP": 150,  # Define HP attribute for Huntsman
    "Damage": 40,  # Define damage attribute for Huntsman
    "Defense": 30,  # Define Defense stat vs attack stat for Huntsman
    "Magic Defense": 40,  # Define magic defense vs spells for Huntsman
    "Strength": 22,
    "Dexterity": 25,
    "Constitution": 20,
    "Intelligence": 15,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Nature"  # Define elemental attribute of the Huntsman's attack
}

huntsman_gear = ["Silver Bow", "Cloak of the Forest"]
huntsman_loot_table = ["Beast Pelt", "Hunter's Trophy", "Forest Essence"]
huntsman_description = "The Huntsman is a skilled tracker and deadly archer, prowling the castle grounds with silent precision. Master of the bow and attuned to the ways of nature, it strikes swiftly and disappears into the shadows, leaving no trace behind."
huntsman_floor_range = (30, 35)  # Huntsman appears on floors 30 to 35
huntsman_initial_stats = huntsman_stats.copy()  # Make a copy of the initial stats
huntsman = Monster("Huntsman", huntsman_stats, huntsman_gear, huntsman_loot_table, difficulty=8, description=huntsman_description, floor_range=huntsman_floor_range, initial_stats=huntsman_initial_stats)
