# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Formatter: Black v19.10b0
#
# Author: Scott Katzelnick
#
# Purpose:
#
# FILE TRANSFER ASSIGNMENT PART THREE
# Users are now asking for a user interface to make using the script easier and more versatile.
#
# Desired features of the UI:
#
# Allow the user to browse and choose a specific folder that will contain the files to be checked daily.
#
# Allow the user to browse and choose a specific folder that will receive the copied files.
#
# Allow the user to manually initiate the 'file check' process that is performed by the script.
#
# You have been asked to create this UI.
#
# Once you have completed this assignment, upload your code to Github

# Import required modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import file_xfer_part2
import file_xfer_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.maxsize(700, 500)
        self.master.minsize(700, 500)
        file_xfer_func.center_window(self, 700, 400)
        self.master.title("Directory Auto-Sync®")
        self.master.config(bg="#333")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_xfer_func.close_app(self))
        arg = self.master

        self.get_lbl = tk.Label(
            self.master,
            font=("Helvetica", 16),
            fg="#fff",
            bg="#333",
            text="Choose Source Directory",
        )
        self.get_lbl.grid(row=0, column=0, padx=(30, 0), pady=(100, 0))

        def select_dir():
            dir_path = filedialog.askdirectory()

        self.get_btn = tk.Button(
            self.master, text="Browse", command=select_dir,
        )
        self.get_btn.grid(row=2, column=0, padx=(30, 0), pady=(10, 0))

        self.lst_dir = Listbox(self.master)
        # ????????

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
