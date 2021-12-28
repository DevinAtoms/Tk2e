import tkinter as tk
from tkinter import *
from tkinter import ttk

from parser import main

root = Tk()
root.geometry('800x600')
# root.resizable(width=False, height=False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
spell_description = ''


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                        )
                )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def runapp():
    global spell_list, spell_name, spell_description
    spell_list, spell_name, spell_description = main.init_actor()
    spell_list_var.set(spell_list)
    desc_string.set(spell_description)


spell_list_var = StringVar()
desc_string = StringVar()

mainFrame = ttk.Frame(root, padding='5 5 5 5')
mainFrame.grid(column=0, row=0, sticky=NSEW)
mainFrame.rowconfigure(2, weight=3)
mainFrame.columnconfigure(6, weight=3)

listFrame = ttk.Frame(mainFrame, padding='5 5 5 5')
listFrame.grid(column=0, row=2, sticky=NS)
listFrame.rowconfigure(2, weight=1)

spell_list_label = ttk.Label(listFrame, text='Spell List')
spell_gen_btn = ttk.Button(listFrame, text='Generate', command=runapp)
spell_listbox = Listbox(listFrame, listvariable=spell_list_var, exportselection=False)

spell_listbox.bind("<<ListboxSelect>>", lambda e: setstring())


def setstring():
    global desc_string, textbox
    textbox['state'] = 'normal'
    textbox.delete(1.0, 'end')
    textbox.insert('end', main.set_desc(spell_listbox.curselection()))
    textbox['state'] = 'disabled'


spell_listbox.grid(column=1, row=2, sticky=NS)
spell_list_label.grid(column=1, row=1, sticky=NS)
spell_gen_btn.grid(column=1, row=3, sticky=NS, pady=5)

textFrame = ttk.Labelframe(mainFrame, text='Description', borderwidth=2)
textFrame.grid(column=6, row=2, sticky=NSEW)
textFrame.columnconfigure(0, weight=1)
textFrame.rowconfigure(0, weight=1)

textbox = tk.Text(textFrame, takefocus=False, wrap='word', exportselection=False)
textbox.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5)
textbox.insert('end', spell_description)

root.mainloop()
