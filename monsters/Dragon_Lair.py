from monsters.bestiary import Monster

dragon_hatchling_stats = {
    "HP": 80,
    "Damage": 20,
    "Defense": 15,
    "Magic Defense": 15,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 12,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 8,
    "Element": "Fire"
}
dragon_hatchling_gear = ["Sharp Claws", "Scaly Hide"]
dragon_hatchling_loot_table = ["Gold", "Dragon Scale", "Dragon Fang"]
dragon_hatchling_description = "Dragon Hatchlings are young dragons just beginning to develop their fiery breath and sharp claws. While smaller and less powerful than their adult counterparts, they are still dangerous adversaries capable of inflicting serious harm."
dragon_hatchling_floor_range = (1, 2)
dragon_hatchling_spells = []
dragon_hatchling_spell_probabilities = {}
dragon_hatchling_initial_stats = dragon_hatchling_stats.copy()
dragon_hatchling = Monster("Dragon Hatchling", dragon_hatchling_stats, dragon_hatchling_gear, dragon_hatchling_loot_table, difficulty=40, description=dragon_hatchling_description, floor_range=dragon_hatchling_floor_range, spells=dragon_hatchling_spells, spell_probabilities=dragon_hatchling_spell_probabilities, initial_stats=dragon_hatchling_initial_stats)

scalesnake_stats = {
    "HP": 120,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "Earth"
}

scalesnake_gear = ["Serpent Fangs"]
scalesnake_loot_table = ["Scalesnake Skin", "Gold Coin", "Jade Eye"]
scalesnake_description = "Scalesnakes are serpentine creatures that slither through the dragon's lair, their scales reflecting the gleam of gold."
scalesnake_floor_range = (1, 2)
scalesnake_spells = []
scalesnake_spell_probabilities = {}
scalesnake_initial_stats = scalesnake_stats.copy()
scalesnake = Monster("Scalesnake", scalesnake_stats, scalesnake_gear, scalesnake_loot_table, difficulty=6, description=scalesnake_description, floor_range=scalesnake_floor_range, spells=scalesnake_spells, spell_probabilities=scalesnake_spell_probabilities, initial_stats=scalesnake_initial_stats)

wyrmling_skirmisher_stats = {
    "HP": 100,
    "Damage": 35,
    "Defense": 15,
    "Magic Defense": 10,
    "Strength": 16,
    "Dexterity": 20,
    "Constitution": 12,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Acid"
}
wyrmling_skirmisher_gear = ["Acidic Fangs", "Wyrm Scale Armor"]
wyrmling_skirmisher_loot_table = ["Wyrm Scale", "Acid Vial", "Gold"]
wyrmling_skirmisher_description = "Wyrmling Skirmishers are agile and cunning, adept at ambushing intruders in the winding tunnels of the Dragon Lair. They strike swiftly with their venomous bites and retreat into the shadows, waiting for the next opportunity to attack."
wyrmling_skirmisher_floor_range = (1, 3)
wyrmling_skirmisher_spells = []
wyrmling_skirmisher_spell_probabilities = {}
wyrmling_skirmisher_initial_stats = wyrmling_skirmisher_stats.copy()
wyrmling_skirmisher = Monster("Wyrmling Skirmisher", wyrmling_skirmisher_stats, wyrmling_skirmisher_gear, wyrmling_skirmisher_loot_table, difficulty=30, description=wyrmling_skirmisher_description, floor_range=wyrmling_skirmisher_floor_range, spells=wyrmling_skirmisher_spells, spell_probabilities=wyrmling_skirmisher_spell_probabilities, initial_stats=wyrmling_skirmisher_initial_stats)

wyvern_scout_stats = {
    "HP": 130,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Poison"
}
wyvern_scout_gear = ["Venomous Stinger", "Leather Cloak"]
wyvern_scout_loot_table = ["Wyvern Scale", "Toxic Fang", "Gold"]
wyvern_scout_description = "Wyvern Scouts are agile and stealthy hunters, patrolling the skies above the Dragon Lair in search of prey. They dive down from above, striking with their venomous stingers before retreating to the safety of the clouds."
wyvern_scout_floor_range = (2, 3)
wyvern_scout_spells = []
wyvern_scout_spell_probabilities = {}
wyvern_scout_initial_stats = wyvern_scout_stats.copy()
wyvern_scout = Monster("Wyvern Scout", wyvern_scout_stats, wyvern_scout_gear, wyvern_scout_loot_table, difficulty=30, description=wyvern_scout_description, floor_range=wyvern_scout_floor_range, spells=wyvern_scout_spells, spell_probabilities=wyvern_scout_spell_probabilities, initial_stats=wyvern_scout_initial_stats)

