from monsters.bestiary import Monster

skeleton_stats = {
    "HP": 70,  # Define HP attribute for Skeleton
    "Damage": 30,  # Define damage attribute for Skeleton
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 12,
    "Dexterity": 10,
    "Constitution": 14,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 4,
    "Element": "None"  # Define elemental attribute of the Skeleton's attack
}
skeleton_gear = ["Rusty Sword", "Broken Shield", "Tattered Armor"]
skeleton_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
skeleton_description = "Skeletons are undead warriors risen from the grave. Despite their lack of flesh, they are strong and resilient fighters, wielding weapons with deadly precision. Their hollow eyes gleam with malice as they seek to vanquish the living."
skeleton_floor_range = (1,5)
skeleton_spells = []
skeleton_spell_probabilities = {}
skeleton_initial_stats = skeleton_stats.copy() # Make a copy of the initial stats
skeleton = Monster("Skeleton", skeleton_stats, skeleton_gear, skeleton_loot_table, difficulty=4, description=skeleton_description, floor_range=skeleton_floor_range, spells=skeleton_spells, spell_probabilities=skeleton_spell_probabilities, initial_stats=skeleton_initial_stats)

zombie_stats = {
    "HP": 80,  # Define HP attribute for Zombie
    "Damage": 20,  # Define damage attribute for Zombie
    "Defense": 15,  # Define Defense stat vs attack stat
    "Magic Defense": 10,  # Define magic defense vs spells
    "Strength": 15,
    "Dexterity": 6,
    "Constitution": 16,
    "Intelligence": 4,
    "Wisdom": 6,
    "Charisma": 2,
    "Element": "None"  # Define elemental attribute of the Zombie's attack
}
zombie_gear = ["Decaying Flesh", "Tattered Clothes"]
zombie_loot_table = ["Gold", "Rotting Flesh", "Zombie Eye"]
zombie_description = "Zombies are reanimated corpses driven by a primal hunger for flesh. Despite their slow movements and decayed appearance, they possess surprising strength and resilience. Their relentless pursuit of living prey makes them a terrifying sight to behold."
zombie_floor_range = (6, 12)
zombie_spells = []
zombie_spell_probabilities = {}
zombie_initial_stats = zombie_stats.copy() # Make a copy of the initial stats
zombie = Monster("Zombie", zombie_stats, zombie_gear, zombie_loot_table, difficulty=6, description=zombie_description, floor_range=zombie_floor_range, spells=zombie_spells, spell_probabilities=zombie_spell_probabilities, initial_stats=zombie_initial_stats)

ghost_stats = {
    "HP": 50,  # Define HP attribute for Ghost
    "Damage": 25,  # Define damage attribute for Ghost
    "Defense": 10,  # Define Defense stat vs attack stat
    "Magic Defense": 30,  # Define magic defense vs spells
    "Strength": 6,
    "Dexterity": 12,
    "Constitution": 10,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 20,
    "Element": "None"  # Define elemental attribute of the Ghost's attack
}
ghost_gear = ["Ethereal Chains", "Ghostly Shroud"]
ghost_loot_table = ["Gold", "Ectoplasm", "Haunting Essence"]
ghost_description = "Ghosts are restless spirits bound to the mortal realm. They haunt ancient ruins and forgotten crypts, seeking revenge on the living. Their ethereal form makes them immune to physical attacks, but they can be banished with the power of magic or sacred artifacts."
ghost_floor_range = (10, 20)
ghost_spells = ["Haunt", "Ethereal Touch"]
ghost_spell_probabilities = {"Haunt": 0.7, "Ethereal Touch": 0.3} 
ghost_initial_stats = ghost_stats.copy() # Make a copy of the initial stats
ghost = Monster("Ghost", ghost_stats, ghost_gear, ghost_loot_table, difficulty=10, description=ghost_description, floor_range=ghost_floor_range, spells=ghost_spells, spell_probabilities=ghost_spell_probabilities, initial_stats=ghost_initial_stats)

ghoul_stats = {
    "HP": 80,  # Define HP attribute for Ghoul
    "Damage": 30,  # Define damage attribute for Ghoul
    "Defense": 20,  # Define Defense stat vs attack stat
    "Magic Defense": 15,  # Define magic defense vs spells
    "Strength": 16,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Ghoul's attack
}
ghoul_gear = ["Rotten Claws", "Decayed Flesh"]
ghoul_loot_table = ["Gold", "Rotting Heart", "Ghoul Fang"]
ghoul_description = "Ghouls are foul undead creatures that feast on the flesh of the living. With razor-sharp claws and an insatiable hunger, they hunt relentlessly through dark crypts and haunted graveyards. Their putrid stench can weaken even the bravest adventurer's resolve."
ghoul_floor_range = (12, 25)
ghoul_spells = []
ghoul_spell_probabilities = {}
ghoul_initial_stats = ghoul_stats.copy() # Make a copy of the initial stats
ghoul = Monster("Ghoul", ghoul_stats, ghoul_gear, ghoul_loot_table, difficulty=12, description=ghoul_description, floor_range=ghoul_floor_range, spells=ghoul_spells, spell_probabilities=ghoul_spell_probabilities, initial_stats=ghoul_initial_stats)

