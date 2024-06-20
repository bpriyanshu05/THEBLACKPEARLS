import sqlite3
from datetime import datetime

class Task:
    def __init__(self, id, description, priority, due_date, completed):
        self.id = id
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

class ToDoList:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             description TEXT,
                             priority TEXT,
                             due_date TEXT,
                             completed INTEGER)''')
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute('''INSERT INTO tasks (description, priority, due_date, completed)
                            VALUES (?, ?, ?, ?)''', (task.description, task.priority, task.due_date, task.completed))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        self.conn.commit()

    def update_task(self, task_id, new_task):
        self.cursor.execute('''UPDATE tasks SET description=?, priority=?, due_date=?, completed=? WHERE id=?''',
                            (new_task.description, new_task.priority, new_task.due_date, new_task.completed, task_id))
        self.conn.commit()

    def view_tasks(self, filter_by=None):
        query = "SELECT * FROM tasks"
        if filter_by:
            query += f" WHERE {filter_by}"
        self.cursor.execute(query)
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(f"ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}, Due Date: {task[3]}, Completed: {task[4]}")

    def close(self):
        self.conn.close()

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            completed = False
            task = Task(None, description, priority, due_date, completed)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
            print("Task deleted successfully.")

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new task description: ")
            priority = input("Enter new task priority (High/Medium/Low): ")
            due_date = input("Enter new task due date (YYYY-MM-DD): ")
            completed = input("Is the task completed? (yes/no): ").lower() == 'yes'
            new_task = Task(task_id, description, priority, due_date, completed)
            todo_list.update_task(task_id, new_task)
            print("Task updated successfully.")

        elif choice == '4':
            filter_choice = input("Filter tasks by (priority/completed/due_date/none): ").lower()
            filter_by = None
            if filter_choice == 'priority':
                priority = input("Enter priority to filter by (High/Medium/Low): ")
                filter_by = f"priority='{priority}'"
            elif filter_choice == 'completed':
                completed = input("Filter by completed tasks only? (yes/no): ").lower() == 'yes'
                filter_by = f"completed={1 if completed else 0}"
            elif filter_choice == 'due_date':
                due_date = input("Enter due date to filter by (YYYY-MM-DD): ")
                filter_by = f"due_date='{due_date}'"
            todo_list.view_tasks(filter_by)

        elif choice == '5':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.update_task(task_id, Task(task_id, "", "", "", True))
            print("Task marked as complete.")

        elif choice == '6':
            todo_list.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