kobold_warrior_stats = {
    "HP": 150,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
kobold_warrior_gear = ["Rusty Sword", "Leather Armor"]
kobold_warrior_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
kobold_warrior_description = "Kobold Warriors are fierce and agile fighters, wielding rusty swords and wearing patchy leather armor. They fiercely defend their lairs with cunning tactics and ferocious determination."
kobold_warrior_floor_range = (2, 4)
kobold_warrior_spells = []
kobold_warrior_spell_probabilities = {}
kobold_warrior_initial_stats = kobold_warrior_stats.copy()
kobold_warrior = Monster("Kobold Warrior", kobold_warrior_stats, kobold_warrior_gear, kobold_warrior_loot_table, difficulty=50, description=kobold_warrior_description, floor_range=kobold_warrior_floor_range, spells=kobold_warrior_spells, spell_probabilities=kobold_warrior_spell_probabilities, initial_stats=kobold_warrior_initial_stats)

kobold_archer_stats = {
    "HP": 120,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "None"
}
kobold_archer_gear = ["Shortbow", "Leather Jerkin"]
kobold_archer_loot_table = ["Gold", "Arrow", "Tattered Quiver"]
kobold_archer_description = "Kobold Archers are skilled marksmen, using shortbows to rain down arrows on their enemies from a distance. They prefer to keep their foes at bay, relying on speed and precision rather than brute force."
kobold_archer_floor_range = (2, 4)
kobold_archer_spells = []
kobold_archer_spell_probabilities = {}
kobold_archer_initial_stats = kobold_archer_stats.copy()
kobold_archer = Monster("Kobold Archer", kobold_archer_stats, kobold_archer_gear, kobold_archer_loot_table, difficulty=30, description=kobold_archer_description, floor_range=kobold_archer_floor_range, spells=kobold_archer_spells, spell_probabilities=kobold_archer_spell_probabilities, initial_stats=kobold_archer_initial_stats)

kobold_thief_stats = {
    "HP": 140,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 16,
    "Element": "None"
}
kobold_thief_gear = ["Dagger of the Shadows", "Cloak of Invisibility"]
kobold_thief_loot_table = ["Gold", "Stolen Gem", "Lockpicks"]
kobold_thief_description = "Kobold Thieves are nimble and stealthy, specializing in sneaking and pilfering. They use daggers of the shadows and cloaks of invisibility to slip past their enemies unnoticed."
kobold_thief_floor_range = (2, 4)
kobold_thief_spells = []
kobold_thief_spell_probabilities = {}
kobold_thief_initial_stats = kobold_thief_stats.copy()
kobold_thief = Monster("Kobold Thief", kobold_thief_stats, kobold_thief_gear, kobold_thief_loot_table, difficulty=40, description=kobold_thief_description, floor_range=kobold_thief_floor_range, spells=kobold_thief_spells, spell_probabilities=kobold_thief_spell_probabilities, initial_stats=kobold_thief_initial_stats)

salamander_sentinel_stats = {
    "HP": 150,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 18,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Fire"
}
salamander_sentinel_gear = ["Flame Whip", "Obsidian Plate Armor"]
salamander_sentinel_loot_table = ["Obsidian Shard", "Fire Gem", "Gold"]
salamander_sentinel_description = "Salamander Sentinels are stalwart guardians of the Dragon Lair, wielding fiery weapons and wearing armor forged from obsidian. They stand watch over the lair's entrances and chambers, ready to repel any intruders with their formidable strength and combat prowess."
salamander_sentinel_floor_range = (2, 4)
salamander_sentinel_spells = []
salamander_sentinel_spell_probabilities = {}
salamander_sentinel_initial_stats = salamander_sentinel_stats.copy()
salamander_sentinel = Monster("Salamander Sentinel", salamander_sentinel_stats, salamander_sentinel_gear, salamander_sentinel_loot_table, difficulty=30, description=salamander_sentinel_description, floor_range=salamander_sentinel_floor_range, spells=salamander_sentinel_spells, spell_probabilities=salamander_sentinel_spell_probabilities, initial_stats=salamander_sentinel_initial_stats)

kobold_artificer_stats = {
    "HP": 130,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 10,
    "Dexterity": 14,
    "Constitution": 14,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "None"
}
kobold_artificer_gear = ["Wand of Arcane Fire", "Robes of the Inventor"]
kobold_artificer_loot_table = ["Gold", "Arcane Component", "Inscribed Scroll"]
kobold_artificer_description = "Kobold Artificers are ingenious inventors, wielding wands of arcane fire and wearing robes adorned with gadgets and gizmos. They excel at crafting traps and gadgets to outsmart their foes."
kobold_artificer_floor_range = (4, 6)
kobold_artificer_spells = []
kobold_artificer_spell_probabilities = {}
kobold_artificer_initial_stats = kobold_artificer_stats.copy()
kobold_artificer = Monster("Kobold Artificer", kobold_artificer_stats, kobold_artificer_gear, kobold_artificer_loot_table, difficulty=40, description=kobold_artificer_description, floor_range=kobold_artificer_floor_range, spells=kobold_artificer_spells, spell_probabilities=kobold_artificer_spell_probabilities, initial_stats=kobold_artificer_initial_stats)

kobold_dragonsoul_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 20,
    "Wisdom": 18,
    "Charisma": 22,
    "Element": "Fire"
}
kobold_dragonsoul_gear = ["Dragon Fang Dagger", "Scaled Robes"]
kobold_dragonsoul_loot_table = ["Gold", "Dragon Scale", "Infernal Gem"]
kobold_dragonsoul_description = "Kobold Dragon-Souls are believed to carry the essence of dragons within them, granting them fiery powers and draconic abilities. They wield dragon fang daggers and wear scaled robes as symbols of their connection to the ancient beasts."
kobold_dragonsoul_floor_range = (4, 6)
kobold_dragonsoul_spells = []
kobold_dragonsoul_spell_probabilities = {}
kobold_dragonsoul_initial_stats = kobold_dragonsoul_stats.copy()
kobold_dragonsoul = Monster("Kobold Dragon-Soul", kobold_dragonsoul_stats, kobold_dragonsoul_gear, kobold_dragonsoul_loot_table, difficulty=60, description=kobold_dragonsoul_description, floor_range=kobold_dragonsoul_floor_range, spells=kobold_dragonsoul_spells, spell_probabilities=kobold_dragonsoul_spell_probabilities, initial_stats=kobold_dragonsoul_initial_stats)

kobold_shaman_stats = {
    "HP": 160,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 35,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 22,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Earth"
}
kobold_shaman_gear = ["Staff of the Elements", "Shamanic Garb"]
kobold_shaman_loot_table = ["Gold", "Elemental Essence", "Shamanic Totem"]
kobold_shaman_description = "Kobold Shamans are spiritual leaders of their tribes, wielding staves of the elements and wearing shamanic garb adorned with tribal symbols. They commune with the earth and spirits to harness the power of nature."
kobold_shaman_floor_range = (4, 6)
kobold_shaman_spells = ["Earthquake", "Blessing of the Spirits", "Elemental Burst"]
kobold_shaman_spell_probabilities = {"Earthquake": 0.4, "Blessing of the Spirits": 0.3, "Elemental Burst": 0.3}
kobold_shaman_initial_stats = kobold_shaman_stats.copy()
kobold_shaman = Monster("Kobold Shaman", kobold_shaman_stats, kobold_shaman_gear, kobold_shaman_loot_table, difficulty=50, description=kobold_shaman_description, floor_range=kobold_shaman_floor_range, spells=kobold_shaman_spells, spell_probabilities=kobold_shaman_spell_probabilities, initial_stats=kobold_shaman_initial_stats)

