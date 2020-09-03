from modules.model.SBCommonTypes import SBPartType
from modules.model.SBCommonTypes import SBBeatType


class SBSongPart:
    def __init__(self, partname="default", parttype=SBPartType.SOMETHING):
        self.name = partname
        self.parttype = parttype
        self.color = 0
        # use a % to indicate a Chord within the part.
        # for each chord in "chords" there must be a % within the text
        self.parttext = []
        self.chords = []
        self.chords_synched_with = None
        self.tempo = 0
        self.beat = SBBeatType.FOUR_FOUR
        self.length_bars = 0

    def getName(self):
        return self.name

    def setTempo(self, tempo):
        self.tempo = tempo

    def setBeat(self, beat):
        self.beat = beat

    def addChord(self, chord):
        self.chords.append(chord)

    def setChords(self, chords):
        self.chords = chords

    def getChords(self):
        return self.chords

    def setLengthInBars(self, bars):
        self.length_bars = bars

    def setPartType(self, tpye):
        self.parttype = type

    def getPartType(self):
        return self.parttype



