from modules.model.SBSongPart import SBSongPart
from modules.model.SBCommonTypes import convertSBPartTypeToString
from modules.view.SBViewElement import SBViewElement
from modules.view.SBViewChord import SBViewChord

class SBViewSongPart(SBViewElement):
    def __init__(self, master, canvas, songpart):
        SBViewElement.__init__(self,100,50)
        self.master = master
        self.songpart = songpart
        self.canvas = canvas
        self.width = 600
        self.height = 120
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="#EEEEEE")
        self.canvas.create_text(self.x+self.width/2, self.y + 10, text=self.songpart.getName())
        self.canvas.create_text(self.x+self.width/2, self.y + 30, text="[" + convertSBPartTypeToString(self.songpart.getPartType()) + "]")
        self.view_chords = []

        x_offset = 0
        self.col = 0
        cnt = 0
        for e in songpart.getChords():
            nc = SBViewChord(self.master, self.canvas, e, self, 0, self.col)
            self.view_chords.append(nc)
            #col = col + e.getLengthInBars() + 1
            cnt = cnt + 1
            self.col = self.col + e.getLengthInBars()

        self.canvas.tag_bind(self.rect, '<Double-Button-1>', self.say_hu)

    def update(self):
        col = 0
        for e in self.view_chords:
            e.setCol(col)
            col = col + e.getChord().getLengthInBars()

    def addChord(self, chord):
        self.songpart.addChord(chord)
        nc = SBViewChord(self.master, self.canvas, chord, self, 0, self.col)
        self.view_chords.append(nc)


    def say_hu(self, event):

        print("hu... double click")




