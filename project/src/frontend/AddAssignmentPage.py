import tkinter as tk
from Page import Page
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
#this is the page for add assignment

class AddAssignmentPage(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self, *args,**kwargs)
        #label for page message
        title1 = tk.Label(self, text = "Please enter the assignmentID:").grid(row = 0, column = 0)
        title2 = tk.Label(self, text = "Please enter the questionID(split with ','):").grid(row = 2)

        #entry box for get assignment number
        self.box1 = tk.Entry(self, bd=5)
        self.box1.grid(row=1, column =0)

        #text box for questionid
        self.box2 = tk.Text(self, height=15, width=45)
        self.box2.grid(row = 3)

        #add submit button
        submit = tk.Button(self, text="Submit", command = self.add_assign())
        submit.grid(row = 5)


    def add_assign(self):
        #get assign num
        assgnID = self.box1.get()
        ques = self.box2.get("1.0", "end")
        ques = ques.split(',')
        #connect to database and insert assignmentID and questions
        if(len(assgnID)>0 and len(ques)>0):
            dbWriter = databaseAPI.databaseWriter.addAssignment(assgnID, ques)



if __name__ == '__main__':
    page = AddAssignmentPage()