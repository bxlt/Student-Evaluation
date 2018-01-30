import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import databaseAPI.databaseWriter as writer
from databaseAPI.databaseConnector import Connector

conn = Connector().getConnection()

class DatabaseWriterTestSuite(unittest.TestCase):

    def _getAssignment(self, cursor, assignment_id):
        cursor.execute(
            '''SELECT a.Name, GROUP_CONCAT(b.ProblemID SEPARATOR ",") as ProblemIDs
                FROM Assignment a
                LEFT JOIN AssignmentQuestions b ON a.AssignmentID=b.AssignmentID
                WHERE a.AssignmentID=%s
                GROUP BY a.AssignmentID
                LIMIT 1''',
            (assignment_id,))
        res = cursor.next()
        ProblemIDS = []
        if (res[1]):
            ProblemIDS = res[1].split(',')
        return {
            "Name": res[0],
            "ProblemIDs": ProblemIDS
        }

    ''' Testing the databaseReader component in the databaseAPI module
    '''
    def testAddAssignmentNoQuestions(self):
        assignment_id = writer.add_assignment('A1', [])
        cursor = conn.cursor()
        actual_assignment = self._getAssignment(cursor, assignment_id)
        cursor.execute("DELETE FROM Assignment");
        cursor.execute("DELETE FROM AssignmentQuestions")
        cursor.execute("DELETE FROM Question")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_assignment, {
            "Name": "A1",
            "ProblemIDs": []
            })

    def testAddAssignmentSingleQuestions(self):
        cursor = conn.cursor()
        questions = []
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description1', "", "Test Answer1"))
        questions.append(str(cursor.lastrowid))
        assignment_id = writer.add_assignment('A1', questions)
        actual_assignment = self._getAssignment(cursor, assignment_id)
        cursor.execute("DELETE FROM Assignment");
        cursor.execute("DELETE FROM AssignmentQuestions")
        cursor.execute("DELETE FROM Question")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_assignment, {
            "Name": "A1",
            "ProblemIDs": questions
            })

    def testAddAssignmentMultipleQuestions(self):
        cursor = conn.cursor()
        questions = []
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description1', "", "Test Answer1"))
        questions.append(str(cursor.lastrowid))
        cursor.execute('INSERT INTO question (Description, Choice, Answer) VALUES (%s, %s, %s)', ('Test Description2', "", "Test Answer2"))
        questions.append(str(cursor.lastrowid))
        assignment_id = writer.add_assignment('A1', questions)
        actual_assignment = self._getAssignment(cursor, assignment_id)
        cursor.execute("DELETE FROM Assignment");
        cursor.execute("DELETE FROM AssignmentQuestions")
        cursor.execute("DELETE FROM Question")
        conn.commit()
        cursor.close()
        self.assertEqual(actual_assignment, {
            "Name": "A1",
            "ProblemIDs": questions
            })

if __name__ == '__main__':
    print(unittest.main())