lich_stats = {
    "HP": 300,  # Define HP attribute for Lich
    "Damage": 80,  # Define damage attribute for Lich
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 60,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 30,
    "Intelligence": 25,
    "Wisdom": 20,
    "Charisma": 20,
    "Element": "Dark"  # Define elemental attribute of the Lich's attack
}
lich_gear = ["Staff of the Damned", "Robes of the Undying"]
lich_loot_table = ["Gold", "Lich's Phylactery", "Dark Tome"]
lich_description = "Liches are undead sorcerers who have transcended death through dark magic, retaining their intellect and magical abilities. They command legions of undead minions, weaving powerful spells and curses to bend reality to their will. Their ultimate goal is immortality, achieved through the creation and protection of their phylactery."
lich_floor_range = (60, 100)
lich_spells = ["Necrotic Bolt", "Soul Drain"]
lich_spell_probabilities = {"Necrotic Bolt": 0.7, "Soul Drain": 0.3} 
lich_initial_stats = lich_stats.copy() # Make a copy of the initial stats
lich = Monster("Lich", lich_stats, lich_gear, lich_loot_table, difficulty=60, description=lich_description, floor_range=lich_floor_range, spells=lich_spells, spell_probabilities=lich_spell_probabilities, initial_stats=lich_initial_stats)

mummy_stats = {
    "HP": 180,  # Define HP attribute for Mummy
    "Damage": 55,  # Define damage attribute for Mummy
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Dark"  # Define elemental attribute of the Mummy's attack
}
mummy_gear = ["Cursed Wrappings", "Ancient Amulet"]
mummy_loot_table = ["Gold", "Mummy Bandage", "Ancient Relic"]
mummy_description = "Mummies are undead creatures preserved through ancient rituals, bound to guard tombs and crypts for eternity. Their desiccated bodies are wrapped in funerary bandages, and they wield ancient curses and dark magic against intruders. Those who disturb their rest face the wrath of the ancient dead."
mummy_floor_range = (30, 60)
mummy_spells = ["Curse of Decay", "Life Drain"]
mummy_spell_probabilities = {"Curse of Decay": 0.6, "Life Drain": 0.4} 
mummy_initial_stats = mummy_stats.copy() # Make a copy of the initial stats
mummy = Monster("Mummy", mummy_stats, mummy_gear, mummy_loot_table, difficulty=30, description=mummy_description, floor_range=mummy_floor_range, spells=mummy_spells, spell_probabilities=mummy_spell_probabilities, initial_stats=mummy_initial_stats)

wraith_stats = {
    "HP": 200,  # Define HP attribute for Wraith
    "Damage": 60,  # Define damage attribute for Wraith
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Dark"  # Define elemental attribute of the Wraith's attack
}
wraith_gear = ["Ethereal Scythe", "Shadow Cloak"]
wraith_loot_table = ["Gold", "Spectral Essence", "Dark Amulet"]
wraith_description = "Wraiths are malevolent spirits trapped between the worlds of the living and the dead. They manifest as shadowy figures wreathed in darkness, draining the life force of those they encounter. Their ethereal forms make them difficult to harm with physical attacks, and their chilling presence instills fear in even the bravest of hearts."
wraith_floor_range = (40, 80)
wraith_spells = ["Soul Drain", "Shadow Bolt"]
wraith_spell_probabilities = {"Soul Drain": 0.6, "Shadow Bolt": 0.4} 
wraith_initial_stats = wraith_stats.copy() # Make a copy of the initial stats
wraith = Monster("Wraith", wraith_stats, wraith_gear, wraith_loot_table, difficulty=40, description=wraith_description, floor_range=wraith_floor_range, spells=wraith_spells, spell_probabilities=wraith_spell_probabilities, initial_stats=wraith_initial_stats)

banshee_stats = {
    "HP": 220,  # Define HP attribute for Banshee
    "Damage": 65,  # Define damage attribute for Banshee
    "Defense": 40,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 16,
    "Element": "Dark"  # Define elemental attribute of the Banshee's attack
}
banshee_gear = ["Wailing Specter", "Tattered Veil"]
banshee_loot_table = ["Gold", "Banshee Essence", "Torn Veil"]
banshee_description = "Banshees are vengeful spirits bound to the mortal realm by tragedy and sorrow. They wail with unearthly screams, haunting the night with their mournful cries and chilling presence. Their spectral form makes them immune to physical attacks, and their piercing shrieks can rend the souls of their victims."
banshee_floor_range = (40, 80)
banshee_spells = ["Wail of Despair", "Soul Siphon"]
banshee_spell_probabilities = {"Wail of Despair": 0.6, "Soul Siphon": 0.4} 
banshee_initial_stats = banshee_stats.copy() # Make a copy of the initial stats
banshee = Monster("Banshee", banshee_stats, banshee_gear, banshee_loot_table, difficulty=40, description=banshee_description, floor_range=banshee_floor_range, spells=banshee_spells, spell_probabilities=banshee_spell_probabilities, initial_stats=banshee_initial_stats)

