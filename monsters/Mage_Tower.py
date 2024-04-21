from monsters.bestiary import Monster

warped_mage_stats = {
    "HP": 120,
    "Damage": 50,
    "Defense": 25,
    "Magic Defense": 40,
    "Strength": 16,
    "Dexterity": 18,
    "Constitution": 20,
    "Intelligence": 22,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

warped_mage_gear = ["Twisted Staff", "Warped Robes"]
warped_mage_loot_table = ["Arcane Essence", "Corrupted Grimoire", "Cursed Scroll"]
warped_mage_description = "The Warped Mage is a practitioner of dark magic, corrupted by the arcane energies it wields. With a twisted staff and wearing warped robes, it seeks to unleash chaos and destruction upon the castle's inhabitants."
warped_mage_floor_range = (38, 40)
warped_mage_spells = ["Dark Bolt", "Chaotic Blast"]
warped_mage_spell_probabilities = {"Dark Bolt": 0.6, "Chaotic Blast": 0.4}
warped_mage_initial_stats = warped_mage_stats.copy()
warped_mage = Monster("Warped Mage", warped_mage_stats, warped_mage_gear, warped_mage_loot_table, difficulty=7, description=warped_mage_description, floor_range=warped_mage_floor_range, spells=warped_mage_spells, spell_probabilities=warped_mage_spell_probabilities, initial_stats=warped_mage_initial_stats)

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
air_elemental_floor_range = (20, 40)
air_elemental_spells = ["Gust", "Thunderstorm"]
air_elemental_spell_probabilities = {"Gust": 0.6, "Thunderstorm": 0.4} 
air_elemental_initial_stats = air_elemental_stats.copy() # Make a copy of the initial stats
air_elemental = Monster("Air Elemental", air_elemental_stats, air_elemental_gear, air_elemental_loot_table, difficulty=20, description=air_elemental_description, floor_range=air_elemental_floor_range, spells=air_elemental_spells, spell_probabilities=air_elemental_spell_probabilities, initial_stats=air_elemental_initial_stats)

mana_elemental_stats = {
    "HP": 120,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 45,
    "Strength": 15,
    "Dexterity": 20,
    "Constitution": 18,
    "Intelligence": 25,
    "Wisdom": 28,
    "Charisma": 20,
    "Element": "Arcane"
}

mana_elemental_gear = ["Ethereal Robes", "Mana Crystal"]
mana_elemental_loot_table = ["Arcane Essence", "Ethereal Dust", "Mana Shard"]
mana_elemental_description = "The Mana Elemental is a manifestation of raw arcane energy, its form shimmering with mystical power. With an affinity for magic, it manipulates the very fabric of reality to unleash devastating spells upon its enemies."
mana_elemental_floor_range = (25, 28)
mana_elemental_spells = ["Arcane Blast", "Mana Surge"]
mana_elemental_spell_probabilities = {"Arcane Blast": 0.6, "Mana Surge": 0.4}
mana_elemental_initial_stats = mana_elemental_stats.copy()
mana_elemental = Monster("Mana Elemental", mana_elemental_stats, mana_elemental_gear, mana_elemental_loot_table, difficulty=6, description=mana_elemental_description, floor_range=mana_elemental_floor_range, spells=mana_elemental_spells, spell_probabilities=mana_elemental_spell_probabilities, initial_stats=mana_elemental_initial_stats)

blue_wisp_stats = {
    "HP": 60,
    "Damage": 20,
    "Defense": 10,
    "Magic Defense": 30,
    "Strength": 10,
    "Dexterity": 25,
    "Constitution": 15,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Arcane"
}

blue_wisp_gear = ["Ethereal Shroud", "Arcane Essence"]
blue_wisp_loot_table = ["Glowing Orb", "Essence Fragment", "Arcane Dust"]
blue_wisp_description = "The Blue Wisp is a spectral entity composed of pure arcane energy. It floats effortlessly through the air, emitting a soft blue glow that illuminates the surrounding area. Beware its magical attacks, for they can disrupt both body and mind."
blue_wisp_floor_range = (15, 20)
blue_wisp_spells = ["Arcane Bolt", "Mana Drain"]
blue_wisp_spell_probabilities = {"Arcane Bolt": 0.7, "Mana Drain": 0.3}
blue_wisp_initial_stats = blue_wisp_stats.copy()
blue_wisp = Monster("Blue Wisp", blue_wisp_stats, blue_wisp_gear, blue_wisp_loot_table, difficulty=5, description=blue_wisp_description, floor_range=blue_wisp_floor_range, spells=blue_wisp_spells, spell_probabilities=blue_wisp_spell_probabilities, initial_stats=blue_wisp_initial_stats)

mana_weaver_stats = {
    "HP": 120,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 15,
    "Dexterity": 20,
    "Constitution": 18,
    "Intelligence": 25,
    "Wisdom": 22,
    "Charisma": 15,
    "Element": "Arcane"
}

mana_weaver_gear = ["Ethereal Robes", "Mana Crystal"]
mana_weaver_loot_table = ["Arcane Essence", "Silk Threads", "Mana Shard"]
mana_weaver_description = "The Mana Weaver is a master of manipulating arcane energies, weaving spells with precision and grace. Clad in shimmering robes adorned with arcane symbols, it channels the raw power of mana to unleash devastating magical attacks."
mana_weaver_floor_range = (40, 42)
mana_weaver_spells = ["Arcane Blast", "Mana Drain"]
mana_weaver_spell_probabilities = {"Arcane Blast": 0.7, "Mana Drain": 0.3}
mana_weaver_initial_stats = mana_weaver_stats.copy()
mana_weaver = Monster("Mana Weaver", mana_weaver_stats, mana_weaver_gear, mana_weaver_loot_table, difficulty=8, description=mana_weaver_description, floor_range=mana_weaver_floor_range, spells=mana_weaver_spells, spell_probabilities=mana_weaver_spell_probabilities, initial_stats=mana_weaver_initial_stats)

arcane_scholar_stats = {
    "HP": 110,
    "Damage": 30,
    "Defense": 15,
    "Magic Defense": 45,
    "Strength": 12,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 28,
    "Wisdom": 25,
    "Charisma": 12,
    "Element": "Arcane"
}

arcane_scholar_gear = ["Tome of Arcana", "Scholar's Robes"]
arcane_scholar_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
arcane_scholar_description = "The Arcane Scholar is a seeker of knowledge, delving into ancient tomes and scrolls to uncover the mysteries of the arcane. With a mind as sharp as any blade, it wields powerful spells with precision and expertise."
arcane_scholar_floor_range = (1,5)
arcane_scholar_spells = ["Arcane Bolt", "Knowledge Drain"]
arcane_scholar_spell_probabilities = {"Arcane Bolt": 0.6, "Knowledge Drain": 0.4}
arcane_scholar_initial_stats = arcane_scholar_stats.copy()
arcane_scholar = Monster("Arcane Scholar", arcane_scholar_stats, arcane_scholar_gear, arcane_scholar_loot_table, difficulty=7, description=arcane_scholar_description, floor_range=arcane_scholar_floor_range, spells=arcane_scholar_spells, spell_probabilities=arcane_scholar_spell_probabilities, initial_stats=arcane_scholar_initial_stats)

mystic_spellbinder_stats = {
    "HP": 130,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 40,
    "Strength": 18,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 25,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Arcane"
}

mystic_spellbinder_gear = ["Spellbound Staff", "Mystic Robes"]
mystic_spellbinder_loot_table = ["Arcane Essence", "Spellbound Crystal", "Glyphed Tome"]
mystic_spellbinder_description = "The Mystic Spellbinder is a wielder of ancient magics, binding spells to its will with enigmatic glyphs and incantations. Cloaked in robes shimmering with arcane energy, it guards the secrets of the arcane with unwavering resolve."
mystic_spellbinder_floor_range = (42, 44)
mystic_spellbinder_spells = ["Arcane Barrage", "Mystic Shield"]
mystic_spellbinder_spell_probabilities = {"Arcane Barrage": 0.7, "Mystic Shield": 0.3}
mystic_spellbinder_initial_stats = mystic_spellbinder_stats.copy()
mystic_spellbinder = Monster("Mystic Spellbinder", mystic_spellbinder_stats, mystic_spellbinder_gear, mystic_spellbinder_loot_table, difficulty=8, description=mystic_spellbinder_description, floor_range=mystic_spellbinder_floor_range, spells=mystic_spellbinder_spells, spell_probabilities=mystic_spellbinder_spell_probabilities, initial_stats=mystic_spellbinder_initial_stats)

celestial_astralweaver_stats = {
    "HP": 150,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 45,
    "Strength": 16,
    "Dexterity": 20,
    "Constitution": 22,
    "Intelligence": 28,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Celestial"
}

celestial_astralweaver_gear = ["Astral Staff", "Celestial Robes"]
celestial_astralweaver_loot_table = ["Celestial Essence", "Astral Crystal", "Stellar Tome"]
celestial_astralweaver_description = "The Celestial Astralweaver channels the power of the cosmos, manipulating the fabric of reality with celestial energies. Adorned in robes adorned with stars, it commands the mysteries of the heavens with profound insight."
celestial_astralweaver_floor_range = (42, 44)
celestial_astralweaver_spells = ["Stellar Burst", "Celestial Shield"]
celestial_astralweaver_spell_probabilities = {"Stellar Burst": 0.7, "Celestial Shield": 0.3}
celestial_astralweaver_initial_stats = celestial_astralweaver_stats.copy()
celestial_astralweaver = Monster("Celestial Astralweaver", celestial_astralweaver_stats, celestial_astralweaver_gear, celestial_astralweaver_loot_table, difficulty=8, description=celestial_astralweaver_description, floor_range=celestial_astralweaver_floor_range, spells=celestial_astralweaver_spells, spell_probabilities=celestial_astralweaver_spell_probabilities, initial_stats=celestial_astralweaver_initial_stats)

celestial_rift_conjurer_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 20,
    "Magic Defense": 50,
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 20,
    "Intelligence": 30,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Celestial"
}

