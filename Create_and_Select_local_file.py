
import os

#select the new file
def select_new_file():
    print("Select an existing file:")
    files = os.listdir()  # ✅ use plural name
    for index, f in enumerate(files, start=1):
        print(f"{index}. {f}")
    
    try:
        file_index = int(input("Enter the file number: "))
        if 1 <= file_index <= len(files):
            selected_file = files[file_index - 1]
            print(f"✅ Selected file: {selected_file}")
            return selected_file
        else:
            print("❌ Invalid file number.")
            return None
    except ValueError:
        print("❌ Please enter a valid number.")
        return None


# Create or select a new file
def create_new_file_or_select_existing_file():
   print("Want to create a new file?")
   choice = input("Enter your choice (yes/no): ")

   if choice.lower() == 'yes':
    new_file_name = input("Enter the file name (e.g., notes.txt):\n")
    try:
      with open(new_file_name, 'x') as file:
        print(f"New file '{new_file_name}' created successfully.")
        return new_file_name
    except FileExistsError:
      print(f"File '{new_file_name}' already exists and selecting it by default.")
      return new_file_name
   else:
    return select_new_file()
    
    


def show_menu():
  print("\n📁 File Reader & Writer")
  print("0. Select new File")
  print("1. Read file")
  print("2. Write to file")
  print("3. Exit")
  print("4. Create a new File")

filename = create_new_file_or_select_existing_file()


while True:
  show_menu()
  choice = input("Enter your choice: ")
   
  if choice == '0':
    temp_file = select_new_file()
    if temp_file:
        filename = temp_file
  
  elif choice == '1':
    print("----------Reading the File----------")
    try:
      with open(filename, 'r') as file:
        content = file.read()
        print(content if content else "File is empty.")
    except FileNotFoundError:
      print(f"File '{filename}' not found.")

  elif choice == '2':
    content = input("Enter the content to write to the file: ")
    print("----------Writing to the File----------")
    with open(filename, 'a') as f:
      f.write(content + '\n')
      print(f"'{content}' is written to the file successfully.")

  elif choice == '3':
    print("Exiting the program.")
    break
  
  elif choice == '4':
    temp_file = create_new_file_or_select_existing_file()
    if temp_file:
        filename = temp_file
    
    

  else:
    print("Invalid choice. Please try again.")
