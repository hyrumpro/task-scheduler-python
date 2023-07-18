import datetime
import tkinter as tk
from tkinter import messagebox

class SmartScheduler:
    def __init__(self):
        self.window = tk.Tk()
        self.tasks = []

        self.name_var = tk.StringVar()
        self.duration_var = tk.StringVar()
        self.deadline_var = tk.StringVar()
        self.priority_var = tk.StringVar()

        self.label_name = tk.Label(self.window, text="Task Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window, textvariable=self.name_var)
        self.entry_name.pack()

        self.label_duration = tk.Label(self.window, text="Duration (in hours):")
        self.label_duration.pack()
        self.entry_duration = tk.Entry(self.window, textvariable=self.duration_var)
        self.entry_duration.pack()

        self.label_deadline = tk.Label(self.window, text="Deadline (YYYY-MM-DD):")
        self.label_deadline.pack()
        self.entry_deadline = tk.Entry(self.window, textvariable=self.deadline_var)
        self.entry_deadline.pack()

        self.label_priority = tk.Label(self.window, text="Priority (1-5):")
        self.label_priority.pack()
        self.entry_priority = tk.Entry(self.window, textvariable=self.priority_var)
        self.entry_priority.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_task)
        self.submit_button.pack()

        self.display_button = tk.Button(self.window, text="Display Schedule", command=self.display_schedule)
        self.display_button.pack()

    def submit_task(self):
        name = self.name_var.get()
        duration = self.duration_var.get()
        deadline = self.deadline_var.get()
        priority = self.priority_var.get()

        if name and duration and deadline and priority:
            try:
                duration = int(duration)
                deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
                priority = int(priority)

                task = {'name': name, 'duration': duration, 'deadline': deadline, 'priority': priority, 'completed': False}
                self.tasks.append(task)

                self.entry_name.delete(0, 'end')
                self.entry_duration.delete(0, 'end')
                self.entry_deadline.delete(0, 'end')
                self.entry_priority.delete(0, 'end')

                self.display_schedule()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please enter valid values.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def complete_task(self, index):
        self.tasks[index]['completed'] = True
        self.display_schedule()

    def delete_task(self, index):
        del self.tasks[index]
        self.display_schedule()

    def update_task(self, index):
        task = self.tasks[index]
        update_window = tk.Toplevel(self.window)
        update_window.title("Update Task Details")

        label_name = tk.Label(update_window, text="Task Name:")
        label_name.pack()
        entry_name = tk.Entry(update_window, textvariable=self.name_var)
        entry_name.pack()
        entry_name.delete(0, 'end')  
        entry_name.insert(0, task['name'])  

        label_duration = tk.Label(update_window, text="Duration (in hours):")
        label_duration.pack()
        entry_duration = tk.Entry(update_window, textvariable=self.duration_var)
        entry_duration.pack()
        entry_duration.delete(0, 'end') 
        entry_duration.insert(0, task['duration']) 

        label_deadline = tk.Label(update_window, text="Deadline (YYYY-MM-DD):")
        label_deadline.pack()
        entry_deadline = tk.Entry(update_window, textvariable=self.deadline_var)
        entry_deadline.pack()
        entry_deadline.delete(0, 'end')  
        entry_deadline.insert(0, task['deadline'].strftime('%Y-%m-%d'))  

        label_priority = tk.Label(update_window, text="Priority (1-5):")
        label_priority.pack()
        entry_priority = tk.Entry(update_window, textvariable=self.priority_var)
        entry_priority.pack()
        entry_priority.delete(0, 'end')  
        entry_priority.insert(0, task['priority'])  


        def save_update():
         name = entry_name.get()
         duration = entry_duration.get()
         deadline = entry_deadline.get()
         priority = entry_priority.get()

         if name and duration and deadline and priority:
             try:
                 duration = int(duration)
                 deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
                 priority = int(priority)

                 task['name'] = name  
                 task['duration'] = duration
                 task['deadline'] = deadline
                 task['priority'] = priority

                 update_window.destroy()
                 self.display_schedule()
             except ValueError:
                 messagebox.showerror("Error", "Invalid input! Please enter valid values.")
         else:
             messagebox.showerror("Error", "Please fill in all the fields.")





        save_button = tk.Button(update_window, text="Save", command=save_update)
        save_button.pack()

    def display_schedule(self):
        schedule_window = tk.Toplevel(self.window)
        schedule_window.title("Optimized Schedule")

        sorted_tasks = sorted(self.tasks, key=lambda task: task['priority'])

        for index, task in enumerate(sorted_tasks, start=1):
            task_text = f"{index}. Task: {task['name']}, Duration: {task['duration']} hours"
            if task['completed']:
                task_text += " (Completed)"
            label = tk.Label(schedule_window, text=task_text)
            label.pack()

            complete_button = tk.Button(schedule_window, text="Complete", command=lambda i=index-1: self.complete_task(i))
            complete_button.pack()

            delete_button = tk.Button(schedule_window, text="Delete", command=lambda i=index-1: self.delete_task(i))
            delete_button.pack()

            update_button = tk.Button(schedule_window, text="Update", command=lambda i=index-1: self.update_task(i))
            update_button.pack()

        close_button = tk.Button(schedule_window, text="Close", command=schedule_window.destroy)
        close_button.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    scheduler = SmartScheduler()
    scheduler.run()












