import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from databaseAPI import databaseReader as r, databaseWriter as w

def pushNewAssignment(assignmentName, questionIDs):
    return w.add_assignment(assignmentName, questionIDs);

def getAllAssignments():
    return r.get_assign();

def getAssignment(assignment_id):
    return r.get_single_assign(assignment_id)



