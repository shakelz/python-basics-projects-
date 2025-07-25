# Todo List

# first let's try to make a function for the options here

def show_menu():
  print("\n📝 To-Do List Menu:")
  print("1. Show Tasks")
  print("2. Add Task")
  print("3. Delete Task")
  print("4. Exit")

def show_list(task):  # if something is repeating then make a function of it
  print("Showing your tasks...")
  for idx, task in enumerate(task, start=1):
    print(f"{idx}. {task}")

task = [] # create a list to add/delete the task

while True:
  show_menu() #Show the menu here
  choice = input("Enter your choice: ")
  if choice == "1":
    if not task:
      print("📭 No tasks found.")
    else:
      print("Showing your tasks...")
      show_list(task)
     
  elif choice == "2":
    print("Adding task...")
    new_task = input("Enter the task you want to add\n")
    task.append(new_task.lower())
  elif choice == "3":
    print("Deleting task...")
    if not task:
      print("No tasks to delete.")
    else:
      print("Showing your tasks...")
      show_list(task) 
      task_index = int(input("Enter the task number to delete: "))
      if 1<= task_index <= len(task):
        del_task = task.pop(task_index -1)
        print(f"Deleted task :{del_task}")
      else:
        print("Invalid task number.")
  elif choice == "4":
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
