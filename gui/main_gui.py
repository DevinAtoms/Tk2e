import tkinter as tk
from json import loads
from tkinter import ttk
from tkinter import simpledialog


class WindowRoot(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Py2E')
        self.geometry('800x600')
        self.config(menu=RootMenuBar(self))
        self.mainFrame = RootMainFrame(self)


class RootMainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.notebook = RootFrameNotebook(self)
        self.nbpage1 = RootNotebookPage(self)
        self.textlabel = ttk.Label(master=self.nbpage1, text='test')
        self.textlabel.grid(row=1, column=1)
        self.nbpage2 = RootNotebookPage(self)
        self.notebook.add(self.nbpage1, text='Page 1')
        self.notebook.add(self.nbpage2, text='Page 2')
        self.grid(row=0, column=0)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class RootMenuBar(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.add_cascade(label='File', menu=RootFileMenu(self, tearoff=0))


class RootFileMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.add_command(label="Import JSON", command=lambda: JsonDialog(self, 'Enter JSON Export'))
        self.add_command(label='Exit', command=exit)


class JsonDialog(simpledialog.Dialog):
    def __init__(self, parent, title):
        simpledialog.Dialog.__init__(self, parent, title)
        self.result = None
        self.entry = None
        self.parent = parent

    def parsejson(self):
        token = loads(self.result)
        act = token['actors']['actor.1']
        return act

    #        sp = {k: v for k, v in it.items() if k[:2] == 'sp'}
    #        sp_lst = [k for k, v in sp.items()]

    def body(self, master):
        self.entry = tk.Text(master, name="entry")
        self.entry.grid(row=1, padx=5, sticky=tk.W + tk.E)

        return self.entry

    def validate(self):
        try:
            result = self.getresult()
            self.result = result
            self.parsejson()
            return 1
        except ValueError as e:
            print(e)
            return 0

    def getresult(self):
        print(self.entry.get('1.0', 'end'))
        return self.entry.get('1.0', 'end')


class RootFrameNotebook(ttk.Notebook):
    def __init__(self, master):
        ttk.Notebook.__init__(self, master)
        self.master = master
        self.grid(row=0, column=0)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class RootNotebookPage(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid(row=0, column=0)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.page_type = None

        def page_setup(page_type):
            self.page_type = page_type


if __name__ == "__main__":
    root = WindowRoot()
    root.mainloop()
