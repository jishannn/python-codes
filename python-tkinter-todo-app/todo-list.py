import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASK_FILE = 'tasks.txt'

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task, done = line.strip().split(' | ')
                task_list.insert(tk.END, task)
                if done == '1':
                    task_list.itemconfig(tk.END, {'fg': 'gray'})
    except FileNotFoundError:
        pass

def save_tasks():
    with open(TASK_FILE, 'w') as file:
        for i in range(task_list.size()):
            task = task_list.get(i)
            done = '1' if task_list.itemcget(i, 'fg') == 'gray' else '0'
            file.write(f'{task} | {done}\n')



def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

    else:
        messagebox.showwarning('Warning', 'Task cannot be empty!')

def remove_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning('Warning', 'Select a task to remove!')

def mark_done():
    try:
        index = task_list.curselection()[0]
        task_list.itemconfig(index, {'fg': 'gray'})
        save_tasks()
    except IndexError:
        messagebox.showwarning('Warning', 'Select a task to mark as done!')

def clear_tasks():
    task_list.delete(0, tk.END)
    save_tasks()


# UI setup
root = tk.Tk()
root.title('To-Do List')

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text='Add Task', command=add_task)
add_button.pack(side=tk.RIGHT)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

remove_button = tk.Button(btn_frame, text='Remove', command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

done_button = tk.Button(btn_frame, text='Mark Done', command=mark_done)
done_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(btn_frame, text='Clear All', command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

# Load existing tasks
load_tasks()

root.mainloop()
