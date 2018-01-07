class Scale(object):
    chrom_sh = 'A A# B C C# D D# E F F# G G#'.split()
    chrom_fl = 'A Bb B C Db D Eb E F Gb G Ab'.split()
    steps = {'m': 1, 'M': 2, 'A': 3}

    def __init__(self, tonic, scale_name, pattern=None):
        self.tonic = tonic.capitalize()
        self.scale_name = scale_name
        self.name = ' '.join([self.tonic, self.scale_name])
        if pattern:
            pattern = [self.steps[step] for step in list(pattern)]
            if sum(pattern) > 12:
                raise ValueError('pattern exceeds octave')
        self.pattern = pattern

    @property
    def pitches(self):
        if (self.tonic in 'Bb Db Eb Gb Ab D F'.split() or
                self.scale_name == 'locrian'):
            chromatic = self.chrom_fl + self.chrom_fl
        else:
            chromatic = self.chrom_sh + self.chrom_sh
        tonic_index = chromatic.index(self.tonic)
        if not self.pattern:
            return chromatic[tonic_index:tonic_index + 12]
        else:
            ind = tonic_index
            pitch_list = [chromatic[ind]]
            for step in list(self.pattern)[:-1]:
                ind += step
                pitch_list.append(chromatic[ind])
            return pitch_list