archer_skeleton_stats = {
    "HP": 120,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 15,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"
}
archer_skeleton_gear = ["Longbow", "Ragged Cloak"]
archer_skeleton_loot_table = ["Gold", "Bone Arrow", "Broken Bow"]
archer_skeleton_description = "Archer Skeletons are undead warriors equipped with longbows and a proficiency in archery. They serve as guardians of ancient tombs and crypts, firing arrows at intruders who dare to disturb the resting place of the dead."
archer_skeleton_floor_range = (60, 120)
archer_skeleton_spells = []
archer_skeleton_spell_probabilities = {}
archer_skeleton_initial_stats = archer_skeleton_stats.copy()
archer_skeleton = Monster("Archer Skeleton", archer_skeleton_stats, archer_skeleton_gear, archer_skeleton_loot_table, difficulty=60, description=archer_skeleton_description, floor_range=archer_skeleton_floor_range, spells=archer_skeleton_spells, spell_probabilities=archer_skeleton_spell_probabilities, initial_stats=archer_skeleton_initial_stats)

skeletal_hound_stats = {
    "HP": 100,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 12,
    "Intelligence": 4,
    "Wisdom": 6,
    "Charisma": 4,
    "Element": "None"
}
skeletal_hound_gear = ["Bony Jaws", "Decayed Collar"]
skeletal_hound_loot_table = ["Gold", "Dog Bone", "Rotted Leather"]
skeletal_hound_description = "Skeletal Hounds are undead creatures reanimated from the bones of deceased dogs. They roam graveyards and haunted places, tracking down intruders with their keen sense of smell and attacking relentlessly with their bony jaws."
skeletal_hound_floor_range = (60, 120)
skeletal_hound_spells = []
skeletal_hound_spell_probabilities = {}
skeletal_hound_initial_stats = skeletal_hound_stats.copy()
skeletal_hound = Monster("Skeletal Hound", skeletal_hound_stats, skeletal_hound_gear, skeletal_hound_loot_table, difficulty=60, description=skeletal_hound_description, floor_range=skeletal_hound_floor_range, spells=skeletal_hound_spells, spell_probabilities=skeletal_hound_spell_probabilities, initial_stats=skeletal_hound_initial_stats)

decrepit_skeleton_stats = {
    "HP": 80,
    "Damage": 15,
    "Defense": 10,
    "Magic Defense": 10,
    "Strength": 10,
    "Dexterity": 12,
    "Constitution": 10,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "None"
}
decrepit_skeleton_gear = ["Rusty Sword", "Tattered Cloth"]
decrepit_skeleton_loot_table = ["Gold", "Bone Fragment", "Decayed Cloth"]
decrepit_skeleton_description = "Decrepit Skeletons are ancient undead warriors, their bones worn and weathered by the passage of time. Despite their frail appearance, they retain a portion of their former combat skills, lashing out with rusty weapons at any who disturb their rest."
decrepit_skeleton_floor_range = (40, 80)
decrepit_skeleton_spells = []
decrepit_skeleton_spell_probabilities = {}
decrepit_skeleton_initial_stats = decrepit_skeleton_stats.copy()
decrepit_skeleton = Monster("Decrepit Skeleton", decrepit_skeleton_stats, decrepit_skeleton_gear, decrepit_skeleton_loot_table, difficulty=40, description=decrepit_skeleton_description, floor_range=decrepit_skeleton_floor_range, spells=decrepit_skeleton_spells, spell_probabilities=decrepit_skeleton_spell_probabilities, initial_stats=decrepit_skeleton_initial_stats)

zombie_dragon_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 40,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"
}
zombie_dragon_gear = ["Decayed Claws", "Rotted Scales"]
zombie_dragon_loot_table = ["Gold", "Dragon Bone", "Putrid Scale"]
zombie_dragon_description = "The Zombie Dragon is a terrifying undead creature, once a mighty dragon brought back to a semblance of life through dark necromantic magic. Its flesh hangs in tatters, and its putrid breath carries the stench of decay. Despite its undead state, it retains much of its former power and ferocity."
zombie_dragon_floor_range = (200, 400)
zombie_dragon_spells = []
zombie_dragon_spell_probabilities = {}
zombie_dragon_initial_stats = zombie_dragon_stats.copy()
zombie_dragon = Monster("Zombie Dragon", zombie_dragon_stats, zombie_dragon_gear, zombie_dragon_loot_table, difficulty=200, description=zombie_dragon_description, floor_range=zombie_dragon_floor_range, spells=zombie_dragon_spells, spell_probabilities=zombie_dragon_spell_probabilities, initial_stats=zombie_dragon_initial_stats)