dragonspawn_stats = {
    "HP": 220,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 45,
    "Dexterity": 30,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"
}

dragonspawn_gear = ["Dragonborn Plate", "Dragonfang Axe"]
dragonspawn_loot_table = ["Dragonspawn Horn", "Dragon Essence", "Ancient Relic"]
dragonspawn_description = "Dragonspawn are half-dragon hybrids created by the dragon to serve as its minions."
dragonspawn_floor_range = (5, 7)
dragonspawn_spells = []
dragonspawn_spell_probabilities = {}
dragonspawn_initial_stats = dragonspawn_stats.copy()
dragonspawn = Monster("Dragonspawn", dragonspawn_stats, dragonspawn_gear, dragonspawn_loot_table, difficulty=8, description=dragonspawn_description, floor_range=dragonspawn_floor_range, spells=dragonspawn_spells, spell_probabilities=dragonspawn_spell_probabilities, initial_stats=dragonspawn_initial_stats)

kobold_sorcerer_stats = {
    "HP": 160,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 12,
    "Dexterity": 14,
    "Constitution": 16,
    "Intelligence": 22,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "None"
}
kobold_sorcerer_gear = ["Sorcerer's Staff", "Arcane Robes"]
kobold_sorcerer_loot_table = ["Gold", "Arcane Essence", "Sorcerer's Tome"]
kobold_sorcerer_description = "Kobold Sorcerers are masters of arcane magic, wielding powerful staves and wearing robes imbued with magical energy. They harness the elements and weave spells with devastating effects."
kobold_sorcerer_floor_range = (5, 7)
kobold_sorcerer_spells = ["Fireball", "Frost Nova", "Lightning Bolt"]
kobold_sorcerer_spell_probabilities = {"Fireball": 0.4, "Frost Nova": 0.3, "Lightning Bolt": 0.3}
kobold_sorcerer_initial_stats = kobold_sorcerer_stats.copy()
kobold_sorcerer = Monster("Kobold Sorcerer", kobold_sorcerer_stats, kobold_sorcerer_gear, kobold_sorcerer_loot_table, difficulty=50, description=kobold_sorcerer_description, floor_range=kobold_sorcerer_floor_range, spells=kobold_sorcerer_spells, spell_probabilities=kobold_sorcerer_spell_probabilities, initial_stats=kobold_sorcerer_initial_stats)

kobold_scout_stats = {
    "HP": 130,
    "Damage": 35,
    "Defense": 15,
    "Magic Defense": 20,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 14,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "None"
}
kobold_scout_gear = ["Dagger", "Leather Armor"]
kobold_scout_loot_table = ["Gold", "Scouting Map", "Dagger of the Shadows"]
kobold_scout_description = "Kobold Scouts are agile and resourceful, tasked with gathering intelligence and exploring dangerous territories. They use daggers and lightweight leather armor to swiftly navigate through enemy territory."
kobold_scout_floor_range = (5, 8)
kobold_scout_spells = []
kobold_scout_spell_probabilities = {}
kobold_scout_initial_stats = kobold_scout_stats.copy()
kobold_scout = Monster("Kobold Scout", kobold_scout_stats, kobold_scout_gear, kobold_scout_loot_table, difficulty=30, description=kobold_scout_description, floor_range=kobold_scout_floor_range, spells=kobold_scout_spells, spell_probabilities=kobold_scout_spell_probabilities, initial_stats=kobold_scout_initial_stats)

kobold_bomber_stats = {
    "HP": 140,
    "Damage": 45,
    "Defense": 15,
    "Magic Defense": 25,
    "Strength": 14,
    "Dexterity": 16,
    "Constitution": 16,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 14,
    "Element": "Fire"
}
kobold_bomber_gear = ["Bomb Satchel", "Fireproof Vest"]
kobold_bomber_loot_table = ["Gold", "Explosive Powder", "Charred Fragment"]
kobold_bomber_description = "Kobold Bombers are pyromaniacs who love nothing more than to cause fiery chaos. They carry bomb satchels filled with explosive powder and wear fireproof vests to protect themselves from their own fiery creations."
kobold_bomber_floor_range = (6, 8)
kobold_bomber_spells = []
kobold_bomber_spell_probabilities = {}
kobold_bomber_initial_stats = kobold_bomber_stats.copy()
kobold_bomber = Monster("Kobold Bomber", kobold_bomber_stats, kobold_bomber_gear, kobold_bomber_loot_table, difficulty=40, description=kobold_bomber_description, floor_range=kobold_bomber_floor_range, spells=kobold_bomber_spells, spell_probabilities=kobold_bomber_spell_probabilities, initial_stats=kobold_bomber_initial_stats)

kobold_trapmaster_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 18,
    "Wisdom": 16,
    "Charisma": 16,
    "Element": "None"
}
kobold_trapmaster_gear = ["Trap Kit", "Camouflaged Garb"]
kobold_trapmaster_loot_table = ["Gold", "Disarmed Trap", "Masterwork Components"]
kobold_trapmaster_description = "Kobold Trapmasters are cunning engineers who specialize in setting deadly traps for unwary adventurers. They carry trap kits and wear camouflaged garb to blend into their surroundings."
kobold_trapmaster_floor_range = (6, 8)
kobold_trapmaster_spells = []
kobold_trapmaster_spell_probabilities = {}
kobold_trapmaster_initial_stats = kobold_trapmaster_stats.copy()
kobold_trapmaster = Monster("Kobold Trapmaster", kobold_trapmaster_stats, kobold_trapmaster_gear, kobold_trapmaster_loot_table, difficulty=50, description=kobold_trapmaster_description, floor_range=kobold_trapmaster_floor_range, spells=kobold_trapmaster_spells, spell_probabilities=kobold_trapmaster_spell_probabilities, initial_stats=kobold_trapmaster_initial_stats)

wyrmguard_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 35,
    "Dexterity": 30,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"
}

