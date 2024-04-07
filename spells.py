class Spell:
    def __init__(self, name, description, damage_type, level, damage, category):
        self.name = name
        self.description = description
        self.damage_type = damage_type
        self.level = level
        self.damage = damage
        self.category = category

# Define spells for each category
evocation_spells = [
    Spell("Flame Burst", "Create a burst of flames that engulfs your enemies.", "Fire", 3, damage=20, category="Evocation"),
    Spell("Thunderclap", "Summon a deafening clap of thunder to stun foes.", "Thunder", 2, damage=15, category="Evocation"),
    Spell("Icy Blast", "Unleash a freezing blast of ice to freeze targets in their tracks.", "Ice", 4, damage=25, category="Evocation"),
    # Add more evocation spells...
]

invocation_spells = [
    Spell("Arcane Bolt", "Launch a bolt of pure arcane energy at your target.", "Arcane", 1, damage=10, category="Invocation"),
    Spell("Shadow Bind", "Conjure dark shadows to bind and immobilize foes.", "Shadow", 3, damage=25, category="Invocation"),
    Spell("Celestial Beam", "Call forth a beam of celestial light to purge evil from the land.", "Light", 5, damage=30, category="Invocation"),
    # Add more invocation spells...
]

curse_spells = [
    Spell("Hex of Misfortune", "Place a hex on a target, causing them to suffer from bad luck.", "Curse", 1, damage=0, category="Curse"),
    Spell("Curse of Weakness", "Inflict a curse upon your enemies, sapping their strength and vitality.", "Curse", 3, damage=0, category="Curse"),
    # Add more curse spells...
]

necromancy_spells = [
    Spell("Soul Drain", "Drain the life force from your enemies to heal yourself.", "Necrotic", 2, damage=15, category="Necromancy"),
    Spell("Raise Dead", "Summon undead minions to serve and obey your commands.", "Necrotic", 3, damage=0, category="Necromancy"),
    # Add more necromancy spells...
]

divination_spells = [
    Spell("Future Sight", "Gain glimpses of the future to anticipate your foes' actions.", "Divination", 1, damage=0, category="Divination"),
    Spell("Mind Probe", "Probe the minds of your enemies to extract valuable information.", "Divination", 4, damage=0, category="Divination"),
    # Add more divination spells...
]

enchantment_spells = [
    Spell("Illusionary Mirage", "Create convincing illusions to deceive and distract your enemies.", "Illusion", 2, damage=0, category="Enchantment"),
    Spell("Enthrall", "Entrance and captivate your foes with your enchanting presence.", "Charm", 1, damage=0, category="Enchantment"),
    # Add more enchantment spells...
]

# Combine all spells into one list
all_spells = evocation_spells + invocation_spells + curse_spells + necromancy_spells + divination_spells + enchantment_spells