ghoul_fleshripper_stats = {
    "HP": 220,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 26,
    "Dexterity": 18,
    "Constitution": 22,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "Dark"
}
ghoul_fleshripper_gear = ["Flesh-tearing Claws", "Decayed Flesh Armor"]
ghoul_fleshripper_loot_table = ["Gold", "Ghoul Fang", "Rotting Flesh"]
ghoul_fleshripper_description = "Ghoul Fleshrippers are undead horrors that roam the night in search of flesh to devour. Their razor-sharp claws tear through flesh and bone with ease, leaving nothing but death and decay in their wake."
ghoul_fleshripper_floor_range = (120, 240)
ghoul_fleshripper_spells = []
ghoul_fleshripper_spell_probabilities = {}
ghoul_fleshripper_initial_stats = ghoul_fleshripper_stats.copy()
ghoul_fleshripper = Monster("Ghoul Fleshripper", ghoul_fleshripper_stats, ghoul_fleshripper_gear, ghoul_fleshripper_loot_table, difficulty=120, description=ghoul_fleshripper_description, floor_range=ghoul_fleshripper_floor_range, spells=ghoul_fleshripper_spells, spell_probabilities=ghoul_fleshripper_spell_probabilities, initial_stats=ghoul_fleshripper_initial_stats)

crypt_servant_stats = {
    "HP": 300,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 45,
    "Strength": 28,
    "Dexterity": 26,
    "Constitution": 30,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Darkness"
}
crypt_servant_gear = ["Gravekeeper's Scythe", "Spectral Armor"]
crypt_servant_loot_table = ["Gold", "Crypt Dust", "Spectral Essence"]
crypt_servant_description = "Crypt Servants are undead guardians tasked with protecting ancient tombs and burial sites. They wield scythes imbued with spectral energy, striking fear into intruders with their haunting presence."
crypt_servant_floor_range = (70, 140)
crypt_servant_spells = ["Spectral Slash", "Shadow Step", "Ethereal Grasp"]
crypt_servant_spell_probabilities = {"Spectral Slash": 0.4, "Shadow Step": 0.3, "Ethereal Grasp": 0.3}
crypt_servant_initial_stats = crypt_servant_stats.copy()
crypt_servant = Monster("Crypt Servant", crypt_servant_stats, crypt_servant_gear, crypt_servant_loot_table, difficulty=70, description=crypt_servant_description, floor_range=crypt_servant_floor_range, spells=crypt_servant_spells, spell_probabilities=crypt_servant_spell_probabilities, initial_stats=crypt_servant_initial_stats)

haunted_skull_stats = {
    "HP": 80,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 15,
    "Dexterity": 20,
    "Constitution": 15,
    "Intelligence": 10,
    "Wisdom": 10,
    "Charisma": 5,
    "Element": "Dark"
}
haunted_skull_gear = ["Ethereal Flames", "Cursed Eye"]
haunted_skull_loot_table = ["Gold", "Spectral Essence", "Enchanted Bone"]
haunted_skull_description = "The Haunted Skull is a malevolent spirit bound to a skeletal visage, its fiery gaze and eerie laughter striking terror into the hearts of those who dare to cross its path."
haunted_skull_floor_range = (6, 8)
haunted_skull_spells = ["Ethereal Blast", "Soul Siphon"]
haunted_skull_spell_probabilities = {"Ethereal Blast": 0.7, "Soul Siphon": 0.3}
haunted_skull_initial_stats = haunted_skull_stats.copy()
haunted_skull = Monster("Haunted Skull", haunted_skull_stats, haunted_skull_gear, haunted_skull_loot_table, difficulty=6, description=haunted_skull_description, floor_range=haunted_skull_floor_range, spells=haunted_skull_spells, spell_probabilities=haunted_skull_spell_probabilities, initial_stats=haunted_skull_initial_stats)

