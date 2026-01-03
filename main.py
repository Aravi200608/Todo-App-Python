import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")

def toggle_task(tasks):
    show_tasks(tasks)
    idx = int(input("Task number to toggle: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = not tasks[idx]["done"]
        save_tasks(tasks)
        print("Task updated.")

def delete_task(tasks):
    show_tasks(tasks)
    idx = int(input("Task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)
        print("Task deleted.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Add  2.Show  3.Toggle  4.Delete  5.Exit")
        ch = input("Choose: ")
        if ch == "1": add_task(tasks)
        elif ch == "2": show_tasks(tasks)
        elif ch == "3": toggle_task(tasks)
        elif ch == "4": delete_task(tasks)
        elif ch == "5": break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()