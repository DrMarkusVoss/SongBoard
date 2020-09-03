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

    def getTempo(self):
        return self.tempo

    def setBeat(self, beat):
        self.beat = beat

    def getBeatsPerBar(self):
        retval = 4
        if (self.beat == SBBeatType.FOUR_FOUR):
            retval = 4
        elif (self.beat == SBBeatType.THREE_FOUR):
            retval = 3

        return retval

    def addPart(self, part):
        self.songparts.append(part)

    def getParts(self):
        return self.songparts

    def getBeat(self):
        return self.beat


