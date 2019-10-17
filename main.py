#!/usr/bin/python3
# basic explanation and original snippet based on the:
# https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

notes = ["A", "A#", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


# read file and parse it
def read_file(filename : str):
    src = open(filename, "r")
    lines = src.readlines()
    meta_data = lines[0]
    note_data = lines[1:]

    return parse_meta_data(meta_data), parse_note_data(note_data)


# metadata:
# tempo -- beats per minute
# TODO add other arguments such as hashes and "b"
def parse_meta_data(meta_data : str):
    meta_data = meta_data.replace("\n","").split()
    tempo = int(meta_data[0])
    tempo = (1000*60.0)/tempo
    return tempo


def parse_note_data(node_data : list):
    music = []
    for data in node_data:
        entries = data.replace("\n","").split()
        note = entries[0]
        dur = int(entries[1][0])
        dot = True if entries[-1] == "." else False
        md = (get_frequency(note), get_duration(dur,dot))
        music.append(md)
    return music

def transpose(note: str):
    
    octave = int(note[-1])
    note_name = note[:-1].replace("b","")
    
    octave = octave if note_name != "A" else octave -1
    note_name = notes[notes.index(note_name)-1]
    
    return note_name + str(octave)


# note example A4
def get_frequency(note : str):

    note = note if note.count("b") == 0 else transpose(note)

    note_name = note[:-1]
    octave = int(note[-1])

    key_number = notes.index(note_name)

    off = 12 if key_number < 3 else 0

    key_number = key_number + off + (12*(octave-1)) +1

    return round(440 * pow(2, (key_number- 49) / 12))

# note lenght is 1/nl [ms]
# - whole note      nl = 1
# - half note       nl = 2
# - quarter note    nl = 4 etc.
def get_duration(nl : int, dot = False):
    base = 1.0/nl
    ext = 0.5*base if dot else 0
    return base+ext


def create_gcode(tempo:int, music : list):
    gcode = ""
    for data in music:
        fqn = data[0]
        dur = data[1]*tempo
        gcode += f'M300 S{fqn} P{round(dur)}\n'
        
    print(gcode)

if __name__ == "__main__":
    print(get_frequency("C0"))
    print(get_duration(4,True))
    tempo, music = read_file("imperial_march.nf")
    create_gcode(tempo,music)
