from tkinter import *
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import SBBeatType


class SBCtrlNewSongDialog:

    def __init__(self, parent, song=None):
        self.song = song
        self.parent = parent
        top = self.top = Toplevel(parent)
        top.title("New Song")

        if (self.song == None):
            sname = StringVar(top, "")
            tempo = StringVar(top,"120")
            self.beat_default = StringVar(top, '4/4')

        else:
            bpb = SBBeatType(SBBeatType.NOTHING)
            sname = StringVar(top, self.song.getName())
            tempo = StringVar(top, str(self.song.getTempo()))
            bpb = SBBeatType(self.song.getBeatsPerBar())
            self.beat_default = StringVar(top, str(bpb.name))

        l_name = Label(top, text="Name:")
        l_name.grid(row=0, column=0)

        self.entry_songname = Entry(top, textvariable=sname)
        self.entry_songname.grid(row=0, column=1)

        l_tempo = Label(top, text="Tempo:")
        l_tempo.grid(row=1, column=0)




        self.entry_songtempo = Entry(top, textvariable=tempo)

        self.entry_songtempo.grid(row=1, column=1)

        l_tempo = Label(top, text="Beat:")
        l_tempo.grid(row=2, column=0)



        beat_choices = {'NOTHING','4/4', '3/4', '6/8'}
        self.beat_default.set('4/4')  # set the default option

        self.entry_beat = OptionMenu(top, self.beat_default, *beat_choices)
        self.entry_beat.grid(row=2, column=1)


        but_ok = Button(top, text="OK", command=self.ok)
        but_ok.grid(row=3, column=0)

        but_cancel = Button(top, text="Cancel", command=self.cancel)
        but_cancel.grid(row=3, column=1)

    def ok(self):
        if (self.song == None):
            newsong = SBSong(self.entry_songname.get())
            newsong.setTempo(int(self.entry_songtempo.get()))
            newsong.setBeat(self.beat_default.get())

            self.parent.setSong(newsong)
        else:
            self.song.setName(self.entry_songname.get())
            self.song.setTempo(int(self.entry_songtempo.get()))
            self.song.setBeat(self.beat_default.get())

        self.top.destroy()

    def cancel(self):
        self.top.destroy()