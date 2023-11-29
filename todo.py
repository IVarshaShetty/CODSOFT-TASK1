import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        self.canvas = tk.Canvas(root, bg="#F5F5F5", height=300, width=400)
        self.canvas.pack()
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 10), bg="#4CAF50", fg="white")
        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks, font=("Helvetica", 10), bg="#008CBA", fg="white")
        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed, font=("Helvetica", 10), bg="#FF9800", fg="white")
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Helvetica", 10), bg="#FF0000", fg="white")
        self.task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 10))
        self.task_listbox.pack()
        self.canvas.create_window(200, 40, window=self.task_entry)
        self.canvas.create_window(200, 80, window=self.add_button)
        self.canvas.create_window(200, 120, window=self.view_button)
        self.canvas.create_window(200, 160, window=self.mark_button)
        self.canvas.create_window(200, 200, window=self.delete_button)
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, f"{len(self.tasks)}. {task} - Not Completed")
            self.task_entry.delete(0, tk.END) 
        else:
            self.show_error("Please enter a task.")
    def view_tasks(self):
        if self.tasks:
            self.task_listbox.delete(0, tk.END)  
            for index, task in enumerate(self.tasks):
                status = 'Completed' if task['completed'] else 'Not Completed'
                self.task_listbox.insert(tk.END, f"{index + 1}. {task['task']} - {status}")
        else:
            self.show_info("No tasks in the list.")
    def mark_completed(self):
        selected_task_index = self.get_selected_index()
        if selected_task_index is not None:
            self.tasks[selected_task_index]["completed"] = True
            self.show_info("Task marked as completed.")
            self.view_tasks() 
            self.show_error("Please select a task.")
    def delete_task(self):
        selected_task_index = self.get_selected_index()
        if selected_task_index is not None:
            deleted_task = self.tasks.pop(selected_task_index)
            self.show_info(f"Task deleted: {deleted_task['task']}")
            self.view_tasks() 
        else:
            self.show_error("Please select a task.")
    def get_selected_index(self):
        try:
            selected_task_index = int(self.task_listbox.curselection()[0])
            if not (0 <= selected_task_index < len(self.tasks)):
                selected_task_index = None
        except (ValueError, IndexError):
            selected_task_index = None
        return selected_task_index
    def show_info(self, message):
        tk.messagebox.showinfo("Info", message)
    def show_error(self, message):
        tk.messagebox.showerror("Error", message)
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

