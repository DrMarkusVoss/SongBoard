from midiutil import MIDIFile
import pygame

class SBMIDIMusicPlayer:
    def __init__(self, midi_filename):
        self.midi_filename = midi_filename

    def setMIDIFile(self, fn):
        self.midi_filename = fn

    def getMIDIFilename(self):
        return self.midi_filename

    def playMusicFromMIDIFile(self):
        # play the midi file in a blocking manner
        clock = pygame.time.Clock()
        pygame.mixer.music.load(self.midi_filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)  # check if playback has finished

    def play(self):
        # mixer config
        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 1024  # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(0.8)

        # listen for interruptions
        try:
            # use the midi file you just saved
            self.playMusicFromMIDIFile()
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            # (works only in console mode)
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit

