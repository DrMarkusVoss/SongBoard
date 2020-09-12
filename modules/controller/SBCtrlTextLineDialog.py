from tkinter import *
from tkinter.scrolledtext import ScrolledText
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.model.SBCommonTypes import convertStringToSBPartType
from modules.model.SBSongPart import SBSongPart

from tkinter import *
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.model.SBCommonTypes import convertStringToSBPartType
from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import SBChordNote
from modules.model.SBCommonTypes import SBChordHarmonic
from modules.model.SBChord import SBChord

class SBCtrlTextLineDialog:

    def __init__(self, parent, textline=None, viewtextline=None):
        self.textline = textline
        self.viewtextline = viewtextline
        self.parent = parent
        top = self.top = Toplevel(parent)
        top.title("Edit Textline")

        l_textline = Label(top, text="Textline (use % to indicate chords):")
        l_textline.grid(row=0, column=0, sticky=W)

        if (self.textline == None):
            str_tl = ""
        else:
            str_tl = str(self.textline)

        self.entry_textline = ScrolledText(top)
        self.entry_textline.grid(row=1, column=0, sticky=W)




        but_ok = Button(top, text="OK", command=self.ok)
        but_ok.grid(row=2, column=0)

        but_cancel = Button(top, text="Cancel", command=self.cancel)
        but_cancel.grid(row=2, column=1)

    def ok(self):
        textline = self.entry_textline.get("1.0", END)

        print(textline)
        if (self.textline == None):
           self.parent.sonpartAddTextline(textline)
        else:
            self.textline == textline

        self.top.destroy()

    def cancel(self):
        self.top.destroy()