wyrmguard_gear = ["Dragon Scale Armor", "Wyrmblade"]
wyrmguard_loot_table = ["Wyrmguard Emblem", "Dragon Scale", "Fire Gem"]
wyrmguard_description = "Wyrmguards are elite warriors sworn to protect the dragon's hoard, clad in armor forged from dragon scales."
wyrmguard_floor_range = (6, 8)
wyrmguard_spells = []
wyrmguard_spell_probabilities = {}
wyrmguard_initial_stats = wyrmguard_stats.copy()
wyrmguard = Monster("Wyrmguard", wyrmguard_stats, wyrmguard_gear, wyrmguard_loot_table, difficulty=8, description=wyrmguard_description, floor_range=wyrmguard_floor_range, spells=wyrmguard_spells, spell_probabilities=wyrmguard_spell_probabilities, initial_stats=wyrmguard_initial_stats)

drake_guardian_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 20,
    "Dexterity": 16,
    "Constitution": 18,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Fire"
}
drake_guardian_gear = ["Scaled Armor", "Firebrand Sword"]
drake_guardian_loot_table = ["Drake Scale", "Dragon Tooth", "Gold"]
drake_guardian_description = "Drake Guardians are fierce defenders of the Dragon Lair, possessing fiery breath and sharp claws. They serve their draconic master with unwavering loyalty, patrolling the lair's corridors and attacking intruders on sight."
drake_guardian_floor_range = (6, 8)
drake_guardian_spells = []
drake_guardian_spell_probabilities = {}
drake_guardian_initial_stats = drake_guardian_stats.copy()
drake_guardian = Monster("Drake Guardian", drake_guardian_stats, drake_guardian_gear, drake_guardian_loot_table, difficulty=30, description=drake_guardian_description, floor_range=drake_guardian_floor_range, spells=drake_guardian_spells, spell_probabilities=drake_guardian_spell_probabilities, initial_stats=drake_guardian_initial_stats)

kobold_flamecaster_stats = {
    "HP": 90,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 25,
    "Strength": 10,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 18,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Fire"
}
kobold_flamecaster_gear = ["Robes of the Firecaster", "Staff of Flames"]
kobold_flamecaster_loot_table = ["Fire Essence", "Charred Scroll", "Gold"]
kobold_flamecaster_description = "Kobold Flamecasters are adept practitioners of fire magic, serving as spellcasters within the Dragon Lair's ranks. They hurl fiery spells at intruders, engulfing them in flames and keeping them at bay while their draconic masters prepare for battle."
kobold_flamecaster_floor_range = (7, 9)
kobold_flamecaster_spells = ["Fireball", "Flame Burst", "Ignite"]
kobold_flamecaster_spell_probabilities = {"Fireball": 0.4, "Flame Burst": 0.3, "Ignite": 0.2}
kobold_flamecaster_initial_stats = kobold_flamecaster_stats.copy()
kobold_flamecaster = Monster("Kobold Flamecaster", kobold_flamecaster_stats, kobold_flamecaster_gear, kobold_flamecaster_loot_table, difficulty=30, description=kobold_flamecaster_description, floor_range=kobold_flamecaster_floor_range, spells=kobold_flamecaster_spells, spell_probabilities=kobold_flamecaster_spell_probabilities, initial_stats=kobold_flamecaster_initial_stats)

dragonkin_berserker_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 22,
    "Dexterity": 14,
    "Constitution": 20,
    "Intelligence": 8,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "None"
}
dragonkin_berserker_gear = ["Dragonhide Armor", "Greatsword of the Wyrm"]
dragonkin_berserker_loot_table = ["Dragon Scale", "Wyrm Fang", "Gold"]
dragonkin_berserker_description = "Dragonkin Berserkers are fearsome warriors, infused with the power and rage of the dragons they serve. They charge into battle with reckless abandon, cleaving through their enemies with massive swords and dragonhide armor."
dragonkin_berserker_floor_range = (7, 9)
dragonkin_berserker_spells = []
dragonkin_berserker_spell_probabilities = {}
dragonkin_berserker_initial_stats = dragonkin_berserker_stats.copy()
dragonkin_berserker = Monster("Dragonkin Berserker", dragonkin_berserker_stats, dragonkin_berserker_gear, dragonkin_berserker_loot_table, difficulty=30, description=dragonkin_berserker_description, floor_range=dragonkin_berserker_floor_range, spells=dragonkin_berserker_spells, spell_probabilities=dragonkin_berserker_spell_probabilities, initial_stats=dragonkin_berserker_initial_stats)

scalebound_enforcer_stats = {
    "HP": 160,
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
scalebound_enforcer_gear = ["Scalebound Plate", "Enforcer's Maul"]
scalebound_enforcer_loot_table = ["Dragonhide", "Enchanted Scale", "Gold"]
scalebound_enforcer_description = "Scalebound Enforcers are elite warriors, clad in armor crafted from the scales of dragons. They wield massive mauls with devastating force, smashing through their enemies with brute strength and precision."
scalebound_enforcer_floor_range = (7, 9)
scalebound_enforcer_spells = []
scalebound_enforcer_spell_probabilities = {}
scalebound_enforcer_initial_stats = scalebound_enforcer_stats.copy()
scalebound_enforcer = Monster("Scalebound Enforcer", scalebound_enforcer_stats, scalebound_enforcer_gear, scalebound_enforcer_loot_table, difficulty=30, description=scalebound_enforcer_description, floor_range=scalebound_enforcer_floor_range, spells=scalebound_enforcer_spells, spell_probabilities=scalebound_enforcer_spell_probabilities, initial_stats=scalebound_enforcer_initial_stats)

scalebound_juggernaut_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 22,
    "Dexterity": 14,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}
scalebound_juggernaut_gear = ["Scalebound Armor", "Juggernaut's Maul"]
scalebound_juggernaut_loot_table = ["Dragonhide", "Enchanted Scale", "Gold"]
scalebound_juggernaut_description = "Scalebound Juggernauts are colossal warriors, clad in armor forged from the toughest dragon scales. They wield massive mauls with overwhelming force, crushing anything that stands in their way with relentless determination."
scalebound_juggernaut_floor_range = (7, 9)
scalebound_juggernaut_spells = []
scalebound_juggernaut_spell_probabilities = {}
scalebound_juggernaut_initial_stats = scalebound_juggernaut_stats.copy()
scalebound_juggernaut = Monster("Scalebound Juggernaut", scalebound_juggernaut_stats, scalebound_juggernaut_gear, scalebound_juggernaut_loot_table, difficulty=30, description=scalebound_juggernaut_description, floor_range=scalebound_juggernaut_floor_range, spells=scalebound_juggernaut_spells, spell_probabilities=scalebound_juggernaut_spell_probabilities, initial_stats=scalebound_juggernaut_initial_stats)

