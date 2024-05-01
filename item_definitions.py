import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class DamageType:
    def __init__(self, name):
        self.name = name

class ElementalProperty:
    def __init__(self, name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, description, damage_type, category, slot, elemental_property=None, stats=None):
        super().__init__(name, description)
        self.damage_type = damage_type
        self.category = category
        self.slot = slot
        self.elemental_property = elemental_property
        self.stats = stats if stats is not None else {}

class Armor(Item):
    def __init__(self, name, description, category, slot, stats=None):
        super().__init__(name, description)
        self.category = category  # Use armor category instead of defense type
        self.slot = slot
        self.stats = stats if stats is not None else {}

class BasicItem(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class WeaponCategory:
    def __init__(self, name):
        self.name = name

class ArmorCategory:
    def __init__(self, name):
        self.name = name

# Define damage types
slashing = DamageType("Slashing")
bludgeoning = DamageType("Bludgeoning")
piercing = DamageType("Piercing")
fire = DamageType("Fire")
ice = DamageType("Ice")
lightning = DamageType("Lightning")
# Add more damage types as needed...

# Define elemental properties
none = ElementalProperty("None")
fire_elemental = ElementalProperty("Fire")
ice_elemental = ElementalProperty("Ice")
lightning_elemental = ElementalProperty("Lightning")
# Add more elemental properties as needed...

# Define weapon categories
one_handed_sword = WeaponCategory("One-Handed Sword")
two_handed_sword = WeaponCategory("Two-Handed Sword")
axe = WeaponCategory("Axe")
staff = WeaponCategory("Staff")
# Add more weapon categories as needed...

# Define armor categories
light_armor = ArmorCategory("Light")
medium_armor = ArmorCategory("Medium")
heavy_armor = ArmorCategory("Heavy")
shield_armor = ArmorCategory("Shield")
# Add more armor categories as needed...

# Define items
basic_items = [
    BasicItem("Gold", "It's money")
]


# Define weapons
weapons = [
    Weapon("Longsword", "A versatile weapon with reach and slicing power", slashing, one_handed_sword, "Right Hand", stats={"Attack": 5, "Strength": 2}),
    Weapon("Warhammer", "A heavy hammer for smashing through armor", bludgeoning, one_handed_sword, "Right Hand"),
    Weapon("Fire Staff", "A staff imbued with the power of fire", fire, staff, "Two-Handed", fire_elemental),
    Weapon("Short Sword", "A short and basic sword", slashing, one_handed_sword, "Right Hand", stats={"Attack": lambda: random.randint(1, 8) + 1}),
    Armor("Basic Shield", "A basic shield", shield_armor, "Left Hand", stats={"Defense": 3}),
    # Add more weapons...
]

# Define armor
armor = [
    Armor("Chain Shirt", "A shirt made of interlocking metal rings", medium_armor, "Chest", stats={"Defense": 2, "Dexterity": -1}),
    Armor("Leather Armor", "Tanned animal hides stitched together", light_armor, "Chest", stats={"Defense": 1}),
    Armor("Plate Armor", "Heavy metal armor", heavy_armor, "Chest", stats={"Defense": 3}),
    # Add more armor...
]