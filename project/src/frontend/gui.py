import tkinter as tk
from Page import Page
from SubmitQuestionsPage import SubmitQuestionsPage
from ViewQuestionsPage import ViewQuestionsPage
from SearchQuestionsPage import SearchQuestionsPage
from AddAssignmentPage import AddAssignmentPage
from ViewAssignmentPage import ViewAssignmentPage

# Main Page of the app which consists of buttons to change between pages.
class MainApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # Create instances of each page type
        submit_question_page = SubmitQuestionsPage(self)
        view_questions_page = ViewQuestionsPage(self)
        search_questions_page = SearchQuestionsPage(self)
        add_assignment_page = AddAssignmentPage(self)
        view_assignment_page = ViewAssignmentPage(self)
        # Hacky way to execute multiple commands on one button press
        def loadViewQuestionsAndRefresh():
            view_questions_page.refreshQuestions()
            view_questions_page.lift()

        # Create button bar and put it onto the main page
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # Route the pages to corresponding buttons
        submit_question_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        view_questions_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        search_questions_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        add_assignment_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        view_assignment_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Create buttons to go to other pages
        submit_question_button = tk.Button(buttonframe, text="Submit A Question", command=submit_question_page.lift)
        view_questions_button = tk.Button(buttonframe, text="View Questions", command=loadViewQuestionsAndRefresh)
        search_questions_button = tk.Button(buttonframe, text="Search Questions", command=search_questions_page.lift)
        add_assignment_button = tk.Button(buttonframe, text="Add Assignment", command=add_assignment_page.lift)
        view_assignment_button = tk.Button(buttonframe, text="View Assignment", command=view_questions_page.lift)

        # Place the buttons onto the button bar
        submit_question_button.pack(side="left")
        view_questions_button.pack(side="left")
        search_questions_button.pack(side="left")
        add_assignment_button.pack(side="left")
        view_assignment_button.pack(side="left")
        submit_question_page.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainApp(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x600")
    root.mainloop()

