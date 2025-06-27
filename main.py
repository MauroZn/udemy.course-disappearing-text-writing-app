import tkinter as tk
from tkinter import messagebox

is_typing = False
typing_timer_id = None
time = 5

def handle_keypress(event=None):
    global is_typing, typing_timer_id
    is_typing = True

    if typing_timer_id is not None:
        window.after_cancel(typing_timer_id)

    typing_timer_id = window.after(1000, set_typing_false)

def set_typing_false():
    global is_typing
    is_typing = False

def start_stop_counter():
    global time
    if is_typing:
        time = 5
    else:
        if time == 0:
            wordsBox.delete("1.0", tk.END)
            messagebox.showinfo("Time's up!", "Time's up! You stopped typing for 5 seconds so the text got deleted!")
            time = 5
        else:
            time -= 1
    timeTextBox.config(text=f"Time: {time}")
    window.after(1000, start_stop_counter)


if __name__ == "__main__":

    window = tk.Tk()

    window.title("Disappearing Text Writing App")
    window.minsize(600,600)

    label = tk.Label(window, text = "Don’t stop writing, or all progress will be lost.", font=('Arial', 16))
    label.pack(pady=20)

    timeTextBox = tk.Label(window, text="Timer: 10", font=('Times New Roman', 20))
    timeTextBox.pack( padx=5)

    wordsBox = tk.Text(window, height=25, width=50)
    wordsBox.pack(pady=20, padx=5)

    wordsBox.bind("<Key>", handle_keypress)

    start_stop_counter()

    window.mainloop()