celestial_rift_conjurer_gear = ["Rift Staff", "Celestial Garb"]
celestial_rift_conjurer_loot_table = ["Celestial Essence", "Rift Shard", "Astral Codex"]
celestial_rift_conjurer_description = "The Celestial Rift Conjurer harnesses the power of interdimensional portals, summoning otherworldly beings with celestial incantations. Clad in garb resonating with celestial energy, it traverses the boundaries between realms with unparalleled mastery."
celestial_rift_conjurer_floor_range = (42, 44)
celestial_rift_conjurer_spells = ["Rift Bolt", "Celestial Barrier"]
celestial_rift_conjurer_spell_probabilities = {"Rift Bolt": 0.7, "Celestial Barrier": 0.3}
celestial_rift_conjurer_initial_stats = celestial_rift_conjurer_stats.copy()
celestial_rift_conjurer = Monster("Celestial Rift Conjurer", celestial_rift_conjurer_stats, celestial_rift_conjurer_gear, celestial_rift_conjurer_loot_table, difficulty=8, description=celestial_rift_conjurer_description, floor_range=celestial_rift_conjurer_floor_range, spells=celestial_rift_conjurer_spells, spell_probabilities=celestial_rift_conjurer_spell_probabilities, initial_stats=celestial_rift_conjurer_initial_stats)

