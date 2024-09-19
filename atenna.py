from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# Adjacent antennae need to operate with different frequencies
freqs = {0 : 'f1', 1:'f2', 2:'f3'}
A1 = model.NewIntVar(0, 2, 'A1')
A2 = model.NewIntVar(0, 2, 'A2')
A3 = model.NewIntVar(0, 2, 'A3')
A4 = model.NewIntVar(0, 2, 'A4')
A5 = model.NewIntVar(0, 2, 'A5')
A6 = model.NewIntVar(0, 2, 'A6')
A7 = model.NewIntVar(0, 2, 'A7')
A8 = model.NewIntVar(0, 2, 'A8')
A9 = model.NewIntVar(0, 2, 'A9')

# Antenna 1 is adjacent to 2, 3, and 4
model.Add(A1 != A2)
model.Add(A1 != A3)
model.Add(A1 != A4)

# Antenna 2 is adjacent to 1, 3, 5, and 6
model.Add(A2 != A1)
model.Add(A2 != A3)
model.Add(A2 != A5)
model.Add(A2 != A6)

# Antenna 3 is adjacent to 1, 2, 6, and 9
model.Add(A3 != A1)
model.Add(A3 != A2)
model.Add(A3 != A6)
model.Add(A3 != A9)

# Antenna 4 is adjacent to 1, 2, and 5.
model.Add(A4 != A1)
model.Add(A4 != A2)
model.Add(A4 != A5)

# Antenna 5 is adjacent to 2 and 4
model.Add(A5 != A2)
model.Add(A5 != A4)

# Antenna 6 is adjacent to 2, 7 and 8
model.Add(A6 != A2)
model.Add(A6 != A7)
model.Add(A6 != A8)

# Antenna 7 is adjacent to 6 and 8
model.Add(A7 != A6)
model.Add(A7 != A8)

# Antenna 8 is adjacent to 7 and 9
model.Add(A8 != A7)
model.Add(A8 != A9)

# Antenna 9 is adjacent to 3 and 8
model.Add(A9 != A3)
model.Add(A9 != A8)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("A1: %s" % freqs[solver.Value(A1)])
    print("A2: %s" % freqs[solver.Value(A2)])
    print("A3: %s" % freqs[solver.Value(A3)])
    print("A4: %s" % freqs[solver.Value(A4)])
    print("A5: %s" % freqs[solver.Value(A5)])
    print("A6: %s" % freqs[solver.Value(A6)])
    print("A7: %s" % freqs[solver.Value(A7)])
    print("A8: %s" % freqs[solver.Value(A8)])
    print("A9: %s" % freqs[solver.Value(A9)])