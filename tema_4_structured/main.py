import tkinter as tk

def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        result.set(f"Resultado: {x + y}")
    except ValueError:
        result.set("Digite números válidos")

root = tk.Tk()
root.title("Sum Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter two numbers:").pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="X:").grid(row=0, column=0)
entry_x = tk.Entry(frame)
entry_x.grid(row=0, column=1)

tk.Label(frame, text="Y:").grid(row=1, column=0)
entry_y = tk.Entry(frame)
entry_y.grid(row=1, column=1)

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Calculate", command=calculate).pack()

root.mainloop()