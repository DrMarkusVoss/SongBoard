from tkinter import *
from modules.model.SBSong import SBSong


class SBCtrlNewSongDialog:

    def __init__(self, parent):
        self.parent = parent
        top = self.top = Toplevel(parent)
        top.title("New Song")

        l_name = Label(top, text="Name:")
        l_name.grid(row=0, column=0)

        self.entry_songname = Entry(top)
        self.entry_songname.grid(row=0, column=1)

        l_tempo = Label(top, text="Tempo:")
        l_tempo.grid(row=1, column=0)


        self.entry_songtempo = Entry(top, textvariable=StringVar(top,"120"))

        self.entry_songtempo.grid(row=1, column=1)

        l_tempo = Label(top, text="Beat:")
        l_tempo.grid(row=2, column=0)

        self.beat_default = StringVar(top)

        beat_choices = {'NOTHING','4/4', '3/4', '6/8'}
        self.beat_default.set('4/4')  # set the default option

        self.entry_beat = OptionMenu(top, self.beat_default, *beat_choices)
        self.entry_beat.grid(row=2, column=1)


        but_ok = Button(top, text="OK", command=self.ok)
        but_ok.grid(row=3, column=0)

        but_cancel = Button(top, text="Cancel", command=self.cancel)
        but_cancel.grid(row=3, column=1)

    def ok(self):
        newsong = SBSong(self.entry_songname.get())
        newsong.setTempo(int(self.entry_songtempo.get()))
        newsong.setBeat(self.beat_default.get())

        self.parent.setSong(newsong)

        self.top.destroy()

    def cancel(self):
        self.top.destroy()