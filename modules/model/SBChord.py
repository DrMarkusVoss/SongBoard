from modules.model.SBCommonTypes import SBArpKind

class SBChord:
    def __init__(self, note, harmonic):
        # SBChordNote
        self.note = note
        # SBChordHarmonic
        self.harmonic = harmonic
        self.length_bars = 0
        self.arp = False
        self.arp_kind = SBArpKind.LOW_TO_HIGH
        self.pitch = 0

    def setArp(self, onoff):
        self.arp = onoff

    def setPitch(self, pitch):
        self.pitch = pitch

    def getPitch(self):
        return self.pitch

    def setArpKind(self, kind):
        self.arp_kind = kind

    def setNote(self, note):
        self.note = note

    def getNoteStr(self):
        return str(self.note.name)

    def setHarmonic(self, harmonic):
        self.harmonic = harmonic

    def setLengthInBars(self, bars):
        self.length_bars = bars

    def getLengthInBars(self):
        return self.length_bars

    def getHarmonicStr(self):
        return str(self.harmonic.name)

    def getHarmonic(self):
        return self.harmonic

