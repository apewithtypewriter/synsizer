from envelope import Envelope
from waves import add_wave
import numpy as np
from scipy import signal


class Sound:
    """
    """
    
    def __init__(self, start, duration, freq, waveform, amplitude = 0.5,
        sample_rate = 44100):
        num_points = int(duration * sample_rate)
        
        self.start = start
        self.stop = start + duration
        self.sample_rate = sample_rate
        self.data = np.zeros(num_points)
        self.add_waveform(amplitude, freq, waveform)
    
    def add_waveform(self, amplitude, freq, waveform):
        self.data = add_wave(self.data, amplitude, freq, waveform,
            self.sample_rate)
                    
    def apply_envelope(self, envelope):
        self.data = envelope.apply_to_sound(self.data)
        
    def apply_filter(self, audio_filter):
        self.data = audio_filter.apply_filter(self.data, self.sample_rate)
            
    def change_pitch(new_pitch):
        pass
