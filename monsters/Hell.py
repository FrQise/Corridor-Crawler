from monsters.bestiary import Monster

hellhound_stats = {
    "HP": 150,  # Define HP attribute for Hellhound
    "Damage": 50,  # Define damage attribute for Hellhound
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 20,  # Define magic defense vs spells
    "Strength": 22,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Fire"  # Define elemental attribute of the Hellhound's attack
}
hellhound_gear = ["Fiery Fangs", "Infernal Hide"]
hellhound_loot_table = ["Gold", "Hellhound Fang", "Charred Bone"]
hellhound_description = "Hellhounds are demonic creatures bound to the infernal realms, their very presence radiating heat and flames. With blazing fur and fiery breath, they stalk the darkest corners of the underworld, hunting down souls to drag back to the fiery pits of Hell. Their ferocity knows no bounds, and their bite burns with hellfire."
hellhound_floor_range = (1, 2)
hellhound_spells = ["Inferno Breath", "Flame Charge"]
hellhound_spell_probabilities = {"Inferno Breath": 0.6, "Flame Charge": 0.4} 
hellhound_initial_stats = hellhound_stats.copy() # Make a copy of the initial stats
hellhound = Monster("Hellhound", hellhound_stats, hellhound_gear, hellhound_loot_table, difficulty=25, description=hellhound_description, floor_range=hellhound_floor_range, spells=hellhound_spells, spell_probabilities=hellhound_spell_probabilities, initial_stats=hellhound_initial_stats)

hellspawned_warrior_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 20,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 15,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Fire"
}

hellspawned_warrior_gear = ["Infernal Plate", "Hellforged Sword"]
hellspawned_warrior_loot_table = ["Fiery Essence", "Charred Helm", "Inferno Shard"]
hellspawned_warrior_description = "The Hellspawned Warrior emerges from the depths of Hell, clad in infernal armor and wielding a sword forged in the flames of damnation. Its fiery gaze strikes fear into the hearts of even the bravest adventurers."
hellspawned_warrior_floor_range = (1, 2)
hellspawned_warrior_spells = ["Flamestrike", "Infernal Rage"]
hellspawned_warrior_spell_probabilities = {"Flamestrike": 0.7, "Infernal Rage": 0.3}
hellspawned_warrior_initial_stats = hellspawned_warrior_stats.copy()
hellspawned_warrior = Monster("Hellspawned Warrior", hellspawned_warrior_stats, hellspawned_warrior_gear, hellspawned_warrior_loot_table, difficulty=8, description=hellspawned_warrior_description, floor_range=hellspawned_warrior_floor_range, spells=hellspawned_warrior_spells, spell_probabilities=hellspawned_warrior_spell_probabilities, initial_stats=hellspawned_warrior_initial_stats)

fire_bat_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 20,
    "Strength": 8,
    "Dexterity": 18,
    "Constitution": 10,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Fire"
}
fire_bat_gear = ["Fiery Fangs", "Flaming Wings"]
fire_bat_loot_table = ["Gold", "Bat Wing", "Fire Essence"]
fire_bat_description = "Fire Bats are nocturnal creatures that dwell in volcanic regions, their bodies infused with the flames of the underworld. They swoop down upon their prey, attacking with blazing fangs and scorching wings."
fire_bat_floor_range = (1, 3)
fire_bat_spells = []
fire_bat_spell_probabilities = {}
fire_bat_initial_stats = fire_bat_stats.copy()
fire_bat = Monster("Fire Bat", fire_bat_stats, fire_bat_gear, fire_bat_loot_table, difficulty=40, description=fire_bat_description, floor_range=fire_bat_floor_range, spells=fire_bat_spells, spell_probabilities=fire_bat_spell_probabilities, initial_stats=fire_bat_initial_stats)

crimsoncap_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 20,
    "Dexterity": 22,
    "Constitution": 24,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Fire"
}
crimsoncap_gear = ["Fiery Scimitar", "Burning Robes"]
crimsoncap_loot_table = ["Gold", "Crimsoncap Mushroom", "Infernal Essence"]
crimsoncap_description = "Crimsoncaps are sinister creatures that inhabit the darkest corners of volcanic caverns. They are adorned with fiery robes and wield scimitars imbued with the flames of the underworld."
crimsoncap_floor_range = (2, 3)
crimsoncap_spells = ["Inferno Burst", "Flame Shield", "Fireball"]
crimsoncap_spell_probabilities = {"Inferno Burst": 0.4, "Flame Shield": 0.3, "Fireball": 0.3}
crimsoncap_initial_stats = crimsoncap_stats.copy()
crimsoncap = Monster("Crimsoncap", crimsoncap_stats, crimsoncap_gear, crimsoncap_loot_table, difficulty=70, description=crimsoncap_description, floor_range=crimsoncap_floor_range, spells=crimsoncap_spells, spell_probabilities=crimsoncap_spell_probabilities, initial_stats=crimsoncap_initial_stats)

lava_leaper_stats = {
    "HP": 250,  # Define HP attribute for Lava Leaper
    "Damage": 70,  # Define damage attribute for Lava Leaper
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"  # Define elemental attribute of the Lava Leaper's attack
}
lava_leaper_gear = ["Magma-covered Claws", "Obsidian Shell"]
lava_leaper_loot_table = ["Gold", "Molten Core", "Obsidian Shard"]
lava_leaper_description = "Lava Leapers are agile creatures that dwell near underground lava flows, using their powerful legs to leap from rock to rock with ease. They are covered in fiery magma, making them immune to the scorching heat of the lava. They can spew streams of molten lava at their enemies and create pools of magma to trap them."
lava_leaper_floor_range = (2, 3)
lava_leaper_spells = []
lava_leaper_spell_probabilities = {}
lava_leaper_initial_stats = lava_leaper_stats.copy() # Make a copy of the initial stats
lava_leaper = Monster("Lava Leaper", lava_leaper_stats, lava_leaper_gear, lava_leaper_loot_table, difficulty=100, description=lava_leaper_description, floor_range=lava_leaper_floor_range, spells=lava_leaper_spells, spell_probabilities=lava_leaper_spell_probabilities, initial_stats=lava_leaper_initial_stats)

