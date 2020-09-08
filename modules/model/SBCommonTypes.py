from enum import Enum


class SBPartType(Enum):
    SOMETHING = 0
    INTRO = 1
    VERSE = 2
    CHORUS = 3
    BRIDGE = 4
    OUTRO = 5
    BREAK = 6
    SOLO = 7
    INTERLUDE = 8

sbparttypedict = {SBPartType.SOMETHING: "SOMETHING",
                  SBPartType.INTRO: "INTRO",
                  SBPartType.VERSE: "VERSE",
                  SBPartType.CHORUS: "CHORUS",
                  SBPartType.BRIDGE: "BRIDGE",
                  SBPartType.OUTRO: "OUTRO",
                  SBPartType.BREAK: "BREAK",
                  SBPartType.SOLO: "SOLO",
                  SBPartType.INTERLUDE: "INTERLUDE"}

sbpartreversetpyedict = {y:x for x,y in sbparttypedict.items()}


def convertSBPartTypeToString(parttype):
    return sbparttypedict[parttype]

def convertStringToSBPartType(parttypestring):
    return sbpartreversetpyedict[parttypestring]

class SBBeatType(Enum):
    NOTHING = 0
    FOUR_FOUR = 1
    THREE_FOUR = 2
    SIX_EIGHT = 3
    FIVE_EIGHT = 4


class SBChordNote(Enum):
    NOTHING = 0
    C = 1
    Db = 2
    D = 3
    Eb = 4
    E = 5
    F = 6
    Gb = 7
    G = 8
    Ab = 9
    A = 10
    Bb = 11
    B = 12

class SBChordHarmonic(Enum):
    MAJOR = 1
    MINOR = 2
    SEVENTH = 3
    NINTH = 4
    DIMINISHED = 5
    AUGMENTED = 6

def convertStringToSBChordHarmonic(charharmstr):
    pass



class SBArpKind(Enum):
    NONE = 0
    LOW_TO_HIGH = 1
    HIGH_TO_LOW = 2
    RANDOM = 3
    MIX_UP = 4
    MIX_DOWN = 5

