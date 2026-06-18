def add_item(item , items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))
#  This is the concept of mutable default argument 