#!/usr/bin/python3
# basic explanation and original snippet based on the:
# https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

# note example A4
def get_frequency(note : str):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

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
def get_len(nl : int, dot = False):
    base = 1000/nl
    ext = 0.5*base if dot else 0
    return round(base+ext)

if __name__ == "__main__":
    print(get_frequency("C0"))
    print(get_len(4,True))