hoardhound_stats = {
    "HP": 180,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Earth"
}

hoardhound_gear = ["Dragonbone Collar"]
hoardhound_loot_table = ["Hoardhound Claw", "Dragon Essence", "Treasure Trove Key"]
hoardhound_description = "Hoardhounds are fierce beasts trained by the dragon to defend its treasure, with jaws capable of crushing steel."
hoardhound_floor_range = (8, 10)
hoardhound_spells = []
hoardhound_spell_probabilities = {}
hoardhound_initial_stats = hoardhound_stats.copy()
hoardhound = Monster("Hoardhound", hoardhound_stats, hoardhound_gear, hoardhound_loot_table, difficulty=7, description=hoardhound_description, floor_range=hoardhound_floor_range, spells=hoardhound_spells, spell_probabilities=hoardhound_spell_probabilities, initial_stats=hoardhound_initial_stats)

gilded_golem_stats = {
    "HP": 250,
    "Damage": 45,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 40,
    "Dexterity": 20,
    "Constitution": 45,
    "Intelligence": 10,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Earth"
}

gilded_golem_gear = ["Golden Gauntlets", "Gleaming Greaves"]
gilded_golem_loot_table = ["Gilded Golem Core", "Gold Ingot", "Precious Gemstone"]
gilded_golem_description = "Gilded Golems are constructs crafted from precious metals, animated to serve as guardians of the hoard."
gilded_golem_floor_range = (8, 10)
gilded_golem_spells = []
gilded_golem_spell_probabilities = {}
gilded_golem_initial_stats = gilded_golem_stats.copy()
gilded_golem = Monster("Gilded Golem", gilded_golem_stats, gilded_golem_gear, gilded_golem_loot_table, difficulty=9, description=gilded_golem_description, floor_range=gilded_golem_floor_range, spells=gilded_golem_spells, spell_probabilities=gilded_golem_spell_probabilities, initial_stats=gilded_golem_initial_stats)

gemstone_gargoyle_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Earth"
}

gemstone_gargoyle_gear = ["Gemstone Greaves", "Crystal Crest"]
gemstone_gargoyle_loot_table = ["Gemstone Fragment", "Ruby Eye", "Sapphire Shard"]
gemstone_gargoyle_description = "Gemstone Gargoyles are stone guardians adorned with jewels, brought to life by the dragon's magic."
gemstone_gargoyle_floor_range = (8, 10)
gemstone_gargoyle_spells = []
gemstone_gargoyle_spell_probabilities = {}
gemstone_gargoyle_initial_stats = gemstone_gargoyle_stats.copy()
gemstone_gargoyle = Monster("Gemstone Gargoyle", gemstone_gargoyle_stats, gemstone_gargoyle_gear, gemstone_gargoyle_loot_table, difficulty=7, description=gemstone_gargoyle_description, floor_range=gemstone_gargoyle_floor_range, spells=gemstone_gargoyle_spells, spell_probabilities=gemstone_gargoyle_spell_probabilities, initial_stats=gemstone_gargoyle_initial_stats)

kobold_flameblade_stats = {
    "HP": 110,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 20,
    "Strength": 14,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Fire"
}
kobold_flameblade_gear = ["Flame-forged Dagger", "Singed Cloak"]
kobold_flameblade_loot_table = ["Fire Essence", "Charred Scroll", "Gold"]
kobold_flameblade_description = "Kobold Flameblades are fierce warriors, wielding blades imbued with the flames of their fiery home. They dart in and out of combat, striking with speed and precision, leaving their enemies scorched and smoldering."
kobold_flameblade_floor_range = (8, 10)
kobold_flameblade_spells = []
kobold_flameblade_spell_probabilities = {}
kobold_flameblade_initial_stats = kobold_flameblade_stats.copy()
kobold_flameblade = Monster("Kobold Flameblade", kobold_flameblade_stats, kobold_flameblade_gear, kobold_flameblade_loot_table, difficulty=30, description=kobold_flameblade_description, floor_range=kobold_flameblade_floor_range, spells=kobold_flameblade_spells, spell_probabilities=kobold_flameblade_spell_probabilities, initial_stats=kobold_flameblade_initial_stats)

dragon_cultist_warrior_stats = {
    "HP": 200,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 35,
    "Dexterity": 30,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"
}

dragon_cultist_warrior_gear = ["Cultist Cuirass", "Dragonblood Blade"]
dragon_cultist_warrior_loot_table = ["Dragon Cultist Insignia", "Obsidian Shard", "Ritual Dagger"]
dragon_cultist_warrior_description = "Dragon Cultist Warriors are fanatical worshippers who serve the dragon, sacrificing their enemies to appease its wrath."
dragon_cultist_warrior_floor_range = (9, 11)
dragon_cultist_warrior_spells = []
dragon_cultist_warrior_spell_probabilities = {}
dragon_cultist_warrior_initial_stats = dragon_cultist_warrior_stats.copy()
dragon_cultist_warrior = Monster("Dragon Cultist Warrior", dragon_cultist_warrior_stats, dragon_cultist_warrior_gear, dragon_cultist_warrior_loot_table, difficulty=8, description=dragon_cultist_warrior_description, floor_range=dragon_cultist_warrior_floor_range, spells=dragon_cultist_warrior_spells, spell_probabilities=dragon_cultist_warrior_spell_probabilities, initial_stats=dragon_cultist_warrior_initial_stats)

dragon_cultist_archer_stats = {
    "HP": 160,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Fire"
}