rotting_abomination_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 30,
    "Dexterity": 15,
    "Constitution": 35,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 5,
    "Element": "Dark"
}
rotting_abomination_gear = ["Putrid Flesh", "Decayed Limbs"]
rotting_abomination_loot_table = ["Gold", "Rotten Heart", "Foul Stench"]
rotting_abomination_description = "The Rotting Abomination is a grotesque amalgamation of decayed flesh and bone, its noxious odor and relentless hunger making it a formidable opponent."
rotting_abomination_floor_range = (8, 10)
rotting_abomination_spells = ["Noxious Eruption", "Putrefying Grasp"]
rotting_abomination_spell_probabilities = {"Noxious Eruption": 0.6, "Putrefying Grasp": 0.4}
rotting_abomination_initial_stats = rotting_abomination_stats.copy()
rotting_abomination = Monster("Rotting Abomination", rotting_abomination_stats, rotting_abomination_gear, rotting_abomination_loot_table, difficulty=8, description=rotting_abomination_description, floor_range=rotting_abomination_floor_range, spells=rotting_abomination_spells, spell_probabilities=rotting_abomination_spell_probabilities, initial_stats=rotting_abomination_initial_stats)

bone_golem_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 40,
    "Dexterity": 20,
    "Constitution": 45,
    "Intelligence": 10,
    "Wisdom": 20,
    "Charisma": 5,
    "Element": "Dark"
}
bone_golem_gear = ["Bone Armor", "Skullcrusher Gauntlets"]
bone_golem_loot_table = ["Gold", "Golem Core", "Cracked Bone"]
bone_golem_description = "The Bone Golem is a towering construct crafted from the bones of fallen warriors, its massive form and relentless strength making it a formidable adversary on the battlefield."
bone_golem_floor_range = (9, 11)
bone_golem_spells = ["Bone Shatter", "Bone Armor"]
bone_golem_spell_probabilities = {"Bone Shatter": 0.7, "Bone Armor": 0.3}
bone_golem_initial_stats = bone_golem_stats.copy()
bone_golem = Monster("Bone Golem", bone_golem_stats, bone_golem_gear, bone_golem_loot_table, difficulty=9, description=bone_golem_description, floor_range=bone_golem_floor_range, spells=bone_golem_spells, spell_probabilities=bone_golem_spell_probabilities, initial_stats=bone_golem_initial_stats)

bone_naga_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 30,
    "Dexterity": 30,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Dark"
}
bone_naga_gear = ["Skeletal Scales", "Serpentine Fangs"]
bone_naga_loot_table = ["Gold", "Naga Skull", "Bone Fragment"]
bone_naga_description = "The Bone Naga is a sinister serpent-like creature composed of animated bones, its hypnotic gaze and venomous bite making it a deadly foe to encounter."
bone_naga_floor_range = (8, 10)
bone_naga_spells = ["Bone Shards", "Venomous Bite"]
bone_naga_spell_probabilities = {"Bone Shards": 0.6, "Venomous Bite": 0.4}
bone_naga_initial_stats = bone_naga_stats.copy()
bone_naga = Monster("Bone Naga", bone_naga_stats, bone_naga_gear, bone_naga_loot_table, difficulty=8, description=bone_naga_description, floor_range=bone_naga_floor_range, spells=bone_naga_spells, spell_probabilities=bone_naga_spell_probabilities, initial_stats=bone_naga_initial_stats)

phantasmal_wraith_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Dark"
}
phantasmal_wraith_gear = ["Ethereal Cloak", "Spectral Scythe"]
phantasmal_wraith_loot_table = ["Gold", "Phantom Essence", "Wisp Shard"]
phantasmal_wraith_description = "The Phantasmal Wraith is a ghostly entity that haunts the ethereal plane, its chilling presence and spectral form striking fear into the hearts of the living."
phantasmal_wraith_floor_range = (9, 11)
phantasmal_wraith_spells = ["Soul Drain", "Ethereal Slash"]
phantasmal_wraith_spell_probabilities = {"Soul Drain": 0.7, "Ethereal Slash": 0.3}
phantasmal_wraith_initial_stats = phantasmal_wraith_stats.copy()
phantasmal_wraith = Monster("Phantasmal Wraith", phantasmal_wraith_stats, phantasmal_wraith_gear, phantasmal_wraith_loot_table, difficulty=9, description=phantasmal_wraith_description, floor_range=phantasmal_wraith_floor_range, spells=phantasmal_wraith_spells, spell_probabilities=phantasmal_wraith_spell_probabilities, initial_stats=phantasmal_wraith_initial_stats)

graveborn_boneknight_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 40,
    "Dexterity": 25,
    "Constitution": 40,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Dark"
}
graveborn_boneknight_gear = ["Skeletal Armor", "Bonecleaver Sword"]
graveborn_boneknight_loot_table = ["Gold", "Boneknight Helm", "Shattered Rib"]
graveborn_boneknight_description = "The Graveborn Boneknight is a fearsome warrior risen from the depths of the underworld, its skeletal form clad in ancient armor and wielding a wicked blade."
graveborn_boneknight_floor_range = (10, 12)
graveborn_boneknight_spells = ["Bonecrush", "Dreadful Charge"]
graveborn_boneknight_spell_probabilities = {"Bonecrush": 0.6, "Dreadful Charge": 0.4}
graveborn_boneknight_initial_stats = graveborn_boneknight_stats.copy()
graveborn_boneknight = Monster("Graveborn Boneknight", graveborn_boneknight_stats, graveborn_boneknight_gear, graveborn_boneknight_loot_table, difficulty=10, description=graveborn_boneknight_description, floor_range=graveborn_boneknight_floor_range, spells=graveborn_boneknight_spells, spell_probabilities=graveborn_boneknight_spell_probabilities, initial_stats=graveborn_boneknight_initial_stats)

