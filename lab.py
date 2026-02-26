"""
6.101 Lab:
SAT Solver
"""

#!/usr/bin/env python3

# import typing  # optional import
# import pprint  # optional import
import doctest
import sys

sys.setrecursionlimit(10_000)
# NO ADDITIONAL IMPORTS

def update_formula(formula, assignment):
    #clause is [(c, True), [d. False]]
    res = []
    for idx, clause in enumerate(formula):
        if assignment in clause:
            continue
        else:
            tmp = []
            for j, literal in enumerate(clause):
                if(literal[0] == assignment[0]):
                    if(literal[1] ^ assignment[1] ==True):
                        continue
                else:
                    tmp.append(literal)
            res.append(tmp)
    return res

original_formula = [
    [('a', True), ('b', True), ('c', True)],
    [('a', False), ('f', True)],
    [('a', False), ('f', False)],
    [('d', False), ('e', True), ('a', True), ('g', True)],
    [('h', False), ('c', True), ('a', False)]
]
res = update_formula(original_formula, ('a', True))
res = update_formula(res, ('f', True))
print(res)





def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise. Does not
    mutate input formula.

    >>> satisfying_assignment([])
    {}
    >>> T, F = True, False
    >>> x = satisfying_assignment([[('a', T), ('b', F), ('c', T)]])
    >>> x.get('a', None) is T or x.get('b', None) is F or x.get('c', None) is T
    True
    >>> satisfying_assignment([[('a', T)], [('a', F)]])
    """
    raise NotImplementedError


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