celestial_rift_magus_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 20,
    "Magic Defense": 55,
    "Strength": 20,
    "Dexterity": 22,
    "Constitution": 22,
    "Intelligence": 32,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Celestial"
}

celestial_rift_magus_gear = ["Riftblade Staff", "Celestial Vestments"]
celestial_rift_magus_loot_table = ["Celestial Essence", "Rift Crystal", "Cosmic Grimoire"]
celestial_rift_magus_description = "The Celestial Rift Magus wields the power of cosmic forces, manipulating rifts in space and time to devastating effect. Draped in vestments infused with celestial energies, it commands the very fabric of reality with unparalleled finesse."
celestial_rift_magus_floor_range = (42, 44)
celestial_rift_magus_spells = ["Cosmic Surge", "Rift Shield"]
celestial_rift_magus_spell_probabilities = {"Cosmic Surge": 0.7, "Rift Shield": 0.3}
celestial_rift_magus_initial_stats = celestial_rift_magus_stats.copy()
celestial_rift_magus = Monster("Celestial Rift Magus", celestial_rift_magus_stats, celestial_rift_magus_gear, celestial_rift_magus_loot_table, difficulty=8, description=celestial_rift_magus_description, floor_range=celestial_rift_magus_floor_range, spells=celestial_rift_magus_spells, spell_probabilities=celestial_rift_magus_spell_probabilities, initial_stats=celestial_rift_magus_initial_stats)

celestial_chronomancer_stats = {
    "HP": 140,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 45,
    "Strength": 16,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 30,
    "Wisdom": 24,
    "Charisma": 18,
    "Element": "Celestial"
}

celestial_chronomancer_gear = ["Chrono Staff", "Celestial Mantle"]
celestial_chronomancer_loot_table = ["Celestial Essence", "Temporal Shard", "Eternal Tome"]
celestial_chronomancer_description = "The Celestial Chronomancer manipulates the flow of time itself, bending temporal reality to its will with celestial chronicles. Draped in a mantle resonating with celestial power, it navigates the ebb and flow of time with unparalleled precision."
celestial_chronomancer_floor_range = (42, 44)
celestial_chronomancer_spells = ["Temporal Shift", "Celestial Intervention"]
celestial_chronomancer_spell_probabilities = {"Temporal Shift": 0.7, "Celestial Intervention": 0.3}
celestial_chronomancer_initial_stats = celestial_chronomancer_stats.copy()
celestial_chronomancer = Monster("Celestial Chronomancer", celestial_chronomancer_stats, celestial_chronomancer_gear, celestial_chronomancer_loot_table, difficulty=8, description=celestial_chronomancer_description, floor_range=celestial_chronomancer_floor_range, spells=celestial_chronomancer_spells, spell_probabilities=celestial_chronomancer_spell_probabilities, initial_stats=celestial_chronomancer_initial_stats)

celestial_manaflayer_stats = {
    "HP": 160,
    "Damage": 50,
    "Defense": 20,
    "Magic Defense": 50,
    "Strength": 22,
    "Dexterity": 24,
    "Constitution": 22,
    "Intelligence": 28,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Celestial"
}

celestial_manaflayer_gear = ["Manaflayer Staff", "Celestial Attire"]
celestial_manaflayer_loot_table = ["Celestial Essence", "Mana Shard", "Aetheric Codex"]
celestial_manaflayer_description = "The Celestial Manaflayer channels the essence of the cosmos, weaving threads of mana with celestial precision. Adorned in attire infused with celestial power, it shapes the very essence of magic with unparalleled mastery."
celestial_manaflayer_floor_range = (42, 44)
celestial_manaflayer_spells = ["Aetheric Surge", "Celestial Veil"]
celestial_manaflayer_spell_probabilities = {"Aetheric Surge": 0.7, "Celestial Veil": 0.3}
celestial_manaflayer_initial_stats = celestial_manaflayer_stats.copy()
celestial_manaflayer = Monster("Celestial Manaflayer", celestial_manaflayer_stats, celestial_manaflayer_gear, celestial_manaflayer_loot_table, difficulty=8, description=celestial_manaflayer_description, floor_range=celestial_manaflayer_floor_range, spells=celestial_manaflayer_spells, spell_probabilities=celestial_manaflayer_spell_probabilities, initial_stats=celestial_manaflayer_initial_stats)

arcane_glyphweaver_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 50,
    "Strength": 18,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 30,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Arcane"
}

