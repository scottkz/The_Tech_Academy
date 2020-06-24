import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import file_xfer_part3


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (700 / 2))
    y = int((screen_height / 2) - (500 / 2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


def close_app(self):
    if messagebox.askokcancel('Quit App', 'Do you want to quit this application?'):
        self.master.destroy()
        os._exit(0)