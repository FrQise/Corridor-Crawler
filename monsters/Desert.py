from monsters.bestiary import Monster

dust_wyrm_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
dust_wyrm_gear = ["Razor Scales", "Sandstorm Armor"]
dust_wyrm_loot_table = {"Gold": (1, 10), "Longsword": (1, 1)}
dust_wyrm_description = "Dust Wyrms are colossal serpentine creatures that burrow beneath the desert sands. They can strike with lightning speed, swallowing their prey whole with their razor-sharp jaws. Legends speak of ancient treasures hidden within their lairs, attracting adventurers seeking fortune and glory."
dust_wyrm_floor_range = (1, 5)
dust_wyrm_spells = []
dust_wyrm_spell_probabilities = {}
dust_wyrm_initial_stats = dust_wyrm_stats.copy()
dust_wyrm = Monster("Dust Wyrm", dust_wyrm_stats, dust_wyrm_gear, dust_wyrm_loot_table, difficulty=3, description=dust_wyrm_description, floor_range=dust_wyrm_floor_range, spells=dust_wyrm_spells, spell_probabilities=dust_wyrm_spell_probabilities, initial_stats=dust_wyrm_initial_stats)

mirage_viper_stats = {
    "HP": 400,
    "Damage": 70,
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
mirage_viper_gear = ["Venomous Fangs", "Dazzling Scales"]
mirage_viper_loot_table = {"Gold": (1, 10), "Longsword": (1, 1)}
mirage_viper_description = "Mirage Vipers are deadly serpents that blend seamlessly into the shifting sands of the desert. Their venomous bite can induce hallucinations, leaving their victims disoriented and vulnerable. Travelers beware, for their deadly embrace can spell certain doom."
mirage_viper_floor_range = (2, 5)
mirage_viper_spells = []
mirage_viper_spell_probabilities = {}
mirage_viper_initial_stats = mirage_viper_stats.copy()
mirage_viper = Monster("Mirage Viper", mirage_viper_stats, mirage_viper_gear, mirage_viper_loot_table, difficulty=3, description=mirage_viper_description, floor_range=mirage_viper_floor_range, spells=mirage_viper_spells, spell_probabilities=mirage_viper_spell_probabilities, initial_stats=mirage_viper_initial_stats)

dune_scorpion_stats = {
    "HP": 300,
    "Damage": 60,
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
dune_scorpion_gear = ["Venomous Stinger", "Carapace Armor"]
dune_scorpion_loot_table = ["Gold", "Scorpion Tail", "Shadowstone"]
dune_scorpion_description = "Dune Scorpions are formidable arachnids that roam the desert sands in search of prey. Their venomous stingers can inject potent neurotoxins, paralyzing their victims and leaving them at the mercy of these deadly predators."
dune_scorpion_floor_range = (2, 5)
dune_scorpion_spells = []
dune_scorpion_spell_probabilities = {}
dune_scorpion_initial_stats = dune_scorpion_stats.copy()
dune_scorpion = Monster("Dune Scorpion", dune_scorpion_stats, dune_scorpion_gear, dune_scorpion_loot_table, difficulty=100, description=dune_scorpion_description, floor_range=dune_scorpion_floor_range, spells=dune_scorpion_spells, spell_probabilities=dune_scorpion_spell_probabilities, initial_stats=dune_scorpion_initial_stats)

sunfire_djinn_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
sunfire_djinn_gear = ["Blazing Scimitar", "Inferno Robes"]
sunfire_djinn_loot_table = ["Gold", "Djinn Essence", "Burning Ember"]
sunfire_djinn_description = "Sunfire Djinns are fiery spirits bound to the scorching deserts, wielding the power of the sun itself. They can conjure flames to incinerate their foes and unleash searing blasts of heat. Only the bravest adventurers dare to challenge their fiery wrath."
sunfire_djinn_floor_range = (2, 5)
sunfire_djinn_spells = []
sunfire_djinn_spell_probabilities = {}
sunfire_djinn_initial_stats = sunfire_djinn_stats.copy()
sunfire_djinn = Monster("Sunfire Djinn", sunfire_djinn_stats, sunfire_djinn_gear, sunfire_djinn_loot_table, difficulty=200, description=sunfire_djinn_description, floor_range=sunfire_djinn_floor_range, spells=sunfire_djinn_spells, spell_probabilities=sunfire_djinn_spell_probabilities, initial_stats=sunfire_djinn_initial_stats)

oasis_guardian_stats = {
    "HP": 700,
    "Damage": 100,
    "Defense": 60,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Water"
}
oasis_guardian_gear = ["Tidal Trident", "Reefscale Armor"]
oasis_guardian_loot_table = ["Gold", "Aquatic Pearl", "Coralspike"]
oasis_guardian_description = "Oasis Guardians are ancient protectors of the desert's hidden oases, summoned to defend against intruders. Their mastery over water allows them to conjure powerful tidal waves and control the flow of the desert's life-giving waters."
oasis_guardian_floor_range = (250, 350)
oasis_guardian_spells = []
oasis_guardian_spell_probabilities = {}
oasis_guardian_initial_stats = oasis_guardian_stats.copy()
oasis_guardian = Monster("Oasis Guardian", oasis_guardian_stats, oasis_guardian_gear, oasis_guardian_loot_table, difficulty=250, description=oasis_guardian_description, floor_range=oasis_guardian_floor_range, spells=oasis_guardian_spells, spell_probabilities=oasis_guardian_spell_probabilities, initial_stats=oasis_guardian_initial_stats)

sandstorm_elemental_stats = {
    "HP": 600,
    "Damage": 80,
    "Defense": 50,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Wind"
}
sandstorm_elemental_gear = ["Whirling Sands", "Tempest Veil"]
sandstorm_elemental_loot_table = ["Gold", "Elemental Essence", "Sands of Time"]
sandstorm_elemental_description = "Sandstorm Elementals are embodiments of the desert's relentless fury, manifesting as swirling tornadoes of sand and wind. They can whip up devastating sandstorms to engulf their foes, tearing flesh from bone with the force of their gales."
sandstorm_elemental_floor_range = (2, 5)
sandstorm_elemental_spells = []
sandstorm_elemental_spell_probabilities = {}
sandstorm_elemental_initial_stats = sandstorm_elemental_stats.copy()
sandstorm_elemental = Monster("Sandstorm Elemental", sandstorm_elemental_stats, sandstorm_elemental_gear, sandstorm_elemental_loot_table, difficulty=200, description=sandstorm_elemental_description, floor_range=sandstorm_elemental_floor_range, spells=sandstorm_elemental_spells, spell_probabilities=sandstorm_elemental_spell_probabilities, initial_stats=sandstorm_elemental_initial_stats)

cactus_behemoth_stats = {
    "HP": 800,
    "Damage": 120,
    "Defense": 70,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Nature"
}
cactus_behemoth_gear = ["Thorny Spikes", "Prickly Armor"]
cactus_behemoth_loot_table = ["Gold", "Cactus Needle", "Essence of Thorns"]
cactus_behemoth_description = "Cactus Behemoths are colossal plant-like creatures that roam the arid deserts, resembling towering cacti. Their thick, spiny armor protects them from harm, and they can impale their enemies with razor-sharp thorns. Beware their wrath, for their rage is as fierce as the desert sun."
cactus_behemoth_floor_range = (2, 5)
cactus_behemoth_spells = []
cactus_behemoth_spell_probabilities = {}
cactus_behemoth_initial_stats = cactus_behemoth_stats.copy()
cactus_behemoth = Monster("Cactus Behemoth", cactus_behemoth_stats, cactus_behemoth_gear, cactus_behemoth_loot_table, difficulty=300, description=cactus_behemoth_description, floor_range=cactus_behemoth_floor_range, spells=cactus_behemoth_spells, spell_probabilities=cactus_behemoth_spell_probabilities, initial_stats=cactus_behemoth_initial_stats)

sirocco_serpent_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 40,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Wind"
}
sirocco_serpent_gear = ["Tempest Fangs", "Zephyr Scales"]
sirocco_serpent_loot_table = ["Gold", "Serpent Scale", "Cyclone Crystal"]
sirocco_serpent_description = "Sirocco Serpents are serpentine beings infused with the power of the desert winds. They can summon swirling sandstorms and unleash blasts of scorching wind upon their enemies. Beware their swift strikes, for they can strike from the shadows of the desert."
sirocco_serpent_floor_range = (200, 300)
sirocco_serpent_spells = []
sirocco_serpent_spell_probabilities = {}
sirocco_serpent_initial_stats = sirocco_serpent_stats.copy()
sirocco_serpent = Monster("Sirocco Serpent", sirocco_serpent_stats, sirocco_serpent_gear, sirocco_serpent_loot_table, difficulty=200, description=sirocco_serpent_description, floor_range=sirocco_serpent_floor_range, spells=sirocco_serpent_spells, spell_probabilities=sirocco_serpent_spell_probabilities, initial_stats=sirocco_serpent_initial_stats)

desert_basilisk_stats = {
    "HP": 600,
    "Damage": 90,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
desert_basilisk_gear = ["Stony Gaze", "Sandstone Scales"]
desert_basilisk_loot_table = ["Gold", "Basilisk Scale", "Desert Crystal"]
desert_basilisk_description = "Desert Basilisks are fearsome reptilian creatures with the ability to turn their victims to stone with a single glance. Their sandstone scales blend seamlessly with the desert sands, allowing them to ambush their prey with deadly precision."
desert_basilisk_floor_range = (200, 300)
desert_basilisk_spells = []
desert_basilisk_spell_probabilities = {}
desert_basilisk_initial_stats = desert_basilisk_stats.copy()
desert_basilisk = Monster("Desert Basilisk", desert_basilisk_stats, desert_basilisk_gear, desert_basilisk_loot_table, difficulty=200, description=desert_basilisk_description, floor_range=desert_basilisk_floor_range, spells=desert_basilisk_spells, spell_probabilities=desert_basilisk_spell_probabilities, initial_stats=desert_basilisk_initial_stats)

dust_devil_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Wind"
}
dust_devil_gear = ["Sandslash Whirlwind", "Turbulent Essence"]
dust_devil_loot_table = ["Gold", "Dust Particle", "Whirlwind Fragment"]
dust_devil_description = "Dust Devils are malevolent spirits that inhabit the swirling sandstorms of the desert. They can tear through flesh with their razor-sharp winds, leaving nothing but devastation in their wake. Beware their wrath, for they spare no mercy for those who dare to trespass in their domain."
dust_devil_floor_range = (150, 250)
dust_devil_spells = []
dust_devil_spell_probabilities = {}
dust_devil_initial_stats = dust_devil_stats.copy()
dust_devil = Monster("Dust Devil", dust_devil_stats, dust_devil_gear, dust_devil_loot_table, difficulty=150, description=dust_devil_description, floor_range=dust_devil_floor_range, spells=dust_devil_spells, spell_probabilities=dust_devil_spell_probabilities, initial_stats=dust_devil_initial_stats)

sand_golem_stats = {
    "HP": 700,
    "Damage": 100,
    "Defense": 70,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
sand_golem_gear = ["Granite Fists", "Sandstone Armor"]
sand_golem_loot_table = ["Gold", "Golem Shard", "Desert Relic"]
sand_golem_description = "Sand Golems are towering constructs crafted from the sands of the desert. Animated by ancient magic, they lumber through the dunes, crushing anything in their path with their massive fists. Only the strongest adventurers dare to challenge these behemoths."
sand_golem_floor_range = (1, 5)
sand_golem_spells = []
sand_golem_spell_probabilities = {}
sand_golem_initial_stats = sand_golem_stats.copy()
sand_golem = Monster("Sand Golem", sand_golem_stats, sand_golem_gear, sand_golem_loot_table, difficulty=300, description=sand_golem_description, floor_range=sand_golem_floor_range, spells=sand_golem_spells, spell_probabilities=sand_golem_spell_probabilities, initial_stats=sand_golem_initial_stats)

sun_scarab_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
sun_scarab_gear = ["Solar Carapace", "Radiant Mandibles"]
sun_scarab_loot_table = ["Gold", "Scarab Shell", "Sunstone"]
sun_scarab_description = "Sun Scarabs are radiant insects that scuttle across the desert sands, basking in the scorching sun. Their golden carapaces reflect the sunlight, blinding their enemies and providing them with protection against the desert heat."
sun_scarab_floor_range = (150, 250)
sun_scarab_spells = []
sun_scarab_spell_probabilities = {}
sun_scarab_initial_stats = sun_scarab_stats.copy()
sun_scarab = Monster("Sun Scarab", sun_scarab_stats, sun_scarab_gear, sun_scarab_loot_table, difficulty=150, description=sun_scarab_description, floor_range=sun_scarab_floor_range, spells=sun_scarab_spells, spell_probabilities=sun_scarab_spell_probabilities, initial_stats=sun_scarab_initial_stats)

mirage_sphinx_stats = {
    "HP": 600,
    "Damage": 90,
    "Defense": 50,
    "Magic Defense": 40,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Air"
}
mirage_sphinx_gear = ["Sands of Illusion", "Phantom Riddles"]
mirage_sphinx_loot_table = ["Gold", "Sphinx Relic", "Illusionary Gem"]
mirage_sphinx_description = "Mirage Sphinxes are enigmatic guardians of the desert, shrouded in mystery and illusion. They can conjure mirages to confuse and disorient their foes, leading them astray in the endless sands."
mirage_sphinx_floor_range = (200, 300)
mirage_sphinx_spells = []
mirage_sphinx_spell_probabilities = {}
mirage_sphinx_initial_stats = mirage_sphinx_stats.copy()
mirage_sphinx = Monster("Mirage Sphinx", mirage_sphinx_stats, mirage_sphinx_gear, mirage_sphinx_loot_table, difficulty=200, description=mirage_sphinx_description, floor_range=mirage_sphinx_floor_range, spells=mirage_sphinx_spells, spell_probabilities=mirage_sphinx_spell_probabilities, initial_stats=mirage_sphinx_initial_stats)

sand_wraith_stats = {
    "HP": 500,
    "Damage": 80,
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
sand_wraith_gear = ["Ethereal Scimitar", "Shifting Sands Cloak"]
sand_wraith_loot_table = ["Gold", "Wraith Essence", "Sands of Eternity"]
sand_wraith_description = "Sand Wraiths are spectral beings that haunt the desolate wastelands of the desert. They drift through the dunes, striking fear into the hearts of travelers with their eerie presence. Beware their otherworldly powers, for they can drain the life force from their victims with a touch."
sand_wraith_floor_range = (200, 300)
sand_wraith_spells = []
sand_wraith_spell_probabilities = {}
sand_wraith_initial_stats = sand_wraith_stats.copy()
sand_wraith = Monster("Sand Wraith", sand_wraith_stats, sand_wraith_gear, sand_wraith_loot_table, difficulty=200, description=sand_wraith_description, floor_range=sand_wraith_floor_range, spells=sand_wraith_spells, spell_probabilities=sand_wraith_spell_probabilities, initial_stats=sand_wraith_initial_stats)

scalding_salamander_stats = {
    "HP": 400,
    "Damage": 70,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
scalding_salamander_gear = ["Infernal Tongue", "Molten Hide"]
scalding_salamander_loot_table = ["Gold", "Salamander Scale", "Blazing Essence"]
scalding_salamander_description = "Scalding Salamanders are fiery reptiles that dwell in the scorching depths of the desert. They can breathe jets of searing flames and withstand the hottest temperatures with their molten hides."
scalding_salamander_floor_range = (150, 250)
scalding_salamander_spells = []
scalding_salamander_spell_probabilities = {}
scalding_salamander_initial_stats = scalding_salamander_stats.copy()
scalding_salamander = Monster("Scalding Salamander", scalding_salamander_stats, scalding_salamander_gear, scalding_salamander_loot_table, difficulty=150, description=scalding_salamander_description, floor_range=scalding_salamander_floor_range, spells=scalding_salamander_spells, spell_probabilities=scalding_salamander_spell_probabilities, initial_stats=scalding_salamander_initial_stats)

sandstrider_nomad_stats = {
    "HP": 450,
    "Damage": 75,
    "Defense": 40,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
sandstrider_nomad_gear = ["Nomadic Spear", "Sandcloak Garb"]
sandstrider_nomad_loot_table = ["Gold", "Nomad's Trinket", "Desert Scroll"]
sandstrider_nomad_description = "Sandstrider Nomads are desert wanderers who traverse the dunes in search of ancient relics and lost treasures. They are skilled warriors and survivalists, adept at navigating the harsh desert terrain and fending off threats from sandstorms and hostile creatures."
sandstrider_nomad_floor_range = (150, 250)
sandstrider_nomad_spells = []
sandstrider_nomad_spell_probabilities = {}
sandstrider_nomad_initial_stats = sandstrider_nomad_stats.copy()
sandstrider_nomad = Monster("Sandstrider Nomad", sandstrider_nomad_stats, sandstrider_nomad_gear, sandstrider_nomad_loot_table, difficulty=150, description=sandstrider_nomad_description, floor_range=sandstrider_nomad_floor_range, spells=sandstrider_nomad_spells, spell_probabilities=sandstrider_nomad_spell_probabilities, initial_stats=sandstrider_nomad_initial_stats)

flame_dancer_stats = {
    "HP": 500,
    "Damage": 80,
    "Defense": 50,
    "Magic Defense": 60,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Fire"
}
flame_dancer_gear = ["Inferno Blades", "Flame-Ember Cloak"]
flame_dancer_loot_table = ["Gold", "Dancing Flame", "Pyro Essence"]
flame_dancer_description = "Flame Dancers are agile warriors who harness the power of fire to weave mesmerizing dances of destruction. Their flaming blades leave trails of scorching heat in their wake, consuming everything in their path."
flame_dancer_floor_range = (200, 300)
flame_dancer_spells = []
flame_dancer_spell_probabilities = {}
flame_dancer_initial_stats = flame_dancer_stats.copy()
flame_dancer = Monster("Flame Dancer", flame_dancer_stats, flame_dancer_gear, flame_dancer_loot_table, difficulty=200, description=flame_dancer_description, floor_range=flame_dancer_floor_range, spells=flame_dancer_spells, spell_probabilities=flame_dancer_spell_probabilities, initial_stats=flame_dancer_initial_stats)

sandstone_gargoyle_stats = {
    "HP": 600,
    "Damage": 90,
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
sandstone_gargoyle_gear = ["Granite Maul", "Sandstone Plates"]
sandstone_gargoyle_loot_table = ["Gold", "Gargoyle Fragment", "Ancient Glyph"]
sandstone_gargoyle_description = "Sandstone Gargoyles are ancient guardians sculpted from the very bedrock of the desert. Imbued with mystical energy, they stand watch over forgotten ruins and sacred sites, ready to defend them from intruders."
sandstone_gargoyle_floor_range = (250, 350)
sandstone_gargoyle_spells = []
sandstone_gargoyle_spell_probabilities = {}
sandstone_gargoyle_initial_stats = sandstone_gargoyle_stats.copy()
sandstone_gargoyle = Monster("Sandstone Gargoyle", sandstone_gargoyle_stats, sandstone_gargoyle_gear, sandstone_gargoyle_loot_table, difficulty=250, description=sandstone_gargoyle_description, floor_range=sandstone_gargoyle_floor_range, spells=sandstone_gargoyle_spells, spell_probabilities=sandstone_gargoyle_spell_probabilities, initial_stats=sandstone_gargoyle_initial_stats)

sand_elemental_stats = {
    "HP": 550,
    "Damage": 85,
    "Defense": 50,
    "Magic Defense": 50,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0,
    "Element": "Earth"
}
sand_elemental_gear = ["Sandslash Claws", "Earthen Armor"]
sand_elemental_loot_table = ["Gold", "Essence of Sand", "Quicksand Shard"]
sand_elemental_description = "Sand Elementals are living embodiments of the desert's unforgiving terrain. They can reshape their sandy forms at will, emerging from the ground to ambush unsuspecting prey and dragging them into the depths of the desert sands."
sand_elemental_floor_range = (200, 300)
sand_elemental_spells = []
sand_elemental_spell_probabilities = {}
sand_elemental_initial_stats = sand_elemental_stats.copy()
sand_elemental = Monster("Sand Elemental", sand_elemental_stats, sand_elemental_gear, sand_elemental_loot_table, difficulty=200, description=sand_elemental_description, floor_range=sand_elemental_floor_range, spells=sand_elemental_spells, spell_probabilities=sand_elemental_spell_probabilities, initial_stats=sand_elemental_initial_stats)

lamia_stats = {
    "HP": 340,
    "Damage": 70,
    "Defense": 50,
    "Magic Defense": 60,
    "Strength": 45,
    "Dexterity": 55,
    "Constitution": 48,
    "Intelligence": 50,
    "Wisdom": 52,
    "Charisma": 58,
    "Element": "Darkness"
}
lamia_gear = ["Serpentine Whip", "Enchanted Robes"]
lamia_loot_table = ["Gold", "Lamia Fang", "Enchanted Silk"]
lamia_description = "Lamias are seductive and deadly creatures with the upper body of a woman and the lower body of a serpent. They lure unsuspecting victims with their beauty, only to ensnare them in their coils and drain their life force."
lamia_floor_range = (80, 160)
lamia_spells = ["Serpent's Kiss", "Charm", "Venomous Strike"]
lamia_spell_probabilities = {"Serpent's Kiss": 0.4, "Charm": 0.3, "Venomous Strike": 0.3}
lamia_initial_stats = lamia_stats.copy()
lamia = Monster("Lamia", lamia_stats, lamia_gear, lamia_loot_table, difficulty=80, description=lamia_description, floor_range=lamia_floor_range, spells=lamia_spells, spell_probabilities=lamia_spell_probabilities, initial_stats=lamia_initial_stats)

sandstalker_scorpion_stats = {
    "HP": 150,
    "Damage": 40,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 30,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 10,
    "Element": "Earth"
}

sandstalker_scorpion_gear = ["Venomous Stinger", "Chitinous Armor"]
sandstalker_scorpion_loot_table = ["Scorpion Venom", "Chitin Fragment", "Stinger Barb"]
sandstalker_scorpion_description = "Sandstalker Scorpions are enormous arachnids that lurk beneath the desert sands, their venomous stingers poised to strike unsuspecting prey."
sandstalker_scorpion_floor_range = (20, 25)
sandstalker_scorpion_spells = []
sandstalker_scorpion_spell_probabilities = {}
sandstalker_scorpion_initial_stats = sandstalker_scorpion_stats.copy()
sandstalker_scorpion = Monster("Sandstalker Scorpion", sandstalker_scorpion_stats, sandstalker_scorpion_gear, sandstalker_scorpion_loot_table, difficulty=7, description=sandstalker_scorpion_description, floor_range=sandstalker_scorpion_floor_range, spells=sandstalker_scorpion_spells, spell_probabilities=sandstalker_scorpion_spell_probabilities, initial_stats=sandstalker_scorpion_initial_stats)

dune_drifter_stats = {
    "HP": 120,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 45,
    "Constitution": 25,
    "Intelligence": 18,
    "Wisdom": 22,
    "Charisma": 15,
    "Element": "Wind"
}

dune_drifter_gear = ["Sandstorm Cloak", "Bladed Sand Boots"]
dune_drifter_loot_table = ["Sand Crystal", "Desert Gem", "Nomad Relic"]
dune_drifter_description = "Dune Drifters are agile creatures that glide effortlessly over the desert dunes, their camouflaged bodies blending seamlessly with the sandy landscape."
dune_drifter_floor_range = (22, 27)
dune_drifter_spells = []
dune_drifter_spell_probabilities = {}
dune_drifter_initial_stats = dune_drifter_stats.copy()
dune_drifter = Monster("Dune Drifter", dune_drifter_stats, dune_drifter_gear, dune_drifter_loot_table, difficulty=6, description=dune_drifter_description, floor_range=dune_drifter_floor_range, spells=dune_drifter_spells, spell_probabilities=dune_drifter_spell_probabilities, initial_stats=dune_drifter_initial_stats)

sirocco_serpent_stats = {
    "HP": 180,
    "Damage": 45,
    "Defense": 35,
    "Magic Defense": 30,
    "Strength": 35,
    "Dexterity": 40,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Fire"
}

sirocco_serpent_gear = ["Scalding Scales", "Searing Fangs"]
sirocco_serpent_loot_table = ["Serpent Scale", "Fire Essence", "Scorched Fang"]
sirocco_serpent_description = "Sirocco Serpents are deadly creatures that ride the desert winds, striking swiftly from above with their razor-sharp fangs."
sirocco_serpent_floor_range = (25, 30)
sirocco_serpent_spells = []
sirocco_serpent_spell_probabilities = {}
sirocco_serpent_initial_stats = sirocco_serpent_stats.copy()
sirocco_serpent = Monster("Sirocco Serpent", sirocco_serpent_stats, sirocco_serpent_gear, sirocco_serpent_loot_table, difficulty=7, description=sirocco_serpent_description, floor_range=sirocco_serpent_floor_range, spells=sirocco_serpent_spells, spell_probabilities=sirocco_serpent_spell_probabilities, initial_stats=sirocco_serpent_initial_stats)

oasis_ogre_stats = {
    "HP": 250,
    "Damage": 55,
    "Defense": 40,
    "Magic Defense": 35,
    "Strength": 50,
    "Dexterity": 30,
    "Constitution": 45,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 20,
    "Element": "Earth"
}

oasis_ogre_gear = ["Boulder Club", "Desert Plate"]
oasis_ogre_loot_table = ["Oasis Gem", "Granite Shard", "Tough Hide"]
oasis_ogre_description = "Oasis Ogres are hulking brutes that guard the precious water sources of the desert, their immense strength a formidable deterrent to would-be intruders."
oasis_ogre_floor_range = (28, 33)
oasis_ogre_spells = []
oasis_ogre_spell_probabilities = {}
oasis_ogre_initial_stats = oasis_ogre_stats.copy()
oasis_ogre = Monster("Oasis Ogre", oasis_ogre_stats, oasis_ogre_gear, oasis_ogre_loot_table, difficulty=8, description=oasis_ogre_description, floor_range=oasis_ogre_floor_range, spells=oasis_ogre_spells, spell_probabilities=oasis_ogre_spell_probabilities, initial_stats=oasis_ogre_initial_stats)

sandstorm_siren_stats = {
    "HP": 200,
    "Damage": 40,
    "Defense": 35,
    "Magic Defense": 40,
    "Strength": 30,
    "Dexterity": 35,
    "Constitution": 30,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 20,
    "Element": "Air"
}

sandstorm_siren_gear = ["Gale Veil", "Whirlwind Harp"]
sandstorm_siren_loot_table = ["Wind Essence", "Dust Crystal", "Cyclone Shard"]
sandstorm_siren_description = "Sandstorm Sirens are ethereal beings that control the desert winds, conjuring devastating sandstorms to engulf their enemies."
sandstorm_siren_floor_range = (30, 35)
sandstorm_siren_spells = ["Sandstorm", "Zephyr's Wrath"]
sandstorm_siren_spell_probabilities = {"Sandstorm": 0.6, "Zephyr's Wrath": 0.4}
sandstorm_siren_initial_stats = sandstorm_siren_stats.copy()
sandstorm_siren = Monster("Sandstorm Siren", sandstorm_siren_stats, sandstorm_siren_gear, sandstorm_siren_loot_table, difficulty=7, description=sandstorm_siren_description, floor_range=sandstorm_siren_floor_range, spells=sandstorm_siren_spells, spell_probabilities=sandstorm_siren_spell_probabilities, initial_stats=sandstorm_siren_initial_stats)

sandswept_sylph_stats = {
    "HP": 100,
    "Damage": 25,
    "Defense": 15,
    "Magic Defense": 30,
    "Strength": 15,
    "Dexterity": 35,
    "Constitution": 20,
    "Intelligence": 25,
    "Wisdom": 30,
    "Charisma": 25,
    "Element": "Air"
}

sandswept_sylph_gear = ["Zephyr Veil", "Gossamer Garments"]
sandswept_sylph_loot_table = ["Sylph Essence", "Whispering Wind", "Ethereal Dust"]
sandswept_sylph_description = "Sandswept Sylphs are agile and graceful creatures that dance across the desert sands, their movements hypnotic and mesmerizing to those who gaze upon them."
sandswept_sylph_floor_range = (20, 25)
sandswept_sylph_spells = []
sandswept_sylph_spell_probabilities = {}
sandswept_sylph_initial_stats = sandswept_sylph_stats.copy()
sandswept_sylph = Monster("Sandswept Sylph", sandswept_sylph_stats, sandswept_sylph_gear, sandswept_sylph_loot_table, difficulty=5, description=sandswept_sylph_description, floor_range=sandswept_sylph_floor_range, spells=sandswept_sylph_spells, spell_probabilities=sandswept_sylph_spell_probabilities, initial_stats=sandswept_sylph_initial_stats)

nomad_warrior_stats = {
    "HP": 120,
    "Damage": 35,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 25,
    "Constitution": 35,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Earth"
}

nomad_warrior_gear = ["Desert Scimitar", "Nomad Armor"]
nomad_warrior_loot_table = ["Warrior's Blade", "Sandstone Shard", "Nomad Medallion"]
nomad_warrior_description = "Nomad Warriors are skilled fighters who roam the desert in search of glory and treasure, their prowess in battle unmatched by many."
nomad_warrior_floor_range = (22, 27)
nomad_warrior_spells = []
nomad_warrior_spell_probabilities = {}
nomad_warrior_initial_stats = nomad_warrior_stats.copy()
nomad_warrior = Monster("Nomad Warrior", nomad_warrior_stats, nomad_warrior_gear, nomad_warrior_loot_table, difficulty=6, description=nomad_warrior_description, floor_range=nomad_warrior_floor_range, spells=nomad_warrior_spells, spell_probabilities=nomad_warrior_spell_probabilities, initial_stats=nomad_warrior_initial_stats)

nomad_archer_stats = {
    "HP": 100,
    "Damage": 30,
    "Defense": 20,
    "Magic Defense": 25,
    "Strength": 25,
    "Dexterity": 35,
    "Constitution": 20,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Wind"
}

nomad_archer_gear = ["Sandbow", "Nomad Quiver"]
nomad_archer_loot_table = ["Archer's Arrow", "Wind Crystal", "Nomad Token"]
nomad_archer_description = "Nomad Archers are skilled marksmen who traverse the desert dunes, their arrows striking with deadly accuracy from a distance."
nomad_archer_floor_range = (22, 27)
nomad_archer_spells = []
nomad_archer_spell_probabilities = {}
nomad_archer_initial_stats = nomad_archer_stats.copy()
nomad_archer = Monster("Nomad Archer", nomad_archer_stats, nomad_archer_gear, nomad_archer_loot_table, difficulty=5, description=nomad_archer_description, floor_range=nomad_archer_floor_range, spells=nomad_archer_spells, spell_probabilities=nomad_archer_spell_probabilities, initial_stats=nomad_archer_initial_stats)

nomad_shaman_stats = {
    "HP": 110,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 35,
    "Strength": 20,
    "Dexterity": 25,
    "Constitution": 25,
    "Intelligence": 30,
    "Wisdom": 35,
    "Charisma": 20,
    "Element": "Earth"
}

nomad_shaman_gear = ["Sandstaff", "Nomad Robes"]
nomad_shaman_loot_table = ["Shamanic Talisman", "Earth Essence", "Nomad Scroll"]
nomad_shaman_description = "Nomad Shamans are wise mystics who commune with the spirits of the desert, wielding powerful earth magic to protect their tribes."
nomad_shaman_floor_range = (24, 29)
nomad_shaman_spells = ["Sandstorm", "Earthen Grasp"]
nomad_shaman_spell_probabilities = {"Sandstorm": 0.5, "Earthen Grasp": 0.5}
nomad_shaman_initial_stats = nomad_shaman_stats.copy()
nomad_shaman = Monster("Nomad Shaman", nomad_shaman_stats, nomad_shaman_gear, nomad_shaman_loot_table, difficulty=6, description=nomad_shaman_description, floor_range=nomad_shaman_floor_range, spells=nomad_shaman_spells, spell_probabilities=nomad_shaman_spell_probabilities, initial_stats=nomad_shaman_initial_stats)

nomad_bulwark_stats = {
    "HP": 180,
    "Damage": 40,
    "Defense": 40,
    "Magic Defense": 30,
    "Strength": 35,
    "Dexterity": 20,
    "Constitution": 45,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Earth"
}

nomad_bulwark_gear = ["Nomad Shield", "Sandstone Armor"]
nomad_bulwark_loot_table = ["Bulwark Barrier", "Nomad Crest", "Sandstone Fragment"]
nomad_bulwark_description = "Nomad Bulwarks are stalwart defenders of their tribes, wielding their shields and armor to withstand even the fiercest of desert storms."
nomad_bulwark_floor_range = (26, 31)
nomad_bulwark_spells = []
nomad_bulwark_spell_probabilities = {}
nomad_bulwark_initial_stats = nomad_bulwark_stats.copy()
nomad_bulwark = Monster("Nomad Bulwark", nomad_bulwark_stats, nomad_bulwark_gear, nomad_bulwark_loot_table, difficulty=7, description=nomad_bulwark_description, floor_range=nomad_bulwark_floor_range, spells=nomad_bulwark_spells, spell_probabilities=nomad_bulwark_spell_probabilities, initial_stats=nomad_bulwark_initial_stats)

nomad_camel_rider_stats = {
    "HP": 140,
    "Damage": 30,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 25,
    "Dexterity": 30,
    "Constitution": 30,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 20,
    "Element": "Earth"
}

nomad_camel_rider_gear = ["Desert Lance", "Nomad Saddle"]
nomad_camel_rider_loot_table = ["Camel Trinket", "Saddle Bag", "Nomad Token"]
nomad_camel_rider_description = "Nomad Camel-Riders are skilled riders who traverse the desert atop their loyal steeds, using their speed and agility to outmaneuver their foes."
nomad_camel_rider_floor_range = (28, 33)
nomad_camel_rider_spells = []
nomad_camel_rider_spell_probabilities = {}
nomad_camel_rider_initial_stats = nomad_camel_rider_stats.copy()
nomad_camel_rider = Monster("Nomad Camel-Rider", nomad_camel_rider_stats, nomad_camel_rider_gear, nomad_camel_rider_loot_table, difficulty=6, description=nomad_camel_rider_description, floor_range=nomad_camel_rider_floor_range, spells=nomad_camel_rider_spells, spell_probabilities=nomad_camel_rider_spell_probabilities, initial_stats=nomad_camel_rider_initial_stats)

oasis_oracle_stats = {
    "HP": 160,
    "Damage": 35,
    "Defense": 30,
    "Magic Defense": 35,
    "Strength": 25,
    "Dexterity": 30,
    "Constitution": 30,
    "Intelligence": 40,
    "Wisdom": 45,
    "Charisma": 25,
    "Element": "Water"
}

oasis_oracle_gear = ["Aqua Mantle", "Crystal Staff"]
oasis_oracle_loot_table = ["Crystal Orb", "Water Essence", "Oasis Token"]
oasis_oracle_description = "Oasis Oracles are mystic beings that guard hidden oases in the desert, their prophetic visions guiding or deceiving travelers who seek their aid."
oasis_oracle_floor_range = (30, 35)
oasis_oracle_spells = ["Water Jet", "Illusionary Mirage"]
oasis_oracle_spell_probabilities = {"Water Jet": 0.6, "Illusionary Mirage": 0.4}
oasis_oracle_initial_stats = oasis_oracle_stats.copy()
oasis_oracle = Monster("Oasis Oracle", oasis_oracle_stats, oasis_oracle_gear, oasis_oracle_loot_table, difficulty=7, description=oasis_oracle_description, floor_range=oasis_oracle_floor_range, spells=oasis_oracle_spells, spell_probabilities=oasis_oracle_spell_probabilities, initial_stats=oasis_oracle_initial_stats)

cactus_colossus_stats = {
    "HP": 300,
    "Damage": 50,
    "Defense": 45,
    "Magic Defense": 40,
    "Strength": 40,
    "Dexterity": 20,
    "Constitution": 50,
    "Intelligence": 20,
    "Wisdom": 25,
    "Charisma": 15,
    "Element": "Earth"
}

cactus_colossus_gear = ["Thorned Club", "Cactus Armor"]
cactus_colossus_loot_table = ["Cactus Needle", "Prickly Pear", "Colossus Core"]
cactus_colossus_description = "Cactus Colossi are enormous humanoid figures composed of living cactus, their sharp spines and tough exterior making them formidable opponents."
cactus_colossus_floor_range = (32, 37)
cactus_colossus_spells = []
cactus_colossus_spell_probabilities = {}
cactus_colossus_initial_stats = cactus_colossus_stats.copy()
cactus_colossus = Monster("Cactus Colossus", cactus_colossus_stats, cactus_colossus_gear, cactus_colossus_loot_table, difficulty=8, description=cactus_colossus_description, floor_range=cactus_colossus_floor_range, spells=cactus_colossus_spells, spell_probabilities=cactus_colossus_spell_probabilities, initial_stats=cactus_colossus_initial_stats)

mirage_marauder_stats = {
    "HP": 140,
    "Damage": 40,
    "Defense": 25,
    "Magic Defense": 20,
    "Strength": 30,
    "Dexterity": 35,
    "Constitution": 25,
    "Intelligence": 20,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Fire"
}

mirage_marauder_gear = ["Heatwave Blade", "Sand Cloak"]
mirage_marauder_loot_table = ["Mirage Essence", "Scorched Coin", "Deceptive Dagger"]
mirage_marauder_description = "Mirage Marauders are illusory bandits that materialize from the desert heat, ambushing travelers with their deceptive tactics."
mirage_marauder_floor_range = (28, 33)
mirage_marauder_spells = ["Illusory Strike", "Heat Mirage"]
mirage_marauder_spell_probabilities = {"Illusory Strike": 0.6, "Heat Mirage": 0.4}
mirage_marauder_initial_stats = mirage_marauder_stats.copy()
mirage_marauder = Monster("Mirage Marauder", mirage_marauder_stats, mirage_marauder_gear, mirage_marauder_loot_table, difficulty=6, description=mirage_marauder_description, floor_range=mirage_marauder_floor_range, spells=mirage_marauder_spells, spell_probabilities=mirage_marauder_spell_probabilities, initial_stats=mirage_marauder_initial_stats)

quicksand_quagmire_stats = {
    "HP": 180,
    "Damage": 25,
    "Defense": 20,
    "Magic Defense": 15,
    "Strength": 30,
    "Dexterity": 10,
    "Constitution": 35,
    "Intelligence": 10,
    "Wisdom": 15,
    "Charisma": 10,
    "Element": "Earth"
}

quicksand_quagmire_gear = ["Silted Grasp"]
quicksand_quagmire_loot_table = ["Quicksand Essence", "Sinking Shard", "Lost Artifact"]
quicksand_quagmire_description = "Quicksand Quagmires are living pits of shifting sand that swallow unwary travelers whole, concealing ancient treasures and forgotten dangers within their depths."
quicksand_quagmire_floor_range = (30, 35)
quicksand_quagmire_spells = ["Quicksand Grasp", "Suffocating Sinkhole"]
quicksand_quagmire_spell_probabilities = {"Quicksand Grasp": 0.7, "Suffocating Sinkhole": 0.3}
quicksand_quagmire_initial_stats = quicksand_quagmire_stats.copy()
quicksand_quagmire = Monster("Quicksand Quagmire", quicksand_quagmire_stats, quicksand_quagmire_gear, quicksand_quagmire_loot_table, difficulty=7, description=quicksand_quagmire_description, floor_range=quicksand_quagmire_floor_range, spells=quicksand_quagmire_spells, spell_probabilities=quicksand_quagmire_spell_probabilities, initial_stats=quicksand_quagmire_initial_stats)

sand_wyrm_stats = {
    "HP": 250,
    "Damage": 45,
    "Defense": 30,
    "Magic Defense": 25,
    "Strength": 40,
    "Dexterity": 25,
    "Constitution": 40,
    "Intelligence": 15,
    "Wisdom": 20,
    "Charisma": 15,
    "Element": "Earth"
}

sand_wyrm_gear = ["Sandstorm Fangs"]
sand_wyrm_loot_table = ["Wyrm Scale", "Ancient Relic", "Sandstone Fragment"]
sand_wyrm_description = "Sand Wyrms are gigantic serpents that burrow beneath the desert sands, capable of swallowing entire caravans whole."
sand_wyrm_floor_range = (32, 37)
sand_wyrm_spells = ["Sandstorm Assault", "Burrow"]
sand_wyrm_spell_probabilities = {"Sandstorm Assault": 0.6, "Burrow": 0.4}
sand_wyrm_initial_stats = sand_wyrm_stats.copy()
sand_wyrm = Monster("Sand Wyrm", sand_wyrm_stats, sand_wyrm_gear, sand_wyrm_loot_table, difficulty=8, description=sand_wyrm_description, floor_range=sand_wyrm_floor_range, spells=sand_wyrm_spells, spell_probabilities=sand_wyrm_spell_probabilities, initial_stats=sand_wyrm_initial_stats)

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
fire_elemental_floor_range = (20, 40)
fire_elemental_spells = ["Fireball", "Flame Burst"]
fire_elemental_spell_probabilities = {"Fireball": 0.6, "Flame Burst": 0.4} 
fire_elemental_initial_stats = fire_elemental_stats.copy() # Make a copy of the initial stats
fire_elemental = Monster("Fire Elemental", fire_elemental_stats, fire_elemental_gear, fire_elemental_loot_table, difficulty=20, description=fire_elemental_description, floor_range=fire_elemental_floor_range, spells=fire_elemental_spells, spell_probabilities=fire_elemental_spell_probabilities, initial_stats=fire_elemental_initial_stats)
print("Loading monsters from desert.py...")

# Define your monsters here...