arcane_glyphweaver_gear = ["Glyph Staff", "Arcane Garb"]
arcane_glyphweaver_loot_table = ["Arcane Essence", "Glyph Shard", "Enchanted Codex"]
arcane_glyphweaver_description = "The Arcane Glyphweaver imbues spells with ancient glyphs, shaping arcane energies with profound insight. Clad in garb adorned with arcane symbols, it wields the secrets of the arcane with unparalleled finesse."
arcane_glyphweaver_floor_range = (42, 44)
arcane_glyphweaver_spells = ["Glyphic Blast", "Arcane Ward"]
arcane_glyphweaver_spell_probabilities = {"Glyphic Blast": 0.7, "Arcane Ward": 0.3}
arcane_glyphweaver_initial_stats = arcane_glyphweaver_stats.copy()
arcane_glyphweaver = Monster("Arcane Glyphweaver", arcane_glyphweaver_stats, arcane_glyphweaver_gear, arcane_glyphweaver_loot_table, difficulty=8, description=arcane_glyphweaver_description, floor_range=arcane_glyphweaver_floor_range, spells=arcane_glyphweaver_spells, spell_probabilities=arcane_glyphweaver_spell_probabilities, initial_stats=arcane_glyphweaver_initial_stats)

arcane_sentinels_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 50,
    "Strength": 18,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 30,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Arcane"
}

arcane_sentinels_gear = ["Arcane Staff", "Sentinel Robes"]
arcane_sentinels_loot_table = ["Arcane Essence", "Sentinel Crystal", "Enchanted Tome"]
arcane_sentinels_description = "The Arcane Sentinels stand guard over the secrets of the Mage Tower, their vigilant gaze piercing through the veils of magic. Clad in robes resonating with arcane energy, they protect the tower's ancient knowledge with unwavering resolve."
arcane_sentinels_floor_range = (42, 44)
arcane_sentinels_spells = ["Arcane Barrage", "Arcane Ward"]
arcane_sentinels_spell_probabilities = {"Arcane Barrage": 0.7, "Arcane Ward": 0.3}
arcane_sentinels_initial_stats = arcane_sentinels_stats.copy()
arcane_sentinels = Monster("Arcane Sentinels", arcane_sentinels_stats, arcane_sentinels_gear, arcane_sentinels_loot_table, difficulty=8, description=arcane_sentinels_description, floor_range=arcane_sentinels_floor_range, spells=arcane_sentinels_spells, spell_probabilities=arcane_sentinels_spell_probabilities, initial_stats=arcane_sentinels_initial_stats)

spellweave_conjurers_stats = {
    "HP": 130,
    "Damage": 45,
    "Defense": 20,
    "Magic Defense": 45,
    "Strength": 16,
    "Dexterity": 20,
    "Constitution": 20,
    "Intelligence": 32,
    "Wisdom": 18,
    "Charisma": 18,
    "Element": "Arcane"
}

spellweave_conjurers_gear = ["Spellweave Staff", "Conjurer Robes"]
spellweave_conjurers_loot_table = ["Arcane Essence", "Spellweave Crystal", "Conjurer's Grimoire"]
spellweave_conjurers_description = "The Spellweave Conjurers wield the threads of magic, spinning spells with intricate patterns of arcane energy. Draped in robes adorned with spellweave patterns, they conjure mystical forces with unparalleled finesse."
spellweave_conjurers_floor_range = (42, 44)
spellweave_conjurers_spells = ["Arcane Blast", "Summon Elemental"]
spellweave_conjurers_spell_probabilities = {"Arcane Blast": 0.7, "Summon Elemental": 0.3}
spellweave_conjurers_initial_stats = spellweave_conjurers_stats.copy()
spellweave_conjurers = Monster("Spellweave Conjurers", spellweave_conjurers_stats, spellweave_conjurers_gear, spellweave_conjurers_loot_table, difficulty=8, description=spellweave_conjurers_description, floor_range=spellweave_conjurers_floor_range, spells=spellweave_conjurers_spells, spell_probabilities=spellweave_conjurers_spell_probabilities, initial_stats=spellweave_conjurers_initial_stats)

mana_imbued_sentry_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 50,
    "Strength": 20,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 28,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

mana_imbued_sentry_gear = ["Mana-imbued Staff", "Sentry Armor"]
mana_imbued_sentry_loot_table = ["Arcane Essence", "Mana Crystal", "Sentry Codex"]
mana_imbued_sentry_description = "The Mana-imbued Sentry is a guardian empowered by the essence of magic, its form infused with mana from the Mage Tower's arcane reservoirs. Clad in armor resonating with mana energy, it defends the tower's sanctity with unyielding determination."
mana_imbued_sentry_floor_range = (42, 44)
mana_imbued_sentry_spells = ["Mana Surge", "Arcane Shield"]
mana_imbued_sentry_spell_probabilities = {"Mana Surge": 0.7, "Arcane Shield": 0.3}
mana_imbued_sentry_initial_stats = mana_imbued_sentry_stats.copy()
mana_imbued_sentry = Monster("Mana-imbued Sentry", mana_imbued_sentry_stats, mana_imbued_sentry_gear, mana_imbued_sentry_loot_table, difficulty=8, description=mana_imbued_sentry_description, floor_range=mana_imbued_sentry_floor_range, spells=mana_imbued_sentry_spells, spell_probabilities=mana_imbued_sentry_spell_probabilities, initial_stats=mana_imbued_sentry_initial_stats)

