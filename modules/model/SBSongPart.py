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
        self.nr_repeats = 0
        self.chord_lines = []

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setNrRepeats(self, nr_repeats):
        self.nr_repeats = nr_repeats

    def getNrRepeats(self):
        return self.nr_repeats

    def setTempo(self, tempo):
        self.tempo = tempo

    def getTempo(self):
        return self.tempo

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

    def deleteChord(self, chord_ind):
        self.chords.pop(chord_ind)

    def addTextline(self, textline):
        self.parttext.append(textline)

    def deleteTextline(self, tl_ind):
        self.parttext.pop(tl_ind)

    def getTextlines(self):
        return self.parttext

    def getTextline(self, tl_ind):
        return self.parttext[ind]




