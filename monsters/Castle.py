from monsters.bestiary import Monster

werewolf_stats = {
    "HP": 260,  # Define HP attribute for Werewolf
    "Damage": 80,  # Define damage attribute for Werewolf
    "Defense": 45,  # Define Defense stat vs attack stat
    "Magic Defense": 40,  # Define magic defense vs spells
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 26,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"  # Define elemental attribute of the Werewolf's attack
}
werewolf_gear = ["Razor-sharp Claws", "Fur Coat"]
werewolf_loot_table = {"Gold":(1, 10), "Longsword":(1,1)}
werewolf_description = "Werewolves are fearsome creatures cursed with lycanthropy, transforming into savage beasts under the light of the full moon. In their wolf form, they possess incredible strength and agility, tearing through their enemies with razor-sharp claws and fangs. Despite their ferocity, some retain a semblance of their human consciousness, tormented by the atrocities they commit while in their bestial state."
werewolf_floor_range = (1,5)
werewolf_spells = []
werewolf_spell_probabilities = {}
werewolf_initial_stats = werewolf_stats.copy() # Make a copy of the initial stats
werewolf = Monster("Werewolf", werewolf_stats, werewolf_gear, werewolf_loot_table, difficulty=50, description=werewolf_description, floor_range=werewolf_floor_range, spells=werewolf_spells, spell_probabilities=werewolf_spell_probabilities, initial_stats=werewolf_initial_stats)

werebear_stats = {
    "HP": 300,
    "Damage": 60,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 30,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 18,
    "Element": "None"
}
werebear_gear = ["Clawed Gauntlets", "Fur Armor"]
werebear_loot_table = ["Gold", "Bear Claw", "Werebear Pelt"]
werebear_description = "Werebears are fearsome creatures that combine the strength and ferocity of bears with the cunning and agility of humans. They are known to roam the wilderness in search of prey, using their powerful claws and teeth to tear through anything in their path."
werebear_floor_range = (60, 120)
werebear_spells = []
werebear_spell_probabilities = {}
werebear_initial_stats = werebear_stats.copy()
werebear = Monster("Werebear", werebear_stats, werebear_gear, werebear_loot_table, difficulty=60, description=werebear_description, floor_range=werebear_floor_range, spells=werebear_spells, spell_probabilities=werebear_spell_probabilities, initial_stats=werebear_initial_stats)

vampire_grunt_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 30,
    "Strength": 25,
    "Dexterity": 30,
    "Constitution": 22,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "Darkness"
}
vampire_grunt_gear = ["Vampiric Claws", "Dark Cloak"]
vampire_grunt_loot_table = ["Gold", "Vampire Fang", "Dark Cloak"]
vampire_grunt_description = "Vampire Grunts are the foot soldiers of the undead, serving their vampire masters with unwavering loyalty. With their vampiric claws and dark cloaks, they strike fear into the hearts of their enemies."
vampire_grunt_floor_range = (60, 120)
vampire_grunt_spells = ["Shadow Step", "Life Drain", "Dark Mist"]
vampire_grunt_spell_probabilities = {"Shadow Step": 0.4, "Life Drain": 0.3, "Dark Mist": 0.3}
vampire_grunt_initial_stats = vampire_grunt_stats.copy()
vampire_grunt = Monster("Vampire Grunt", vampire_grunt_stats, vampire_grunt_gear, vampire_grunt_loot_table, difficulty=60, description=vampire_grunt_description, floor_range=vampire_grunt_floor_range, spells=vampire_grunt_spells, spell_probabilities=vampire_grunt_spell_probabilities, initial_stats=vampire_grunt_initial_stats)

vrykolakas_stats = {
    "HP": 250,
    "Damage": 50,
    "Defense": 30,
    "Magic Defense": 40,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 28,
    "Intelligence": 30,
    "Wisdom": 32,
    "Charisma": 38,
    "Element": "Darkness"
}
vrykolakas_gear = ["Ethereal Fangs", "Shadow Cloak"]
vrykolakas_loot_table = ["Gold", "Ectoplasm", "Vampire Dust"]
vrykolakas_description = "Vrykolakas are ancient undead creatures, cursed to roam the night in search of blood. With their ethereal fangs and shadow cloak, they strike fear into the hearts of mortals, feeding on their life force to sustain their cursed existence."
vrykolakas_floor_range = (80, 160)
vrykolakas_spells = ["Shadow Bolt", "Soul Drain", "Ethereal Shift"]
vrykolakas_spell_probabilities = {"Shadow Bolt": 0.4, "Soul Drain": 0.3, "Ethereal Shift": 0.3}
vrykolakas_initial_stats = vrykolakas_stats.copy()
vrykolakas = Monster("Vrykolakas", vrykolakas_stats, vrykolakas_gear, vrykolakas_loot_table, difficulty=80, description=vrykolakas_description, floor_range=vrykolakas_floor_range, spells=vrykolakas_spells, spell_probabilities=vrykolakas_spell_probabilities, initial_stats=vrykolakas_initial_stats)

upyr_stats = {
    "HP": 400,
    "Damage": 85,
    "Defense": 65,
    "Magic Defense": 75,
    "Strength": 60,
    "Dexterity": 70,
    "Constitution": 62,
    "Intelligence": 65,
    "Wisdom": 68,
    "Charisma": 72,
    "Element": "Darkness"
}
upyr_gear = ["Vampiric Claws", "Nightshade Cloak"]
upyr_loot_table = ["Gold", "Vampire Fang", "Nightshade Essence"]
upyr_description = "Upyrs are powerful and ancient vampires, wielding dark magic and preying on the souls of the living. With their vampiric claws and nightshade cloak, they strike fear into the hearts of mortals, draining them of their life essence."
upyr_floor_range = (80, 160)
upyr_spells = ["Dark Pact", "Vampiric Drain", "Shadow Step"]
upyr_spell_probabilities = {"Dark Pact": 0.4, "Vampiric Drain": 0.3, "Shadow Step": 0.3}
upyr_initial_stats = upyr_stats.copy()
upyr = Monster("Upyr", upyr_stats, upyr_gear, upyr_loot_table, difficulty=80, description=upyr_description, floor_range=upyr_floor_range, spells=upyr_spells, spell_probabilities=upyr_spell_probabilities, initial_stats=upyr_initial_stats)

spectral_knight_stats = {
    "HP": 100,  # Define HP attribute for Spectral Knight
    "Damage": 30,  # Define damage attribute for Spectral Knight
    "Defense": 20,  # Define Defense stat vs attack stat for Spectral Knight
    "Magic Defense": 30,  # Define magic defense vs spells for Spectral Knight
    "Strength": 15,
    "Dexterity": 10,
    "Constitution": 15,
    "Intelligence": 8,
    "Wisdom": 12,
    "Charisma": 10,
    "Element": "Shadow"  # Define elemental attribute of the Spectral Knight's attack
}

spectral_knight_gear = ["Spectral Blade", "Ghostly Armor"]
spectral_knight_loot_table = ["Gold", "Health Elixir", "Rare Rune"]
spectral_knight_description = "Spectral Knights are ancient warriors trapped between realms, wielding ghostly weapons and armor. Their spectral nature grants them resistance against physical attacks, while their enchanted gear makes them formidable foes in battle."
spectral_knight_floor_range = (3, 5)  # Spectral Knights appear on floors 3 to 5
spectral_knight_spells = ["Ethereal Slash", "Soul Drain"]
spectral_knight_spell_probabilities = {spectral_knight_spells[0]: 0.7,spectral_knight_spells[1]: 0.3}
spectral_knight_initial_stats = spectral_knight_stats.copy() 
spectral_knight = Monster("Spectral Knight", spectral_knight_stats, spectral_knight_gear, spectral_knight_loot_table, difficulty=3, description=spectral_knight_description, floor_range=spectral_knight_floor_range, spells=spectral_knight_spells, spell_probabilities=spectral_knight_spell_probabilities, initial_stats=spectral_knight_initial_stats)

