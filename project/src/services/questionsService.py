import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from databaseAPI import databaseReader as r, databaseWriter as w

def pushNewQuestion(question, answer):
    w.add_question(question, answer) if (question and answer is not ('' or None)) else None

def pullAllQuestions():
    questions = [x[0] for x in r.getQuestions()]

    return questions