etheric_gargoyles_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 20,
    "Wisdom": 18,
    "Charisma": 16,
    "Element": "Arcane"
}

etheric_gargoyles_gear = ["Gargoyle Stone", "Etheric Armor"]
etheric_gargoyles_loot_table = ["Arcane Essence", "Gargoyle Shard", "Ethereal Tome"]
etheric_gargoyles_description = "Etheric Gargoyles, brought to life by ancient spells, watch over the Mage Tower with stoic vigilance. Carved from enchanted stone and adorned with etheric armor, they stand as silent sentinels, ever ready to defend the tower's secrets."
etheric_gargoyles_floor_range = (42, 44)
etheric_gargoyles_spells = ["Stone Barrage", "Ethereal Shield"]
etheric_gargoyles_spell_probabilities = {"Stone Barrage": 0.7, "Ethereal Shield": 0.3}
etheric_gargoyles_initial_stats = etheric_gargoyles_stats.copy()
etheric_gargoyles = Monster("Etheric Gargoyles", etheric_gargoyles_stats, etheric_gargoyles_gear, etheric_gargoyles_loot_table, difficulty=8, description=etheric_gargoyles_description, floor_range=etheric_gargoyles_floor_range, spells=etheric_gargoyles_spells, spell_probabilities=etheric_gargoyles_spell_probabilities, initial_stats=etheric_gargoyles_initial_stats)

mana_forged_guardian_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 45,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

mana_forged_guardian_gear = ["Mana-Forged Core", "Guardian Plate"]
mana_forged_guardian_loot_table = ["Arcane Essence", "Mana-Forged Shard", "Guardian Codex"]
mana_forged_guardian_description = "The Mana-Forged Guardian, crafted from arcane energies and enchanted metals, stands as a formidable protector of the Mage Tower. Powered by a mana-forged core and clad in impenetrable guardian plate, it defends the tower's sanctity with unwavering resolve."
mana_forged_guardian_floor_range = (42, 44)
mana_forged_guardian_spells = ["Mana Strike", "Guardian's Shield"]
mana_forged_guardian_spell_probabilities = {"Mana Strike": 0.7, "Guardian's Shield": 0.3}
mana_forged_guardian_initial_stats = mana_forged_guardian_stats.copy()
mana_forged_guardian = Monster("Mana-Forged Guardian", mana_forged_guardian_stats, mana_forged_guardian_gear, mana_forged_guardian_loot_table, difficulty=8, description=mana_forged_guardian_description, floor_range=mana_forged_guardian_floor_range, spells=mana_forged_guardian_spells, spell_probabilities=mana_forged_guardian_spell_probabilities, initial_stats=mana_forged_guardian_initial_stats)

enchanted_automaton_stats = {
    "HP": 170,
    "Damage": 55,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 24,
    "Dexterity": 22,
    "Constitution": 28,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

enchanted_automaton_gear = ["Enchanted Core", "Automaton Plating"]
enchanted_automaton_loot_table = ["Arcane Essence", "Enchanted Shard", "Automaton Manual"]
enchanted_automaton_description = "The Enchanted Automaton, a marvel of arcane engineering, roams the halls of the Mage Tower with mechanical precision. Powered by an enchanted core and armored in enchanted plating, it executes its programmed directives with flawless efficiency."
enchanted_automaton_floor_range = (42, 44)
enchanted_automaton_spells = ["Arcane Surge", "Automaton Defense"]
enchanted_automaton_spell_probabilities = {"Arcane Surge": 0.7, "Automaton Defense": 0.3}
enchanted_automaton_initial_stats = enchanted_automaton_stats.copy()
enchanted_automaton = Monster("Enchanted Automaton", enchanted_automaton_stats, enchanted_automaton_gear, enchanted_automaton_loot_table, difficulty=8, description=enchanted_automaton_description, floor_range=enchanted_automaton_floor_range, spells=enchanted_automaton_spells, spell_probabilities=enchanted_automaton_spell_probabilities, initial_stats=enchanted_automaton_initial_stats)

sigil_bound_warden_stats = {
    "HP": 190,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 45,
    "Strength": 26,
    "Dexterity": 22,
    "Constitution": 32,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

sigil_bound_warden_gear = ["Sigil Core", "Warden's Plate"]
sigil_bound_warden_loot_table = ["Arcane Essence", "Sigil Shard", "Warden's Codex"]
sigil_bound_warden_description = "The Sigil-Bound Warden, animated by arcane sigils of protection, stands as a bastion of defense within the Mage Tower. Empowered by a sigil core and armored in warden's plate, it wards off intruders with steadfast determination."
sigil_bound_warden_floor_range = (42, 44)
sigil_bound_warden_spells = ["Sigil Strike", "Warden's Shield"]
sigil_bound_warden_spell_probabilities = {"Sigil Strike": 0.7, "Warden's Shield": 0.3}
sigil_bound_warden_initial_stats = sigil_bound_warden_stats.copy()
sigil_bound_warden = Monster("Sigil-Bound Warden", sigil_bound_warden_stats, sigil_bound_warden_gear, sigil_bound_warden_loot_table, difficulty=8, description=sigil_bound_warden_description, floor_range=sigil_bound_warden_floor_range, spells=sigil_bound_warden_spells, spell_probabilities=sigil_bound_warden_spell_probabilities, initial_stats=sigil_bound_warden_initial_stats)

arcane_archivist_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 50,
    "Strength": 20,
    "Dexterity": 20,
    "Constitution": 25,
    "Intelligence": 28,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Arcane"
}

arcane_archivist_gear = ["Codex Staff", "Archivist Robes"]
arcane_archivist_loot_table = ["Arcane Essence", "Codex Shard", "Ancient Tome"]
arcane_archivist_description = "The Arcane Archivists meticulously catalog the arcane knowledge within the Mage Tower, wielding their staffs with scholarly precision. Cloaked in robes adorned with arcane symbols, they safeguard the tower's vast repository of magical lore."
arcane_archivist_floor_range = (42, 44)
arcane_archivist_spells = ["Arcane Insight", "Codex Blast"]
arcane_archivist_spell_probabilities = {"Arcane Insight": 0.7, "Codex Blast": 0.3}
arcane_archivist_initial_stats = arcane_archivist_stats.copy()
arcane_archivist = Monster("Arcane Archivist", arcane_archivist_stats, arcane_archivist_gear, arcane_archivist_loot_table, difficulty=8, description=arcane_archivist_description, floor_range=arcane_archivist_floor_range, spells=arcane_archivist_spells, spell_probabilities=arcane_archivist_spell_probabilities, initial_stats=arcane_archivist_initial_stats)

celestial_arbiters_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 55,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 26,
    "Wisdom": 24,
    "Charisma": 20,
    "Element": "Celestial"
}