gargoyle_sentinel_stats = {
    "HP": 120,  # Define HP attribute for Gargoyle Sentinel
    "Damage": 25,  # Define damage attribute for Gargoyle Sentinel
    "Defense": 25,  # Define Defense stat vs attack stat for Gargoyle Sentinel
    "Magic Defense": 25,  # Define magic defense vs spells for Gargoyle Sentinel
    "Strength": 20,
    "Dexterity": 10,
    "Constitution": 20,
    "Intelligence": 6,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "Earth"  # Define elemental attribute of the Gargoyle Sentinel's attack
}
gargoyle_sentinel_gear = ["Stone Hammer", "Stone Plate Armor"]
gargoyle_sentinel_loot_table = ["Gold", "Ancient Relic", "Large Crystal"]
gargoyle_sentinel_description = "Gargoyle Sentinels are ancient guardians sculpted from living stone. With immense strength and durability, they stand watch over long-forgotten ruins, ready to crush any intruders foolish enough to disturb their slumber."
gargoyle_sentinel_floor_range = (6, 8)  # Gargoyle Sentinels appear on floors 6 to 8
gargoyle_sentinel_spells = ["Stone Skin", "Earthquake"]
gargoyle_sentinel_spell_probabilities = {gargoyle_sentinel_spells[0]: 0.6, gargoyle_sentinel_spells[1]: 0.4}  # Probability of each spell being cast by the Gargoyle Sentinel
gargoyle_sentinel_initial_stats = gargoyle_sentinel_stats.copy()  # Make a copy of the initial stats
gargoyle_sentinel = Monster("Gargoyle Sentinel", gargoyle_sentinel_stats, gargoyle_sentinel_gear, gargoyle_sentinel_loot_table, difficulty=4, description=gargoyle_sentinel_description, floor_range=gargoyle_sentinel_floor_range, spells=gargoyle_sentinel_spells, spell_probabilities=gargoyle_sentinel_spell_probabilities, initial_stats=gargoyle_sentinel_initial_stats)

blacksteel_brute_stats = {
    "HP": 220,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 35,
    "Strength": 30,
    "Dexterity": 15,
    "Constitution": 40,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "None"
}

blacksteel_brute_gear = ["Greatsword of Darkness", "Blacksteel Armor"]
blacksteel_brute_loot_table = ["Blacksteel Shard", "Dark Essence", "Brutal Trophy"]
blacksteel_brute_description = "The Blacksteel Brute is a fearsome adversary, wielding a massive greatsword forged from dark steel. Its imposing figure and relentless strength make it a formidable opponent in battle."
blacksteel_brute_floor_range = (42, 45)
blacksteel_brute_initial_stats = blacksteel_brute_stats.copy()
blacksteel_brute = Monster("Blacksteel Brute", blacksteel_brute_stats, blacksteel_brute_gear, blacksteel_brute_loot_table, difficulty=10, description=blacksteel_brute_description, floor_range=blacksteel_brute_floor_range, initial_stats=blacksteel_brute_initial_stats)

ghostly_guardsman_stats = {
    "HP": 100,  # Define HP attribute for Ghostly Guardsman
    "Damage": 25,  # Define damage attribute for Ghostly Guardsman
    "Defense": 20,  # Define Defense stat vs attack stat for Ghostly Guardsman
    "Magic Defense": 25,  # Define magic defense vs spells for Ghostly Guardsman
    "Strength": 15,
    "Dexterity": 12,
    "Constitution": 14,
    "Intelligence": 10,
    "Wisdom": 8,
    "Charisma": 6,
    "Element": "Spirit"  # Define elemental attribute of the Ghostly Guardsman's attack
}

ghostly_guardsman_gear = ["Spectral Sword", "Ghostly Armor"]
ghostly_guardsman_loot_table = ["Silver Coin", "Ectoplasm", "Haunted Relic"]
ghostly_guardsman_description = "The Ghostly Guardsman is a spectral entity bound to guard ancient ruins or cursed tombs. Once a loyal protector, now a restless spirit, it wanders eternally, seeking to deter intruders with its spectral powers."
ghostly_guardsman_floor_range = (12, 15)  # Ghostly Guardsman appears on floors 12 to 15
ghostly_guardsman_spells = ["Phantom Strike", "Ethereal Shield"]
ghostly_guardsman_spell_probabilities = {ghostly_guardsman_spells[0]: 0.6, ghostly_guardsman_spells[1]: 0.4}  # Probability of each spell being cast by the Ghostly Guardsman
ghostly_guardsman_initial_stats = ghostly_guardsman_stats.copy()  # Make a copy of the initial stats
ghostly_guardsman = Monster("Ghostly Guardsman", ghostly_guardsman_stats, ghostly_guardsman_gear, ghostly_guardsman_loot_table, difficulty=6, description=ghostly_guardsman_description, floor_range=ghostly_guardsman_floor_range, spells=ghostly_guardsman_spells, spell_probabilities=ghostly_guardsman_spell_probabilities, initial_stats=ghostly_guardsman_initial_stats)

haunter_herald_stats = {
    "HP": 120,  # Define HP attribute for Haunter Herald
    "Damage": 40,  # Define damage attribute for Haunter Herald
    "Defense": 25,  # Define Defense stat vs attack stat for Haunter Herald
    "Magic Defense": 35,  # Define magic defense vs spells for Haunter Herald
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 16,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Shadow"  # Define elemental attribute of the Haunter Herald's attack
}

haunter_herald_gear = ["Spectral Scythe", "Cloak of the Abyss"]
haunter_herald_loot_table = ["Dark Coin", "Soul Essence", "Cursed Scroll"]
haunter_herald_description = "The Haunter Herald is a sinister apparition, wielding dark powers and commanding legions of shadows. It appears as a harbinger of doom, foretelling calamity and despair wherever it roams."
haunter_herald_floor_range = (16, 18)  # Haunter Herald appears on floors 16 to 18
haunter_herald_spells = ["Shadow Nova", "Abyssal Grasp"]
haunter_herald_spell_probabilities = {haunter_herald_spells[0]: 0.7, haunter_herald_spells[1]: 0.3}  # Probability of each spell being cast by the Haunter Herald
haunter_herald_initial_stats = haunter_herald_stats.copy()  # Make a copy of the initial stats
haunter_herald = Monster("Haunter Herald", haunter_herald_stats, haunter_herald_gear, haunter_herald_loot_table, difficulty=7, description=haunter_herald_description, floor_range=haunter_herald_floor_range, spells=haunter_herald_spells, spell_probabilities=haunter_herald_spell_probabilities, initial_stats=haunter_herald_initial_stats)

nightshade_stalker_stats = {
    "HP": 90,  # Define HP attribute for Nightshade Stalker
    "Damage": 30,  # Define damage attribute for Nightshade Stalker
    "Defense": 18,  # Define Defense stat vs attack stat for Nightshade Stalker
    "Magic Defense": 25,  # Define magic defense vs spells for Nightshade Stalker
    "Strength": 16,
    "Dexterity": 20,
    "Constitution": 12,
    "Intelligence": 14,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "Poison"  # Define elemental attribute of the Nightshade Stalker's attack
}

