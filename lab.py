"""
6.101 Lab:
SAT Solver
"""

#!/usr/bin/env python3

# import typing  # optional import
import pprint  # optional import
import doctest
import sys

sys.setrecursionlimit(10_000)
# NO ADDITIONAL IMPORTS

def update_formula(formula, assignment):
    #clause is [(c, True), [d. False]]
    res = []
    for  clause in formula:
        if assignment in clause:
            continue
        else:
            tmp = []
            for literal in clause:
                if(literal[0] == assignment[0]):
                    if(literal[1] ^ assignment[1] ==True):
                        continue
                else:
                    tmp.append(literal)
            res.append(tmp)
    return res


def has_single_clause(formula):
    for clause in formula:
        if(len(clause) == 1):
            return True
        

def get_single_clause(formula):
    for clause in formula:
        if(len(clause) == 1):
            yield clause

def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise. Does not
    mutate input formula.
    """""

    res ={}
    def helper(x):
        if x == [[]]:
            return None
        if(x == []):
            return res
        else:
            for clause in get_single_clause(x):
                for literal in clause:
                    if(literal[0] in res):
                        continue
                    f = update_formula(x, literal)
                    res[literal[0]] = literal[1]
                    recur = helper(f)
                    if(recur == None):
                        del res[literal[0]]
                        return None
                    if(recur != None):
                        return res
            
            clause = x[0]
            for literal in clause:
                if(literal[0] in res):
                    continue
                f = update_formula(x, literal)
                if([] in f):
                    return None
                res[literal[0]] = literal[1]
                recur = helper(f)
                if(recur != None):
                    return res
                else:
                    del res[literal[0]]
    return helper(formula)




cnf = [[('a', True), ('b', True)], [('a', False), ('b', False), ('c', True)], [('b', True), ('c', True)], [('b', True), ('c', False)]]
print(satisfying_assignment(cnf))


def boolify_scheduling_problem(student_preferences, room_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of room names (strings) that work for that student

    room_capacities: a dictionary mapping each room name to a positive integer
                     for how many students can fit in that room

    Returns: a CNF formula encoding the scheduling problem which can serve as
        an input to satisfying_assignment, as per the lab write-up

    We assume no student or room names contain underscores. This function
    should not mutate its inputs.
    """
    raise NotImplementedError


if __name__ == "__main__":
    #_doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    #doctest.testmod(optionflags=_doctest_flags)
    pass