from .databaseConnector import Connector as c
from typing import List

'''
The purpose of this appliance is to have the ability to write to the database
given a writing query (WE SHOULD LIMIT THE DB WRITING TO THIS OBJECT)

'''
connector = c()    # singleton instance
def add_assignment(name: str, problem_ids: List[str]) -> str:
    '''Adds an assignment with the given assignment information.

    Args:
        name: The name of the assignment
        problem_ids: the list of problem_id for this assignment
    Return:
        the assignment_id of the newly created assignment.
    '''
    add_assignment = "INSERT INTO Assignment (Name) VALUES (%s)"
    assign_problem = "INSERT INTO AssignmentQuestions (ProblemID, AssignmentID) VALUES (%s, %s)"
    cnx = connector.getConnection()
    cursor = cnx.cursor()

    data_assignment = (name,)
    cursor.execute(add_assignment, data_assignment)
    assignment_id = cursor.lastrowid

    for problem_id in problem_ids:
        cursor.execute(assign_problem, (problem_id, assignment_id))

    cnx.commit()
    cursor.close()
    cnx.close()
    return assignment_id


def add_question(description: str, answer: str) -> str:
    '''Adds a question with a description and answer.

    Args:
        description: The description of the question (ie. the actual question)
        answer: the answer to the question
    Return:
        the question_id of the newly created question.
    '''
    add_question = "INSERT INTO Question (Description, Choice, Answer) VALUES (%s, %s, %s)"
    cnx = connector.getConnection()
    cursor = cnx.cursor()

    data_question = (description, "", answer)
    cursor.execute(add_question, data_question)
    question_id = cursor.lastrowid

    cnx.commit()
    cursor.close()
    cnx.close()
    return question_id


if __name__ == "__main__":
   question_id = add_question("question?", "answer?")
   add_assignment = add_assignment('first assignment', [question_id])