nightshade_stalker_gear = ["Toxic Claws", "Venomous Cloak"]
nightshade_stalker_loot_table = ["Toxic Fang", "Poisonous Spore", "Nightshade Extract"]
nightshade_stalker_description = "The Nightshade Stalker is a deadly predator lurking in the shadows, waiting to ambush its prey. With razor-sharp claws coated in venom, it strikes swiftly and silently, leaving behind only darkness and poison."
nightshade_stalker_floor_range = (19, 21)  # Nightshade Stalker appears on floors 19 to 21
nightshade_stalker_spells = ["Toxic Cloud", "Shadowstep"]
nightshade_stalker_spell_probabilities = {nightshade_stalker_spells[0]: 0.6, nightshade_stalker_spells[1]: 0.4}  # Probability of each spell being cast by the Nightshade Stalker
nightshade_stalker_initial_stats = nightshade_stalker_stats.copy()  # Make a copy of the initial stats
nightshade_stalker = Monster("Nightshade Stalker", nightshade_stalker_stats, nightshade_stalker_gear, nightshade_stalker_loot_table, difficulty=6, description=nightshade_stalker_description, floor_range=nightshade_stalker_floor_range, spells=nightshade_stalker_spells, spell_probabilities=nightshade_stalker_spell_probabilities, initial_stats=nightshade_stalker_initial_stats)

castle_ghoul_stats = {
    "HP": 150,  # Define HP attribute for Castle Ghoul
    "Damage": 45,  # Define damage attribute for Castle Ghoul
    "Defense": 30,  # Define Defense stat vs attack stat for Castle Ghoul
    "Magic Defense": 40,  # Define magic defense vs spells for Castle Ghoul
    "Strength": 22,
    "Dexterity": 16,
    "Constitution": 20,
    "Intelligence": 14,
    "Wisdom": 10,
    "Charisma": 6,
    "Element": "Necrotic"  # Define elemental attribute of the Castle Ghoul's attack
}

castle_ghoul_gear = ["Cursed Blade", "Tattered Shroud"]
castle_ghoul_loot_table = ["Spectral Coin", "Ghastly Essence", "Cursed Amulet"]
castle_ghoul_description = "The Castle Ghoul is an undead monstrosity haunting the ruins of an ancient fortress. Its eerie presence chills the air, and its ghastly visage strikes fear into the hearts of all who dare to trespass into its domain."
castle_ghoul_floor_range = (22, 25)  # Castle Ghoul appears on floors 22 to 25
castle_ghoul_spells = ["Soul Drain", "Necrotic Blast"]
castle_ghoul_spell_probabilities = {castle_ghoul_spells[0]: 0.7, castle_ghoul_spells[1]: 0.3}  # Probability of each spell being cast by the Castle Ghoul
castle_ghoul_initial_stats = castle_ghoul_stats.copy()  # Make a copy of the initial stats

castle_ghoul = Monster("Castle Ghoul", castle_ghoul_stats, castle_ghoul_gear, castle_ghoul_loot_table, difficulty=7, description=castle_ghoul_description, floor_range=castle_ghoul_floor_range, spells=castle_ghoul_spells, spell_probabilities=castle_ghoul_spell_probabilities, initial_stats=castle_ghoul_initial_stats)

apparition_archer_stats = {
    "HP": 110,  # Define HP attribute for Apparition Archer
    "Damage": 35,  # Define damage attribute for Apparition Archer
    "Defense": 20,  # Define Defense stat vs attack stat for Apparition Archer
    "Magic Defense": 25,  # Define magic defense vs spells for Apparition Archer
    "Strength": 14,
    "Dexterity": 22,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Spectral"  # Define elemental attribute of the Apparition Archer's attack
}

apparition_archer_gear = ["Phantom Bow", "Ghostly Quiver"]
apparition_archer_loot_table = ["Spectral Arrow", "Ethereal Bowstring", "Apparition Shard"]
apparition_archer_description = "The Apparition Archer is a ghostly marksman, haunting the ruins with its spectral bow and arrows. Its shots strike with eerie precision, piercing through both flesh and spirit."
apparition_archer_floor_range = (26, 28)  # Apparition Archer appears on floors 26 to 28
apparition_archer_spells = ["Phantom Shot", "Spectral Veil"]
apparition_archer_spell_probabilities = {apparition_archer_spells[0]: 0.6, apparition_archer_spells[1]: 0.4}  # Probability of each spell being cast by the Apparition Archer
apparition_archer_initial_stats = apparition_archer_stats.copy()  # Make a copy of the initial stats
apparition_archer = Monster("Apparition Archer", apparition_archer_stats, apparition_archer_gear, apparition_archer_loot_table, difficulty=6, description=apparition_archer_description, floor_range=apparition_archer_floor_range, spells=apparition_archer_spells, spell_probabilities=apparition_archer_spell_probabilities, initial_stats=apparition_archer_initial_stats)

cursed_captain_stats = {
    "HP": 130,  # Define HP attribute for Cursed Captain
    "Damage": 40,  # Define damage attribute for Cursed Captain
    "Defense": 25,  # Define Defense stat vs attack stat for Cursed Captain
    "Magic Defense": 30,  # Define magic defense vs spells for Cursed Captain
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 22,
    "Intelligence": 16,
    "Wisdom": 14,
    "Charisma": 12,
    "Element": "Undead"  # Define elemental attribute of the Cursed Captain's attack
}

cursed_captain_gear = ["Spectral Cutlass", "Ghostly Tricorn Hat"]
cursed_captain_loot_table = ["Haunted Doubloon", "Cursed Compass", "Spectral Spyglass"]
cursed_captain_description = "The Cursed Captain is the ghostly commander of a long-lost pirate ship, forever cursed to roam the seas of the afterlife. With his spectral crew, he pillages and plunders any unfortunate souls who dare to cross his path."
cursed_captain_floor_range = (30, 35)  # Cursed Captain appears on floors 30 to 35
cursed_captain_spells = ["Spectral Cannonade", "Dreaded Curse"]
cursed_captain_spell_probabilities = {cursed_captain_spells[0]: 0.7, cursed_captain_spells[1]: 0.3}  # Probability of each spell being cast by the Cursed Captain
cursed_captain_initial_stats = cursed_captain_stats.copy()  # Make a copy of the initial stats

cursed_captain = Monster("Cursed Captain", cursed_captain_stats, cursed_captain_gear, cursed_captain_loot_table, difficulty=7, description=cursed_captain_description, floor_range=cursed_captain_floor_range, spells=cursed_captain_spells, spell_probabilities=cursed_captain_spell_probabilities, initial_stats=cursed_captain_initial_stats)

phalanx_stats = {
    "HP": 160,  # Define HP attribute for Phalanx
    "Damage": 50,  # Define damage attribute for Phalanx
    "Defense": 35,  # Define Defense stat vs attack stat for Phalanx
    "Magic Defense": 40,  # Define magic defense vs spells for Phalanx
    "Strength": 25,
    "Dexterity": 18,
    "Constitution": 28,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Steel"  # Define elemental attribute of the Phalanx's attack
}

phalanx_gear = ["Adamantine Spear", "Tower Shield"]
phalanx_loot_table = ["Forged Emblem", "Phalanx Helm", "Ancient Pike"]
phalanx_description = "The Phalanx is an ancient golem, crafted from enchanted metal and bound to protect the castle's inner sanctum. Its impenetrable shield and spear make it an unyielding defender against any who would dare to breach the fortress walls."
phalanx_floor_range = (25, 30)  # Phalanx appears on floors 25 to 30
phalanx_spells = ["Iron Wall", "Steel Strike"]
phalanx_spell_probabilities = {phalanx_spells[0]: 0.6, phalanx_spells[1]: 0.4}  # Probability of each spell being cast by the Phalanx
phalanx_initial_stats = phalanx_stats.copy()  # Make a copy of the initial stats
phalanx = Monster("Phalanx", phalanx_stats, phalanx_gear, phalanx_loot_table, difficulty=8, description=phalanx_description, floor_range=phalanx_floor_range, spells=phalanx_spells, spell_probabilities=phalanx_spell_probabilities, initial_stats=phalanx_initial_stats)

