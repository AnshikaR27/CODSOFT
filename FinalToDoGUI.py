import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3


# Initialize the initial root window
initial_root = Tk()
initial_root.title("ToDo")
initial_root.geometry("300x200")
initial_root.config(bg='#d0ba93')

fra = Label(initial_root, text="ToDo", font=('champion', 40), fg="white", bg="#d0ba93")
fra.pack()
fra.place(anchor="center", relx=0.5, rely=0.5)

conn = sqlite3.connect('data.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todoList(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')

def insertdata(task):
    query = "INSERT INTO todoList(task) VALUES(?);"
    conn.execute(query, (task,))
    conn.commit()

def deletebytask(taskval):
    query = "Delete from todoList where task = ?;"
    conn.execute(query, (taskval,))
    conn.commit()

def main_window():
    initial_root.destroy()

    main = Tk()
    main.title("TODO")
    main.geometry("800x700")
    main.resizable(False, False)
    main.configure(background="#FAEBD7")

    def add(event):
        if len(addtask.get()) == 0:
            messagebox.showerror("ERROR", "No data available. Please enter a task.")
        else:
            insertdata(addtask.get())
            addtask.delete(0, END)
            populate()

        

    def deletetask(event):
        selected_task = listbox.get(ANCHOR)
        if selected_task:
            deletebytask(selected_task)
            populate()


    header_frame = Frame(main, bg="#FAEBD7")
    header_frame.pack(fill="x")

    header_label = Label(
        header_frame,
        text="The To-Do List",
        font=("Brush Script MT", 30),
        background="#FAEBD7",
        foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    add_frame = Frame(main, bg="#FAEBD7")
    add_frame.pack()

    addtask = Entry(
        add_frame,
        font=("Verdana"),
        background="#e9e4dc",
        border=2
    )
    addtask.pack(ipadx=20, ipady=5, fill="both")


    Label(
        main,
        text="Your Tasks",
        background="#FAEBD7",
        foreground="#8B4513",
        font=("Calibri", 18),
    ).pack(pady=(15,0))

    def show():
        query = "SELECT * FROM todoList;"
        return conn.execute(query)

    def populate():
        listbox.delete(0, END)
        for row in show():
            listbox.insert(END, row[1])

  
    taskframe = tkinter.Frame(
    main,
    bg="#FAEBD7",
    padx=20, 
    pady=20  
)
    taskframe.pack(fill=BOTH, expand=300)
    taskframe.pack(fill=BOTH, expand=300)
    scrollbar = Scrollbar(taskframe)
    scrollbar.pack(side=RIGHT, fill=Y)


    listbox = Listbox(
    taskframe,
    font=("Calibri, 13"),
    bg="white",
    fg="#452209",
    selectbackground="#eeeeee",
    selectforeground="#1d1d1d",
    border=2
 
)


    listbox.pack(fill=BOTH, expand=200)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    listbox.bind("<Double-Button-1>", deletetask)
    listbox.bind("<Delete>", deletetask)

    addtask.bind('<Return>', add)

    populate()

    Label(
        main,
        text="      Double Click On A Task to Delete",
        background="#FAEBD7",
        foreground="#8B4513",
       font=("Calibri", 14),
    ).pack(side=BOTTOM, pady=10)

    Label(
        main,
        text="TIP : Press Enter key To Insert A Task In the Listbox, ",
        background="#FAEBD7",
        foreground="#8B4513",
       font=("Calibri", 14),
    ).pack(side=BOTTOM, pady=4)


initial_root.after(1000, main_window)
initial_root.mainloop()
