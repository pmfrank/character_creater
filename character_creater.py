import random
import os
import sqlite3
from helper_functions import *
from variables import *
import json


# Class to hold character information
class Character():

    def __init__(self):
        self.race = str()
        self.subrace = str()
        self.clss = str()
        self.ability_scores = {'strength': 0,
                                'dexterity': 0,
                                'constitution': 0,
                                'intelligence': 0,
                                'wisdom': 0,
                                'charisma': 0}
        self.gender = str()
        self.background = str()
        self.alignment = str()
        self.traits = list()
        self.ideals = str()
        self.bonds = str()
        self.flaws = str()
        self.height = str()
        self.weight = str()
        self.armor_class = int()
        self.weapons = list()

# Test if Database exist, if not, create it
if not os.path.exists(DATABASE):
    create_database()

# Test if character table exists
with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='character' ''')
    if cursor.fetchone()[0]==0 : 
        create_table('character')

with open('races.json','r') as races:
    race_info = json.load(races)

character = Character()
character.race = 'elf'
character.subrace = 'high elf'
character.ability_scores[(race_info['races'][character.race]['traits']['ability score increase']).split()[0]] += \
    int((race_info['races'][character.race]['traits']['ability score increase']).split()[1])
character.ability_scores[(race_info['races'][character.race]['traits']['subrace'][character.subrace]['traits']['ability score increase']).split()[0]] += \
    int((race_info['races'][character.race]['traits']['subrace'][character.subrace]['traits']['ability score increase']).split()[1])
print(character.ability_scores)