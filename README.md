# SAT Solver

This is a Python-based SAT solver implementation created as part of the MIT 6.1010 course.

## Overview
The goal of this project is to provide a programmatic interface for solving boolean satisfiability problems. The system can evaluate Boolean formulas formatted in Conjunctive Normal Form (CNF) and find variables assignments that satisfy all clauses.

### Features
- **CNF Evaluation**: Can effectively process and evaluate boolean formulas represented in CNF.
- **Satisfiability**: Determines if a satisfying assignment exists for a given formula and returns one if it does.
- **Problem Modeling**: Includes an application to model real-world constraints—such as a student room-scheduling problem—into Boolean formulas that the SAT solver can resolve.

## Files
- `lab.py`: The core SAT solver implementation, including logic for updating formulas, finding satisfying assignments, and generating boolean formulas for the scheduling problem.
- `server.py`: A web server to interact with the solver.
- `test.py`: Unit tests to verify the solver logic.
