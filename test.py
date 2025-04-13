import json
import tkinter as tk
from tkinter import ttk

# Define the Task class to represent each task
class Task:
    def __init__(self, name, description, priority, due_date):
        self.name = name
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date
        }

# Define the TaskManager class to handle task operations
class TaskManager:
    def __init__(self, json_file='data.json'):
        self.json_file = json_file
        self.tasks = []
        self.load_tasks_from_json()

    def load_tasks_from_json(self):
        try:
            with open(self.json_file, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [
                    Task(name, data['description'], data['priority'], data['due_date'])
                    for name, data in tasks_data.items()
                ]
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

    def get_filtered_tasks(self, name_filter=None, priority_filter=None, due_date_filter=None):
        filtered = self.tasks
        if name_filter:
            filtered = [task for task in filtered if name_filter.lower() in task.name.lower()]
        if priority_filter and priority_filter != "All":
            filtered = [task for task in filtered if task.priority.lower() == priority_filter.lower()]
        if due_date_filter:
            filtered = [task for task in filtered if task.due_date == due_date_filter]
        return filtered

    def sort_tasks(self, sort_key='name', reverse=False):
        self.tasks.sort(key=lambda task: getattr(task, sort_key), reverse=reverse)


# Define the TaskManagerGUI class to create the Tkinter interface
class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.task_manager = TaskManager()
        self.sort_order = {
            'name': True,
            'description': True,
            'priority': True,
            'due_date': True
        }
        self.setup_gui()
        self.populate_tree()

    def setup_gui(self):
        # Search/filter fields
        tk.Label(self.root, text="Name:", font=("Poppins", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Priority:", font=("Poppins", 12)).grid(row=0, column=2, padx=5, pady=5)
        self.priority_var = tk.StringVar()
        self.priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var)
        self.priority_dropdown['values'] = ("All", "High", "Medium", "Low")
        self.priority_dropdown.current(0)
        self.priority_dropdown.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.root, text="Due Date (YYYY-MM-DD):", font=("Poppins", 12)).grid(row=0, column=4, padx=5, pady=5)
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=0, column=5, padx=5, pady=5)

        self.filter_button = tk.Button(self.root, text="Filter", command=self.apply_filter, font=("Poppins", 10, "bold"))
        self.filter_button.grid(row=0, column=6, padx=5, pady=5)

        # Treeview
        columns = ('name', 'description', 'priority', 'due_date')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize(), command=lambda _col=col: self.sort_tasks(_col))
            self.tree.column(col, width=150)
        self.tree.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

    def populate_tree(self, tasks=None):
        for i in self.tree.get_children():
            self.tree.delete(i)

        if tasks is None:
            tasks = self.task_manager.tasks

        for task in tasks:
            self.tree.insert('', 'end', values=(
                task.name, task.description, task.priority, task.due_date))

    def apply_filter(self):
        name_filter = self.name_entry.get()
        priority_filter = self.priority_var.get()
        due_date_filter = self.due_date_entry.get()
        filtered_tasks = self.task_manager.get_filtered_tasks(name_filter, priority_filter, due_date_filter)
        self.populate_tree(filtered_tasks)

    def sort_tasks(self, sort_key):
        reverse = not self.sort_order[sort_key]
        self.task_manager.sort_tasks(sort_key, reverse=reverse)
        self.populate_tree()
        self.sort_order[sort_key] = reverse


# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
