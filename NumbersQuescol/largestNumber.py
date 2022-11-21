
def largest(items):
    largest = items[0]

    for item in items:
        if largest < item:
            largest = item
    return largest

items = [10, -1, 0, 12, 1, 100, 100, 1, 0, 21, -2]

print(largest(items))