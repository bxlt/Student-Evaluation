import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import tkinter as tk
from services import questionsService
from Page import Page

# Page where you can enter a question
class SubmitQuestionsPage(Page):
   # Initialize and setup the page
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       # Label prompting user to enter a question
       question_label = tk.Label(self, text="Enter your question below:")

       # Textbox where question can be entered
       self.question_textbox = tk.Text(self, height=15, width=45)

       # Put label and textbox onto the page
       question_label.grid(row=0, sticky='W')
       self.question_textbox.grid(row=1)

       # Label prompting user to enter a solution to the question
       answer_label = tk.Label(self, text="Enter the solution to the question:")

       # Textbox for the answer
       self.answer_textbox = tk.Text(self, height=15, width=45)

       # Put the answer label and textbox onto page
       answer_label.grid(row=3, sticky='W')
       self.answer_textbox.grid(row=4)

       # Create and add to the page a submit button to submit a question
       submit_question_button = tk.Button(self, text="Submit", command=self.submit_question)
       submit_question_button.grid(row=5)

   # Saves the question entered to the database
   def submit_question(self):
       # Retrieve text from textboxs
       question = self.question_textbox.get("1.0", "end")
       answer = self.answer_textbox.get("1.0", "end")

       # save to database
       questionsService.pushNewQuestion(question, answer)

       # clear original contents
       self.question_textbox.delete("1.0", "end")
       self.answer_textbox.delete("1.0", "end")
