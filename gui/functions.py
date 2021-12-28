from parser import *
from tkinter import ttk, filedialog
from tkinter import *

global spells_list





def get_list(it):
    spells = main.act_spells(it)
    spells_list = [k for k, v in spells.items()]


def set_desc(selection, spell_dict):
    spell_name = spells_list[selection]
    spell_description = spells[spell_name]['description']
    return spell_description
