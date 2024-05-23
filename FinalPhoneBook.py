from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk


root = Tk()
root.title("TODO")
root.geometry("500x600")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.configure(background="#E6EAFF")

conn = sqlite3.connect('phonebook.db')
conn.execute('''CREATE TABLE IF NOT EXISTS phonebook(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL CHECK(length(phone_number) = 10),
    email TEXT NOT NULL,
    address TEXT NOT NULL
);''')

conn.commit()

# Add Information
def add():
    name = Name.get()
    phone = Number.get()
    email = Email.get()
    addr = address.get(1.0, "end-1c")

    if name == "" or phone == "" or email == "" or addr == "":
        messagebox.showwarning("Warning", "Please fill in all fields")
        return

    conn.execute('INSERT INTO phonebook (name, phone_number, email, address) VALUES (?, ?, ?, ?)', (name, phone, email, addr))
    conn.commit()
    update_book()

# View Information
def view(event):
    try:
        selected_id = select.curselection()[0]
        data = select.get(selected_id)
        cursor = conn.execute('SELECT * FROM phonebook WHERE name=?', (data,))
        record = cursor.fetchone()

        if record:
            Name.set(record[1])
            Number.set(record[2])
            Email.set(record[3])
            address.delete(1.0, "end")
            address.insert(1.0, record[4])
    except IndexError:
        messagebox.showwarning("Warning", "Please select an entry")

# Delete Information
def delete(event):
    try:
        selected_id = select.curselection()[0]
        data = select.get(selected_id)
        conn.execute('DELETE FROM phonebook WHERE name=?', (data,))
        conn.commit()
        update_book()
    except IndexError:
        messagebox.showwarning("Warning", "Please select an entry")

def reset():
    Name.set('')
    Number.set('')
    Email.set('')
    address.delete(1.0, "end")

# Update Information
def update_book():
    select.delete(0, END)
    cursor = conn.execute('SELECT name FROM phonebook')
    for row in cursor:
        select.insert(END, row[0])

# Search Contacts


# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()
Email = StringVar()

header_frame = Frame(root, bg="#E6EAFF")
header_frame.pack(fill="x")

header_label = Label(
	header_frame,
	text="Phonebook",
	font=("Brush Script MT", 30),
	background="#E6EAFF",
	foreground="black"
)
header_label.pack(padx=20, pady=(5, 8))


form_frame = Frame(root, bg="#E6EAFF")
form_frame.pack(pady=2)

Label(form_frame, text='Name', font='arial 12 bold', bg="#E6EAFF", fg="black", border=2).grid(row=0, column=0, padx=5, pady=5, sticky=E)
Entry(form_frame, textvariable=Name, width=50, bg="white").grid(row=0, column=1, padx=5, pady=5)

Label(form_frame, text='Phone No.', font='arial 12 bold', bg="#E6EAFF", fg="black", border=2).grid(row=1, column=0, padx=5, pady=5, sticky=E)
Entry(form_frame, textvariable=Number, width=50, bg="white").grid(row=1, column=1, padx=5, pady=5)

Label(form_frame, text='Email', font='arial 12 bold', bg="#E6EAFF", fg="black", border=2).grid(row=2, column=0, padx=5, pady=5, sticky=E)
Entry(form_frame, textvariable=Email, width=50, bg="white").grid(row=2, column=1, padx=5, pady=5)

Label(form_frame, text='Address', font='arial 12 bold', bg="#E6EAFF", fg="black", border=2).grid(row=3, column=0, padx=5, pady=5, sticky=NE)
address = Text(form_frame, width=37, height=3, bg="white")
address.grid(row=3, column=1, padx=5, pady=5)

button_frame = Frame(root, bg="#E6EAFF")
button_frame.pack(pady=5)

Button(button_frame, text="Add", font="arial 12 bold", command=add, fg="black").grid(row=0, column=0, padx=10, pady=2)
Button(button_frame, text="Reset", font="arial 12 bold", command=reset, fg="black").grid(row=0, column=3, padx=10, pady=2)

scroll_bar = Scrollbar(root, orient=VERTICAL)



taskframe = tk.Frame(
    root,
    bg="#E6EAFF",
    padx=40, 
    pady=30,
    width=20,
    height=10 
)
taskframe.pack(fill="both")
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)

select = Listbox(
    taskframe,
    font=("Calibri, 13"),
    bg="white",
    fg="black",
    selectbackground="#eeeeee",
    selectforeground="#1d1d1d",
    border=2
    
)


select.pack(fill="both")
select.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=select.yview)

select.bind("<Double-Button-1>", delete)
select.bind("<Delete>", delete)


select.bind('<Return>', view)
update_book()

Labelframe = tk.Frame(
    root,
    bg="#E6EAFF",
    padx=20, 
    pady=20  
).pack(side="bottom", fill=BOTH, expand=50)




Label(
        Labelframe,
        text="      Double Click On Any Name to Delete their contact",
        background="#E6EAFF",
        foreground="black",
       font=("Calibri", 10),
    ).pack(side="bottom", pady=1)

Label(
	Labelframe,
	text="TIP : Select any Name from the Phonebook, and press Enter key To view their PII, ",
	background="#E6EAFF",
	foreground="black",
	font=("Calibri", 10),
).pack(side="bottom", pady=1)




root.mainloop()


