import Note
from tkinter import *

class Print:
    note = Note.Note

    def input_text (self):
        name = input('Введите наименование заметки: ')
        text = input('Введите заметку: ')
        note = name + '\n'+ text + '\n'
        
        return note