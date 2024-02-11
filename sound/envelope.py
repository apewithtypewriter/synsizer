import json

import numpy as np

from config import Config


class Envelope:
    """
    """
    
    def __init__(self, params = Config.defaults["envelope"]):
        self.params = params
        self.check_if_valid()
        
    def apply_to_sound(self, data):
        num_points = len(data)
        
        a_num_points = int(np.floor(
            num_points * self.params["a"]["duration"]))
        a_amplitude = self.params["a"]["amplitude"]
        
        ad_num_points = a_num_points + int(np.floor(
            num_points * self.params["d"]["duration"]))
        d_amplitude = self.params["d"]["amplitude"]
        
        ads_num_points = ad_num_points + int(np.floor(
            num_points * self.params["s"]["duration"]))
        s_amplitude = self.params["s"]["amplitude"]
        
        adsr_num_points = ads_num_points + int(np.floor(
            num_points * self.params["r"]["duration"]))
        r_amplitude = self.params["r"]["amplitude"]
        
        for i in range(0, a_num_points):
            data[i] *= i * (a_amplitude / a_num_points)
            
        for i in range(a_num_points, ad_num_points):
            data[i] *= (a_amplitude 
                        - (i - a_num_points)
                        * (a_amplitude - d_amplitude)
                        / (ad_num_points - a_num_points))
        
        for i in range(ad_num_points, ads_num_points):
            data[i] *= s_amplitude
        
        for i in range(ads_num_points, adsr_num_points):
            data[i] *= (s_amplitude
                        - (i - ads_num_points)
                        * (s_amplitude - r_amplitude)
                        / (adsr_num_points - ads_num_points))
                
        return data
        
    def check_if_valid(self):
        total_duration = (self.params["a"]["duration"]
                          + self.params["d"]["duration"]
                          + self.params["s"]["duration"]
                          + self.params["r"]["duration"])
                         
        if total_duration != 1.0:
            raise ValueError(f"Filter duration does not equal 100%.")
            
        if self.params["d"]["amplitude"] != self.params["s"]["amplitude"]:
            raise ValueError("Decay amplitude must equal sustain amplitude.")
            
        if self.params["d"]["amplitude"] > self.params["a"]["amplitude"]:
            raise ValueError(
                "Decay amplitude is greater than attack amplitude.")