dragon_cultist_archer_gear = ["Cultist Hood", "Dragonbone Bow"]
dragon_cultist_archer_loot_table = ["Dragon Cultist Insignia", "Dragon Fang Arrow", "Enchanted Quiver"]
dragon_cultist_archer_description = "Dragon Cultist Archers are fanatical worshippers who serve the dragon, sacrificing their enemies to appease its wrath."
dragon_cultist_archer_floor_range = (9, 11)
dragon_cultist_archer_spells = []
dragon_cultist_archer_spell_probabilities = {}
dragon_cultist_archer_initial_stats = dragon_cultist_archer_stats.copy()
dragon_cultist_archer = Monster("Dragon Cultist Archer", dragon_cultist_archer_stats, dragon_cultist_archer_gear, dragon_cultist_archer_loot_table, difficulty=7, description=dragon_cultist_archer_description, floor_range=dragon_cultist_archer_floor_range, spells=dragon_cultist_archer_spells, spell_probabilities=dragon_cultist_archer_spell_probabilities, initial_stats=dragon_cultist_archer_initial_stats)

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
fire_elemental_floor_range = (10, 12)
fire_elemental_spells = ["Fireball", "Flame Burst"]
fire_elemental_spell_probabilities = {"Fireball": 0.6, "Flame Burst": 0.4} 
fire_elemental_initial_stats = fire_elemental_stats.copy() # Make a copy of the initial stats
fire_elemental = Monster("Fire Elemental", fire_elemental_stats, fire_elemental_gear, fire_elemental_loot_table, difficulty=20, description=fire_elemental_description, floor_range=fire_elemental_floor_range, spells=fire_elemental_spells, spell_probabilities=fire_elemental_spell_probabilities, initial_stats=fire_elemental_initial_stats)

air_elemental_stats = {
    "HP": 150,  # Define HP attribute for Air Elemental
    "Damage": 50,  # Define damage attribute for Air Elemental
    "Defense": 30,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 18,
    "Dexterity": 16,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Air"  # Define elemental attribute of the Air Elemental's attack
}
air_elemental_gear = ["Gaseous Form", "Wind Veil"]
air_elemental_loot_table = ["Gold", "Air Essence", "Cloud Crystal"]
air_elemental_description = "Air Elementals are ethereal beings composed of swirling winds and invisible currents. They wield the power of the skies, summoning mighty storms and tearing through enemies with razor-sharp gusts. Their elusive nature makes them difficult to pin down, as they can effortlessly slip through cracks and dissipate into thin air."
air_elemental_floor_range = (10, 12)
air_elemental_spells = ["Gust", "Thunderstorm"]
air_elemental_spell_probabilities = {"Gust": 0.6, "Thunderstorm": 0.4} 
air_elemental_initial_stats = air_elemental_stats.copy() # Make a copy of the initial stats
air_elemental = Monster("Air Elemental", air_elemental_stats, air_elemental_gear, air_elemental_loot_table, difficulty=20, description=air_elemental_description, floor_range=air_elemental_floor_range, spells=air_elemental_spells, spell_probabilities=air_elemental_spell_probabilities, initial_stats=air_elemental_initial_stats)

dragon_cultist_mage_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 25,
    "Magic Defense": 40,
    "Strength": 20,
    "Dexterity": 25,
    "Constitution": 30,
    "Intelligence": 40,
    "Wisdom": 35,
    "Charisma": 25,
    "Element": "Fire"
}

dragon_cultist_mage_gear = ["Cultist Robes", "Dragonfire Staff"]
dragon_cultist_mage_loot_table = ["Dragon Cultist Insignia", "Scroll of Flame", "Tome of Arcane Secrets"]
dragon_cultist_mage_description = "Dragon Cultist Mages are fanatical worshippers who serve the dragon, sacrificing their enemies to appease its wrath."
dragon_cultist_mage_floor_range = (10, 12)
dragon_cultist_mage_spells = ["Fireball", "Inferno"]
dragon_cultist_mage_spell_probabilities = {"Fireball": 0.7, "Inferno": 0.3}
dragon_cultist_mage_initial_stats = dragon_cultist_mage_stats.copy()
dragon_cultist_mage = Monster("Dragon Cultist Mage", dragon_cultist_mage_stats, dragon_cultist_mage_gear, dragon_cultist_mage_loot_table, difficulty=8, description=dragon_cultist_mage_description, floor_range=dragon_cultist_mage_floor_range, spells=dragon_cultist_mage_spells, spell_probabilities=dragon_cultist_mage_spell_probabilities, initial_stats=dragon_cultist_mage_initial_stats)

dragon_cultist_rider_stats = {
    "HP": 220,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 40,
    "Dexterity": 35,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Fire"
}

dragon_cultist_rider_gear = ["Cultist Helm", "Dragon Lance"]
dragon_cultist_rider_loot_table = ["Dragon Cultist Insignia", "Rider's Spurs", "Dragonhide Saddle"]
dragon_cultist_rider_description = "Dragon Cultist Riders are fanatical worshippers who serve the dragon, sacrificing their enemies to appease its wrath."
dragon_cultist_rider_floor_range = (10, 12)
dragon_cultist_rider_spells = []
dragon_cultist_rider_spell_probabilities = {}
dragon_cultist_rider_initial_stats = dragon_cultist_rider_stats.copy()
dragon_cultist_rider = Monster("Dragon Cultist Rider", dragon_cultist_rider_stats, dragon_cultist_rider_gear, dragon_cultist_rider_loot_table, difficulty=8, description=dragon_cultist_rider_description, floor_range=dragon_cultist_rider_floor_range, spells=dragon_cultist_rider_spells, spell_probabilities=dragon_cultist_rider_spell_probabilities, initial_stats=dragon_cultist_rider_initial_stats)

dragon_cultist_assassin_stats = {
    "HP": 200,
    "Damage": 60,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 30,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 20,
    "Element": "Fire"
}

dragon_cultist_assassin_gear = ["Cultist Hood", "Dragon Fang Dagger"]
dragon_cultist_assassin_loot_table = ["Dragon Cultist Insignia", "Assassin's Poison", "Shadow Cloak"]
dragon_cultist_assassin_description = "Dragon Cultist Assassins are fanatical worshippers who serve the dragon, sacrificing their enemies to appease its wrath."
dragon_cultist_assassin_floor_range = (11, 13)
dragon_cultist_assassin_spells = []
dragon_cultist_assassin_spell_probabilities = {}
dragon_cultist_assassin_initial_stats = dragon_cultist_assassin_stats.copy()
dragon_cultist_assassin = Monster("Dragon Cultist Assassin", dragon_cultist_assassin_stats, dragon_cultist_assassin_gear, dragon_cultist_assassin_loot_table, difficulty=8, description=dragon_cultist_assassin_description, floor_range=dragon_cultist_assassin_floor_range, spells=dragon_cultist_assassin_spells, spell_probabilities=dragon_cultist_assassin_spell_probabilities, initial_stats=dragon_cultist_assassin_initial_stats)