sinister_squire_stats = {
    "HP": 100,  # Define HP attribute for Sinister Squire
    "Damage": 35,  # Define damage attribute for Sinister Squire
    "Defense": 20,  # Define Defense stat vs attack stat for Sinister Squire
    "Magic Defense": 25,  # Define magic defense vs spells for Sinister Squire
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 16,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Dark"  # Define elemental attribute of the Sinister Squire's attack
}

sinister_squire_gear = ["Cursed Lance", "Shadow Armor"]
sinister_squire_loot_table = ["Darkened Crest", "Sinister Gauntlet", "Shadowy Banner"]
sinister_squire_description = "The Sinister Squire is a loyal servant of the castle's dark lord, wielding a cursed lance and clad in shadowy armor. Silent and deadly, it patrols the corridors, ready to strike down any intruders in the name of its master."
sinister_squire_floor_range = (20, 25)  # Sinister Squire appears on floors 20 to 25
sinister_squire_spells = ["Shadow Strike", "Dark Pact"]
sinister_squire_spell_probabilities = {sinister_squire_spells[0]: 0.6, sinister_squire_spells[1]: 0.4}  # Probability of each spell being cast by the Sinister Squire
sinister_squire_initial_stats = sinister_squire_stats.copy()  # Make a copy of the initial stats

sinister_squire = Monster("Sinister Squire", sinister_squire_stats, sinister_squire_gear, sinister_squire_loot_table, difficulty=6, description=sinister_squire_description, floor_range=sinister_squire_floor_range, spells=sinister_squire_spells, spell_probabilities=sinister_squire_spell_probabilities, initial_stats=sinister_squire_initial_stats)

inquisitor_stats = {
    "HP": 140,  # Define HP attribute for Inquisitor
    "Damage": 45,  # Define damage attribute for Inquisitor
    "Defense": 30,  # Define Defense stat vs attack stat for Inquisitor
    "Magic Defense": 35,  # Define magic defense vs spells for Inquisitor
    "Strength": 20,
    "Dexterity": 22,
    "Constitution": 25,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Dark"  # Define elemental attribute of the Inquisitor's attack
}

inquisitor_gear = ["Judgement Halberd", "Inquisitor's Robes"]
inquisitor_loot_table = ["Purified Tome", "Inquisition Seal", "Dark Relic"]
inquisitor_description = "The Inquisitor is a relentless hunter of heretics and traitors, wielding holy power and dark magic in equal measure. Bound by oath to root out evil, it will stop at nothing to enforce its twisted sense of justice."
inquisitor_floor_range = (28, 32)  # Inquisitor appears on floors 28 to 32
inquisitor_spells = ["Divine Wrath", "Shadow Bolt"]
inquisitor_spell_probabilities = {inquisitor_spells[0]: 0.6, inquisitor_spells[1]: 0.4}  # Probability of each spell being cast by the Inquisitor
inquisitor_initial_stats = inquisitor_stats.copy()  # Make a copy of the initial stats
inquisitor = Monster("Inquisitor", inquisitor_stats, inquisitor_gear, inquisitor_loot_table, difficulty=7, description=inquisitor_description, floor_range=inquisitor_floor_range, spells=inquisitor_spells, spell_probabilities=inquisitor_spell_probabilities, initial_stats=inquisitor_initial_stats)

ironclad_sentinel_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 25,
    "Dexterity": 12,
    "Constitution": 30,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "None"
}

ironclad_sentinel_gear = ["Iron Tower Shield", "Heavy Plate Armor"]
ironclad_sentinel_loot_table = ["Ironclad Badge", "Fortress Key", "Reinforced Gauntlet"]
ironclad_sentinel_description = "The Ironclad Sentinel is a formidable guardian of the castle walls, clad in impenetrable armor and wielding a massive tower shield. Its imposing presence strikes fear into the hearts of any who dare to challenge its defense."
ironclad_sentinel_floor_range = (35, 40)
ironclad_sentinel_spells = []
ironclad_sentinel_spell_probabilities = {}
ironclad_sentinel_initial_stats = ironclad_sentinel_stats.copy()
ironclad_sentinel = Monster("Ironclad Sentinel", ironclad_sentinel_stats, ironclad_sentinel_gear, ironclad_sentinel_loot_table, difficulty=8, description=ironclad_sentinel_description, floor_range=ironclad_sentinel_floor_range, spells=ironclad_sentinel_spells, spell_probabilities=ironclad_sentinel_spell_probabilities, initial_stats=ironclad_sentinel_initial_stats)

stoneguard_knight_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 25,
    "Strength": 22,
    "Dexterity": 15,
    "Constitution": 28,
    "Intelligence": 12,
    "Wisdom": 18,
    "Charisma": 10,
    "Element": "None"
}

stoneguard_knight_gear = ["Stone Sword", "Tower Shield"]
stoneguard_knight_loot_table = ["Knight's Crest", "Stoneguard Helm", "Guardian Shard"]
stoneguard_knight_description = "The Stoneguard Knight is a stalwart defender, sworn to protect the castle walls, wielding a sturdy sword and shield. Its unwavering loyalty and steadfast resolve make it a formidable opponent to any who seek to breach the fortress."
stoneguard_knight_floor_range = (30, 35)
stoneguard_knight_spells = []
stoneguard_knight_spell_probabilities = {}
stoneguard_knight_initial_stats = stoneguard_knight_stats.copy()
stoneguard_knight = Monster("Stoneguard Knight", stoneguard_knight_stats, stoneguard_knight_gear, stoneguard_knight_loot_table, difficulty=7, description=stoneguard_knight_description, floor_range=stoneguard_knight_floor_range, spells=stoneguard_knight_spells, spell_probabilities=stoneguard_knight_spell_probabilities, initial_stats=stoneguard_knight_initial_stats)

castle_crusader_stats = {
    "HP": 200,
    "Damage": 55,
    "Defense": 45,
    "Magic Defense": 30,
    "Strength": 28,
    "Dexterity": 18,
    "Constitution": 35,
    "Intelligence": 14,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "None"
}

castle_crusader_gear = ["Holy Longsword", "Crusader Plate Armor"]
castle_crusader_loot_table = ["Crusader's Medallion", "Divine Tome", "Blessed Relic"]
castle_crusader_description = "The Castle Crusader is a valiant champion of righteousness, sworn to protect the castle from all manner of evil. With divine fervor and unyielding resolve, it leads the charge against the forces of darkness."
castle_crusader_floor_range = (40, 45)
castle_crusader_spells = []
castle_crusader_spell_probabilities = {}
castle_crusader_initial_stats = castle_crusader_stats.copy()
castle_crusader = Monster("Castle Crusader", castle_crusader_stats, castle_crusader_gear, castle_crusader_loot_table, difficulty=9, description=castle_crusader_description, floor_range=castle_crusader_floor_range, spells=castle_crusader_spells, spell_probabilities=castle_crusader_spell_probabilities, initial_stats=castle_crusader_initial_stats)

blacksteel_brute_stats = {
    "HP": 220,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 35,
    "Strength": 30,
    "Dexterity": 15,
    "Constitution": 40,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "None"
}

