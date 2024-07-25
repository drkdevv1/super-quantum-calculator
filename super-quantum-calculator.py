import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def show_screen():
    screen = tk.Toplevel(root)
    screen.attributes('-fullscreen', True)
    screen.attributes('-topmost', True)
    screen.bind('<Escape>', lambda e: screen.destroy())

    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    img = Image.open("assets/Wh46bS2Gw8vUC6iQh2wEd6.jpg")
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    label = tk.Label(screen, image=img)
    label.image = img
    label.pack(fill=tk.BOTH, expand=True)


def on_calculate():
    if entry1.get() and entry2.get():
        show_screen()
    else:
        messagebox.showwarning("Warning", "Both fields must be filled.")


root = tk.Tk()
root.title("Super Quantum Calculator")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

tk.Label(root, text=" ", font=('Arial', 18)).grid(
    row=0, column=0)
entry1 = tk.Entry(root, width=10, font=('Arial', 18))
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="+", font=('Arial', 18)
         ).grid(row=0, column=2, padx=10, pady=10)

entry2 = tk.Entry(root, width=10, font=('Arial', 18))
entry2.grid(row=0, column=3, padx=10, pady=10)

tk.Label(root, text=" ", font=('Arial', 18)).grid(
    row=0, column=4)

button = tk.Button(root, text="Calculate", padx=20, pady=10,
                   font=('Arial', 18), command=on_calculate)
button.grid(row=1, column=0, columnspan=5, pady=10)

tk.Label(root, text="=", font=('Arial', 18)).grid(
    row=2, column=0, padx=10, pady=10, sticky="e")
result_label = tk.Label(root, text="", font=('Arial', 18))
result_label.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

root.mainloop()