scalebound_sorcerer_stats = {
    "HP": 180,
    "Damage": 65,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 25,
    "Dexterity": 30,
    "Constitution": 30,
    "Intelligence": 45,
    "Wisdom": 35,
    "Charisma": 25,
    "Element": "Fire"
}

scalebound_sorcerer_gear = ["Sorcerer's Robes", "Dragonbone Staff"]
scalebound_sorcerer_loot_table = ["Dragon Cultist Insignia", "Scroll of Firestorm", "Tome of Forbidden Knowledge"]
scalebound_sorcerer_description = "Scalebound Sorcerers are spellcasters who harness the power of dragon magic to unleash devastating spells."
scalebound_sorcerer_floor_range = (11, 13)
scalebound_sorcerer_spells = ["Fireball", "Dragon's Breath"]
scalebound_sorcerer_spell_probabilities = {"Fireball": 0.6, "Dragon's Breath": 0.4}
scalebound_sorcerer_initial_stats = scalebound_sorcerer_stats.copy()
scalebound_sorcerer = Monster("Scalebound Sorcerer", scalebound_sorcerer_stats, scalebound_sorcerer_gear, scalebound_sorcerer_loot_table, difficulty=8, description=scalebound_sorcerer_description, floor_range=scalebound_sorcerer_floor_range, spells=scalebound_sorcerer_spells, spell_probabilities=scalebound_sorcerer_spell_probabilities, initial_stats=scalebound_sorcerer_initial_stats)

chromatic_crawler_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 40,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Mixed"
}

chromatic_crawler_gear = ["Chromatic Carapace", "Venomous Mandibles"]
chromatic_crawler_loot_table = ["Chromatic Scale", "Toxic Venom", "Prismatic Eye"]
chromatic_crawler_description = "Chromatic Crawlers are monstrous creatures with scales that shift through a rainbow of colors. They are highly venomous and fiercely territorial."
chromatic_crawler_floor_range = (11, 13)
chromatic_crawler_spells = []
chromatic_crawler_spell_probabilities = {}
chromatic_crawler_initial_stats = chromatic_crawler_stats.copy()
chromatic_crawler = Monster("Chromatic Crawler", chromatic_crawler_stats, chromatic_crawler_gear, chromatic_crawler_loot_table, difficulty=9, description=chromatic_crawler_description, floor_range=chromatic_crawler_floor_range, spells=chromatic_crawler_spells, spell_probabilities=chromatic_crawler_spell_probabilities, initial_stats=chromatic_crawler_initial_stats)

dragonkin_shaman_stats = {
    "HP": 200,
    "Damage": 55,
    "Defense": 25,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 30,
    "Constitution": 35,
    "Intelligence": 40,
    "Wisdom": 40,
    "Charisma": 25,
    "Element": "Fire"
}

dragonkin_shaman_gear = ["Dragonkin Headdress", "Dragonbone Staff"]
dragonkin_shaman_loot_table = ["Dragon Cultist Insignia", "Shamanic Totem", "Searing Scroll"]
dragonkin_shaman_description = "Dragonkin Shamans are mystics who commune with dragons, wielding both elemental and spiritual magic."
dragonkin_shaman_floor_range = (12, 15)
dragonkin_shaman_spells = ["Flame Surge", "Spiritual Shield"]
dragonkin_shaman_spell_probabilities = {"Flame Surge": 0.6, "Spiritual Shield": 0.4}
dragonkin_shaman_initial_stats = dragonkin_shaman_stats.copy()
dragonkin_shaman = Monster("Dragonkin Shaman", dragonkin_shaman_stats, dragonkin_shaman_gear, dragonkin_shaman_loot_table, difficulty=8, description=dragonkin_shaman_description, floor_range=dragonkin_shaman_floor_range, spells=dragonkin_shaman_spells, spell_probabilities=dragonkin_shaman_spell_probabilities, initial_stats=dragonkin_shaman_initial_stats)


### ADD MORE MOBS ###


magmafire_drake_stats = {
    "HP": 350,
    "Damage": 80,
    "Defense": 45,
    "Magic Defense": 40,
    "Strength": 55,
    "Dexterity": 40,
    "Constitution": 50,
    "Intelligence": 30,
    "Wisdom": 35,
    "Charisma": 30,
    "Element": "Fire"
}

magmafire_drake_gear = ["Scorching Scales", "Volcanic Claws"]
magmafire_drake_loot_table = ["Molten Core", "Flame Scale", "Ember Crystal"]
magmafire_drake_description = "Magmafire Drakes are fierce dragons that dwell deep within volcanic caverns. Their very presence ignites the air around them, and their molten breath leaves nothing but ash in its wake."
magmafire_drake_floor_range = (15, 18)
magmafire_drake_spells = []
magmafire_drake_spell_probabilities = {}
magmafire_drake_initial_stats = magmafire_drake_stats.copy()
magmafire_drake = Monster("Magmafire Drake", magmafire_drake_stats, magmafire_drake_gear, magmafire_drake_loot_table, difficulty=9, description=magmafire_drake_description, floor_range=magmafire_drake_floor_range, spells=magmafire_drake_spells, spell_probabilities=magmafire_drake_spell_probabilities, initial_stats=magmafire_drake_initial_stats)

thunderstorm_wyrm_stats = {
    "HP": 380,
    "Damage": 75,
    "Defense": 50,
    "Magic Defense": 45,
    "Strength": 60,
    "Dexterity": 45,
    "Constitution": 55,
    "Intelligence": 35,
    "Wisdom": 40,
    "Charisma": 35,
    "Element": "Electricity"
}