blacksteel_brute_gear = ["Greatsword of Darkness", "Blacksteel Armor"]
blacksteel_brute_loot_table = ["Blacksteel Shard", "Dark Essence", "Brutal Trophy"]
blacksteel_brute_description = "The Blacksteel Brute is a fearsome adversary, wielding a massive greatsword forged from dark steel. Its imposing figure and relentless strength make it a formidable opponent in battle."
blacksteel_brute_floor_range = (42, 45)
blacksteel_brute_spells = []
blacksteel_brute_spell_probabilities = {}
blacksteel_brute_initial_stats = blacksteel_brute_stats.copy()
blacksteel_brute = Monster("Blacksteel Brute", blacksteel_brute_stats, blacksteel_brute_gear, blacksteel_brute_loot_table, difficulty=10, description=blacksteel_brute_description, floor_range=blacksteel_brute_floor_range, spells=blacksteel_brute_spells, spell_probabilities=blacksteel_brute_spell_probabilities, initial_stats=blacksteel_brute_initial_stats)

armored_arbiter_stats = {
    "HP": 190,
    "Damage": 55,
    "Defense": 45,
    "Magic Defense": 40,
    "Strength": 28,
    "Dexterity": 20,
    "Constitution": 35,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "None"
}

armored_arbiter_gear = ["Judgement Blade", "Arbiter's Plate"]
armored_arbiter_loot_table = ["Arbiter's Insignia", "Divine Scroll", "Golden Scales"]
armored_arbiter_description = "The Armored Arbiter is a righteous enforcer, wielding a mighty blade and clad in impenetrable armor. Its unwavering sense of justice and divine protection make it a formidable foe for any who oppose it."
armored_arbiter_floor_range = (38, 40)
armored_arbiter_spells = []
armored_arbiter_spell_probabilities = {}
armored_arbiter_initial_stats = armored_arbiter_stats.copy()
armored_arbiter = Monster("Armored Arbiter", armored_arbiter_stats, armored_arbiter_gear, armored_arbiter_loot_table, difficulty=9, description=armored_arbiter_description, floor_range=armored_arbiter_floor_range, spells=armored_arbiter_spells, spell_probabilities=armored_arbiter_spell_probabilities, initial_stats=armored_arbiter_initial_stats)

knightly_bannerman_stats = {
    "HP": 170,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 25,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 14,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "None"
}

knightly_bannerman_gear = ["Banner Lance", "Bannerman's Armor"]
knightly_bannerman_loot_table = ["Bannerman's Pennant", "Royal Crest", "Chivalrous Medal"]
knightly_bannerman_description = "The Knightly Bannerman is a stalwart defender of the castle, wielding a lance emblazoned with the kingdom's colors. With unwavering loyalty and courage, it leads the charge against the enemy forces."
knightly_bannerman_floor_range = (36, 38)
knightly_bannerman_spells = []
knightly_bannerman_spell_probabilities = {}
knightly_bannerman_initial_stats = knightly_bannerman_stats.copy()
knightly_bannerman = Monster("Knightly Bannerman", knightly_bannerman_stats, knightly_bannerman_gear, knightly_bannerman_loot_table, difficulty=8, description=knightly_bannerman_description, floor_range=knightly_bannerman_floor_range, spells=knightly_bannerman_spells, spell_probabilities=knightly_bannerman_spell_probabilities, initial_stats=knightly_bannerman_initial_stats)

ironbound_infantry_stats = {
    "HP": 150,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 20,
    "Dexterity": 18,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "None"
}

ironbound_infantry_gear = ["Iron Spear", "Ironbound Armor"]
ironbound_infantry_loot_table = ["Ironbound Insignia", "Battle Standard", "Rusty Halberd"]
ironbound_infantry_description = "The Ironbound Infantry is a disciplined soldier, armed with a sturdy spear and protected by ironbound armor. Trained to withstand the toughest of battles, it serves as the backbone of the castle's defenses."
ironbound_infantry_floor_range = (34, 36)
ironbound_infantry_spells = []
ironbound_infantry_spell_probabilities = {}
ironbound_infantry_initial_stats = ironbound_infantry_stats.copy()
ironbound_infantry = Monster("Ironbound Infantry", ironbound_infantry_stats, ironbound_infantry_gear, ironbound_infantry_loot_table, difficulty=7, description=ironbound_infantry_description, floor_range=ironbound_infantry_floor_range, spells=ironbound_infantry_spells, spell_probabilities=ironbound_infantry_spell_probabilities, initial_stats=ironbound_infantry_initial_stats)

citadel_champion_stats = {
    "HP": 210,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 22,
    "Constitution": 35,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 18,
    "Element": "None"
}

citadel_champion_gear = ["Champion's Blade", "Citadel Armor"]
citadel_champion_loot_table = ["Champion's Crest", "Heroic Medallion", "Valor Token"]
citadel_champion_description = "The Citadel Champion is an elite warrior, renowned for its prowess in battle and unmatched valor. With a mighty blade in hand and wearing formidable armor, it stands as a beacon of hope in the face of adversity."
citadel_champion_floor_range = (44, 46)
citadel_champion_spells = []
citadel_champion_spell_probabilities = {}
citadel_champion_initial_stats = citadel_champion_stats.copy()
citadel_champion = Monster("Citadel Champion", citadel_champion_stats, citadel_champion_gear, citadel_champion_loot_table, difficulty=10, description=citadel_champion_description, floor_range=citadel_champion_floor_range, spells=citadel_champion_spells, spell_probabilities=citadel_champion_spell_probabilities, initial_stats=citadel_champion_initial_stats)

citadel_crusader_stats = {
    "HP": 220,
    "Damage": 65,
    "Defense": 55,
    "Magic Defense": 45,
    "Strength": 32,
    "Dexterity": 25,
    "Constitution": 40,
    "Intelligence": 18,
    "Wisdom": 22,
    "Charisma": 20,
    "Element": "None"
}

citadel_crusader_gear = ["Crusader's Greatsword", "Crusader's Plate"]
citadel_crusader_loot_table = ["Crusader's Insignia", "Divine Relic", "Holy Grail"]
citadel_crusader_description = "The Citadel Crusader is the epitome of knightly virtue, wielding a massive greatsword and adorned in sacred plate armor. With unwavering faith and unyielding determination, it smites all who threaten the castle's sanctity."
citadel_crusader_floor_range = (48, 50)
citadel_crusader_spells = []
citadel_crusader_spell_probabilities = {}
citadel_crusader_initial_stats = citadel_crusader_stats.copy()
citadel_crusader = Monster("Citadel Crusader", citadel_crusader_stats, citadel_crusader_gear, citadel_crusader_loot_table, difficulty=11, description=citadel_crusader_description, floor_range=citadel_crusader_floor_range, spells=citadel_crusader_spells, spell_probabilities=citadel_crusader_spell_probabilities, initial_stats=citadel_crusader_initial_stats)

castle_conscript_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "None"
}

castle_conscript_gear = ["Castle Pike", "Conscript's Armor"]
castle_conscript_loot_table = ["Conscript's Badge", "Battle Standard", "Bronze Coin"]
castle_conscript_description = "The Castle Conscript is a trained soldier, armed with a sturdy pike and wearing chainmail armor. Though lacking in experience, its loyalty to the castle and willingness to fight make it a valuable asset in times of war."
castle_conscript_floor_range = (32, 34)
castle_conscript_spells = []
castle_conscript_spell_probabilities = {}
castle_conscript_initial_stats = castle_conscript_stats.copy()
castle_conscript = Monster("Castle Conscript", castle_conscript_stats, castle_conscript_gear, castle_conscript_loot_table, difficulty=7, description=castle_conscript_description, floor_range=castle_conscript_floor_range, spells=castle_conscript_spells, spell_probabilities=castle_conscript_spell_probabilities, initial_stats=castle_conscript_initial_stats)

squire_sentry_stats = {
    "HP": 130,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 16,
    "Dexterity": 20,
    "Constitution": 26,
    "Intelligence": 12,
    "Wisdom": 14,
    "Charisma": 16,
    "Element": "None"
}

