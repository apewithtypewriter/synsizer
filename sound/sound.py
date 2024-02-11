from envelope import Envelope
from waves import add_wave
import numpy as np
from scipy import signal


class Sound:
    """Create and modify a sound tone with specified properties
    
    Sounds are the basic building blocks of synsizer synthesis. They
    are added to Clips in order to create a sound clip.
    
    Keyword arguments:
    start       -- where in a Clip you wish the Sound to begin
    duration    -- length of time (in seconds) the sound lasts
    amplitude   -- the loudness (float from 0.0 to 1.0)
    freq        -- frequency (pitch in Hz)
    sample_rate -- samples (data points) per second (44100 Hz default)
    envelope    -- an Envelope object that shapes the sound amplitude
    filter      -- a Filter object that boosts or diminishes specified
                   frequency ranges
    
    Methods:
    add_waveform   -- add a soundwave to Sound data
    apply_envelope -- modify Sound data with Envelope
    apply_filter   -- modify Sound data with Filter
    change_pitch   -- adjust the Sound frequency
    """
    
    def __init__(self, start, duration, freq, waveform, amplitude=0.5,
        sample_rate=44100):
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
            
    def change_pitch(self, new_pitch):
        pass