graveborn_fleshripper_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Dark"
}
graveborn_fleshripper_gear = ["Decaying Flesh", "Rotting Claws"]
graveborn_fleshripper_loot_table = ["Gold", "Fleshripper Talon", "Rotten Heart"]
graveborn_fleshripper_description = "The Graveborn Fleshripper is a grotesque abomination created from the remains of fallen warriors, its mangled form and razor-sharp claws tearing through flesh with ease."
graveborn_fleshripper_floor_range = (9, 11)
graveborn_fleshripper_spells = ["Bloodlust", "Fleshrender"]
graveborn_fleshripper_spell_probabilities = {"Bloodlust": 0.7, "Fleshrender": 0.3}
graveborn_fleshripper_initial_stats = graveborn_fleshripper_stats.copy()
graveborn_fleshripper = Monster("Graveborn Fleshripper", graveborn_fleshripper_stats, graveborn_fleshripper_gear, graveborn_fleshripper_loot_table, difficulty=9, description=graveborn_fleshripper_description, floor_range=graveborn_fleshripper_floor_range, spells=graveborn_fleshripper_spells, spell_probabilities=graveborn_fleshripper_spell_probabilities, initial_stats=graveborn_fleshripper_initial_stats)

graveborn_bonecrusher_stats = {
    "HP": 220,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 45,
    "Dexterity": 30,
    "Constitution": 45,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Dark"
}
graveborn_bonecrusher_gear = ["Boneplate Armor", "Crushing Gauntlets"]
graveborn_bonecrusher_loot_table = ["Gold", "Bonecrusher Shard", "Shattered Skull"]
graveborn_bonecrusher_description = "The Graveborn Bonecrusher is a relentless juggernaut of death, its massive frame and immense strength capable of pulverizing even the sturdiest of foes with its bone-shattering blows."
graveborn_bonecrusher_floor_range = (10, 12)
graveborn_bonecrusher_spells = ["Bonecrush", "Skeletal Smash"]
graveborn_bonecrusher_spell_probabilities = {"Bonecrush": 0.7, "Skeletal Smash": 0.3}
graveborn_bonecrusher_initial_stats = graveborn_bonecrusher_stats.copy()
graveborn_bonecrusher = Monster("Graveborn Bonecrusher", graveborn_bonecrusher_stats, graveborn_bonecrusher_gear, graveborn_bonecrusher_loot_table, difficulty=10, description=graveborn_bonecrusher_description, floor_range=graveborn_bonecrusher_floor_range, spells=graveborn_bonecrusher_spells, spell_probabilities=graveborn_bonecrusher_spell_probabilities, initial_stats=graveborn_bonecrusher_initial_stats)

graveborn_soulflayer_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 40,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 20,
    "Element": "Dark"
}
graveborn_soulflayer_gear = ["Soulshredder Scythe", "Shadowcloak Robes"]
graveborn_soulflayer_loot_table = ["Gold", "Soulflayer Essence", "Tattered Spirit"]
graveborn_soulflayer_description = "The Graveborn Soulflayer is a sinister being that feeds on the essence of souls, its malevolent presence and deadly scythe striking fear into the hearts of its victims."
graveborn_soulflayer_floor_range = (11, 13)
graveborn_soulflayer_spells = ["Soul Harvest", "Shadow Strike"]
graveborn_soulflayer_spell_probabilities = {"Soul Harvest": 0.7, "Shadow Strike": 0.3}
graveborn_soulflayer_initial_stats = graveborn_soulflayer_stats.copy()
graveborn_soulflayer = Monster("Graveborn Soulflayer", graveborn_soulflayer_stats, graveborn_soulflayer_gear, graveborn_soulflayer_loot_table, difficulty=11, description=graveborn_soulflayer_description, floor_range=graveborn_soulflayer_floor_range, spells=graveborn_soulflayer_spells, spell_probabilities=graveborn_soulflayer_spell_probabilities, initial_stats=graveborn_soulflayer_initial_stats)

