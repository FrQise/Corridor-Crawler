from spells import Spell
import importlib.util
from os.path import dirname, basename, isfile, join
import glob

def import_monsters_from_biome(game):
    monsters = []
    current_biome = game.current_biome
    current_difficulty = game.current_difficulty
    # print("Current biome from monster.py :", current_biome, "current difficulty from monsters.py:", current_difficulty)
    
    if current_biome is not None:
        biome_module_name = current_biome.name.lower().replace(" ", "_") + ".py"
        biome_module_path = join(dirname(__file__), biome_module_name)
        
        # print("Biome module path:", biome_module_path)  # Debug print statement
        
        if isfile(biome_module_path):
            try:
                spec = importlib.util.spec_from_file_location(basename(biome_module_path).split(".")[0], biome_module_path)
                biome_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(biome_module)
                
                for name, obj in biome_module.__dict__.items():
                    if isinstance(obj, Monster) and obj.floor_range[0] <= current_difficulty <= obj.floor_range[1]:
                        monsters.append(obj)
            except Exception as e:
                # print("Error loading biome module:", e)  # Debug print statement
                pass
        else:
            # print("Biome module not found at:", biome_module_path)  # Debug print statement
            pass
    
    return monsters




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