celestial_arbiters_gear = ["Celestial Staff", "Arbiter Vestments"]
celestial_arbiters_loot_table = ["Celestial Essence", "Arbiter Crystal", "Divine Scroll"]
celestial_arbiters_description = "The Celestial Arbiters serve as judges of celestial law within the Mage Tower, wielding their staffs with divine authority. Clad in vestments imbued with celestial radiance, they enforce justice with unwavering conviction."
celestial_arbiters_floor_range = (42, 44)
celestial_arbiters_spells = ["Divine Judgment", "Celestial Barrier"]
celestial_arbiters_spell_probabilities = {"Divine Judgment": 0.7, "Celestial Barrier": 0.3}
celestial_arbiters_initial_stats = celestial_arbiters_stats.copy()
celestial_arbiters = Monster("Celestial Arbiters", celestial_arbiters_stats, celestial_arbiters_gear, celestial_arbiters_loot_table, difficulty=8, description=celestial_arbiters_description, floor_range=celestial_arbiters_floor_range, spells=celestial_arbiters_spells, spell_probabilities=celestial_arbiters_spell_probabilities, initial_stats=celestial_arbiters_initial_stats)

elemental_conduits_stats = {
    "HP": 170,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 45,
    "Strength": 24,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 22,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Arcane"
}

elemental_conduits_gear = ["Conduit Staff", "Elemental Vestments"]
elemental_conduits_loot_table = ["Arcane Essence", "Conduit Shard", "Elemental Codex"]
elemental_conduits_description = "The Elemental Conduits channel the raw power of the elements within the Mage Tower, their staffs crackling with elemental energy. Draped in vestments attuned to the elements, they manipulate the forces of nature with unparalleled mastery."
elemental_conduits_floor_range = (42, 44)
elemental_conduits_spells = ["Elemental Surge", "Conduit Shield"]
elemental_conduits_spell_probabilities = {"Elemental Surge": 0.7, "Conduit Shield": 0.3}
elemental_conduits_initial_stats = elemental_conduits_stats.copy()
elemental_conduits = Monster("Elemental Conduits", elemental_conduits_stats, elemental_conduits_gear, elemental_conduits_loot_table, difficulty=8, description=elemental_conduits_description, floor_range=elemental_conduits_floor_range, spells=elemental_conduits_spells, spell_probabilities=elemental_conduits_spell_probabilities, initial_stats=elemental_conduits_initial_stats)

arcane_devourers_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 26,
    "Dexterity": 24,
    "Constitution": 32,
    "Intelligence": 22,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

arcane_devourers_gear = ["Devourer Staff", "Arcane Armor"]
arcane_devourers_loot_table = ["Arcane Essence", "Devourer Shard", "Eldritch Tome"]
arcane_devourers_description = "The Arcane Devourers hunger for magical energy within the Mage Tower, their staffs pulsating with dark power. Clad in armor infused with eldritch energies, they consume arcane essence to fuel their insatiable appetite."
arcane_devourers_floor_range = (42, 44)
arcane_devourers_spells = ["Arcane Drain", "Eldritch Burst"]
arcane_devourers_spell_probabilities = {"Arcane Drain": 0.7, "Eldritch Burst": 0.3}
arcane_devourers_initial_stats = arcane_devourers_stats.copy()
arcane_devourers = Monster("Arcane Devourers", arcane_devourers_stats, arcane_devourers_gear, arcane_devourers_loot_table, difficulty=8, description=arcane_devourers_description, floor_range=arcane_devourers_floor_range, spells=arcane_devourers_spells, spell_probabilities=arcane_devourers_spell_probabilities, initial_stats=arcane_devourers_initial_stats)

voidwalker_stats = {
    "HP": 170,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 55,
    "Strength": 24,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 26,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Void"
}

