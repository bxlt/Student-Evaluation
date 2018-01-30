import tkinter as tk


# Abstract Page class that creates a frame and a method to view the frame
class Page(tk.Frame):
    # Initialize Page
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    # Display Page
    def show(self):
        self.lift()