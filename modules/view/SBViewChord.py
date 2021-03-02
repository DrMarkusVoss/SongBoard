from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.view.SBViewElement import SBViewElement
from modules.controller.SBCtrlNewChordDialog import SBCtrlNewChordDialog
import tkinter as tk

class SBViewChord(SBViewElement):
    def __init__(self, master, canvas, chord, parent, row, col):

        self.xoffset = 10
        self.parent = parent
        self.master = master
        self.chord = chord
        self.am_i_selected = False

        SBViewElement.__init__(self, parent.getX()+self.xoffset+col*40, parent.getY()+50+50*row, self.chord.getLengthInBars() * 40, 20)

        self.canvas = canvas
        #self.width = self.chord.getLengthInBars() * 40
        #self.height = 20
        self.rect = None


        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill="light blue")

        self.text = self.canvas.create_text(self.x + 10, self.y + 10, text=self.getUpdatedText(), anchor=tk.W)
        self.canvas.tag_bind(self.rect, '<Double-Button-1>', self.clickEditChord)
        self.canvas.tag_bind(self.text, '<Double-Button-1>', self.clickEditChord)
        self.canvas.tag_bind(self.rect, '<Button-1>', self.iAmSelected)
        self.canvas.tag_bind(self.text, '<Button-1>', self.iAmSelected)

    def getUpdatedText(self):
        if (self.chord.getHarmonicStr() != "MAJOR"):
            if (self.chord.getHarmonicStr() == "MINOR"):
                harm_txt = "m"
            elif (self.chord.getHarmonicStr() == "SEVENTH"):
                harm_txt = "7"
            elif (self.chord.getHarmonicStr() == "NINTH"):
                harm_txt = "9"
            elif (self.chord.getHarmonicStr() == "DIMINISHED"):
                harm_txt = "d"
            elif (self.chord.getHarmonicStr() == "AUGMENTED"):
                harm_txt = "a"
            else:
                harm_txt = ""
        else:
            harm_txt = ""
        rect_text = self.chord.getNoteStr() + harm_txt
        return rect_text

    def deleteGeometry(self):
        self.canvas.delete(self.rect)
        self.canvas.delete(self.text)

    def getXMax(self):
        crds = self.canvas.coords(self.rect)
        return crds[2]

    def updateMyGeometry(self):
        self.width = self.chord.getLengthInBars() * 40
        self.canvas.coords(self.rect, self.x, self.y, self.x + self.width, self.y + self.height)
        self.canvas.coords(self.text, self.x + 10, self.y + 10)
        self.canvas.itemconfig(self.text, text=self.getUpdatedText())
        outcolor = "black"

        if (self.am_i_selected == True):
            outcolor = "red"
        else:
            outcolor = "black"
        self.canvas.itemconfig(self.rect, outline=outcolor)


    def update(self):
        self.updateMyGeometry()
        self.parent.update()

    def setCol(self, col):
        self.setX(self.parent.getX()+self.xoffset+col*40)
        self.updateMyGeometry()

    def setRow(self, row):
        self.setY(self.parent.getY()+50+50*row)
        self.updateMyGeometry()


    def getChord(self):
        return self.chord


    def clickEditChord(self, event):

        print("Edit Chord")

        d = SBCtrlNewChordDialog(self.master, self.chord, self)

        self.master.wait_window(d.top)
        self.update()
        print("lib = " + str(self.chord.getLengthInBars()))

    def select(self, trueorfalse):
        self.am_i_selected = trueorfalse

    def iAmSelected(self, event):
        #print("me is selected")
        self.parent.selectChord(self)





