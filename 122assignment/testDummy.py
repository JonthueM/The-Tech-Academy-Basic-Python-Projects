import tkinter as tk

root = tk.Tk()
root.geometry("600x40")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

rectangle_1 = tk.Label(root, text="Column 1", bg="green", fg="white")
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="EW")

rectangle_2 = tk.Label(root, text="Colum 2", bg="red", fg="white")
rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10, sticky="EW")

root.mainloop()
