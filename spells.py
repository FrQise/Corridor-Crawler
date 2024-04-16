class Spell:
    def __init__(self, name, description, damage_type, damage, category, spell_type, duration=None, player_buff=None, monster_debuff=None, extra_effect=None):
        self.name = name
        self.description = description
        self.damage_type = damage_type
        self.damage = damage
        self.category = category
        self.spell_type = spell_type  # Define the type of the spell (Attack, Buff, Debuff, Special)
        self.player_buff = player_buff  # Dictionary to store player stat buffs
        self.monster_debuff = monster_debuff  # Dictionary to store monster stat debuffs
        self.extra_effect = extra_effect  # Extra effect of the spell
        self.duration = duration # Define the duration of the spell in room

# Define spells for each category
evocation_spells = [
    Spell("Flame Burst", "Create a burst of flames that engulfs your enemies.", "Fire", damage=20, category="Evocation", spell_type="Attack"),
    Spell("Thunderclap", "Summon a deafening clap of thunder to stun foes.", "Thunder", damage=15, category="Evocation", spell_type="Attack"),
    Spell("Icy Blast", "Unleash a freezing blast of ice to freeze targets in their tracks.", "Ice", damage=25, category="Evocation", spell_type="Attack"),
    # Add more evocation spells...
]

invocation_spells = [
    Spell("Arcane Bolt", "Launch a bolt of pure arcane energy at your target.", "Arcane", damage=10, category="Invocation", spell_type="Attack"),
    Spell("Shadow Bind", "Conjure dark shadows to bind and immobilize foes.", "Shadow", damage=25, category="Invocation", spell_type="Attack"),
    Spell("Celestial Beam", "Call forth a beam of celestial light to purge evil from the land.", "Light", damage=30, category="Invocation", spell_type="Attack"),
    # Add more invocation spells...
]

# Define player stat buffs and monster stat debuffs for spells
player_buff = {'strength': 5, 'defense': 3}  # Example: Increase player's strength and defense
monster_debuff = {'defense': -2}  # Example: Decrease monster's defense

# Define spells with player buffs and monster debuffs
buff_spells = [
    Spell("Strength of the Bear", "Grant the caster the strength of a bear.", None, damage=0, category="Buff", spell_type="Buff", duration=1, player_buff={'Strength': 10}),
    Spell("Healing Light", "Channel healing light to restore HP.", None, damage=0, category="Buff", spell_type="Buff", player_buff={'HP': 10}, extra_effect="Healing")
    # Add more buff/debuff spells...
]

debuff_spells = [
Spell("Weakness Curse", "Curse the enemy to weaken their defenses.", None, damage=0, category="Debuff", spell_type="Debuff", monster_debuff={'Strength': -10}, extra_effect="Debuff")

]

# Define spells with extra effects
extra_effect_spells = [
    Spell("Time Warp", "Manipulate time to allow the caster to take two turns in one.", None, damage=0, category="Temporal", spell_type="Special", extra_effect="Double Turn"),
    # Add more spells with extra effects...
]

# Combine all spells into one list
all_spells = evocation_spells + invocation_spells + buff_spells + extra_effect_spells + debuff_spells
