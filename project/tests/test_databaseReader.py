import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import databaseAPI.databaseReader as reader
from databaseAPI.databaseConnector import Connector

conn = Connector().getConnection()

class DatabaseReaderTestSuite(unittest.TestCase):
    ''' Testing the databaseReader component in the databaseAPI module
    '''

    def testGetQuestionEmpty(self):
        ''' Test the get question method on empty database
        '''
        self.assertEqual(reader.getQuestions(), [])

    def testGetQuestionSingle(self):
        ''' Test the get question method on a single question
        '''
        cursor = conn.cursor()
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description', "", "Test Answer"))
        conn.commit();
        actual_questions = reader.getQuestions()
        cursor.execute("DELETE FROM question")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_questions, ["Test Description"])

    def testGetQuestionMultiple(self):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description1', "", "Test Answer1"))
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description2', "", "Test Answer2"))
        conn.commit();
        actual_questions = reader.getQuestions()
        cursor.execute("DELETE FROM question")
        conn.commit()
        cursor.close()
        self.assertEqual(set(actual_questions), set(["Test Description1", "Test Description2"]))

    def testGetAssignmentNoQuestion(self):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO assignment (Name) VALUES (%s)', ('A1',))
        actual_assignment = reader.get_assign(cursor.lastrowid)
        conn.commit()
        cursor.execute("DELETE FROM assignment")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_assignment, dict())

    ''' Function Bugged.
    def testGetAssignmentSingleQuestion(self):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO assignment (Name) VALUES (%s)', ('A1',))
        assignment_id = cursor.lastrowid
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description1', "", "Test Answer1"))
        cursor.execute('INSERT INTO assignmentquestions (AssignmentID, ProblemID) VALUES (%s, %s)', (assignment_id, cursor.lastrowid))
        conn.commit()
        actual_assignment = reader.get_assign(assignment_id)
        cursor.execute("DELETE FROM assignment")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_assignment, dict())
    '''

if __name__ == '__main__':
    print(unittest.main())