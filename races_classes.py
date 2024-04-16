from item_definitions import weapons, armor

class Race:
    def __init__(self, name, description, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.name = name
        self.description = description
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

# Define Races
human = Race("Human", "Adaptable and versatile")

elf = Race("Elf", "Graceful and attuned to nature", dexterity=2, intelligence=1, charisma=1)

dwarf = Race("Dwarf", "Strong and resilient", strength=2, constitution=2, wisdom=1)

goblin = Race("Goblin", "Small little ugly green guy", strength=-2, constitution=-1, dexterity=3)

class Class:
    def __init__(self, name, description, stats=None, weapon_proficiencies=None, armor_proficiencies=None, spell_categories=None):
        self.name = name
        self.description = description
        self.stats = stats if stats is not None else {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        self.weapon_proficiencies = weapon_proficiencies if weapon_proficiencies is not None else []
        self.armor_proficiencies = armor_proficiencies if armor_proficiencies is not None else []
        self.spell_categories = spell_categories if spell_categories is not None else []

    def apply_class_modifiers(self, player_stats):
        for stat, value in self.stats.items():
            player_stats[stat] += value

    def check_weapon_proficiency(self, weapon):
        return weapon in self.weapon_proficiencies

    def check_armor_proficiency(self, armor):
        # Check if the armor's category is in the class's armor proficiencies
        return armor.category in self.armor_proficiencies

    def check_spell_category(self, spell):
        return spell.category in self.spell_categories

# Define classes
fighter = Class("Fighter", "Masters of martial combat", stats={"Strength": 13, "Constitution": 12},
                 weapon_proficiencies=["One-Handed Sword", "Axe"], armor_proficiencies=["Light Armor", "Medium Armor", "Heavy Armor", "Left Hand"], spell_categories=[])

wizard = Class("Wizard", "Masters of arcane magic", stats={"Intelligence": 3, "Wisdom": 2},
               spell_categories=["Evocation", "Invocation", "Divination"], weapon_proficiencies=["Staff"], armor_proficiencies=["Light Armor"])

rogue = Class("Rogue", "Stealthy and skilled in deception", stats={"Dexterity": 3, "Charisma": 2},
              weapon_proficiencies=["Dagger", "Shortbow"], armor_proficiencies=["Light Armor"], spell_categories=[])

cleric = Class("Cleric", "Divine agents serving a higher power", stats={"Wisdom": 4, "Charisma": 1},
               spell_categories=["Evocation", "Invocation", "Divination", "Necromancy"], weapon_proficiencies=["Mace", "Warhammer"],
               armor_proficiencies=["Medium Armor", "Shield"])

sorcerer = Class("Sorcerer", "Innate spellcasters wielding raw magical power", stats={"Charisma": 4, "Constitution": 1},
                 spell_categories=["Evocation", "Invocation", "Enchantment"], weapon_proficiencies=["Dagger"], armor_proficiencies=["Robe"])