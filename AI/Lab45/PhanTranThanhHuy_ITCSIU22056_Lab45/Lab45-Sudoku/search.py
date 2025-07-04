"""
In search.py, you will implement Backtracking and AC3 searching algorithms
for solving Sudoku problem which is called by sudoku.py
"""

from csp import *
from copy import deepcopy
import util
from collections import deque

def Backtracking_Search(csp):
    """
    Backtracking search initialize the initial assignment
    and calls the recursive backtrack function
    """
    "***YOUR CODE HERE ***"
    if not AC3(csp):  # Optional preprocessing
        return None

    # Initial assignment: variables with a single value
    assignment = dict((v, csp.values[v]) for v in csp.variables if len(csp.values[v]) == 1)
    return Recursive_Backtracking(assignment, csp)

def Recursive_Backtracking(assignment, csp):
    """
    The recursive function which assigns value using backtracking
    """
    "***YOUR CODE HERE ***"
    if isComplete(assignment):
        return assignment

    var = Select_Unassigned_Variables(assignment, csp)
    for value in Order_Domain_Values(var, assignment, csp):
        if isConsistent(var, value, assignment, csp):
            local_assignment = assignment.copy()
            local_assignment[var] = value

            # Optimized deepcopy
            local_csp = deepcopy(csp)
            local_csp.peers = csp.peers  # Avoid deepcopying large static structure

            inferences = {}

            if Inference(local_assignment, inferences, local_csp, var, value) != "FAILURE":
                local_assignment.update(inferences)
                result = Recursive_Backtracking(local_assignment, local_csp)
                if result:
                    return result
    return None

def Inference(assignment, inferences, csp, var, value):
    """
    Forward checking using concept of Inferences
    """

    inferences[var] = value

    for neighbor in csp.peers[var]:
        if neighbor not in assignment and value in csp.values[neighbor]:
            if len(csp.values[neighbor]) == 1:
                return "FAILURE"

            remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

            if len(remaining) == 1:
                flag = Inference(assignment, inferences, csp, neighbor, remaining)
                if flag == "FAILURE":
                    return "FAILURE"

    return inferences

def Order_Domain_Values(var, assignment, csp):
    """
    Returns string of values of given variable
    """
    return csp.values[var]

def Select_Unassigned_Variables(assignment, csp):
    """
    Selects new variable to be assigned using minimum remaining value (MRV)
    """
    unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv

def isComplete(assignment):
    """
    Check if assignment is complete
    """
    return set(assignment.keys()) == set(squares)

def isConsistent(var, value, assignment, csp):
    """
    Check if assignment is consistent
    """
    for neighbor in csp.peers[var]:
        if neighbor in assignment.keys() and assignment[neighbor] == value:
            return False
    return True

def forward_checking(csp, assignment, var, value):
    csp.values[var] = value
    for neighbor in csp.peers[var]:
        csp.values[neighbor] = csp.values[neighbor].replace(value, '')

def display(values):
    """
    Display the solved sudoku on screen
    """
    for row in rows:
        if row in 'DG':
            print("-------------------------------------------")
        for col in cols:
            if col in '47':
                print(' | ', values[row + col], ' ', end=' ')
            else:
                print(values[row + col], ' ', end=' ')
        print(end='\n')

def write(values):
    """
    Write the string output of solved sudoku to file
    """
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output


def AC3(csp):
    """
    AC-3 algorithm for constraint propagation.
    Returns True if arc consistency is enforced throughout the CSP.
    """
    queue = deque([(Xi, Xj) for Xi in csp.variables for Xj in csp.peers[Xi]])

    while queue:
        Xi, Xj = queue.popleft()
        if Revise(csp, Xi, Xj):
            if len(csp.values[Xi]) == 0:
                return False  # Failure
            for Xk in csp.peers[Xi] - {Xj}:
                queue.append((Xk, Xi))
    return True


def Revise(csp, Xi, Xj):
    """
    Revise the domain of Xi to enforce arc consistency with Xj.
    Returns True if domain of Xi was revised.
    """
    revised = False
    to_remove = []

    for x in csp.values[Xi]:
        # If no value y in Xj allows (x, y) to satisfy the constraint, remove x
        if all(x == y for y in csp.values[Xj]):
            to_remove.append(x)

    if to_remove:
        for val in to_remove:
            csp.values[Xi] = csp.values[Xi].replace(val, '')
        revised = True

    return revised