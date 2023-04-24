from pulp import *
from tabulate import tabulate

prob1 = LpProblem("f1", LpMinimize)
prob07 = LpProblem("f07", LpMinimize)
prob05 = LpProblem("f05", LpMinimize)

x11 = LpVariable("x1", lowBound=0)
x21 = LpVariable("x2", lowBound=0)

x107 = LpVariable("x1", lowBound=0)
x207 = LpVariable("x2", lowBound=0)

x105 = LpVariable("x1", lowBound=0)
x205 = LpVariable("x2", lowBound=0)

prob1 += x11 + 2*x21 >= 2
prob1 += 2*x11 + 5*x21 <= 10
prob1 += 12*x11 + 8*x21 <= 24

prob1 += 2*x11 + 3*x21

prob1.solve()

prob07 += x107 + 2*x207 >= 1
prob07 += 2*x107 + 5*x207 <= 11
prob07 += 12*x107 + 8*x207 <= 25

prob07 += 2*x107 + 3*x207

prob07.solve()

prob05 += x105 + 2*x205 >= 0
prob05 += 2*x105 + 5*x205 <= 12
prob05 += 12*x105 + 8*x205 <= 26

prob05 += 2*x105 + 3*x205

prob05.solve()

tabl = []

row = []

for v in prob1.variables():
    row.append(v.varValue)

row.append(value(prob1.objective))
row.append(1)
tabl.append(row)

row = []

for v in prob07.variables():
    row.append(v.varValue)

row.append(value(prob07.objective))
row.append(0.7)
tabl.append(row)

row = []

for v in prob05.variables():
    row.append(v.varValue)

row.append(value(prob05.objective))
row.append(0.5)
tabl.append(row)

print(tabulate(tabl, headers=["x1", "x2", "f", "lambda"], tablefmt='grid'))