def assignmma(q):
    n = 20
    if q == 'A#':
        n = 1
    if q == 'Bb':
        n = 1
    if q == 'B':
        n = 2
    if q == 'Cb':
        n = 2
    if q == 'B#':
        n = 3
    if q == 'C':
        n = 3
    if q == 'C#':
        n = 4
    if q == 'Db':
        n = 4
    if q == 'D':
        n = 5
    if q == 'D#':
        n = 6
    if q == 'Eb':
        n = 6
    if q == 'E':
        n = 7
    if q == 'Fb':
        n = 7
    if q == 'E#':
        n = 8
    if q == 'F':
        n = 8
    if q == 'F#':
        n = 9
    if q == 'Gb':
        n = 9
    if q == 'G':
        n = 10
    if q == 'G#':
        n = 11
    if q == 'Ab':
        n = 11
    if q == 'A':
        n = 12
    return n


def assignint(z):
    if z == 0:
        x = 'Perfect Octave/Unison'
    if z == 1:
        x = 'Minor Second'
    if z == 2:
        x = 'Major Second'
    if z == 3:
        x = 'Minor Third'
    if z == 4:
        x = 'Major Third/Diminished Fourth'
    if z == 5:
        x = 'Perfect Fourth'
    if z == 6:
        x = 'Augmented Fourth/Tritone/Diminished Fifth'
    if z == 7:
        x = 'Perfect Fifth'
    if z == 8:
        x = 'Augmented Fifth/Minor Sixth'
    if z == 9:
        x = 'Major Sixth'
    if z == 10:
        x = 'Minor Seventh'
    if z == 11:
        x = 'Major Seventh'
    return x
