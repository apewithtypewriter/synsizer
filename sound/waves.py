import numpy as np
from scipy import signal


def add_wave(data, amplitude, freq, waveform, sample_rate):
    """
    """
    
    waveforms = {
        "sin": np.sin,
        "saw": signal.sawtooth,
        "square": signal.square,
        "triangle": signal.sawtooth
    }
    
    for i in range(0, len(data)):
        data[i] += amplitude * waveforms[waveform](
            2 * np.pi * freq * i / sample_rate)
        
    return data
        
