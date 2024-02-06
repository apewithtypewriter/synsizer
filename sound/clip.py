from sound import Sound
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write


class Clip:
    """
    """
    
    def __init__(self, start, stop, sample_rate = 44100):
        num_points = int((stop - start) * sample_rate)
        self.start = start
        self.stop = stop
        self.sample_rate = sample_rate
        self.data = np.zeros(num_points)
        
    def add_sound(self, new_sound):
        startpoint = int(np.floor(new_sound.start * self.sample_rate))
        endpoint = startpoint + len(new_sound.data)
        self.data[startpoint:endpoint] += new_sound.data
        
    def loop(self, n):
        self.data = np.repeat(self.data, n)
        
    def plot(self, show = True, save = False):
        plt.plot(self.data)
        
        if show:
            plt.show()
        
        if save:
            plt.savefig("clip_output.png")
        
    def save(self, path):
        write(path, self.sample_rate, self.data)
