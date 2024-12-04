import tkinter as tk
from tkinter import messagebox
from text_to_html_file import html_file

def enter(d):
    with open("f.txt", "w") as f:
        write = f"My name is {d['name']}.\nMy age is {d['age']}.\nMy gender is {d['gender']}."
        f.write(write)
    messagebox.showinfo("Success", "Data saved to f.txt!")

def save_data():
    d = {
        "name": name_var.get(),
        "age": age_var.get(),
        "gender": gender_var.get()
    }
    if not all(d.values()):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    enter(d)

# Create the main window
root = tk.Tk()
root.title("User Information Form")

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()

# Form fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=gender_var).grid(row=2, column=1, padx=10, pady=5)

# Save button
tk.Button(root, text="Save", command=save_data).grid(row=3, column=0, padx=10, pady=5)

# Convert to HTML button (using lambda to delay function call)
tk.Button(root, text="Convert to html", command=lambda: html_file("f.txt", "f.html")).grid(row=3, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
