from tkinter import *
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.model.SBCommonTypes import convertStringToSBPartType
from modules.model.SBSongPart import SBSongPart

class SBCtrlNewPartDialog:

    def __init__(self, parent):
        self.parent = parent
        top = self.top = Toplevel(parent)
        top.title("New Songpart")

        l_name = Label(top, text="Name:")
        l_name.grid(row=0, column=0)

        self.entry_songname = Entry(top)
        self.entry_songname.grid(row=0, column=1)

        l_tempo = Label(top, text="Tempo:")
        l_tempo.grid(row=1, column=0)


        self.entry_songtempo = Entry(top, textvariable=StringVar(top,"0"))

        self.entry_songtempo.grid(row=1, column=1)

        l_tempo = Label(top, text="Beat:")
        l_tempo.grid(row=2, column=0)

        self.beat_default = StringVar(top)

        beat_choices = {'NOTHING','4/4', '3/4', '6/8'}
        self.beat_default.set('NOTHING')  # set the default option

        self.entry_beat = OptionMenu(top, self.beat_default, *beat_choices)
        self.entry_beat.grid(row=2, column=1)

        l_type = Label(top, text="Type:")
        l_type.grid(row=3, column=0)

        self.type_default = StringVar(top)


        type_choices = {'SOMETHING', 'INTRO', 'VERSE', 'CHORUS', 'BRIDGE', 'OUTRO', 'BREAK', 'SOLO', 'INTERLUDE'}
        self.type_default.set('SOMETHING')  # set the default option

        self.entry_type = OptionMenu(top, self.type_default, *type_choices)
        self.entry_type.grid(row=3, column=1)


        but_ok = Button(top, text="OK", command=self.ok)
        but_ok.grid(row=4, column=0)

        but_cancel = Button(top, text="Cancel", command=self.cancel)
        but_cancel.grid(row=4, column=1)

    def ok(self):
        newpart = SBSongPart(self.entry_songname.get(), convertStringToSBPartType(self.type_default.get()) )
        newpart.setTempo(int(self.entry_songtempo.get()))
        newpart.setBeat(self.beat_default.get())

        self.parent.songAddPart(newpart)

        self.top.destroy()

    def cancel(self):
        self.top.destroy()
