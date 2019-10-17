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


if __name__ == "__main__":
    print(get_frequency("C0"))
