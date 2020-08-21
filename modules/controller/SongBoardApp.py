import tkinter as tk


from modules.controller.SBCtrlNewSongDialog import SBCtrlNewSongDialog


class SongBoardApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()

        self.song = None
        self.song_name = "---"

        self.create_widgets()

    def create_widgets(self):
        self.canvas_width = 750
        self.canvas_height = 700
        self.w = tk.Canvas(self.master, bg="grey",
                   width=self.canvas_width,
                   height=self.canvas_height)

        self.w.pack()

        y = int(self.canvas_height / 2)
        self.w.create_line(0, y, self.canvas_width, y, fill="#476042")

        self.label_song = tk.Label(self, text="Song: ")
        self.label_song.grid(row=0, column=0)
        self.label_songname = tk.Label(self, text=self.song_name)
        self.label_songname.grid(row=0, column=1)
        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Song"
        self.but_new_part["command"] = self.createNewSong
        self.but_new_part.grid(row=1, column=0)

        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Part"
        self.but_new_part["command"] = self.say_hi
        self.but_new_part.grid(row=1, column=1)

        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Chord"
        self.but_new_part["command"] = self.say_hi
        self.but_new_part.grid(row=1, column=2)

        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Textline"
        self.but_new_part["command"] = self.say_hi
        self.but_new_part.grid(row=1, column=3)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=5)


    def setSong(self, song):
        self.song = song
        self.label_songname["text"] = str(self.song.getName())

    def say_hi(self):
        print("hi there, everyone!")

    def createNewSong(self):
        print("new song...")
        d = SBCtrlNewSongDialog(self)
        self.wait_window(d.top)

