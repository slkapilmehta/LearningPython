expense = [2200, 2350, 2600, 2130, 2190]

diff = expense[1]-expense[0]
print(diff)

if 2000 in expense:
    print("yes")
else:
    print("no")

expense.insert(1, 1950)
print(expense)