graveborn_necroblade_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 40,
    "Dexterity": 45,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Dark"
}
graveborn_necroblade_gear = ["Necrotic Blade", "Darkened Armor"]
graveborn_necroblade_loot_table = ["Gold", "Necroblade Shard", "Tainted Essence"]
graveborn_necroblade_description = "The Graveborn Necroblade is a fearsome warrior adept in the dark arts of necromancy, its razor-sharp blade and unholy powers striking terror into the hearts of its enemies."
graveborn_necroblade_floor_range = (10, 12)
graveborn_necroblade_spells = ["Soul Siphon", "Deathly Strike"]
graveborn_necroblade_spell_probabilities = {"Soul Siphon": 0.6, "Deathly Strike": 0.4}
graveborn_necroblade_initial_stats = graveborn_necroblade_stats.copy()
graveborn_necroblade = Monster("Graveborn Necroblade", graveborn_necroblade_stats, graveborn_necroblade_gear, graveborn_necroblade_loot_table, difficulty=10, description=graveborn_necroblade_description, floor_range=graveborn_necroblade_floor_range, spells=graveborn_necroblade_spells, spell_probabilities=graveborn_necroblade_spell_probabilities, initial_stats=graveborn_necroblade_initial_stats)

graveborn_dark_mage_stats = {
    "HP": 160,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 35,
    "Strength": 20,
    "Dexterity": 30,
    "Constitution": 30,
    "Intelligence": 45,
    "Wisdom": 35,
    "Charisma": 25,
    "Element": "Dark"
}
graveborn_dark_mage_gear = ["Shadowweave Robes", "Voidstaff"]
graveborn_dark_mage_loot_table = ["Gold", "Dark Mage Tome", "Shadow Crystal"]
graveborn_dark_mage_description = "The Graveborn Dark Mage is a master of dark sorcery, wielding shadowy magic and summoning unholy powers to obliterate its foes with dark energy."
graveborn_dark_mage_floor_range = (9, 11)
graveborn_dark_mage_spells = ["Dark Bolt", "Shadow Nova"]
graveborn_dark_mage_spell_probabilities = {"Dark Bolt": 0.7, "Shadow Nova": 0.3}
graveborn_dark_mage_initial_stats = graveborn_dark_mage_stats.copy()
graveborn_dark_mage = Monster("Graveborn Dark Mage", graveborn_dark_mage_stats, graveborn_dark_mage_gear, graveborn_dark_mage_loot_table, difficulty=9, description=graveborn_dark_mage_description, floor_range=graveborn_dark_mage_floor_range, spells=graveborn_dark_mage_spells, spell_probabilities=graveborn_dark_mage_spell_probabilities, initial_stats=graveborn_dark_mage_initial_stats)

damnation_book_stats = {
    "HP": 350,
    "Damage": 20,
    "Defense": 50,
    "Magic Defense": 70,
    "Strength": 10,
    "Dexterity": 30,
    "Constitution": 60,
    "Intelligence": 80,
    "Wisdom": 80,
    "Charisma": 50,
    "Element": "Dark"
}
damnation_book_gear = ["Tanned Hide Cover", "Sinister Pages"]
damnation_book_loot_table = ["Gold", "Cursed Knowledge", "Enchanted Bookmark"]
damnation_book_description = "The Damnation Book is a massive leather-bound tome whose cover is adorned with the tanned hide of an intelligent being. It bears a snarling face with unnaturally intelligent eyes, which communicate in a high, nasal voice. Its pages contain forbidden knowledge and dark incantations, tempting those who dare to open it with promises of power at a terrible cost."
damnation_book_floor_range = (15, 17)
damnation_book_spells = ["Soul Bind", "Dark Revelation"]
damnation_book_spell_probabilities = {"Soul Bind": 0.7, "Dark Revelation": 0.3}
damnation_book_initial_stats = damnation_book_stats.copy()
damnation_book = Monster("Damnation Book", damnation_book_stats, damnation_book_gear, damnation_book_loot_table, difficulty=15, description=damnation_book_description, floor_range=damnation_book_floor_range, spells=damnation_book_spells, spell_probabilities=damnation_book_spell_probabilities, initial_stats=damnation_book_initial_stats)

minotaur_skeleton_stats = {
    "HP": 280,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 50,
    "Dexterity": 35,
    "Constitution": 60,
    "Intelligence": 15,
    "Wisdom": 25,
    "Charisma": 10,
    "Element": "Dark"
}
minotaur_skeleton_gear = ["Bony Horns", "Rusty Axe"]
minotaur_skeleton_loot_table = ["Gold", "Minotaur Skull", "Broken Horn"]
minotaur_skeleton_description = "The Minotaur Skeleton is the reanimated remains of a fearsome minotaur warrior, its bony form still possessing great strength and wielding a rusted axe with deadly precision."
minotaur_skeleton_floor_range = (11, 13)
minotaur_skeleton_spells = ["Bone Crush", "Rage"]
minotaur_skeleton_spell_probabilities = {"Bone Crush": 0.6, "Rage": 0.4}
minotaur_skeleton_initial_stats = minotaur_skeleton_stats.copy()
minotaur_skeleton = Monster("Minotaur Skeleton", minotaur_skeleton_stats, minotaur_skeleton_gear, minotaur_skeleton_loot_table, difficulty=11, description=minotaur_skeleton_description, floor_range=minotaur_skeleton_floor_range, spells=minotaur_skeleton_spells, spell_probabilities=minotaur_skeleton_spell_probabilities, initial_stats=minotaur_skeleton_initial_stats)

