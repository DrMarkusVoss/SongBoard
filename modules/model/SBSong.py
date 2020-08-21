from modules.model.SBCommonTypes import SBBeatType

class SBSong:
    def __init__(self, name):
        self.name = name
        self.songparts = []
        self.tempo = 0
        self.beat = SBBeatType.FOUR_FOUR

    def getName(self):
        return self.name

    def setTempo(self, tempo):
        self.tempo = tempo