infernal_imp_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 30,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
infernal_imp_gear = ["Fiery Pitchfork", "Infernal Horns"]
infernal_imp_loot_table = ["Gold", "Impish Essence", "Hellfire Ember"]
infernal_imp_description = "Infernal Imps are mischievous and malevolent creatures that thrive in the fiery depths of Hell. They delight in causing chaos and tormenting the souls of the damned with their fiery pranks and sharp pitchforks."
infernal_imp_floor_range = (2, 4)
infernal_imp_spells = []
infernal_imp_spell_probabilities = {}
infernal_imp_initial_stats = infernal_imp_stats.copy()
infernal_imp = Monster("Infernal Imp", infernal_imp_stats, infernal_imp_gear, infernal_imp_loot_table, difficulty=50, description=infernal_imp_description, floor_range=infernal_imp_floor_range, spells=infernal_imp_spells, spell_probabilities=infernal_imp_spell_probabilities, initial_stats=infernal_imp_initial_stats)

hellwasp_stats = {
    "HP": 90,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 12,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Fire"
}
hellwasp_gear = ["Fiery Stinger", "Infernal Wings"]
hellwasp_loot_table = ["Gold", "Hellwasp Venom", "Infernal Wing Fragment"]
hellwasp_description = "Hellwasps are infernal insects imbued with the flames of the underworld. They patrol the fiery realms, their stingers dripping with venom that can inflict agonizing pain upon their victims."
hellwasp_floor_range = (2, 4)
hellwasp_spells = []
hellwasp_spell_probabilities = {}
hellwasp_initial_stats = hellwasp_stats.copy()
hellwasp = Monster("Hellwasp", hellwasp_stats, hellwasp_gear, hellwasp_loot_table, difficulty=60, description=hellwasp_description, floor_range=hellwasp_floor_range, spells=hellwasp_spells, spell_probabilities=hellwasp_spell_probabilities, initial_stats=hellwasp_initial_stats)

salamander_stats = {
    "HP": 180,  # Define HP attribute for Salamander
    "Damage": 55,  # Define damage attribute for Salamander
    "Defense": 35,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 20,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Fire"  # Define elemental attribute of the Salamander's attack
}
salamander_gear = ["Flaming Spear", "Fire-resistant Scales"]
salamander_loot_table = ["Gold", "Salamander Scale", "Fire Essence"]
salamander_description = "Salamanders are fiery reptilian creatures that dwell in volcanic regions and molten caverns. They are immune to the searing heat of their environment and harness the power of fire in combat. With their flaming spears and scorching breath, they incinerate their foes, leaving behind nothing but ash."
salamander_floor_range = (2, 4)
salamander_spells = []
salamander_spell_probabilities = {}
salamander_initial_stats = salamander_stats.copy() # Make a copy of the initial stats
salamander = Monster("Salamander", salamander_stats, salamander_gear, salamander_loot_table, difficulty=40, description=salamander_description, floor_range=salamander_floor_range, spells=salamander_spells, spell_probabilities=salamander_spell_probabilities, initial_stats=salamander_initial_stats)

burnbones_stats = {
    "HP": 140,
    "Damage": 50,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 22,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Fire"
}

burnbones_gear = ["Charred Remnants", "Blazing Skull"]
burnbones_loot_table = ["Ember Ash", "Singed Rib", "Infernal Essence"]
burnbones_description = "The Burnbones is a fiery apparition, its skeletal form wreathed in flames that consume everything in their path. With a skull that burns with infernal fire, it spreads destruction throughout the castle, leaving behind only ash and cinder."
burnbones_floor_range = (4, 6)
burnbones_spells = ["Pyroblast", "Inferno"]
burnbones_spell_probabilities = {"Pyroblast": 0.6, "Inferno": 0.4}
burnbones_initial_stats = burnbones_stats.copy()
burnbones = Monster("Burnbones", burnbones_stats, burnbones_gear, burnbones_loot_table, difficulty=7, description=burnbones_description, floor_range=burnbones_floor_range, spells=burnbones_spells, spell_probabilities=burnbones_spell_probabilities, initial_stats=burnbones_initial_stats)

molten_drifter_stats = {
    "HP": 400,  # Define HP attribute for Molten Drifter
    "Damage": 120,  # Define damage attribute for Molten Drifter
    "Defense": 60,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 45,
    "Intelligence": 18,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"  # Define elemental attribute of the Molten Drifter's attack
}
molten_drifter_gear = ["Magma-covered Claws", "Obsidian Shell"]
molten_drifter_loot_table = ["Gold", "Molten Core", "Obsidian Shard"]
molten_drifter_description = "Molten Drifters are fiery beings born from the depths of the earth, their bodies constantly aflame with molten lava. They roam the underground chambers and lava-filled caverns, leaving trails of fire in their wake. With their magma-covered claws and ability to spew scorching flames, they are formidable adversaries, capable of turning stone to ash with a single touch."
molten_drifter_floor_range = (4, 6)
molten_drifter_spells = []
molten_drifter_spell_probabilities = {}
molten_drifter_initial_stats = molten_drifter_stats.copy() # Make a copy of the initial stats
molten_drifter = Monster("Molten Drifter", molten_drifter_stats, molten_drifter_gear, molten_drifter_loot_table, difficulty=150, description=molten_drifter_description, floor_range=molten_drifter_floor_range, spells=molten_drifter_spells, spell_probabilities=molten_drifter_spell_probabilities, initial_stats=molten_drifter_initial_stats)