squire_sentry_gear = ["Squire's Sword", "Sentry's Shield"]
squire_sentry_loot_table = ["Sentry's Insignia", "Knight's Token", "Iron Coin"]
squire_sentry_description = "The Squire Sentry is a young warrior, eager to prove itself in battle. With sword in hand and shield raised, it stands watch over the castle's gates, ready to defend its home at a moment's notice."
squire_sentry_floor_range = (28, 30)
squire_sentry_spells = []
squire_sentry_spell_probabilities = {}
squire_sentry_initial_stats = squire_sentry_stats.copy()
squire_sentry = Monster("Squire Sentry", squire_sentry_stats, squire_sentry_gear, squire_sentry_loot_table, difficulty=6, description=squire_sentry_description, floor_range=squire_sentry_floor_range, spells=squire_sentry_spells, spell_probabilities=squire_sentry_spell_probabilities, initial_stats=squire_sentry_initial_stats)

royal_guardsman_stats = {
    "HP": 180,
    "Damage": 50,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 25,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "None"
}

royal_guardsman_gear = ["Royal Sword", "Golden Plate"]
royal_guardsman_loot_table = ["Royal Insignia", "Knight's Medal", "Golden Coin"]
royal_guardsman_description = "The Royal Guardsman is an elite defender of the castle, sworn to protect the royal family and their domain. Wielding a gleaming sword and clad in ornate armor, it serves as a formidable barrier against any who dare to threaten the kingdom."
royal_guardsman_floor_range = (42, 45)
royal_guardsman_spells = []
royal_guardsman_spell_probabilities = {}
royal_guardsman_initial_stats = royal_guardsman_stats.copy()
royal_guardsman = Monster("Royal Guardsman", royal_guardsman_stats, royal_guardsman_gear, royal_guardsman_loot_table, difficulty=9, description=royal_guardsman_description, floor_range=royal_guardsman_floor_range, spells=royal_guardsman_spells, spell_probabilities=royal_guardsman_spell_probabilities, initial_stats=royal_guardsman_initial_stats)

bloodhound_jailer_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "None"
}

bloodhound_jailer_gear = ["Iron Whip", "Chainmail Armor"]
bloodhound_jailer_loot_table = ["Jailer's Key", "Bloodhound Collar", "Rusty Shackles"]
bloodhound_jailer_description = "The Bloodhound Jailer is a merciless enforcer, tasked with keeping prisoners in line within the castle's dungeons. Armed with a cruel whip and armored in chainmail, it instills fear in the hearts of those unfortunate enough to cross its path."
bloodhound_jailer_floor_range = (36, 38)
bloodhound_jailer_spells = []
bloodhound_jailer_spell_probabilities = {}
bloodhound_jailer_initial_stats = bloodhound_jailer_stats.copy()
bloodhound_jailer = Monster("Bloodhound Jailer", bloodhound_jailer_stats, bloodhound_jailer_gear, bloodhound_jailer_loot_table, difficulty=8, description=bloodhound_jailer_description, floor_range=bloodhound_jailer_floor_range, spells=bloodhound_jailer_spells, spell_probabilities=bloodhound_jailer_spell_probabilities, initial_stats=bloodhound_jailer_initial_stats)

enchanted_armor_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 28,
    "Dexterity": 18,
    "Constitution": 35,
    "Intelligence": 16,
    "Wisdom": 20,
    "Charisma": 14,
    "Element": "None"
}

enchanted_armor_gear = ["Spectral Shield", "Enchanted Plate"]
enchanted_armor_loot_table = ["Enchanted Essence", "Magic Shard", "Ancient Relic"]
enchanted_armor_description = "The Enchanted Armor is a mystical guardian, animated by ancient magic to defend the castle's treasures. Adorned in shimmering plate and wielding a spectral shield, it stands sentinel against intruders with unwavering resolve."
enchanted_armor_floor_range = (44, 46)
enchanted_armor_spells = []
enchanted_armor_spell_probabilities = {}
enchanted_armor_initial_stats = enchanted_armor_stats.copy()
enchanted_armor = Monster("Enchanted Armor", enchanted_armor_stats, enchanted_armor_gear, enchanted_armor_loot_table, difficulty=10, description=enchanted_armor_description, floor_range=enchanted_armor_floor_range, spells=enchanted_armor_spells, spell_probabilities=enchanted_armor_spell_probabilities, initial_stats=enchanted_armor_initial_stats)

darkmage_acolyte_stats = {
    "HP": 140,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 18,
    "Dexterity": 22,
    "Constitution": 25,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 16,
    "Element": "Dark"
}

darkmage_acolyte_gear = ["Shadow Staff", "Dark Robes"]
darkmage_acolyte_loot_table = ["Dark Crystal", "Forbidden Grimoire", "Arcane Essence"]
darkmage_acolyte_description = "The Darkmage Acolyte is a devoted follower of dark magic, wielding sinister powers to serve its master's will. Clad in dark robes and wielding a shadowy staff, it conjures eldritch energies to unleash upon its enemies."
darkmage_acolyte_floor_range = (38, 40)
darkmage_acolyte_spells = ["Shadow Bolt", "Dark Ritual"]
darkmage_acolyte_spell_probabilities = {"Shadow Bolt": 0.6, "Dark Ritual": 0.4}
darkmage_acolyte_initial_stats = darkmage_acolyte_stats.copy()
darkmage_acolyte = Monster("Darkmage Acolyte", darkmage_acolyte_stats, darkmage_acolyte_gear, darkmage_acolyte_loot_table, difficulty=8, description=darkmage_acolyte_description, floor_range=darkmage_acolyte_floor_range, spells=darkmage_acolyte_spells, spell_probabilities=darkmage_acolyte_spell_probabilities, initial_stats=darkmage_acolyte_initial_stats)

darkmage_channeler_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 35,
    "Magic Defense": 45,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 25,
    "Wisdom": 22,
    "Charisma": 18,
    "Element": "Dark"
}

darkmage_channeler_gear = ["Shadow Scepter", "Cursed Mantle"]
darkmage_channeler_loot_table = ["Eldritch Orb", "Forbidden Tome", "Void Shard"]
darkmage_channeler_description = "The Darkmage Channeler is a master of the arcane, channeling dark energies to bend reality to its will. Cloaked in cursed mantle and wielding a shadow scepter, it commands the forces of darkness with terrifying precision."
darkmage_channeler_floor_range = (42, 44)
darkmage_channeler_spells = ["Dark Pulse", "Shadow Surge"]
darkmage_channeler_spell_probabilities = {"Dark Pulse": 0.5, "Shadow Surge": 0.5}
darkmage_channeler_initial_stats = darkmage_channeler_stats.copy()
darkmage_channeler = Monster("Darkmage Channeler", darkmage_channeler_stats, darkmage_channeler_gear, darkmage_channeler_loot_table, difficulty=9, description=darkmage_channeler_description, floor_range=darkmage_channeler_floor_range, spells=darkmage_channeler_spells, spell_probabilities=darkmage_channeler_spell_probabilities, initial_stats=darkmage_channeler_initial_stats)

ironbound_legionnaire_stats = {
    "HP": 160,
    "Damage": 40,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 22,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 14,
    "Wisdom": 16,
    "Charisma": 12,
    "Element": "None"
}

