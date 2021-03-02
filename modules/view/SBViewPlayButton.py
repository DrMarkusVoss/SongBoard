from modules.view.SBViewElement import SBViewElement
from time import sleep

class SBViewPlayButton(SBViewElement):
    def __init__(self, master, canvas, parent):
        self.master = master
        self.canvas = canvas
        self.parent = parent

        SBViewElement.__init__(self, self.parent.getX() + self.parent.getWidth() - 40, self.parent.getY()+10, 30, 30)

        self.circbut = self.canvas.create_oval(self.x, self.y, self.x + self.getWidth(), self.y + self.getHeight(),fill="white")
        self.trianglebut = self.canvas.create_polygon(self.x + 10, self.y + 5, self.x + 10, self.y + 25, self.x + 25,
                                                      self.y + 15, self.x + 10, self.y + 5)

        self.canvas.tag_bind(self.circbut, '<Button-1>', self.playPressed)
        self.canvas.tag_bind(self.trianglebut, '<Button-1>', self.playPressed)

    def playPressed(self, event):
        self.master.reselectSongpart(self.parent)
        self.canvas.itemconfig(self.circbut, outline="red")
        self.canvas.itemconfig(self.trianglebut, fill="red")
        self.master.update()

        self.master.playSelSongpartAudio()

        self.canvas.itemconfig(self.circbut, outline="black")
        self.canvas.itemconfig(self.trianglebut, fill="black")




