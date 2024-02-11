import numpy as np
from scipy import signal


class Filter:
    """
    """
    
    def __init__(self, cutoff_freq, filter_type="lowpass"):
        self.cutoff_freq = cutoff_freq
        self.filter_type = filter_type
        
    def apply_filter(self, data, sample_rate):
        if self.filter_type == "lowpass":
            sos = signal.butter(2, self.cutoff_freq, btype="lowpass",
                fs = sample_rate, output = "sos")
            
        elif self.filter_type == "highpass":
            sos = signal.butter(2, self.cutoff_freq, btype="highpass",
                fs = sample_rate, output="sos")
            
        elif self.filter_type == "bandpass":
            sos = signal.butter(2, [self.cutoff_freq[0], self.cutoff_freq[1]],
                btype = "highpass", fs=sample_rate, output="sos")
                
        elif self.filter_type == "bandstop":
            sos = signal.butter(2, [self.cutoff_freq[0], self.cutoff_freq[1]],
                btype="highpass", fs=sample_rate, output="sos")
                
        else:
            raise ValueError(f"\"{self.filter_type}\" is not a valid filter")
        
        filtered_data = signal.sosfilt(sos, data)
        
        return filtered_data
            
