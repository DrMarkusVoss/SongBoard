from enum import Enum

class SBPartType(Enum):
    SOMETHING = 0
    INTRO = 1
    VERSE = 2
    CHORUS = 3
    BRIDGE = 4
    OUTTRO = 5
    INTERLUDE = 6


class SBBeatType(Enum):
    NOTHING = 0
    FOUR_FOUR = 1
    THREE_FOUR = 2
    SIX_EIGHT = 3

class SBChordNote(Enum):
    C = 1
    C# = 2
    D = 3
    D# = 4
    E = 5
    F = 6
    F# = 7
    G = 8
    G# = 9
    A = 10
    A# = 11
    B = 12

class SBChordHarmonic(Enum):
    MAJOR = 1
    MINOR = 2
    SEVENTH = 3
    NINTH = 4

class SBArpKind(Enum):
    LOW_TO_HIGH = 1
    HIGH_TO_LOW = 2
    RANDOWM = 3
    MIX_UP = 4
    MIX_DOWN = 5
