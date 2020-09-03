from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.view.SBViewElement import SBViewElement
from modules.controller.SBCtrlNewChordDialog import SBCtrlNewChordDialog
import tkinter as tk

class SBViewChord(SBViewElement):
    def __init__(self, master, canvas, chord, parent, row, col):
        SBViewElement.__init__(self,parent.getX()+col*40, parent.getY()+50+30*row)
        self.parent = parent
        self.master = master
        self.chord = chord
        self.canvas = canvas
        self.width = self.chord.getLengthInBars() * 40
        self.height = 20
        self.rect = None


        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="#EEEEEE")

        self.text = self.canvas.create_text(self.x + 10, self.y + 10, text=self.getUpdatedText(), anchor=tk.W)
        self.canvas.tag_bind(self.rect, '<Double-Button-1>', self.clickEditChord)
        self.canvas.tag_bind(self.text, '<Double-Button-1>', self.clickEditChord)

    def getUpdatedText(self):
        if (self.chord.getHarmonicStr() != "MAJOR"):
            if (self.chord.getHarmonicStr() == "MINOR"):
                harm_txt = "m"
            elif (self.chord.getHarmonicStr() == "SEVENTH"):
                harm_txt = "7"
            elif (self.chord.getHarmonicStr() == "NINTH"):
                harm_txt = "9"
            else:
                harm_txt = ""
        else:
            harm_txt = ""
        rect_text = self.chord.getNoteStr() + harm_txt
        return rect_text


    def updateMyGeometry(self):
        self.width = self.chord.getLengthInBars() * 40
        self.canvas.coords(self.rect, self.x, self.y, self.x + self.width, self.y + self.height)
        self.canvas.coords(self.text, self.x + 10, self.y + 10)
        self.canvas.itemconfig(self.text, text=self.getUpdatedText())


    def update(self):
        self.updateMyGeometry()
        self.parent.update()

    def setCol(self, col):
        self.setX(self.parent.getX()+col*40)
        self.updateMyGeometry()

    def setRow(self, row):
        self.setY(self.parent.getY()+50+30*row)
        self.updateMyGeometry()


    def getChord(self):
        return self.chord


    def clickEditChord(self, event):

        print("Edit Chord")

        d = SBCtrlNewChordDialog(self.master, self.chord, self)

        self.master.wait_window(d.top)
        self.update()
        print("lib = " + str(self.chord.getLengthInBars()))



