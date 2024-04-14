class God:
    def __init__(self, name, description, altar_description, buffs):
        self.name = name
        self.description = description
        self.altar_description = altar_description
        self.buffs = buffs

# Define the gods and their buffs
gods = [
    God(
        name="God of Strength",
        description="The mighty deity who grants strength and power to those who worship him.",
        altar_description="An imposing stone altar adorned with symbols of strength and courage.",
        buffs={
            "Strength": 5,  # Increase Strength by 5
            "Constitution": 2  # Increase Constitution by 2
            # Add more buffs as needed
        }
    ),
    God(
        name="Goddess of Wisdom",
        description="The wise deity who bestows knowledge and insight upon her followers.",
        altar_description="A serene marble altar with ancient tomes and scrolls scattered around it.",
        buffs={
            "Intelligence": 5,  # Increase Intelligence by 5
            "Wisdom": 5  # Increase Wisdom by 5
            # Add more buffs as needed
        }
    ),
    # Add more gods with their respective buffs and altar descriptions
]
