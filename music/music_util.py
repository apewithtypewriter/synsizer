import numpy as np
import re


def pitch2freq(letter, octave, sharps, flats):
    pitches = {
        "C": 16.35160,
        "D": 18.35405,
        "E": 20.60172,
        "F": 21.82676,
        "G": 24.49971,
        "A": 27.50000,
        "B": 30.86771
    }
    
    natural_freq = pitches[letter] * octave**2
    n = 12 * np.log2(natural_freq / 440) + 49
    
    if sharps > 0:
        new_n = n + sharps
    elif flats > 0:
        new_n = n - flats
    else:
        new_n = n
        
    freq = 440 * 2**((n - 49) / 12)
    
    return freq


def pitch(pitch_str):
    note = re.fullmatch(r"[A-G]((#+)|(b+))?[0-9]?", pitch_str)
    
    if note:
        letter = re.search(r"[A-G]", pitch_str).group(0)
        octave = int(re.search(r"[0-9]", pitch_str).group(0))
        sharps_str = re.search(r"#+", pitch_str)
        flats_str = re.search(r"b+", pitch_str)
        
        if sharps_str:
            sharps = len(sharps_str.group(0))
        else:
            sharps = 0
            
        if flats_str:
            flats = len(flats_str.group(0))
        else:
            flats = 0
            
        freq = pitch2freq(letter, octave, sharps, flats)
        
        return freq
        
    else:
        raise SyntaxError("Invalid pitch syntax")
