from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.view.SBViewElement import SBViewElement
from modules.view.SBViewChord import SBViewChord
from modules.controller.SBCtrlNewPartDialog import SBCtrlNewPartDialog
from modules.view.SBViewPlayButton import SBViewPlayButton
import tkinter as tk

class SBViewSongPart(SBViewElement):
    def __init__(self, master, canvas, songpart, row=0):
        SBViewElement.__init__(self,100,50+row*130, 600, 120)
        self.master = master
        self.songpart = songpart
        self.canvas = canvas
        #self.width = 600
        #self.height = 120
        self.row = row
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="#EEEEEE")
        self.canvas.create_text(self.x+self.width/2, self.y + 10, text=self.songpart.getName())
        self.canvas.create_text(self.x+self.width/2, self.y + 30, text="[" + convertSBPartTypeToString(self.songpart.getPartType()) + "]")
        self.canvas.create_text(self.x+10, self.y+10, text="cycles: "+str(self.songpart.getNrRepeats()), anchor=tk.W, fill="dark grey")
        self.view_chords = []
        self.am_i_selected = False
        self.selected_viewchord = None
        self.view_textlines = []
        self.view_textline_elements = []


        self.but_play = SBViewPlayButton(self.master, self.canvas, self)

        x_offset = 0
        self.col = 0
        cnt = 0
        chord_row = 0

        textline_elements = []
        for tls in self.songpart.getTextlines():
            if (not(tls == None)):
                splt = self.splitUpTextline(tls)
                print(splt)
                for te in splt:
                    textline_elements.append(te)

        #tl = self.splitUpTextline(self.songpart.getTextlines())
        for e in songpart.getChords():
            nc = SBViewChord(self.master, self.canvas, e, self, chord_row, self.col)

            if (cnt < len(textline_elements)):
                self.createTextLineElement(textline_elements[cnt+1], nc)

            self.view_chords.append(nc)
            me_coords = self.canvas.coords(self.rect)
            if (nc.getXMax() > me_coords[2]):
                chord_row = chord_row + 1
                nc.setRow(chord_row)
                self.col = 0
                nc.setCol(self.col)


            #col = col + e.getLengthInBars() + 1
            cnt = cnt + 1
            self.col = self.col + e.getLengthInBars()

        self.canvas.tag_bind(self.rect, '<Double-Button-1>', self.say_hu)
        self.canvas.tag_bind(self.rect, '<Button-1>', self.iAmSelected)

        self.createViewTextlines()

    def getSongpart(self):
        return self.songpart

    def createViewTextlines(self):
        self.view_textlines = []
        txt_row = 0
        for e in self.songpart.getTextlines():
            tl = self.canvas.create_text(self.x + 10, self.y + 130 + 20*txt_row, text=e,
                                    anchor=tk.W, fill="dark grey")
            self.view_textlines.append(tl)
            txt_row = txt_row + 1

    def createTextLineElement(self, textline_el, viewchord):
        vtl = self.canvas.create_text(viewchord.x + 10, viewchord.y + 30, text=self.removeCR(textline_el),
                                anchor=tk.W, fill="dark grey")
        self.view_textline_elements.append(vtl)

    def splitUpTextline(self,tl):
        t = ""
        t = tl.split("%")
        return t

    def removeCR(self, text):
        return text.strip("\n")

    def createViewContent(self):
        self.view_textlines = []
        txt_row = 0
        chord_row = 0
        for e in self.songpart.getTextlines():
            num_chords = e.count("%")
            for i in range(num_chords):
                chrds = self.songpart.getChords()
                e = chrds[i]
                nc = SBViewChord(self.master, self.canvas, e, self, chord_row, self.col)
                self.view_chords.append(nc)
            self.canvas.create_text(self.x + 10, self.y + 110 + 20 * txt_row, text=e,
                                    anchor=tk.W, fill="dark grey")
            self.view_textlines.append(e)
            txt_row = txt_row + 1
            chord_row = chord_row + 1
            self.col = 0

    def update(self):
        self.col = 0
        outcolor = "black"
        if (self.am_i_selected == True):
            outcolor = "red"
        else:
            outcolor = "black"
        self.canvas.itemconfig(self.rect, outline=outcolor)

        chord_row = 0
        for e in self.view_chords:
            me_coords = self.canvas.coords(self.rect)
            if (e.getXMax() > me_coords[2]):
                chord_row = chord_row + 1
                e.setRow(chord_row)
                self.col = 0
                e.setCol(self.col)

            self.col = self.col + e.getChord().getLengthInBars()


        self.createViewTextlines()

    def addChord(self, chord):
        self.songpart.addChord(chord)
        nc = SBViewChord(self.master, self.canvas, chord, self, 0, self.col)
        self.view_chords.append(nc)


    def say_hu(self, event):

        print("Edit Songpart")

        d = SBCtrlNewPartDialog(self.master, self.songpart, self)

        self.master.wait_window(d.top)
        self.update()
        print("repeats = " + str(self.songpart.getNrRepeats()))

    def select(self, trueorfalse):
        self.am_i_selected = trueorfalse
        if (trueorfalse == False):
            if (not (self.selected_viewchord == None)):
                self.selected_viewchord.select(False)
                self.selected_viewchord.update()
                self.selected_viewchord = None
                self.update()

    def iAmSelected(self, event):
        if (not (self.selected_viewchord == None)):
            self.selected_viewchord.select(False)
            self.selected_viewchord = None

        self.master.reselectSongpart(self)

    def selectChord(self, viewchord):
        if (not (self.selected_viewchord == None)):
            self.selected_viewchord.select(False)
            self.selected_viewchord.update()
        self.selected_viewchord = viewchord
        self.selected_viewchord.select(True)
        self.update()
        self.selected_viewchord.update()
        if (self.am_i_selected == False):
            self.master.reselectSongpart(self)

    def deleteSelectedChord(self):
        if (self.selected_viewchord == None):
            print("can't delete chord, none selected!")
        else:
            ind = self.view_chords.index(self.selected_viewchord)
            self.selected_viewchord.deleteGeometry()
            self.view_chords.pop(ind)
            self.selected_viewchord = None
            self.songpart.deleteChord(ind)
            self.update()






