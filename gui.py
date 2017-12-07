class GUI:
    import Tkinter as tk
    global tk
    def __init__(self):
        w = tk.Tk()
        w.attributes('-fullscreen', True)
        w.config(background='white', cursor='none')
        w.bind("w", lambda e: w.destroy())
        w.mainloop()

    def display(self, arg):
        label = tk.Label(w, text="Hello")
        label.pack()
