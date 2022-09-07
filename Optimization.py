# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:19:11 2022
@author: sp7012
"""
from ortools.linear_solver import pywraplp
  
def Maximizationproblem():
 
    solver = pywraplp.Solver.CreateSolver('SCIP')
 
    vara = solver.IntVar(0.0, solver.infinity(), 'vara')
 
    varb = solver.IntVar(0.0, solver.infinity(), 'varb')
 
    varc = solver.IntVar(0.0, solver.infinity(), 'varc')
 
     # 3*a + 6*b + 2*c <= 50
 
    cons_in1 = solver.Constraint(-solver.infinity(), 49)
 
    cons_in1.SetCoefficient(vara, 3)
 
    cons_in1.SetCoefficient(varb, 6)
 
    cons_in1.SetCoefficient(varc, 2)
 
      # 4*a - 6*b + 8*c <= 45
 
    cons_in2 = solver.Constraint(-solver.infinity(), 39)
 
    cons_in2.SetCoefficient(vara, 4)
 
    cons_in2.SetCoefficient(varb, -6)
 
    cons_in2.SetCoefficient(varc, 8)
 
      # 3*a + b - 5*c <= 37
 
    cons_in3 = solver.Constraint(-solver.infinity(), 37)
 
    cons_in3.SetCoefficient(vara, 3)
 
    cons_in3.SetCoefficient(varb, 1)
 
    cons_in3.SetCoefficient(varc, -5)
 
    # [END constraints]
 
      # [objective segment of program]
 
    obj_prog = solver.Objective()
 
    obj_prog.SetCoefficient(vara, 3)
 
    obj_prog.SetCoefficient(varb, 2)
 
    obj_prog.SetCoefficient(varc, 2)
 
    obj_prog.SetMaximization()
 
      # Calling solver
 
    solver.Solve()
  
     # Print segment of program
 
    print('Highest objective function value = %d' % solver.Objective().Value())
 
    print()
  
    for variable in [vara, varb, varc]:
 
        print('%s = %d' % (variable.name(), variable.solution_value()))
 
    Maximizationproblem()