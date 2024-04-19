from spells import Spell

class Monster:
    def __init__(self, name, stats, gear, loot_table, difficulty, description, floor_range, spells=None, spell_probabilities=None, initial_stats=None):
        self.name = name
        self.stats = stats
        self.initial_stats = stats.copy()
        self.gear = gear
        self.loot_table = loot_table
        self.difficulty = difficulty
        self.floor_range = floor_range
        self.description = description
        self.initial_hp = stats["HP"] #Initialize initial HP attribute
        self.initial_stats = initial_stats
        self.spells = spells if spells else [] # List of spells the monster can use
        self.spell_probabilities = spell_probabilities if spell_probabilities else {}  # Probability for each spell