voidwalker_gear = ["Void Staff", "Darkened Robes"]
voidwalker_loot_table = ["Void Essence", "Dark Shard", "Obsidian Tome"]
voidwalker_description = "The Voidwalkers emerge from the shadows, wielding dark magic within the Mage Tower. Clad in robes imbued with void energy, they serve as conduits for the mysterious powers of the abyss, striking fear into the hearts of all who oppose them."
voidwalker_floor_range = (42, 44)
voidwalker_spells = ["Shadow Bolt", "Void Shield"]
voidwalker_spell_probabilities = {"Shadow Bolt": 0.7, "Void Shield": 0.3}
voidwalker_initial_stats = voidwalker_stats.copy()
voidwalker = Monster("Voidwalker", voidwalker_stats, voidwalker_gear, voidwalker_loot_table, difficulty=8, description=voidwalker_description, floor_range=voidwalker_floor_range, spells=voidwalker_spells, spell_probabilities=voidwalker_spell_probabilities, initial_stats=voidwalker_initial_stats)

celestial_magisters_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 24,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 28,
    "Wisdom": 26,
    "Charisma": 20,
    "Element": "Celestial"
}

celestial_magisters_gear = ["Celestial Staff", "Magisterial Robes"]
celestial_magisters_loot_table = ["Celestial Essence", "Magisterial Shard", "Divine Codex"]
celestial_magisters_description = "The Celestial Magisters channel the radiant energies of the heavens within the Mage Tower, their staffs glowing with divine light. Draped in robes infused with celestial power, they command the forces of light with unparalleled grace."
celestial_magisters_floor_range = (42, 44)
celestial_magisters_spells = ["Divine Wrath", "Celestial Blessing"]
celestial_magisters_spell_probabilities = {"Divine Wrath": 0.7, "Celestial Blessing": 0.3}
celestial_magisters_initial_stats = celestial_magisters_stats.copy()
celestial_magisters = Monster("Celestial Magisters", celestial_magisters_stats, celestial_magisters_gear, celestial_magisters_loot_table, difficulty=8, description=celestial_magisters_description, floor_range=celestial_magisters_floor_range, spells=celestial_magisters_spells, spell_probabilities=celestial_magisters_spell_probabilities, initial_stats=celestial_magisters_initial_stats)

celestial_scribes_stats = {
    "HP": 160,
    "Damage": 40,
    "Defense": 35,
    "Magic Defense": 55,
    "Strength": 20,
    "Dexterity": 22,
    "Constitution": 28,
    "Intelligence": 26,
    "Wisdom": 28,
    "Charisma": 20,
    "Element": "Celestial"
}

celestial_scribes_gear = ["Celestial Quill", "Scribe's Robes"]
celestial_scribes_loot_table = ["Celestial Essence", "Scribe's Scroll", "Divine Tome"]
celestial_scribes_description = "The Celestial Scribes, scholars of the heavens, wander the halls of the Mage Tower, recording the celestial knowledge with divine precision. Adorned in robes glowing with celestial light, they uphold the sanctity of celestial wisdom with reverence."
celestial_scribes_floor_range = (42, 44)
celestial_scribes_spells = ["Divine Script", "Celestial Lore"]
celestial_scribes_spell_probabilities = {"Divine Script": 0.7, "Celestial Lore": 0.3}
celestial_scribes_initial_stats = celestial_scribes_stats.copy()
celestial_scribes = Monster("Celestial Scribes", celestial_scribes_stats, celestial_scribes_gear, celestial_scribes_loot_table, difficulty=8, description=celestial_scribes_description, floor_range=celestial_scribes_floor_range, spells=celestial_scribes_spells, spell_probabilities=celestial_scribes_spell_probabilities, initial_stats=celestial_scribes_initial_stats)

celestial_arcanologist_stats = {
    "HP": 170,
    "Damage": 45,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 22,
    "Dexterity": 24,
    "Constitution": 30,
    "Intelligence": 28,
    "Wisdom": 26,
    "Charisma": 20,
    "Element": "Celestial"
}

celestial_arcanologist_gear = ["Celestial Codex", "Arcane Garb"]
celestial_arcanologist_loot_table = ["Celestial Essence", "Arcanologist Shard", "Astral Tome"]
celestial_arcanologist_description = "The Celestial Arcanologists delve into the mysteries of the cosmos within the Mage Tower, their studies guided by celestial intuition. Clad in garments infused with celestial energies, they unravel the secrets of the arcane with celestial insight."
celestial_arcanologist_floor_range = (42, 44)
celestial_arcanologist_spells = ["Celestial Inquiry", "Astral Infusion"]
celestial_arcanologist_spell_probabilities = {"Celestial Inquiry": 0.7, "Astral Infusion": 0.3}
celestial_arcanologist_initial_stats = celestial_arcanologist_stats.copy()
celestial_arcanologist = Monster("Celestial Arcanologist", celestial_arcanologist_stats, celestial_arcanologist_gear, celestial_arcanologist_loot_table, difficulty=8, description=celestial_arcanologist_description, floor_range=celestial_arcanologist_floor_range, spells=celestial_arcanologist_spells, spell_probabilities=celestial_arcanologist_spell_probabilities, initial_stats=celestial_arcanologist_initial_stats)

