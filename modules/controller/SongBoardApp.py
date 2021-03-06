import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

from modules.controller.SBCtrlNewSongDialog import SBCtrlNewSongDialog
from modules.controller.SBCtrlNewPartDialog import SBCtrlNewPartDialog
from modules.view.SBViewSongPart import SBViewSongPart
from modules.controller.SBCtrlNewChordDialog import SBCtrlNewChordDialog
from modules.controller.SBCtrlChordsToMidi import SBCtrlSongToMIDI
from modules.controller.SBCtrlPlayMIDI import SBMIDIMusicPlayer
from modules.model.SBSong import SBSong
from modules.model.SBSongPart import SBSongPart
from modules.controller.SBCtrlTextLineDialog import SBCtrlTextLineDialog

import pickle

class SongBoardApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()

        self.menu = tk.Menu(master, tearoff=False)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New Song", command=self.menuNewFile)
        self.filemenu.add_command(label="Open Song...", command=self.menuOpenFile)
        self.filemenu.add_command(label="Save Song As...", command=self.menuSaveFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.destroy)

        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.menuAbout)

        self.master.config(menu=self.menu)

        self.song = None
        self.song_name = "---"
        self.song_tempo = "---"
        self.song_beat = "---"

        self.selected_songpart = None
        self.selected_songpart_view = None


        self.create_widgets()

    def menuNewFile(self):
        self.createNewSong()

    def menuOpenFile(self):
        filename = askopenfilename(filetypes=[("SongBoard Song Files", "*.sb")])
        print(filename)
        with open(filename, 'rb') as f:
            song = pickle.load(f)
        self.setSong(song)
        self.setSongParts()

    def menuSaveFile(self):
        filename = asksaveasfile(filetypes=[("SongBoard Song Files", "*.sb")])
        print(filename)
        with open(filename.name, 'wb') as f:
           pickle.dump(self.song, f)

    def menuAbout(self):
        print("This is a simple example of a menu")

    def create_widgets(self):
        self.canvas_elements = []
        self.canvas_width = 750
        self.canvas_height = 700
        self.canvas = tk.Canvas(self.master, bg="light grey",
                                width=self.canvas_width,
                                height=self.canvas_height)

        self.canvas.pack()

        self.but_edit_song = self.canvas.create_rectangle(5, 10, 250, 90, outline="dark grey", fill="white")

        self.canvas_songname = self.canvas.create_text(10, 20, text=self.song_name, anchor=tk.W)
        self.canvas_tempo = self.canvas.create_text(10, 40, text="BPM: " + str(self.song_tempo), anchor=tk.W)
        self.canvas_beat = self.canvas.create_text(10,60, text="Beat: " + self.song_beat, anchor = tk.W)

        #font_e = ('Arial', 20, 'bold italic')

        #self.but_edit_song_e = self.canvas.create_text(25,77, text="e", fill="dark grey", font=font_e)

        self.master.bind('<BackSpace>', self.BackspacePressed)
        self.canvas.tag_bind(self.but_edit_song, "<Double-Button-1>", self.editSong)
        self.canvas.tag_bind(self.canvas_songname, "<Double-Button-1>", self.editSong)
        self.canvas.tag_bind(self.canvas_tempo, "<Double-Button-1>", self.editSong)
        self.canvas.tag_bind(self.canvas_beat, "<Double-Button-1>", self.editSong)


        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Part"
        self.but_new_part["command"] = self.createNewSongPart
        self.but_new_part.grid(row=0, column=0)

        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Chord"
        self.but_new_part["command"] = self.createNewChord
        self.but_new_part.grid(row=0, column=1)

        self.but_new_part = tk.Button(self)
        self.but_new_part["text"] = "New Textline"
        self.but_new_part["command"] = self.createNewTextline
        self.but_new_part.grid(row=0, column=2)

        self.but_play_audio = tk.Button(self)
        self.but_play_audio["text"] = "Play Song Audio"
        self.but_play_audio["command"] = self.playSongAudio
        self.but_play_audio.grid(row=0, column=3)

        self.but_play_audio = tk.Button(self)
        self.but_play_audio["text"] = "Play sel. Songpart Audio"
        self.but_play_audio["command"] = self.playSelSongpartAudio
        self.but_play_audio.grid(row=0, column=4)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=0, column=5)


    def setSong(self, song):
        self.song = song
        self.canvas.itemconfigure(self.canvas_songname, text=self.song.getName())
        self.canvas.itemconfigure(self.canvas_tempo, text ="BPM: " + str(self.song.getTempo()))
        self.canvas.itemconfigure(self.canvas_beat, text="Beat: " + self.song.getBeat())

    def setSongParts(self):
        cnt = 0
        for e in self.song.getParts():
            self.addSongPartToCanvas(e, cnt)
            cnt = cnt + 1


    def say_hi(self):
        print("hi there, everyone!")

    def createNewSong(self):
        print("new song...")
        d = SBCtrlNewSongDialog(self)
        self.wait_window(d.top)

    def editSong(self, event):
        print("edit song...")
        d = SBCtrlNewSongDialog(self, self.song)
        self.wait_window(d.top)


    def createNewChord(self):
        if (self.selected_songpart == None):
            print("No songpart selected. To add a Chord select a songpart first.")
        else:
            print("new chord...")
            d = SBCtrlNewChordDialog(self)
            self.wait_window(d.top)

    def createNewTextline(self):
        if (self.selected_songpart == None):
            print("No songpart selected. To add a textline select a songpart first.")
        else:
            print("new textline...")
            d = SBCtrlTextLineDialog(self)
            self.wait_window(d.top)


    def songAddPart(self, part):
        self.song.addPart(part)
        self.addSongPartToCanvas(part, len(self.song.getParts())-1)

    def addSongPartToCanvas(self, part, row):
        sp = SBViewSongPart(self, self.canvas, part, row)
        self.canvas_elements.append(sp)
        #self.selected_songpart = part
        #self.selected_songpart_view = sp
        #self.selected_songpart_view.select(True)

    def songpartAddChord(self, chord):
        self.selected_songpart_view.addChord(chord)
        self.selected_songpart_view.update()

    def sonpartAddTextline(self, textline):
        self.selected_songpart.addTextline(textline)
        self.selected_songpart_view.update()


    def reselectSongpart(self, songpartview):
        if (not(self.selected_songpart_view == None)):
            self.selected_songpart_view.select(False)
            self.selected_songpart_view.update()
        self.selected_songpart_view = songpartview
        self.selected_songpart = songpartview.getSongpart()
        self.selected_songpart_view.select(True)
        self.selected_songpart_view.update()


    def createNewSongPart(self):
        print("new songpart...")
        d = SBCtrlNewPartDialog(self)
        self.wait_window(d.top)

    def playSongAudio(self):
        print("play song audio")
        s2m = SBCtrlSongToMIDI(self.song, "temp.mid")
        s2m.writeMIDIFile()
        mp = SBMIDIMusicPlayer("temp.mid")
        mp.play()

    def playSelSongpartAudio(self):
        print("play selected songpart audio")
        newsong = SBSong("temp")
        newsong.setBeat(self.song.getBeat())
        newsong.setTempo(self.song.getTempo())
        newsong.addPart(self.selected_songpart)
        s2m = SBCtrlSongToMIDI(newsong, "temp.mid")
        s2m.writeMIDIFile()
        mp = SBMIDIMusicPlayer("temp.mid")
        mp.play()

    def BackspacePressed(self, event):
        # delete selected chord
        self.selected_songpart_view.deleteSelectedChord()
        pass





