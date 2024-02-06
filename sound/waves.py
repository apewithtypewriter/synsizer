import numpy as np
from scipy import signal


def add_wave(data, amplitude, freq, waveform, sample_rate):
    """Add a waveform to sound data
    
    Multiple waves may be added to a Sound. In that case, the principle
    of the superposition of waves (add together amplitudes for each
    corresponding time t).
    
    Waveform options: sin, saw, square, triangle
    
    Keyword arguments:
    data        -- the audio data array (numpy array of floats)
    amplitude   -- the loudness (float from 0.0 to 1.0)
    freq        -- frequency (pitch in Hz)
    sample_rate -- samples (data points) per second (44100 Hz default)
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
        
