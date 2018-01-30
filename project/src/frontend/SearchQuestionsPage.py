import tkinter as tk
from Page import Page

#  Page to search saved questions
class SearchQuestionsPage(Page):
    # Initialize and setup searcg page
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       # Search box to type query
       search_box = tk.Text(self, height = 1, width = 15)
       # Search button to trigger search query
       search_button = tk.Button(self, text="Search", command = self.query_questions)
       # Place box and button onto the page
       search_box.grid(row="0", column="0")
       search_button.grid(row="0", column="1")

   # *Searches through the database to find questions matching the query
   def query_questions(self):
       # *To be implemented
       return