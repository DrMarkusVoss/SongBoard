from midiutil import MIDIFile
from modules.model.SBSong import SBSong
from modules.model.SBCommonTypes import SBChordHarmonic

# from mingus.core.progressions import to_chords, determine
# import mingus.core.notes as notes

class SBCtrlSongToMIDI:
    def __init__(self, song, midi_filename):
        self.song = song
        self.midi_filename = midi_filename
        track = 0
        time = 0  # In beats
        tempo = self.song.getTempo()  # In BPM

        self.midi_file = MIDIFile(1)
        self.midi_file.addTempo(track, time, tempo)
        # simple piano chord structure interval
        self.chord_major_int = [0,4,7]
        self.chord_minor_int = [0,3,7]
        self.chord_dim_int = [0,3,6]
        self.chord_aug_int =[0,4,8]
        self.midi_notes = {"C": 60, "Db": 61, "D": 62, "Eb": 63, "E": 64, "F": 65, "Gb": 66, "G": 67, "Ab": 68, "A": 69, "Bb": 70, "B": 71}


    def process(self):
        track = 0
        channel = 0
        time = 0  # In beats
        duration = self.song.getBeatsPerBar()  # In beats
        volume = 100  # 0-127, as per the MIDI standard

        for sp in self.song.getParts():
            for r in range(sp.getNrRepeats()):
                for c in sp.getChords():
                    print("writing note: " + c.getNoteStr())
                    #self.midi_file.addNote(track,channel, self.midi_notes[c.getNoteStr()], time, duration, volume)
                    for b in range(c.getLengthInBars()):
                        if (c.getHarmonic() == SBChordHarmonic.MAJOR):
                            for n in self.chord_major_int:
                                note = self.midi_notes[c.getNoteStr()] + n + c.getPitch()*12
                                self.midi_file.addNote(track, channel, note, time, duration, volume)
                        elif (c.getHarmonic() == SBChordHarmonic.MINOR):
                            for n in self.chord_minor_int:
                                note = self.midi_notes[c.getNoteStr()] + n + c.getPitch()*12
                                self.midi_file.addNote(track, channel, note, time, duration, volume)
                        elif (c.getHarmonic() == SBChordHarmonic.DIMINISHED):
                            for n in self.chord_dim_int:
                                note = self.midi_notes[c.getNoteStr()] + n + c.getPitch()*12
                                self.midi_file.addNote(track, channel, note, time, duration, volume)
                        elif (c.getHarmonic() == SBChordHarmonic.AUGMENTED):
                            for n in self.chord_aug_int:
                                note = self.midi_notes[c.getNoteStr()] + n + c.getPitch()*12
                                self.midi_file.addNote(track, channel, note, time, duration, volume)

                        time = time + self.song.getBeatsPerBar()


    def writeMIDIFile(self):
        self.process()
        with open(self.midi_filename, "wb") as output_file:
            self.midi_file.writeFile(output_file)