thunderstorm_wyrm_gear = ["Thunderous Scales", "Storm Surge Fangs"]
thunderstorm_wyrm_loot_table = ["Thunder Shard", "Electrified Scale", "Charged Essence"]
thunderstorm_wyrm_description = "Thunderstorm Wyrms are colossal dragons that command the power of lightning. They rule the skies, unleashing bolts of electricity upon any who dare challenge them."
thunderstorm_wyrm_floor_range = (15, 18)
thunderstorm_wyrm_spells = []
thunderstorm_wyrm_spell_probabilities = {}
thunderstorm_wyrm_initial_stats = thunderstorm_wyrm_stats.copy()
thunderstorm_wyrm = Monster("Thunderstorm Wyrm", thunderstorm_wyrm_stats, thunderstorm_wyrm_gear, thunderstorm_wyrm_loot_table, difficulty=9, description=thunderstorm_wyrm_description, floor_range=thunderstorm_wyrm_floor_range, spells=thunderstorm_wyrm_spells, spell_probabilities=thunderstorm_wyrm_spell_probabilities, initial_stats=thunderstorm_wyrm_initial_stats)

frostshard_drake_stats = {
    "HP": 330,
    "Damage": 70,
    "Defense": 48,
    "Magic Defense": 45,
    "Strength": 50,
    "Dexterity": 45,
    "Constitution": 48,
    "Intelligence": 35,
    "Wisdom": 40,
    "Charisma": 35,
    "Element": "Ice"
}

frostshard_drake_gear = ["Frosty Scales", "Glacial Claws"]
frostshard_drake_loot_table = ["Frost Shard", "Icicle Fang", "Frozen Heart"]
frostshard_drake_description = "Frostshard Drakes are formidable dragons that dwell in icy caverns. Their breath freezes all in its path, and their frosty scales are as hard as diamond."
frostshard_drake_floor_range = (17, 19)
frostshard_drake_spells = []
frostshard_drake_spell_probabilities = {}
frostshard_drake_initial_stats = frostshard_drake_stats.copy()
frostshard_drake = Monster("Frostshard Drake", frostshard_drake_stats, frostshard_drake_gear, frostshard_drake_loot_table, difficulty=9, description=frostshard_drake_description, floor_range=frostshard_drake_floor_range, spells=frostshard_drake_spells, spell_probabilities=frostshard_drake_spell_probabilities, initial_stats=frostshard_drake_initial_stats)

infernal_scaleback_stats = {
    "HP": 360,
    "Damage": 85,
    "Defense": 42,
    "Magic Defense": 40,
    "Strength": 58,
    "Dexterity": 40,
    "Constitution": 52,
    "Intelligence": 30,
    "Wisdom": 35,
    "Charisma": 30,
    "Element": "Fire"
}

infernal_scaleback_gear = ["Infernal Scales", "Lava Spine"]
infernal_scaleback_loot_table = ["Inferno Shard", "Molten Fang", "Smoldering Heart"]
infernal_scaleback_description = "Infernal Scalebacks are ferocious dragons that inhabit volcanic regions. Their fiery breath and molten scales make them nearly invulnerable to conventional attacks."
infernal_scaleback_floor_range = (17, 19)
infernal_scaleback_spells = []
infernal_scaleback_spell_probabilities = {}
infernal_scaleback_initial_stats = infernal_scaleback_stats.copy()
infernal_scaleback = Monster("Infernal Scaleback", infernal_scaleback_stats, infernal_scaleback_gear, infernal_scaleback_loot_table, difficulty=9, description=infernal_scaleback_description, floor_range=infernal_scaleback_floor_range, spells=infernal_scaleback_spells, spell_probabilities=infernal_scaleback_spell_probabilities, initial_stats=infernal_scaleback_initial_stats)

stormrage_wyrm_stats = {
    "HP": 380,
    "Damage": 75,
    "Defense": 50,
    "Magic Defense": 45,
    "Strength": 60,
    "Dexterity": 45,
    "Constitution": 55,
    "Intelligence": 35,
    "Wisdom": 40,
    "Charisma": 35,
    "Element": "Electricity"
}

stormrage_wyrm_gear = ["Stormy Scales", "Thunderstrike Talons"]
stormrage_wyrm_loot_table = ["Storm Shard", "Tempest Fang", "Electric Core"]
stormrage_wyrm_description = "Stormrage Wyrms are majestic dragons that soar through the tempestuous skies. They command the power of thunder and lightning, wreaking havoc upon their foes."
stormrage_wyrm_floor_range = (17, 19)
stormrage_wyrm_spells = []
stormrage_wyrm_spell_probabilities = {}
stormrage_wyrm_initial_stats = stormrage_wyrm_stats.copy()
stormrage_wyrm = Monster("Stormrage Wyrm", stormrage_wyrm_stats, stormrage_wyrm_gear, stormrage_wyrm_loot_table, difficulty=9, description=stormrage_wyrm_description, floor_range=stormrage_wyrm_floor_range, spells=stormrage_wyrm_spells, spell_probabilities=stormrage_wyrm_spell_probabilities, initial_stats=stormrage_wyrm_initial_stats)

blazewing_wyvern_stats = {
    "HP": 350,
    "Damage": 80,
    "Defense": 45,
    "Magic Defense": 40,
    "Strength": 55,
    "Dexterity": 40,
    "Constitution": 50,
    "Intelligence": 30,
    "Wisdom": 35,
    "Charisma": 30,
    "Element": "Fire"
}

blazewing_wyvern_gear = ["Blazing Scales", "Inferno Fangs"]
blazewing_wyvern_loot_table = ["Blaze Shard", "Scorching Fang", "Infernal Core"]
blazewing_wyvern_description = "Blazewing Wyverns are swift and agile dragons that leave trails of fire in their wake. Their fiery breath incinerates all in its path, leaving nothing but ash behind."
blazewing_wyvern_floor_range = (17, 19)
blazewing_wyvern_spells = []
blazewing_wyvern_spell_probabilities = {}
blazewing_wyvern_initial_stats = blazewing_wyvern_stats.copy()
blazewing_wyvern = Monster("Blazewing Wyvern", blazewing_wyvern_stats, blazewing_wyvern_gear, blazewing_wyvern_loot_table, difficulty=9, description=blazewing_wyvern_description, floor_range=blazewing_wyvern_floor_range, spells=blazewing_wyvern_spells, spell_probabilities=blazewing_wyvern_spell_probabilities, initial_stats=blazewing_wyvern_initial_stats)
