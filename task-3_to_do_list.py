class Task:
  def __init__(self, title, description=""):
    self.title = title
    self.description = description
    self.completed = False  # Track task completion status

tasks = []  # List to store tasks

def create_task():
  title = input("Enter task title: ")
  description = input("Enter task description (optional): ")
  tasks.append(Task(title, description))
  print("Task created successfully!")

def view_tasks():
  if not tasks:
    print("There are no tasks to display.")
    return
  print("\nTasks:")
  for i, task in enumerate(tasks):
    completion_status = "Completed" if task.completed else "Pending"
    print(f"{i+1}. {task.title} ({completion_status})")
  print("")

def update_task():
  if not tasks:
    print("There are no tasks to update.")
    return
  view_tasks()
  try:
    task_index = int(input("Enter the number of the task to update: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
      print("Invalid task number.")
      return
    task = tasks[task_index]
    new_title = input("Enter a new title (or leave blank to keep current): ")
    if new_title:
      task.title = new_title
    new_description = input("Enter a new description (or leave blank to keep current): ")
    if new_description:
      task.description = new_description
    print("Task updated successfully!")
  except ValueError:
    print("Invalid input. Please enter a number.")

def delete_task():
  if not tasks:
    print("There are no tasks to delete.")
    return
  view_tasks()
  try:
    task_index = int(input("Enter the number of the task to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
      print("Invalid task number.")
      return
    del tasks[task_index]
    print("Task deleted successfully!")
  except ValueError:
    print("Invalid input. Please enter a number.")

def mark_complete():
  if not tasks:
    print("There are no tasks to mark complete.")
    return
  view_tasks()
  try:
    task_index = int(input("Enter the number of the task to mark complete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
      print("Invalid task number.")
      return
    tasks[task_index].completed = True
    print("Task marked complete successfully!")
  except ValueError:
    print("Invalid input. Please enter a number.")

def main_menu():
  print("\nTask Management System")
  print("1. Create Task")
  print("2. View Tasks")
  print("3. Update Task")
  print("4. Delete Task")
  print("5. Mark Task Complete")
  print("6. Exit")
  choice = input("Enter your choice: ")
  return choice

while True:
  choice = main_menu()
  if choice == '1':
    create_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    update_task()
  elif choice == '4':
    delete_task()
  elif choice == '5':
    mark_complete()
  elif choice == '6':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