inferno_wraith_stats = {
    "HP": 600,
    "Damage": 100,
    "Defense": 50,
    "Magic Defense": 70,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
inferno_wraith_gear = ["Hellfire Scythe", "Ethereal Shroud"]
inferno_wraith_loot_table = ["Gold", "Infernal Soul", "Shadowfire Essence"]
inferno_wraith_description = "Inferno Wraiths are spectral beings consumed by eternal flames, haunting the depths of Hell with their burning wrath. They can phase through solid objects and unleash blasts of infernal energy to annihilate their foes."
inferno_wraith_floor_range = (4, 6)
inferno_wraith_spells = []
inferno_wraith_spell_probabilities = {}
inferno_wraith_initial_stats = inferno_wraith_stats.copy()
inferno_wraith = Monster("Inferno Wraith", inferno_wraith_stats, inferno_wraith_gear, inferno_wraith_loot_table, difficulty=250, description=inferno_wraith_description, floor_range=inferno_wraith_floor_range, spells=inferno_wraith_spells, spell_probabilities=inferno_wraith_spell_probabilities, initial_stats=inferno_wraith_initial_stats)

doombringer_stats = {
    "HP": 700,
    "Damage": 110,
    "Defense": 70,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
doombringer_gear = ["Blade of Ruin", "Cloak of Despair"]
doombringer_loot_table = ["Gold", "Doombringer's Mark", "Cursed Relic"]
doombringer_description = "Doombringers are harbingers of destruction and despair, wielding cursed weapons that bring ruin to all who stand against them. They revel in chaos and thrive in the midst of carnage, spreading misery and suffering wherever they go."
doombringer_floor_range = (5, 7)
doombringer_spells = []
doombringer_spell_probabilities = {}
doombringer_initial_stats = doombringer_stats.copy()
doombringer = Monster("Doombringer", doombringer_stats, doombringer_gear, doombringer_loot_table, difficulty=300, description=doombringer_description, floor_range=doombringer_floor_range, spells=doombringer_spells, spell_probabilities=doombringer_spell_probabilities, initial_stats=doombringer_initial_stats)

infernal_juggernaut_stats = {
    "HP": 900,
    "Damage": 130,
    "Defense": 90,
    "Magic Defense": 70,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
infernal_juggernaut_gear = ["Molten Maul", "Infernal Plate"]
infernal_juggernaut_loot_table = ["Gold", "Infernal Core", "Demonic Essence"]
infernal_juggernaut_description = "Infernal Juggernauts are colossal and unstoppable forces of destruction, clad in armor forged from the flames of Hell itself. They charge into battle with reckless abandon, crushing everything in their path with their immense strength and fiery rage."
infernal_juggernaut_floor_range = (5, 7)
infernal_juggernaut_spells = []
infernal_juggernaut_spell_probabilities = {}
infernal_juggernaut_initial_stats = infernal_juggernaut_stats.copy()
infernal_juggernaut = Monster("Infernal Juggernaut", infernal_juggernaut_stats, infernal_juggernaut_gear, infernal_juggernaut_loot_table, difficulty=350, description=infernal_juggernaut_description, floor_range=infernal_juggernaut_floor_range, spells=infernal_juggernaut_spells, spell_probabilities=infernal_juggernaut_spell_probabilities, initial_stats=infernal_juggernaut_initial_stats)

blazing_banshee_stats = {
    "HP": 600,
    "Damage": 100,
    "Defense": 50,
    "Magic Defense": 80,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
blazing_banshee_gear = ["Cursed Scream", "Eternal Ember"]
blazing_banshee_loot_table = ["Gold", "Banshee's Wail", "Infernal Tears"]
blazing_banshee_description = "Blazing Banshees are ethereal spirits consumed by the flames of Hell, haunting the scorched plains with their mournful cries. They unleash blasts of hellfire and curses upon those who dare to intrude upon their domain."
blazing_banshee_floor_range = (5, 8)
blazing_banshee_spells = []
blazing_banshee_spell_probabilities = {}
blazing_banshee_initial_stats = blazing_banshee_stats.copy()
blazing_banshee = Monster("Blazing Banshee", blazing_banshee_stats, blazing_banshee_gear, blazing_banshee_loot_table, difficulty=250, description=blazing_banshee_description, floor_range=blazing_banshee_floor_range, spells=blazing_banshee_spells, spell_probabilities=blazing_banshee_spell_probabilities, initial_stats=blazing_banshee_initial_stats)

incubus_stats = {
    "HP": 600,
    "Damage": 100,
    "Defense": 60,
    "Magic Defense": 80,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
incubus_gear = ["Seductive Blade", "Shadow Veil"]
incubus_loot_table = ["Gold", "Infernal Charm", "Demon's Kiss"]
incubus_description = "Incubi are demonic seducers who prey on mortal desires, luring victims into their embrace with promises of power and pleasure. Once ensnared, they drain their victims' life force and corrupt their souls for eternity."
incubus_floor_range = (6, 8)
incubus_spells = []
incubus_spell_probabilities = {}
incubus_initial_stats = incubus_stats.copy()
incubus = Monster("Incubus", incubus_stats, incubus_gear, incubus_loot_table, difficulty=250, description=incubus_description, floor_range=incubus_floor_range, spells=incubus_spells, spell_probabilities=incubus_spell_probabilities, initial_stats=incubus_initial_stats)

ashen_abomination_stats = {
    "HP": 800,
    "Damage": 120,
    "Defense": 80,
    "Magic Defense": 70,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
ashen_abomination_gear = ["Corrupted Claws", "Shadowed Carapace"]
ashen_abomination_loot_table = ["Gold", "Ashen Essence", "Dark Corruption"]
ashen_abomination_description = "Ashen Abominations are grotesque and malformed creatures forged from the ashes of fallen souls. They roam the scorched wastelands of Hell, leaving devastation in their wake as they consume everything in their path."
ashen_abomination_floor_range = (6, 8)
ashen_abomination_spells = []
ashen_abomination_spell_probabilities = {}
ashen_abomination_initial_stats = ashen_abomination_stats.copy()
ashen_abomination = Monster("Ashen Abomination", ashen_abomination_stats, ashen_abomination_gear, ashen_abomination_loot_table, difficulty=300, description=ashen_abomination_description, floor_range=ashen_abomination_floor_range, spells=ashen_abomination_spells, spell_probabilities=ashen_abomination_spell_probabilities, initial_stats=ashen_abomination_initial_stats)

fire_elemental_stats = {
    "HP": 150,  # Define HP attribute for Fire Elemental
    "Damage": 50,  # Define damage attribute for Fire Elemental
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Fire"  # Define elemental attribute of the Fire Elemental's attack
}
fire_elemental_gear = ["Fiery Form", "Inferno Cloak"]
fire_elemental_loot_table = ["Gold", "Fire Essence", "Fire Ruby"]
fire_elemental_description = "Fire Elementals are creatures of pure flame, conjured from the heart of volcanoes and infernos. They wield the destructive power of fire, engulfing their enemies in searing flames and scorching heat. Their fiery presence can ignite fear in the hearts of even the bravest adventurers."
fire_elemental_floor_range = (6, 8)
fire_elemental_spells = ["Fireball", "Flame Burst"]
fire_elemental_spell_probabilities = {"Fireball": 0.6, "Flame Burst": 0.4} 
fire_elemental_initial_stats = fire_elemental_stats.copy() # Make a copy of the initial stats
fire_elemental = Monster("Fire Elemental", fire_elemental_stats, fire_elemental_gear, fire_elemental_loot_table, difficulty=20, description=fire_elemental_description, floor_range=fire_elemental_floor_range, spells=fire_elemental_spells, spell_probabilities=fire_elemental_spell_probabilities, initial_stats=fire_elemental_initial_stats)

infernal_knight_stats = {
    "HP": 900,
    "Damage": 130,
    "Defense": 90,
    "Magic Defense": 80,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
infernal_knight_gear = ["Infernal Blade", "Knight's Inferno Armor"]
infernal_knight_loot_table = ["Gold", "Knight's Crest", "Infernal Emblem"]
infernal_knight_description = "Infernal Knights are elite warriors of Hell, clad in armor forged in the flames of damnation. They wield blazing swords that cleave through steel and bone with ease, defending the infernal realm from all who dare to challenge its dark dominion."
infernal_knight_floor_range = (6, 8)
infernal_knight_spells = []
infernal_knight_spell_probabilities = {}
infernal_knight_initial_stats = infernal_knight_stats.copy()
infernal_knight = Monster("Infernal Knight", infernal_knight_stats, infernal_knight_gear, infernal_knight_loot_table, difficulty=350, description=infernal_knight_description, floor_range=infernal_knight_floor_range, spells=infernal_knight_spells, spell_probabilities=infernal_knight_spell_probabilities, initial_stats=infernal_knight_initial_stats)

demoness_succubus_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
demoness_succubus_gear = ["Seduction Whip", "Shadow Veil"]
demoness_succubus_loot_table = ["Gold", "Succubus Kiss", "Dark Temptation"]
demoness_succubus_description = "Demoness Succubi are seductive and deadly temptresses who lure mortals into their embrace with promises of pleasure and power. With their hypnotic beauty and beguiling charms, they ensnare their prey and drain their life force to sustain themselves in the infernal realm."
demoness_succubus_floor_range = (7, 9)
demoness_succubus_spells = []
demoness_succubus_spell_probabilities = {}
demoness_succubus_initial_stats = demoness_succubus_stats.copy()
demoness_succubus = Monster("Demoness Succubus", demoness_succubus_stats, demoness_succubus_gear, demoness_succubus_loot_table, difficulty=150, description=demoness_succubus_description, floor_range=demoness_succubus_floor_range, spells=demoness_succubus_spells, spell_probabilities=demoness_succubus_spell_probabilities, initial_stats=demoness_succubus_initial_stats)

soul_devourer_stats = {
    "HP": 500,
    "Damage": 90,
    "Defense": 60,
    "Magic Defense": 70,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
soul_devourer_gear = ["Soulreaper Scythe", "Shadow Cloak"]
soul_devourer_loot_table = ["Gold", "Soul Essence", "Dark Relic"]
soul_devourer_description = "Soul Devourers are sinister beings that feed on the souls of the damned, harvesting them with their razor-sharp scythes. They lurk in the shadows of Hell, waiting to pounce on unsuspecting victims and drag them into eternal torment."
soul_devourer_floor_range = (7, 9)
soul_devourer_spells = []
soul_devourer_spell_probabilities = {}
soul_devourer_initial_stats = soul_devourer_stats.copy()
soul_devourer = Monster("Soul Devourer", soul_devourer_stats, soul_devourer_gear, soul_devourer_loot_table, difficulty=200, description=soul_devourer_description, floor_range=soul_devourer_floor_range, spells=soul_devourer_spells, spell_probabilities=soul_devourer_spell_probabilities, initial_stats=soul_devourer_initial_stats)

demon_brute_stats = {
    "HP": 800,
    "Damage": 120,
    "Defense": 80,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
demon_brute_gear = ["Hellforged Axe", "Demonhide Armor"]
demon_brute_loot_table = ["Gold", "Demon Blood", "Infernal Trophy"]
demon_brute_description = "Demon Brutes are massive and fearsome warriors of Hell, wielding enormous axes forged in the fires of damnation. They are relentless in their pursuit of souls, crushing anything that stands in their way with brute strength and ferocity."
demon_brute_floor_range = (7, 9)
demon_brute_spells = []
demon_brute_spell_probabilities = {}
demon_brute_initial_stats = demon_brute_stats.copy()
demon_brute = Monster("Demon Brute", demon_brute_stats, demon_brute_gear, demon_brute_loot_table, difficulty=300, description=demon_brute_description, floor_range=demon_brute_floor_range, spells=demon_brute_spells, spell_probabilities=demon_brute_spell_probabilities, initial_stats=demon_brute_initial_stats)

magma_brute_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 22,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Fire"
}
magma_brute_gear = ["Molten Maul", "Obsidian Plate"]
magma_brute_loot_table = ["Gold", "Magma Shard", "Obsidian Fragment"]
magma_brute_description = "The Magma Brute is a massive creature forged in the fiery depths of the earth. Its body is encased in molten rock and magma, making it nearly impervious to physical harm. It wields a mighty molten maul, capable of crushing anything in its path."
magma_brute_floor_range = (7, 9)
magma_brute_spells = []
magma_brute_spell_probabilities = {}
magma_brute_initial_stats = magma_brute_stats.copy()
magma_brute = Monster("Magma Brute", magma_brute_stats, magma_brute_gear, magma_brute_loot_table, difficulty=120, description=magma_brute_description, floor_range=magma_brute_floor_range, spells=magma_brute_spells, spell_probabilities=magma_brute_spell_probabilities, initial_stats=magma_brute_initial_stats)

soul_reaper_stats = {
    "HP": 800,
    "Damage": 120,
    "Defense": 80,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Dark"
}
soul_reaper_gear = ["Reaper's Scythe", "Soul Shroud"]
soul_reaper_loot_table = ["Gold", "Soul Reaper's Sickle", "Darkened Soulstone"]
soul_reaper_description = "Soul Reapers are merciless harvesters of souls, wielding scythes imbued with the power to sever the ties between life and death. They roam the depths of Hell, reaping the souls of the damned and adding them to their spectral army."
soul_reaper_floor_range = (8, 10)
soul_reaper_spells = []
soul_reaper_spell_probabilities = {}
soul_reaper_initial_stats = soul_reaper_stats.copy()
soul_reaper = Monster("Soul Reaper", soul_reaper_stats, soul_reaper_gear, soul_reaper_loot_table, difficulty=300, description=soul_reaper_description, floor_range=soul_reaper_floor_range, spells=soul_reaper_spells, spell_probabilities=soul_reaper_spell_probabilities, initial_stats=soul_reaper_initial_stats)

hellhound_alpha_stats = {
    "HP": 1000,
    "Damage": 150,
    "Defense": 100,
    "Magic Defense": 80,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
hellhound_alpha_gear = ["Infernal Fangs", "Alpha's Fury"]
hellhound_alpha_loot_table = ["Gold", "Hellhound's Essence", "Alpha's Dominance"]
hellhound_alpha_description = "Hellhound Alphas are the leaders of pack of infernal beasts, commanding them with unmatched ferocity and strength. They are fearsome predators, hunting down intruders in the fiery depths of Hell with relentless determination."
hellhound_alpha_floor_range = (8, 10)
hellhound_alpha_spells = []
hellhound_alpha_spell_probabilities = {}
hellhound_alpha_initial_stats = hellhound_alpha_stats.copy()
hellhound_alpha = Monster("Hellhound Alpha", hellhound_alpha_stats, hellhound_alpha_gear, hellhound_alpha_loot_table, difficulty=400, description=hellhound_alpha_description, floor_range=hellhound_alpha_floor_range, spells=hellhound_alpha_spells, spell_probabilities=hellhound_alpha_spell_probabilities, initial_stats=hellhound_alpha_initial_stats)

flesh_golem_stats = {
    "HP": 300,  # Define HP attribute for Flesh Golem
    "Damage": 80,  # Define damage attribute for Flesh Golem
    "Defense": 50,  # Define Defense stat vs attack stat
    "Magic Defense": 50,  # Define magic defense vs spells
    "Strength": 28,
    "Dexterity": 14,
    "Constitution": 28,
    "Intelligence": 6,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"  # Define elemental attribute of the Flesh Golem's attack
}
flesh_golem_gear = ["Massive Fists", "Toughened Flesh"]
flesh_golem_loot_table = ["Gold", "Flesh Golem Core", "Tattered Flesh"]
flesh_golem_description = "Flesh Golems are hulking constructs stitched together from the remains of multiple corpses. Animated through dark necromantic magic, they obey the commands of their masters with unwavering loyalty. With their immense strength and resilience, they are formidable guardians and relentless foes."
flesh_golem_floor_range = (8, 10)
flesh_golem_spells = []
flesh_golem_spell_probabilities = {}
flesh_golem_initial_stats = flesh_golem_stats.copy() # Make a copy of the initial stats
flesh_golem = Monster("Flesh Golem", flesh_golem_stats, flesh_golem_gear, flesh_golem_loot_table, difficulty=50, description=flesh_golem_description, floor_range=flesh_golem_floor_range, spells=flesh_golem_spells, spell_probabilities=flesh_golem_spell_probabilities, initial_stats=flesh_golem_initial_stats)

doomfiend_stats = {
    "HP": 200,
    "Damage": 70,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 18,
    "Charisma": 15,
    "Element": "Fire"
}

doomfiend_gear = ["Infernal Crown", "Cursed Gauntlets"]
doomfiend_loot_table = ["Eternal Ember", "Soulfire Shard", "Doomed Scroll"]
doomfiend_description = "The Doomfiend, an ancient creature born of the deepest pits of Hell, exudes an aura of pure malevolence. Its very presence warps the fabric of reality, leaving only destruction and despair in its wake."
doomfiend_floor_range = (8, 10)
doomfiend_spells = ["Hellfire Nova", "Abyssal Rift"]
doomfiend_spell_probabilities = {"Hellfire Nova": 0.6, "Abyssal Rift": 0.4}
doomfiend_initial_stats = doomfiend_stats.copy()
doomfiend = Monster("Doomfiend", doomfiend_stats, doomfiend_gear, doomfiend_loot_table, difficulty=9, description=doomfiend_description, floor_range=doomfiend_floor_range, spells=doomfiend_spells, spell_probabilities=doomfiend_spell_probabilities, initial_stats=doomfiend_initial_stats)

magma_elemental_stats = {
    "HP": 160,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 18,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Fire"
}

magma_elemental_gear = ["Volcanic Rock Armor", "Lava Core"]
magma_elemental_loot_table = ["Molten Shard", "Inferno Essence", "Obsidian Fragment"]
magma_elemental_description = "The Magma Elemental, a creature born from the molten depths of the earth, roams the hellish landscape, leaving trails of lava in its wake. Its fiery presence is enough to melt even the sturdiest of armor."
magma_elemental_floor_range = (9, 11)
magma_elemental_spells = ["Lava Burst", "Magma Wave"]
magma_elemental_spell_probabilities = {"Lava Burst": 0.7, "Magma Wave": 0.3}
magma_elemental_initial_stats = magma_elemental_stats.copy()
magma_elemental = Monster("Magma Elemental", magma_elemental_stats, magma_elemental_gear, magma_elemental_loot_table, difficulty=7, description=magma_elemental_description, floor_range=magma_elemental_floor_range, spells=magma_elemental_spells, spell_probabilities=magma_elemental_spell_probabilities, initial_stats=magma_elemental_initial_stats)

hellspawned_juggernaut_stats = {
    "HP": 220,
    "Damage": 75,
    "Defense": 60,
    "Magic Defense": 30,
    "Strength": 35,
    "Dexterity": 30,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 18,
    "Charisma": 15,
    "Element": "Fire"
}

hellspawned_juggernaut_gear = ["Infernal Armor", "Hellforge Hammer"]
hellspawned_juggernaut_loot_table = ["Brimstone Shard", "Hellfire Gem", "Infernal Plate"]
hellspawned_juggernaut_description = "The Hellspawned Juggernaut, a towering behemoth of flame and fury, smashes through anything in its path with unstoppable force. Its relentless assault leaves nothing but scorched earth behind."
hellspawned_juggernaut_floor_range = (9, 11)
hellspawned_juggernaut_spells = ["Meteor Strike", "Infernal Smash"]
hellspawned_juggernaut_spell_probabilities = {"Meteor Strike": 0.6, "Infernal Smash": 0.4}
hellspawned_juggernaut_initial_stats = hellspawned_juggernaut_stats.copy()
hellspawned_juggernaut = Monster("Hellspawned Juggernaut", hellspawned_juggernaut_stats, hellspawned_juggernaut_gear, hellspawned_juggernaut_loot_table, difficulty=10, description=hellspawned_juggernaut_description, floor_range=hellspawned_juggernaut_floor_range, spells=hellspawned_juggernaut_spells, spell_probabilities=hellspawned_juggernaut_spell_probabilities, initial_stats=hellspawned_juggernaut_initial_stats)

hellspawned_warlock_stats = {
    "HP": 180,
    "Damage": 65,
    "Defense": 45,
    "Magic Defense": 50,
    "Strength": 20,
    "Dexterity": 25,
    "Constitution": 30,
    "Intelligence": 30,
    "Wisdom": 28,
    "Charisma": 25,
    "Element": "Fire"
}

hellspawned_warlock_gear = ["Infernal Robes", "Staff of Flames"]
hellspawned_warlock_loot_table = ["Darkfire Essence", "Hellbound Tome", "Soulstone"]
hellspawned_warlock_description = "The Hellspawned Warlock, a master of infernal magic, conjures dark flames from the depths of Hell itself. Its sinister incantations sow chaos and despair, turning the battlefield into a nightmarish hellscape."
hellspawned_warlock_floor_range = (9, 11)
hellspawned_warlock_spells = ["Hellfire Blast", "Soul Drain"]
hellspawned_warlock_spell_probabilities = {"Hellfire Blast": 0.7, "Soul Drain": 0.3}
hellspawned_warlock_initial_stats = hellspawned_warlock_stats.copy()
hellspawned_warlock = Monster("Hellspawned Warlock", hellspawned_warlock_stats, hellspawned_warlock_gear, hellspawned_warlock_loot_table, difficulty=8, description=hellspawned_warlock_description, floor_range=hellspawned_warlock_floor_range, spells=hellspawned_warlock_spells, spell_probabilities=hellspawned_warlock_spell_probabilities, initial_stats=hellspawned_warlock_initial_stats)

tormentor_stats = {
    "HP": 180,
    "Damage": 65,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 15,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Dark"
}

tormentor_gear = ["Soul Chains", "Shadow Cloak"]
tormentor_loot_table = ["Cursed Essence", "Tortured Soul Fragment", "Shadow Shroud"]
tormentor_description = "The Tormentor is a specter of anguish, bound by dark energy to inflict suffering upon any who cross its path. It feeds on despair, manifesting its malevolent powers to ensnare and torment the living."
tormentor_floor_range = (10, 12)
tormentor_spells = ["Dark Vortex", "Soul Drain"]
tormentor_spell_probabilities = {"Dark Vortex": 0.7, "Soul Drain": 0.3}
tormentor_initial_stats = tormentor_stats.copy()
tormentor = Monster("Tormentor", tormentor_stats, tormentor_gear, tormentor_loot_table, difficulty=8, description=tormentor_description, floor_range=tormentor_floor_range, spells=tormentor_spells, spell_probabilities=tormentor_spell_probabilities, initial_stats=tormentor_initial_stats)

emberfiend_stats = {
    "HP": 160,
    "Damage": 60,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 22,
    "Dexterity": 22,
    "Constitution": 24,
    "Intelligence": 18,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "Fire"
}

emberfiend_gear = ["Burning Embers", "Flame Cloak"]
emberfiend_loot_table = ["Charred Scale", "Blazing Heart", "Inferno Essence"]
emberfiend_description = "The Emberfiend is a creature of pure flame, its wrath fueled by the inferno that courses through its veins. It leaves behind scorched earth and smoldering remains, a testament to its fiery rage."
emberfiend_floor_range = (10, 12)
emberfiend_spells = ["Fireball", "Flame Burst"]
emberfiend_spell_probabilities = {"Fireball": 0.6, "Flame Burst": 0.4}
emberfiend_initial_stats = emberfiend_stats.copy()
emberfiend = Monster("Emberfiend", emberfiend_stats, emberfiend_gear, emberfiend_loot_table, difficulty=7, description=emberfiend_description, floor_range=emberfiend_floor_range, spells=emberfiend_spells, spell_probabilities=emberfiend_spell_probabilities, initial_stats=emberfiend_initial_stats)


hellfire_wraith_stats = {
    "HP": 150,
    "Damage": 55,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 20,
    "Dexterity": 25,
    "Constitution": 20,
    "Intelligence": 20,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Dark"
}

hellfire_wraith_gear = ["Cursed Shackles", "Shadow Veil"]
hellfire_wraith_loot_table = ["Shadow Essence", "Tormented Spirit", "Darkened Soul Gem"]
hellfire_wraith_description = "The Hellfire Wraith is a phantasmal entity cloaked in shadow and flame. It brings forth the fires of damnation to consume its enemies, leaving behind only smoky remnants of their existence."
hellfire_wraith_floor_range = (10, 12)
hellfire_wraith_spells = ["Shadowflame", "Soul Burn"]
hellfire_wraith_spell_probabilities = {"Shadowflame": 0.6, "Soul Burn": 0.4}
hellfire_wraith_initial_stats = hellfire_wraith_stats.copy()
hellfire_wraith = Monster("Hellfire Wraith", hellfire_wraith_stats, hellfire_wraith_gear, hellfire_wraith_loot_table, difficulty=7, description=hellfire_wraith_description, floor_range=hellfire_wraith_floor_range, spells=hellfire_wraith_spells, spell_probabilities=hellfire_wraith_spell_probabilities, initial_stats=hellfire_wraith_initial_stats)


abyssal_fiend_stats = {
    "HP": 200,
    "Damage": 70,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Dark"
}

abyssal_fiend_gear = ["Void Blade", "Abyssal Cloak"]
abyssal_fiend_loot_table = ["Dark Essence", "Shadowsteel Shard", "Eldritch Rune"]
abyssal_fiend_description = "The Abyssal Fiend is a creature born from the depths of the underworld, its form twisted and corrupted by the powers of darkness. It seeks to drag its victims into the abyss, where they will be consumed by eternal darkness."
abyssal_fiend_floor_range = (11, 13)
abyssal_fiend_spells = ["Dark Pulse", "Shadow Wave"]
abyssal_fiend_spell_probabilities = {"Dark Pulse": 0.6, "Shadow Wave": 0.4}
abyssal_fiend_initial_stats = abyssal_fiend_stats.copy()
abyssal_fiend = Monster("Abyssal Fiend", abyssal_fiend_stats, abyssal_fiend_gear, abyssal_fiend_loot_table, difficulty=8, description=abyssal_fiend_description, floor_range=abyssal_fiend_floor_range, spells=abyssal_fiend_spells, spell_probabilities=abyssal_fiend_spell_probabilities, initial_stats=abyssal_fiend_initial_stats)

cursed_emberbeast_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 15,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Fire"
}

cursed_emberbeast_gear = ["Smoldering Pelt", "Blazing Fang"]
cursed_emberbeast_loot_table = ["Cursed Ember", "Infernal Ash", "Brimstone Heart"]
cursed_emberbeast_description = "The Cursed Emberbeast is a fearsome creature, its body engulfed in flames that never die. Born from the darkest pits of the inferno, it leaves behind a trail of destruction and ash wherever it roams."
cursed_emberbeast_floor_range = (11, 13)
cursed_emberbeast_spells = ["Scorch", "Conflagration"]
cursed_emberbeast_spell_probabilities = {"Scorch": 0.7, "Conflagration": 0.3}
cursed_emberbeast_initial_stats = cursed_emberbeast_stats.copy()
cursed_emberbeast = Monster("Cursed Emberbeast", cursed_emberbeast_stats, cursed_emberbeast_gear, cursed_emberbeast_loot_table, difficulty=8, description=cursed_emberbeast_description, floor_range=cursed_emberbeast_floor_range, spells=cursed_emberbeast_spells, spell_probabilities=cursed_emberbeast_spell_probabilities, initial_stats=cursed_emberbeast_initial_stats)

infernal_leviathan_stats = {
    "HP": 250,
    "Damage": 80,
    "Defense": 50,
    "Magic Defense": 60,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Fire"
}

infernal_leviathan_gear = ["Molten Scales", "Scorching Talon"]
infernal_leviathan_loot_table = ["Infernal Scale", "Lava Core", "Volcanic Essence"]
infernal_leviathan_description = "The Infernal Leviathan is a colossal serpent of flame, its body wreathed in molten lava that burns everything it touches. Awoken from its slumber in the depths of the underworld, it rises to wreak havoc upon the world above."
infernal_leviathan_floor_range = (11, 13)
infernal_leviathan_spells = ["Magma Blast", "Firestorm"]
infernal_leviathan_spell_probabilities = {"Magma Blast": 0.6, "Firestorm": 0.4}
infernal_leviathan_initial_stats = infernal_leviathan_stats.copy()
infernal_leviathan = Monster("Infernal Leviathan", infernal_leviathan_stats, infernal_leviathan_gear, infernal_leviathan_loot_table, difficulty=9, description=infernal_leviathan_description, floor_range=infernal_leviathan_floor_range, spells=infernal_leviathan_spells, spell_probabilities=infernal_leviathan_spell_probabilities, initial_stats=infernal_leviathan_initial_stats)

doomfire_drake_stats = {
    "HP": 200,
    "Damage": 70,
    "Defense": 45,
    "Magic Defense": 50,
    "Strength": 28,
    "Dexterity": 23,
    "Constitution": 35,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Fire"
}

doomfire_drake_gear = ["Searing Scales", "Inferno Fang"]
doomfire_drake_loot_table = ["Doomfire Scale", "Cinder Core", "Hellfire Essence"]
doomfire_drake_description = "The Doomfire Drake is a ferocious beast, its body covered in scales that radiate intense heat. Born from the heart of a volcano, it takes to the skies with wings of fire, leaving destruction in its wake."
doomfire_drake_floor_range = (12, 15)
doomfire_drake_spells = ["Fire Breath", "Infernal Roar"]
doomfire_drake_spell_probabilities = {"Fire Breath": 0.6, "Infernal Roar": 0.4}
doomfire_drake_initial_stats = doomfire_drake_stats.copy()
doomfire_drake = Monster("Doomfire Drake", doomfire_drake_stats, doomfire_drake_gear, doomfire_drake_loot_table, difficulty=9, description=doomfire_drake_description, floor_range=doomfire_drake_floor_range, spells=doomfire_drake_spells, spell_probabilities=doomfire_drake_spell_probabilities, initial_stats=doomfire_drake_initial_stats)

demonic_incinerator_stats = {
    "HP": 180,
    "Damage": 65,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 15,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Fire"
}

demonic_incinerator_gear = ["Soulflame Cloak", "Infernal Gauntlets"]
demonic_incinerator_loot_table = ["Hellfire Shard", "Charred Heart", "Demon's Ember"]
demonic_incinerator_description = "The Demonic Incinerator is a towering inferno of malice and destruction, its very presence engulfing everything in flames. With eyes burning with the fires of the abyss, it leaves behind only scorched earth and ashes in its wake."
demonic_incinerator_floor_range = (12, 15)
demonic_incinerator_spells = ["Hellfire Nova", "Soulflame Burst"]
demonic_incinerator_spell_probabilities = {"Hellfire Nova": 0.7, "Soulflame Burst": 0.3}
demonic_incinerator_initial_stats = demonic_incinerator_stats.copy()
demonic_incinerator = Monster("Demonic Incinerator", demonic_incinerator_stats, demonic_incinerator_gear, demonic_incinerator_loot_table, difficulty=8, description=demonic_incinerator_description, floor_range=demonic_incinerator_floor_range, spells=demonic_incinerator_spells, spell_probabilities=demonic_incinerator_spell_probabilities, initial_stats=demonic_incinerator_initial_stats)

demonic_brimstonecaller_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 24,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 14,
    "Element": "Fire"
}

demonic_brimstonecaller_gear = ["Infernal Staff", "Brimstone Robes"]
demonic_brimstonecaller_loot_table = ["Demonic Essence", "Searing Ash", "Brimstone Shard"]
demonic_brimstonecaller_description = "The Demonic Brimstonecaller is a master of infernal magic, summoning flames from the depths of the abyss to engulf its foes. Clad in robes of brimstone, it leaves behind a trail of destruction wherever it treads."
demonic_brimstonecaller_floor_range = (12, 15)
demonic_brimstonecaller_spells = ["Infernal Blast", "Hellfire Rain"]
demonic_brimstonecaller_spell_probabilities = {"Infernal Blast": 0.7, "Hellfire Rain": 0.3}
demonic_brimstonecaller_initial_stats = demonic_brimstonecaller_stats.copy()
demonic_brimstonecaller = Monster("Demonic Brimstonecaller", demonic_brimstonecaller_stats, demonic_brimstonecaller_gear, demonic_brimstonecaller_loot_table, difficulty=9, description=demonic_brimstonecaller_description, floor_range=demonic_brimstonecaller_floor_range, spells=demonic_brimstonecaller_spells, spell_probabilities=demonic_brimstonecaller_spell_probabilities, initial_stats=demonic_brimstonecaller_initial_stats)

demonic_ashbringer_stats = {
    "HP": 160,
    "Damage": 55,
    "Defense": 28,
    "Magic Defense": 32,
    "Strength": 22,
    "Dexterity": 18,
    "Constitution": 26,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "Fire"
}

demonic_ashbringer_gear = ["Infernal Blade", "Ashen Armor"]
demonic_ashbringer_loot_table = ["Demonic Dust", "Smoldering Embers", "Ashen Fragment"]
demonic_ashbringer_description = "The Demonic Ashbringer is a relentless hunter, its fiery blade leaving behind only ashes in its wake. Clad in armor forged from the remnants of infernal flames, it seeks out souls to consume and torment."
demonic_ashbringer_floor_range = (13, 16)
demonic_ashbringer_spells = ["Ashen Strike", "Flame Nova"]
demonic_ashbringer_spell_probabilities = {"Ashen Strike": 0.6, "Flame Nova": 0.4}
demonic_ashbringer_initial_stats = demonic_ashbringer_stats.copy()
demonic_ashbringer = Monster("Demonic Ashbringer", demonic_ashbringer_stats, demonic_ashbringer_gear, demonic_ashbringer_loot_table, difficulty=8, description=demonic_ashbringer_description, floor_range=demonic_ashbringer_floor_range, spells=demonic_ashbringer_spells, spell_probabilities=demonic_ashbringer_spell_probabilities, initial_stats=demonic_ashbringer_initial_stats)

demonic_scorchbeast_stats = {
    "HP": 190,
    "Damage": 65,
    "Defense": 32,
    "Magic Defense": 38,
    "Strength": 28,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Fire"
}

demonic_scorchbeast_gear = ["Infernal Claws", "Scorching Hide"]
demonic_scorchbeast_loot_table = ["Demonic Scale", "Smoldering Fang", "Inferno Heart"]
demonic_scorchbeast_description = "The Demonic Scorchbeast is a winged terror, soaring through the infernal skies with a roar that echoes through the depths of hell. With claws that drip with molten fire, it leaves a trail of devastation in its wake."
demonic_scorchbeast_floor_range = (13, 16)
demonic_scorchbeast_spells = ["Scorching Gale", "Infernal Roar"]
demonic_scorchbeast_spell_probabilities = {"Scorching Gale": 0.7, "Infernal Roar": 0.3}
demonic_scorchbeast_initial_stats = demonic_scorchbeast_stats.copy()
demonic_scorchbeast = Monster("Demonic Scorchbeast", demonic_scorchbeast_stats, demonic_scorchbeast_gear, demonic_scorchbeast_loot_table, difficulty=9, description=demonic_scorchbeast_description, floor_range=demonic_scorchbeast_floor_range, spells=demonic_scorchbeast_spells, spell_probabilities=demonic_scorchbeast_spell_probabilities, initial_stats=demonic_scorchbeast_initial_stats)

demonic_soulreaper_stats = {
    "HP": 170,
    "Damage": 58,
    "Defense": 29,
    "Magic Defense": 34,
    "Strength": 24,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 15,
    "Wisdom": 17,
    "Charisma": 13,
    "Element": "Fire"
}

demonic_soulreaper_gear = ["Infernal Scythe", "Soulbound Shackles"]
demonic_soulreaper_loot_table = ["Demonic Essence", "Cursed Soul", "Infernal Chain"]
demonic_soulreaper_description = "The Demonic Soulreaper is a harbinger of doom, its scythe reaping souls with merciless efficiency. Bound by chains forged from infernal flames, it serves as a grim reminder of the fate that awaits all who oppose the forces of hell."
demonic_soulreaper_floor_range = (14, 17)
demonic_soulreaper_spells = ["Soul Siphon", "Infernal Gaze"]
demonic_soulreaper_spell_probabilities = {"Soul Siphon": 0.6, "Infernal Gaze": 0.4}
demonic_soulreaper_initial_stats = demonic_soulreaper_stats.copy()
demonic_soulreaper = Monster("Demonic Soulreaper", demonic_soulreaper_stats, demonic_soulreaper_gear, demonic_soulreaper_loot_table, difficulty=8, description=demonic_soulreaper_description, floor_range=demonic_soulreaper_floor_range, spells=demonic_soulreaper_spells, spell_probabilities=demonic_soulreaper_spell_probabilities, initial_stats=demonic_soulreaper_initial_stats)


### ADD MORE MOBS HERE ###


pyroclasmic_titan_stats = {
    "HP": 1200,
    "Damage": 180,
    "Defense": 120,
    "Magic Defense": 100,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
pyroclasmic_titan_gear = ["Inferno Maul", "Titanic Inferno Armor"]
pyroclasmic_titan_loot_table = ["Gold", "Titan's Ember", "Pyroclasmic Core"]
pyroclasmic_titan_description = "Pyroclasmic Titans are towering colossi of flame and fury, wreaking havoc upon the land with every step. Their mighty fists crush mountains and their fiery breath scorches the earth, leaving behind only smoldering ruins in their wake."
pyroclasmic_titan_floor_range = (17, 19)
pyroclasmic_titan_spells = []
pyroclasmic_titan_spell_probabilities = {}
pyroclasmic_titan_initial_stats = pyroclasmic_titan_stats.copy()
pyroclasmic_titan = Monster("Pyroclasmic Titan", pyroclasmic_titan_stats, pyroclasmic_titan_gear, pyroclasmic_titan_loot_table, difficulty=500, description=pyroclasmic_titan_description, floor_range=pyroclasmic_titan_floor_range, spells=pyroclasmic_titan_spells, spell_probabilities=pyroclasmic_titan_spell_probabilities, initial_stats=pyroclasmic_titan_initial_stats)

### ADD MORE MOBS HERE ###