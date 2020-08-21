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

    def setArp(self, onoff):
        self.arp = onoff

    def setArpKind(self, kind):
        self.arp_kind = kind

    def setNote(self, note):
        self.note = note

    def setHarmonic(self, harmonic):
        self.harmonic = harmonic

    def setLengthInBars(self, bars):
        self.length_bars = bars

