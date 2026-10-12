print("Shopping list maker")
items = []

while True:
    item = input("Add an item (blank to finish): ").strip()
    if not item:
        break
    items.append(item)

if not items:
    print("Your list is empty.")
else:
    unique = {}
    for item in items:
        unique[item.casefold()] = item

    print("\nYour shopping list:")
    for number, item in enumerate(sorted(unique.values(), key=str.casefold), 1):
        print(f"{number}. {item}")
