import tkinter
import tkinter.ttk
def fixed_map(style,option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.
    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
def SetupStyle():
    style = tkinter.ttk.Style()
    style.map('Treeview', foreground=fixed_map(style,'foreground'),background=fixed_map(style,'background'))
    return style
def ResetNotebook(notebook,style):
    pass
