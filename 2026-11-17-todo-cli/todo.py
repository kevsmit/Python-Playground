import json
import os
import sys

TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE) as f:
        return json.load(f)


def save(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def show(todos):
    if not todos:
        print("Nothing to do.")
        return
    for i, item in enumerate(todos, start=1):
        mark = "x" if item["done"] else " "
        print(f"{i}. [{mark}] {item['text']}")


def get_index(todos, arg):
    try:
        n = int(arg)
    except ValueError:
        sys.exit(f"Not a number: {arg}")
    if n < 1 or n > len(todos):
        sys.exit(f"No item #{n}")
    return n - 1


def main():
    args = sys.argv[1:]
    todos = load()

    if not args or args[0] == "list":
        show(todos)
    elif args[0] == "add" and len(args) > 1:
        todos.append({"text": " ".join(args[1:]), "done": False})
        save(todos)
        print(f"Added #{len(todos)}")
    elif args[0] == "done" and len(args) == 2:
        i = get_index(todos, args[1])
        todos[i]["done"] = True
        save(todos)
        print(f"Marked #{i + 1} done")
    elif args[0] == "remove" and len(args) == 2:
        i = get_index(todos, args[1])
        removed = todos.pop(i)
        save(todos)
        print(f"Removed: {removed['text']}")
    elif args[0] == "clear":
        todos = [t for t in todos if not t["done"]]
        save(todos)
        print("Cleared finished items")
    else:
        print("Usage: python todo.py [list | add TEXT | done N | remove N | clear]")


if __name__ == "__main__":
    main()
