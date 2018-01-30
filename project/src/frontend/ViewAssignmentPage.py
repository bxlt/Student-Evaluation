import tkinter as tk
from Page import Page
import databaseReader as reader

class ViewAssignmentPage(Page):
   # Initalize and setup the view page
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       # ***** Need To Parse Questions In ***** having db problems *****

       assignment_number_label = tk.Label(self, text="Enter Assignment Number")

       self.assignment_number_textbox = tk.Text(self, height=1, width=15)

       id = self.assignment_number_textbox.get("1.0", "end")
       assignments = reader.get_assign()

       #for i in assignments




