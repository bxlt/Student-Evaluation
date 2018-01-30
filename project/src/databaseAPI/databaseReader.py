from .databaseConnector import Connector as c

'''
The purpose of this appliance is to send queries to the dataabase to retrieve 
data as read-only after a secure connector has been made.
'''

connector = c()    # singleton instance

def getQuestions():
    ''' None -> list of tuples representing the rows of the question
    Returns a list of rows (in tuples) from the questions entity
    '''

    cnx = connector.getConnection()
    cursor = cnx.cursor()

    query = ("SELECT Description FROM  `Question` LIMIT 0 , 30")

    cursor.execute(query)
    rows = cursor.fetchall()

    cnx.close()

    return rows


def get_assign():
    conn = connector.getConnection()
    query = ("SELECT Name FROM  `Assignment` LIMIT 0 , 30")
    if (conn != None):
        # get questionid
        cursor = conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows

def get_single_assign(assignment_id):
    '''Adds an assignment with the given assignment information.

    Args:
        name: The name of the assignment
        problem_ids: the list of problem_id for this assignment
    Return:
        the assignment_id of the newly created assignment.
    '''
    conn = connector.getConnection()
    query = ("SELECT "
                "a.AssignmentID, a.Name, GROUP_CONCAT(b.Description SEPARATOR ',') AS Questions, GROUP_CONCAT(b.Description SEPARATOR ',') AS Answers"
            "FROM Assignment a"
            "JOIN AssignmentQuestions b ON a.AssignmentID=b.AssignmentID"
            "JOIN Question c ON c.QuestionID=b.ProblemID"
            "WHERE a.assignmentID=%s"
            "GROUP BY a.assignmentID"
            "LIMIT 1")
    if (conn != None):
        # get questionid
        cursor = conn.cursor()
        cursor.execute(query, (assignment_id,))

        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows
    return assignment_id

if __name__ == '__main__':
    d = c()                 # test singleton
    print(d == connector)
    print(getQuestions())   # testing
    print(get_assign())
