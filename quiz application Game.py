import tkinter as tk
from tkinter import messagebox

quiz = [
    ("Capital of India?", ["Nagpur", "New Delhi", "Mumbai", "Nashik"], "New Delhi"),
    ("2 + 2 =", ["3", "4", "5", "2"], "4"),
    ("Python is a...", ["Snake", "Game", "Language", "Animal"], "Language")
]
current_q = 0
score = 0

def load_question():
    question, options, _ = quiz[current_q]
    q_label.config(text=question)
    for i in range(4):
        buttons[i].config(text=options[i], value=options[i])
    selected.set(None)

def next_question():
    global current_q, score
    if selected.get() == "":
        messagebox.showwarning("Select an option", "Please choose an answer.")
        return
    if selected.get() == quiz[current_q][2]:
        score += 1
    current_q += 1
    if current_q >= len(quiz):
        messagebox.showinfo("Quiz Over", f"Your score is {score}/{len(quiz)}")
        root.destroy()
    else:
        load_question()

root = tk.Tk()
root.title("Simple Quiz")
root.geometry("400x300")

q_label = tk.Label(root, text="", font=("Arial", 16))
q_label.pack(pady=20)

selected = tk.StringVar(value="")

buttons = []
for _ in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected, value="", font=("Arial", 12))
    btn.pack(anchor="w", padx=50)
    buttons.append(btn)

next_btn = tk.Button(root, text="Next", command=next_question)
next_btn.pack(pady=20)

load_question()
root.mainloop()