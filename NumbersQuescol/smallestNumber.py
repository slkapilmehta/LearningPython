def small(items):
    if len(items) > 0:
        smallest = items[0]
        for item in items:
            if smallest > item:
                smallest = item

        return smallest
    else:
        print("none")

items = [1,2,-3,9, -3, -27, -27, 0]
print(small(items))