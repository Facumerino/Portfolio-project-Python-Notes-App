#libraries
import os
import time

#classes
class Notebook:

    def __init__(self):

        self.notes_list = []
        self.reminders_list = []
        self.tasks_list = []
        self.menu()

    """With Init you go to Menu"""

#menu displayed to the user
    def menu(self):

        os.system("cls")
        
        print("Welcome back {user}!".format(user = User))
        print("What do you want to do?")

#Check if Notes in notes_list exist, if yes print every Note title
        print("\nCurrent Notes:\n")
        if self.notes_list:
            for note in self.notes_list:
                print(note.title)
        else:
            print("No notes available.")
#Check if reminders in reminders_list exist, if yes print every reminder
        print("\nReminders:\n")
        if self.reminders_list:
            for reminder in self.reminders_list:
                print(reminder.event + " Date: " + reminder.date)
        else:
            print("No reminders available.")
#Check if tasks in tasks_list exist, if yes print every task
        print("\nTasks:\n")
        if self.tasks_list:
            for task in self.tasks_list:
                print(task.title + " Priority: " + task.priority)
        else:
            print("No tasks available.")

#options inside the menu
        print("\n1. Create new Note")
        print("2. Create a new reminder")
        print("3. Create a new task")
        print("4. Delete a task")
        print("5. Delete a reminder")
        print("6. Delete a note")

#takes into account what the user wants to do and ejecute the correct action
        choose = input("\nChoose the option (number) do you want to make: ")
#Create new Note
        if choose == "1":  
                self.create_new_note()
#Create new Reminder                        
        elif choose == "2":
                self.create_new_reminder()  
#create new task
        elif choose == "3":
                self.create_new_task()
        elif choose == "4":
                self.delete_task()
        elif choose == "5":
                self.delete_reminder()
        elif choose == "6":
                self.delete_note()
        else:
            print("Unknown option")
            time.sleep(3)
            self.menu()


 

#create new note function
    def create_new_note(self):
        os.system("cls")

        content = input("Write something to the notebook:\n\n")
        title = input("\nWhats the title?:\n\n")

        """Create new Object from Note class"""
        self.notes_list.append(Note(title, content))

        print("\nnote created successfully!")
        time.sleep(3)

        self.menu()
        
    def delete_note(self, title=None):
        os.system("cls")
        if title is None:
            title = input("Which note do you want to delete?\n\n")
            
        for nt in self.notes_list:
            if nt.title == title:
                self.notes_list.remove(nt)
                print("\nNote deleted successfully!")
            else:
                print("\nNote not found, try again!")
        time.sleep(3)

        self.menu()
        
        time.sleep(3)

        self.menu()

#representation of the notebook
    def repr(self):
        print(self.name)
        
#create new reminder function        
    def create_new_reminder(self):
        os.system("cls")

        event = input("For what do we have to remind you?:\n\n")
        date = input("\nDate:\n\n")

        """Create new Object from Note class"""
        self.reminders_list.append(Reminder(event, date))

        print("\nreminder created successfully!")
        time.sleep(3)

        self.menu()
        
    def delete_reminder(self, event=None):
        os.system("cls")
        if event is None:
            event = input("Which reminder do you want to delete?\n\n")
            
        for rmd in self.reminders_list:
            if rmd.event == event:
                self.reminders_list.remove(rmd)
                print("\nReminder deleted successfully!")
            else:
                print("\nReminder not found, try again!")
        time.sleep(3)

        self.menu()
        
        time.sleep(3)

        self.menu()

#create new task function
    def create_new_task(self):
        os.system("cls")

        title = input("Which task do you want to acomplish?:\n\n")
        priority = input("\nPriority of the task:\n\n")

        """Create new Object from Note class"""
        self.tasks_list.append(Task(title, priority))

        print("\ntask created successfully!")
        time.sleep(3)

        self.menu()
        
    def delete_task(self, title=None):
        os.system("cls")
        if title is None:
            title = input("Which task do you want to delete?\n\n")
            
        for task in self.tasks_list:
            if task.title == title:
                self.tasks_list.remove(task)
                print("\nTask deleted successfully!")
            else:
                print("\nTask not found, try again!")

        time.sleep(3)

        self.menu()
        
        time.sleep(3)

        self.menu()
#notes class
class Note:
    def __init__(self, title, content = None):
        self.title = title
        self.content = content
#reminders class
class Reminder:
    def __init__(self, event, date = None):
        self.event = event
        self.date = date
#tasks class
class Task:
    def __init__(self, title, priority = None):
        self.title = title
        self.priority = priority
#introduction of the application to the user
os.system("cls")

print("Hi, welcome to your personal notes app, here you can have your own notebook and write on it, creating notes, reminders, tasks and many more!" )
time.sleep(4)
User = input("\nTo start off, tell us your name: ")
print("\nNice to meet you {name}, we are going to jump into a quick tutorial for you to start using our app".format(name = User))
time.sleep(3)

print("\nEverything gets organized in your very special notebook, so we are creating one for you!")
time.sleep(4)
print("\nYour Notebook was created successfully!")
print("\nNow you are going to be redirected to our menu. From there you can: edit your notebook, create notes, reminders and more!")
time.sleep(5)
print("\nWe leave you here, now discover for yourself, good luck!")
time.sleep(5)
os.system("cls")

#default notebook, which will we the base of everything. everythings works on top of it
Notebook()








