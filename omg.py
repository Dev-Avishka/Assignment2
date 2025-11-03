

'''

omg.py - One Must Go - GUI client code
This file will read from data.txt and provide a GUI for users to vote on categories.
when category is displayed, user can select one option  to vote
once voted the program shall increment the vote count for that option and save back to data.txt
and then move to next category
each item in a category is a button
each button when clicked will register a vote for that option
each button will be in a grid layout
and no Next button to move to next category, it will move automatically after voting
if no more categories, display a message and ask if the user wants to exit with a button saying exit
this program will be OOP
and use TKINTER for GUI
Shall display "One Must Go " on top
Shall display the Category as "Category: <category name>"
'''

import json
import tkinter as tk
from tkinter import messagebox
file_path = 'data.txt'
# load data at start
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except:
    data = []
def save_data(data):
    #save data back to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
class OneMustGoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("One Must Go Voting")
        self.master.geometry("400x300")

        title_label = tk.Label(master, text="One Must Go", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)
        self.current_index = 0
        self.create_widgets()
        self.show_category()

    def create_widgets(self):
        
        self.category_label = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.category_label.pack(pady=10)
        
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

    def show_category(self):
        if self.current_index >= len(data):
            messagebox.showinfo("End", "No more categories to vote on. Thank you!")
            self.master.quit()
            return

        category = data[self.current_index]
        self.category_label.config(text=f"Category: {category['name']}")

        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        for option in category['options']:
            btn = tk.Button(self.buttons_frame, text=option['name'], width=20,
                            command=lambda opt=option: self.vote(opt))
            btn.pack(pady=5)

    def vote(self, option):
        option['votes'] += 1
        save_data(data)
        self.current_index += 1
        self.show_category()
if __name__ == "__main__":
    root = tk.Tk()
    app = OneMustGoApp(root)
    root.mainloop()