ironbound_legionnaire_gear = ["Iron Spear", "Legionnaire's Plate"]
ironbound_legionnaire_loot_table = ["Ironbound Insignia", "Battle Standard", "Rusty Halberd"]
ironbound_legionnaire_description = "The Ironbound Legionnaire is a disciplined soldier, armed with a sturdy spear and wearing ironbound armor. Trained to follow orders without question, it serves as the backbone of the castle's military force."
ironbound_legionnaire_floor_range = (32, 34)
ironbound_legionnaire_spells = []
ironbound_legionnaire_spell_probabilities = {}
ironbound_legionnaire_initial_stats = ironbound_legionnaire_stats.copy()
ironbound_legionnaire = Monster("Ironbound Legionnaire", ironbound_legionnaire_stats, ironbound_legionnaire_gear, ironbound_legionnaire_loot_table, difficulty=7, description=ironbound_legionnaire_description, floor_range=ironbound_legionnaire_floor_range, spells=ironbound_legionnaire_spells, spell_probabilities=ironbound_legionnaire_spell_probabilities, initial_stats=ironbound_legionnaire_initial_stats)

bandit_marauder_stats = {
    "HP": 140,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 20,
    "Constitution": 28,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 14,
    "Element": "None"
}

bandit_marauder_gear = ["Rusty Blade", "Tattered Cloak"]
bandit_marauder_loot_table = ["Bandit's Insignia", "Stolen Loot", "Sack of Coins"]
bandit_marauder_description = "The Bandit Marauder is a ruthless brigand, preying on travelers and plundering villages to enrich itself. Armed with a rusty blade and wearing tattered clothes, it roams the castle's outskirts in search of easy prey."
bandit_marauder_floor_range = (26, 28)
bandit_marauder_spells = []
bandit_marauder_spell_probabilities = {}
bandit_marauder_initial_stats = bandit_marauder_stats.copy()
bandit_marauder = Monster("Bandit Marauder", bandit_marauder_stats, bandit_marauder_gear, bandit_marauder_loot_table, difficulty=6, description=bandit_marauder_description, floor_range=bandit_marauder_floor_range, spells=bandit_marauder_spells, spell_probabilities=bandit_marauder_spell_probabilities, initial_stats=bandit_marauder_initial_stats)

deaths_head_tree_stats = {
    "HP": 220,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 18,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 24,
    "Charisma": 10,
    "Element": "Dark"
}

deaths_head_tree_gear = ["Twisted Roots", "Death's Grasp"]
deaths_head_tree_loot_table = ["Wilted Leaf", "Decayed Bark", "Soulwood Branch"]
deaths_head_tree_description = "The Death's Head Tree is a malevolent presence, its twisted form looming over the castle grounds like a harbinger of doom. With roots that ensnare and branches that grasp, it feeds on the life force of those unfortunate enough to cross its path."
deaths_head_tree_floor_range = (48, 50)
deaths_head_tree_spells = ["Shadowroot Curse", "Necrotic Embrace"]
deaths_head_tree_spell_probabilities = {"Shadowroot Curse": 0.7, "Necrotic Embrace": 0.3}
deaths_head_tree_initial_stats = deaths_head_tree_stats.copy()
deaths_head_tree = Monster("Death's Head Tree", deaths_head_tree_stats, deaths_head_tree_gear, deaths_head_tree_loot_table, difficulty=11, description=deaths_head_tree_description, floor_range=deaths_head_tree_floor_range, spells=deaths_head_tree_spells, spell_probabilities=deaths_head_tree_spell_probabilities, initial_stats=deaths_head_tree_initial_stats)

bonebat_stats = {
    "HP": 120,
    "Damage": 35,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 18,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 14,
    "Charisma": 10,
    "Element": "Dark"
}

bonebat_gear = ["Bone Wings", "Razor Fangs"]
bonebat_loot_table = ["Bat Skull", "Bone Fragment", "Dark Essence"]
bonebat_description = "The Bonebat is a ghastly amalgamation of skeletal remains and the ferocity of a bat. With razor-sharp fangs and wings crafted from bone, it swoops through the castle corridors in search of prey."
bonebat_floor_range = (36, 38)
bonebat_spells = ["Spectral Swoop", "Bone Shriek"]
bonebat_spell_probabilities = {"Spectral Swoop": 0.6, "Bone Shriek": 0.4}
bonebat_initial_stats = bonebat_stats.copy()
bonebat = Monster("Bonebat", bonebat_stats, bonebat_gear, bonebat_loot_table, difficulty=6, description=bonebat_description, floor_range=bonebat_floor_range, spells=bonebat_spells, spell_probabilities=bonebat_spell_probabilities, initial_stats=bonebat_initial_stats)

helmed_horror_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 26,
    "Dexterity": 20,
    "Constitution": 30,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 12,
    "Element": "None"
}

helmed_horror_gear = ["Steel Helm", "Enchanted Plate"]
helmed_horror_loot_table = ["Helmed Horror Shard", "Mystic Essence", "Arcane Residue"]
helmed_horror_description = "The Helmed Horror is an imposing figure, clad in enchanted armor and donning a steel helm. Animated by dark magic, it marches through the castle's halls with unwavering determination, seeking out intruders to crush beneath its iron grip."
helmed_horror_floor_range = (42, 44)
helmed_horror_spells = ["Ironclad Charge", "Spectral Slash"]
helmed_horror_spell_probabilities = {"Ironclad Charge": 0.6, "Spectral Slash": 0.4}
helmed_horror_initial_stats = helmed_horror_stats.copy()
helmed_horror = Monster("Helmed Horror", helmed_horror_stats, helmed_horror_gear, helmed_horror_loot_table, difficulty=9, description=helmed_horror_description, floor_range=helmed_horror_floor_range, spells=helmed_horror_spells, spell_probabilities=helmed_horror_spell_probabilities, initial_stats=helmed_horror_initial_stats)

slithering_hoard_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 22,
    "Dexterity": 28,
    "Constitution": 25,
    "Intelligence": 12,
    "Wisdom": 16,
    "Charisma": 10,
    "Element": "Poison"
}

slithering_hoard_gear = ["Toxic Fangs", "Venomous Scales"]
slithering_hoard_loot_table = ["Venom Sac", "Corroded Armor", "Toxic Charm"]
slithering_hoard_description = "The Slithering Hoard is a mass of serpentine creatures, their bodies covered in venomous scales and dripping with toxic saliva. They move as one, slithering through the castle's corridors in search of prey to overwhelm with their poisonous attacks."
slithering_hoard_floor_range = (42, 44)
slithering_hoard_spells = ["Venomous Bite", "Acidic Spray"]
slithering_hoard_spell_probabilities = {"Venomous Bite": 0.6, "Acidic Spray": 0.4}
slithering_hoard_initial_stats = slithering_hoard_stats.copy()
slithering_hoard = Monster("Slithering Hoard", slithering_hoard_stats, slithering_hoard_gear, slithering_hoard_loot_table, difficulty=9, description=slithering_hoard_description, floor_range=slithering_hoard_floor_range, spells=slithering_hoard_spells, spell_probabilities=slithering_hoard_spell_probabilities, initial_stats=slithering_hoard_initial_stats)

nightmare_stats = {
    "HP": 200,
    "Damage": 50,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 26,
    "Dexterity": 24,
    "Constitution": 30,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "Shadow"
}

nightmare_gear = ["Dark Mane", "Infernal Hooves"]
nightmare_loot_table = ["Nightmare Essence", "Darkened Bridle", "Shadowhoof Shard"]
nightmare_description = "A Nightmare is a fearsome steed, its dark mane billowing with shadowy energy and its hooves leaving behind trails of infernal flames. Born from the depths of darkness, it serves as a mount for the castle's darkest denizens, carrying them swiftly through the shadows."
nightmare_floor_range = (44, 46)
nightmare_spells = ["Shadow Charge", "Infernal Roar"]
nightmare_spell_probabilities = {"Shadow Charge": 0.6, "Infernal Roar": 0.4}
nightmare_initial_stats = nightmare_stats.copy()
nightmare = Monster("Nightmare", nightmare_stats, nightmare_gear, nightmare_loot_table, difficulty=10, description=nightmare_description, floor_range=nightmare_floor_range, spells=nightmare_spells, spell_probabilities=nightmare_spell_probabilities, initial_stats=nightmare_initial_stats)

