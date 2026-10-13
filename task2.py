operations = [(1, 100.0), (3, 250.5), (1, 50.0), (12, 400.0), (3, 20.0)]

totals = [0.0] * 12         # масив фіксованого розміру
for month, amount in operations:
    totals[month - 1] += amount   # номер місяця слугує індексом

for i in range(12):
    print(f"Місяць {i + 1}: {totals[i]}")
