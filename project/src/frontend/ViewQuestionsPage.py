import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import tkinter as tk
from services import questionsService
from Page import Page

# Page to view all the questions that have been saved
class ViewQuestionsPage(Page):
   # Initalize and setup the view page
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.label = {}

   def refreshQuestions(self):
       # *Retrieve questions from database and display - to be implemented
       questions = questionsService.pullAllQuestions()
       # Will load all questions by querying the database.
       self.label.clear()

       for question in questions:
           lb = tk.Label(self, text=question)
           lb.pack(side="top", fill="both", expand=True)
           self.label[question] = lb

       return questions
