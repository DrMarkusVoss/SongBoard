import tkinter as tk

from modules.controller.SongBoardApp import SongBoardApp



root = tk.Tk()
app = SongBoardApp(master=root)
root.geometry("800x750+20+20")
root.title("SongBoard by Dr. Markus Voss")
app.mainloop()