ogre_zombie_stats = {
    "HP": 400,
    "Damage": 65,
    "Defense": 45,
    "Magic Defense": 35,
    "Strength": 60,
    "Dexterity": 25,
    "Constitution": 70,
    "Intelligence": 10,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Dark"
}
ogre_zombie_gear = ["Decayed Flesh", "Crude Club"]
ogre_zombie_loot_table = ["Gold", "Ogre Skull", "Putrid Flesh"]
ogre_zombie_description = "The Ogre Zombie is a hulking undead creature, its massive frame and rotting flesh making it a formidable opponent on the battlefield. It lumbers forward with a crude club, seeking to crush anything in its path."
ogre_zombie_floor_range = (14, 16)
ogre_zombie_spells = ["Decay", "Bone Breaker"]
ogre_zombie_spell_probabilities = {"Decay": 0.7, "Bone Breaker": 0.3}
ogre_zombie_initial_stats = ogre_zombie_stats.copy()
ogre_zombie = Monster("Ogre Zombie", ogre_zombie_stats, ogre_zombie_gear, ogre_zombie_loot_table, difficulty=14, description=ogre_zombie_description, floor_range=ogre_zombie_floor_range, spells=ogre_zombie_spells, spell_probabilities=ogre_zombie_spell_probabilities, initial_stats=ogre_zombie_initial_stats)

skeletal_juggernaut_stats = {
    "HP": 500,
    "Damage": 70,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 70,
    "Dexterity": 40,
    "Constitution": 80,
    "Intelligence": 15,
    "Wisdom": 30,
    "Charisma": 10,
    "Element": "Dark"
}
skeletal_juggernaut_gear = ["Reinforced Bones", "Ancient Warhammer"]
skeletal_juggernaut_loot_table = ["Gold", "Juggernaut Plate", "Broken Warhammer"]
skeletal_juggernaut_description = "The Skeletal Juggernaut is a massive undead warrior, its skeletal frame augmented with reinforced bones and wielding an ancient warhammer with devastating force. It advances relentlessly, crushing everything in its path."
skeletal_juggernaut_floor_range = (16, 18)
skeletal_juggernaut_spells = ["Bone Shatter", "Death Charge"]
skeletal_juggernaut_spell_probabilities = {"Bone Shatter": 0.6, "Death Charge": 0.4}
skeletal_juggernaut_initial_stats = skeletal_juggernaut_stats.copy()
skeletal_juggernaut = Monster("Skeletal Juggernaut", skeletal_juggernaut_stats, skeletal_juggernaut_gear, skeletal_juggernaut_loot_table, difficulty=16, description=skeletal_juggernaut_description, floor_range=skeletal_juggernaut_floor_range, spells=skeletal_juggernaut_spells, spell_probabilities=skeletal_juggernaut_spell_probabilities, initial_stats=skeletal_juggernaut_initial_stats)

tyrannosaurus_zombie_stats = {
    "HP": 600,
    "Damage": 80,
    "Defense": 70,
    "Magic Defense": 60,
    "Strength": 80,
    "Dexterity": 30,
    "Constitution": 90,
    "Intelligence": 10,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Dark"
}
tyrannosaurus_zombie_gear = ["Decayed Scales", "Bone Spikes"]
tyrannosaurus_zombie_loot_table = ["Gold", "Tyrannosaurus Skull", "Rotted Flesh"]
tyrannosaurus_zombie_description = "The Tyrannosaurus Zombie is a colossal undead predator, its massive form and decayed scales making it a terrifying sight on the battlefield. With bone spikes protruding from its body, it charges forward with relentless ferocity, seeking to devour anything in its path."
tyrannosaurus_zombie_floor_range = (18, 20)
tyrannosaurus_zombie_spells = ["Rending Bite", "Decay Aura"]
tyrannosaurus_zombie_spell_probabilities = {"Rending Bite": 0.7, "Decay Aura": 0.3}
tyrannosaurus_zombie_initial_stats = tyrannosaurus_zombie_stats.copy()
tyrannosaurus_zombie = Monster("Tyrannosaurus Zombie", tyrannosaurus_zombie_stats, tyrannosaurus_zombie_gear, tyrannosaurus_zombie_loot_table, difficulty=18, description=tyrannosaurus_zombie_description, floor_range=tyrannosaurus_zombie_floor_range, spells=tyrannosaurus_zombie_spells, spell_probabilities=tyrannosaurus_zombie_spell_probabilities, initial_stats=tyrannosaurus_zombie_initial_stats)

