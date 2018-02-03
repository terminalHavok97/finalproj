class GUI:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError('<GUI import error>')
    global tk

    def __init__(self):
        self.textToSet = ""

    def setupWindow(self, root):
        root.attributes('-fullscreen', True)
        root.config(background='white', cursor='none')
        root.bind("<space>", lambda e: root.destroy())

    def updateText(self, root, t):
        tk.Label(root, text=t).pack()