hound_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 24,
    "Dexterity": 22,
    "Constitution": 20,
    "Intelligence": 10,
    "Wisdom": 12,
    "Charisma": 8,
    "Element": "None"
}

hound_gear = ["Razor Fangs", "Iron Collar"]
hound_loot_table = ["Hound Tooth", "Bloodied Fur", "Guardian Whistle"]
hound_description = "The Hound is a fierce guardian of the castle, its razor-sharp fangs and iron collar marking it as a loyal servant to its master. With keen senses and unmatched ferocity, it patrols the castle grounds, ready to pounce on any intruders."
hound_floor_range = (30, 32)
hound_spells = []
hound_spell_probabilities = {}
hound_initial_stats = hound_stats.copy()
hound = Monster("Hound", hound_stats, hound_gear, hound_loot_table, difficulty=7, description=hound_description, floor_range=hound_floor_range, spells=hound_spells, spell_probabilities=hound_spell_probabilities, initial_stats=hound_initial_stats)

cursed_courtesan_stats = {
    "HP": 160,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 22,
    "Dexterity": 28,
    "Constitution": 25,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 26,
    "Element": "Dark"
}

cursed_courtesan_gear = ["Seductive Veil", "Enchanted Gown"]
cursed_courtesan_loot_table = ["Cursed Rose", "Torn Garter", "Dark Desire Essence"]
cursed_courtesan_description = "The Cursed Courtesan is a haunting figure, her beauty masking a darkness that ensnares those who dare to gaze upon her. With a seductive veil and an enchanted gown, she lures unsuspecting victims into her grasp, leaving them cursed for eternity."
cursed_courtesan_floor_range = (36, 38)
cursed_courtesan_spells = ["Seduction", "Enthrall"]
cursed_courtesan_spell_probabilities = {"Seduction": 0.6, "Enthrall": 0.4}
cursed_courtesan_initial_stats = cursed_courtesan_stats.copy()
cursed_courtesan = Monster("Cursed Courtesan", cursed_courtesan_stats, cursed_courtesan_gear, cursed_courtesan_loot_table, difficulty=8, description=cursed_courtesan_description, floor_range=cursed_courtesan_floor_range, spells=cursed_courtesan_spells, spell_probabilities=cursed_courtesan_spell_probabilities, initial_stats=cursed_courtesan_initial_stats)

executioner_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 28,
    "Dexterity": 22,
    "Constitution": 30,
    "Intelligence": 16,
    "Wisdom": 18,
    "Charisma": 12,
    "Element": "None"
}

executioner_gear = ["Executioner's Axe", "Iron Mask"]
executioner_loot_table = ["Bloody Hood", "Guillotine Blade", "Executioner's Badge"]
executioner_description = "The Executioner is a grim figure, wielding a massive axe and wearing an iron mask that hides his face. Tasked with carrying out the castle's darkest deeds, he strikes fear into the hearts of all who cross his path, leaving behind a trail of blood and sorrow."
executioner_floor_range = (40, 42)
executioner_spells = ["Decapitate", "Soul Siphon"]
executioner_spell_probabilities = {"Decapitate": 0.6, "Soul Siphon": 0.4}
executioner_initial_stats = executioner_stats.copy()
executioner = Monster("Executioner", executioner_stats, executioner_gear, executioner_loot_table, difficulty=9, description=executioner_description, floor_range=executioner_floor_range, spells=executioner_spells, spell_probabilities=executioner_spell_probabilities, initial_stats=executioner_initial_stats)

knight_of_the_keep_stats = {
    "HP": 200,
    "Damage": 60,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "None"
}

knight_of_the_keep_gear = ["Plate Armor", "Keeper's Blade"]
knight_of_the_keep_loot_table = ["Knight's Crest", "Keepsake Pendant", "Defender's Gauntlet"]
knight_of_the_keep_description = "The Knight of the Keep is a valiant warrior sworn to defend the castle's stronghold. Clad in plate armor and wielding the Keeper's Blade, they stand as stalwart guardians, ready to repel any threat to the kingdom."
knight_of_the_keep_floor_range = (45, 48)
knight_of_the_keep_spells = []
knight_of_the_keep_spell_probabilities = {}
knight_of_the_keep_initial_stats = knight_of_the_keep_stats.copy()
knight_of_the_keep = Monster("Knight of the Keep", knight_of_the_keep_stats, knight_of_the_keep_gear, knight_of_the_keep_loot_table, difficulty=10, description=knight_of_the_keep_description, floor_range=knight_of_the_keep_floor_range, spells=knight_of_the_keep_spells, spell_probabilities=knight_of_the_keep_spell_probabilities, initial_stats=knight_of_the_keep_initial_stats)

royal_guardsman_stats = {
    "HP": 180,
    "Damage": 55,
    "Defense": 45,
    "Magic Defense": 35,
    "Strength": 28,
    "Dexterity": 25,
    "Constitution": 30,
    "Intelligence": 18,
    "Wisdom": 20,
    "Charisma": 25,
    "Element": "None"
}

royal_guardsman_gear = ["Royal Armor", "Regal Spear"]
royal_guardsman_loot_table = ["Royal Emblem", "Noble Crest", "Guardian's Oath"]
royal_guardsman_description = "The Royal Guardsman is an elite soldier tasked with protecting the royal family and their castle. Adorned in royal armor and wielding a regal spear, they exemplify loyalty, honor, and courage in their duty to defend the kingdom's rulers."
royal_guardsman_floor_range = (40, 42)
royal_guardsman_spells = []
royal_guardsman_spell_probabilities = {}
royal_guardsman_initial_stats = royal_guardsman_stats.copy()
royal_guardsman = Monster("Royal Guardsman", royal_guardsman_stats, royal_guardsman_gear, royal_guardsman_loot_table, difficulty=9, description=royal_guardsman_description, floor_range=royal_guardsman_floor_range, spells=royal_guardsman_spells, spell_probabilities=royal_guardsman_spell_probabilities, initial_stats=royal_guardsman_initial_stats)

ironclad_golem_stats = {
    "HP": 200,  # Define HP attribute for Ironclad Golem
    "Damage": 60,  # Define damage attribute for Ironclad Golem
    "Defense": 40,  # Define Defense stat vs attack stat for Ironclad Golem
    "Magic Defense": 50,  # Define magic defense vs spells for Ironclad Golem
    "Strength": 30,
    "Dexterity": 10,
    "Constitution": 35,
    "Intelligence": 5,
    "Wisdom": 10,
    "Charisma": 5,
    "Element": "Earth"  # Define elemental attribute of the Ironclad Golem's attack
}

ironclad_golem_gear = ["Iron Fist", "Adamantine Plating"]
ironclad_golem_loot_table = ["Iron Core", "Golem Shard", "Ancient Cog"]
ironclad_golem_description = "The Ironclad Golem is a massive construct, forged from enchanted metals and animated by ancient magic. It serves as an unyielding guardian, defending the castle's inner chambers with its immense strength and impenetrable armor."
ironclad_golem_floor_range = (35, 40)  # Ironclad Golem appears on floors 35 to 40
ironclad_golem_initial_stats = ironclad_golem_stats.copy()  # Make a copy of the initial stats
ironclad_golem = Monster("Ironclad Golem", ironclad_golem_stats, ironclad_golem_gear, ironclad_golem_loot_table, difficulty=9, description=ironclad_golem_description, floor_range=ironclad_golem_floor_range, initial_stats=ironclad_golem_initial_stats)
