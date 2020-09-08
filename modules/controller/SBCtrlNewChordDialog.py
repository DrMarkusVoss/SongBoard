from tkinter import *
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.model.SBCommonTypes import convertStringToSBPartType
from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import SBChordNote
from modules.model.SBCommonTypes import SBChordHarmonic
from modules.model.SBChord import SBChord

class SBCtrlNewChordDialog:

    def __init__(self, parent, chord=None, viewchord=None):
        self.chord = chord
        self.viewChord = viewchord
        self.parent = parent
        top = self.top = Toplevel(parent)
        top.title("Edit Chord")

        l_length = Label(top, text="Length in Bars:")
        l_length.grid(row=0, column=0, sticky=E)

        if (self.chord == None):
            str_len = "4"
        else:
            str_len = str(chord.getLengthInBars())

        self.entry_length = Entry(top, textvariable=StringVar(top, str_len))
        self.entry_length.grid(row=0, column=1, sticky=W)


        l_note = Label(top, text="Note:")
        l_note.grid(row=1, column=0, sticky=E)

        self.note_default = StringVar(top)

        note_choices = set()

        for e in SBChordNote.__members__:
            note_choices.add(e)

        if (self.chord == None):
            str_note_default = "C"
        else:
            str_note_default = self.chord.getNoteStr()

        self.note_default.set(str_note_default)  # set the default option

        self.entry_note = OptionMenu(top, self.note_default, *note_choices)
        self.entry_note.grid(row=1, column=1, sticky=W)

        l_harmonic = Label(top, text="Harmonic:")
        l_harmonic.grid(row=2, column=0, sticky=E)

        self.harmonic_default = StringVar(top)

        harmonic_choices = set()

        for e in SBChordHarmonic.__members__:
            harmonic_choices.add(e)

        if (self.chord == None):
            str_harm_default = "MINOR"
        else:
            str_harm_default = self.chord.getHarmonicStr()

        self.harmonic_default.set(str_harm_default)  # set the default option

        self.entry_harmonic = OptionMenu(top, self.harmonic_default, *harmonic_choices)
        self.entry_harmonic.grid(row=2, column=1, sticky=W)

        # ---
        l_pitch = Label(top, text="Pitch (0=C-5):")
        l_pitch.grid(row=3, column=0, sticky=E)

        self.pitch_default = StringVar(top)

        pitch_choices = set()

        for e in range(-5,5):
            pitch_choices.add(str(e))

        if (self.chord == None):
            str_pitch_default = "0"
        else:
            str_pitch_default = str(self.chord.getPitch())

        self.pitch_default.set(str_pitch_default)  # set the default option

        self.entry_pitch = OptionMenu(top, self.pitch_default, *pitch_choices)
        self.entry_pitch.grid(row=3, column=1, sticky=W)
        # ---




        but_ok = Button(top, text="OK", command=self.ok)
        but_ok.grid(row=4, column=0)

        but_cancel = Button(top, text="Cancel", command=self.cancel)
        but_cancel.grid(row=4, column=1)

    def ok(self):

        newchord = SBChord(SBChordNote.__members__[self.note_default.get()], SBChordHarmonic.__members__[self.harmonic_default.get()], )

        print("chordlength = " + str(self.entry_length.get()))
        newchord.setLengthInBars(int(self.entry_length.get()))
        newchord.setPitch(int(self.pitch_default.get()))

        if (self.chord == None):
            self.parent.songpartAddChord(newchord)
        else:
            self.chord.setNote(SBChordNote.__members__[self.note_default.get()])
            self.chord.setLengthInBars(int(self.entry_length.get()))
            self.chord.setHarmonic(SBChordHarmonic.__members__[self.harmonic_default.get()])
            self.chord.setPitch(int(self.pitch_default.get()))
            #print("chordlength chord = " + str(self.chord.getLengthInBars()))
            #self.viewChord.setChord(self.chord)

        self.top.destroy()

    def cancel(self):
        self.top.destroy()