mana_bound_wolf_stats = {
    "HP": 140,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 22,
    "Dexterity": 26,
    "Constitution": 28,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

mana_bound_wolf_gear = ["Mana Essence Fangs", "Bound Fur"]
mana_bound_wolf_loot_table = ["Arcane Essence", "Mana Fang", "Wolf Pelt"]
mana_bound_wolf_description = "The Mana-Bound Wolf prowls the corridors of the Mage Tower, its fur infused with arcane energies. With fangs dripping with mana essence, it hunts with primal instinct, guarding the tower's secrets with fierce loyalty."
mana_bound_wolf_floor_range = (42, 44)
mana_bound_wolf_spells = ["Mana Bite", "Arcane Howl"]
mana_bound_wolf_spell_probabilities = {"Mana Bite": 0.7, "Arcane Howl": 0.3}
mana_bound_wolf_initial_stats = mana_bound_wolf_stats.copy()
mana_bound_wolf = Monster("Mana-Bound Wolf", mana_bound_wolf_stats, mana_bound_wolf_gear, mana_bound_wolf_loot_table, difficulty=8, description=mana_bound_wolf_description, floor_range=mana_bound_wolf_floor_range, spells=mana_bound_wolf_spells, spell_probabilities=mana_bound_wolf_spell_probabilities, initial_stats=mana_bound_wolf_initial_stats)

mana_bound_bear_stats = {
    "HP": 180,
    "Damage": 60,
    "Defense": 35,
    "Magic Defense": 45,
    "Strength": 26,
    "Dexterity": 22,
    "Constitution": 32,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

mana_bound_bear_gear = ["Mana Essence Claws", "Bound Hide"]
mana_bound_bear_loot_table = ["Arcane Essence", "Mana Claw", "Bear Pelt"]
mana_bound_bear_description = "The Mana-Bound Bear roams the Mage Tower, its hide infused with mana energy. With claws shimmering with arcane power, it defends the tower's territory with unmatched strength, a guardian of the arcane wilderness."
mana_bound_bear_floor_range = (42, 44)
mana_bound_bear_spells = ["Mana Swipe", "Arcane Roar"]
mana_bound_bear_spell_probabilities = {"Mana Swipe": 0.7, "Arcane Roar": 0.3}
mana_bound_bear_initial_stats = mana_bound_bear_stats.copy()
mana_bound_bear = Monster("Mana-Bound Bear", mana_bound_bear_stats, mana_bound_bear_gear, mana_bound_bear_loot_table, difficulty=8, description=mana_bound_bear_description, floor_range=mana_bound_bear_floor_range, spells=mana_bound_bear_spells, spell_probabilities=mana_bound_bear_spell_probabilities, initial_stats=mana_bound_bear_initial_stats)

mana_bound_golem_stats = {
    "HP": 200,
    "Damage": 55,
    "Defense": 50,
    "Magic Defense": 50,
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 35,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Arcane"
}

mana_bound_golem_gear = ["Mana Core", "Bound Plates"]
mana_bound_golem_loot_table = ["Arcane Essence", "Mana Shard", "Golem Fragment"]
mana_bound_golem_description = "The Mana-Bound Golem, forged from arcane energies, stands sentinel within the Mage Tower. Powered by a mana core, and armored in bound plates, it executes its duties with mechanical precision, a silent guardian of the arcane halls."
mana_bound_golem_floor_range = (42, 44)
mana_bound_golem_spells = ["Mana Strike", "Arcane Barrier"]
mana_bound_golem_spell_probabilities = {"Mana Strike": 0.7, "Arcane Barrier": 0.3}
mana_bound_golem_initial_stats = mana_bound_golem_stats.copy()
mana_bound_golem = Monster("Mana-Bound Golem", mana_bound_golem_stats, mana_bound_golem_gear, mana_bound_golem_loot_table, difficulty=8, description=mana_bound_golem_description, floor_range=mana_bound_golem_floor_range, spells=mana_bound_golem_spells, spell_probabilities=mana_bound_golem_spell_probabilities, initial_stats=mana_bound_golem_initial_stats)

mana_bound_treant_stats = {
    "HP": 220,
    "Damage": 60,
    "Defense": 55,
    "Magic Defense": 55,
    "Strength": 32,
    "Dexterity": 20,
    "Constitution": 40,
    "Intelligence": 20,
    "Wisdom": 24,
    "Charisma": 18,
    "Element": "Arcane"
}

mana_bound_treant_gear = ["Mana Bark", "Bound Vines"]
mana_bound_treant_loot_table = ["Arcane Essence", "Mana Sap", "Treant Branch"]
mana_bound_treant_description = "The Mana-Bound Treant, an embodiment of the arcane forest, roams the Mage Tower's inner sanctum. With bark infused with mana essence and vines bound by arcane energy, it protects the tower's natural balance with ancient wisdom."
mana_bound_treant_floor_range = (42, 44)
mana_bound_treant_spells = ["Mana Slam", "Arcane Entanglement"]
mana_bound_treant_spell_probabilities = {"Mana Slam": 0.7, "Arcane Entanglement": 0.3}
mana_bound_treant_initial_stats = mana_bound_treant_stats.copy()
mana_bound_treant = Monster("Mana-Bound Treant", mana_bound_treant_stats, mana_bound_treant_gear, mana_bound_treant_loot_table, difficulty=8, description=mana_bound_treant_description, floor_range=mana_bound_treant_floor_range, spells=mana_bound_treant_spells, spell_probabilities=mana_bound_treant_spell_probabilities, initial_stats=mana_bound_treant_initial_stats)
