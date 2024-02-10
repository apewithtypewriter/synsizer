from clip import Clip
from sound import Sound
from envelope import Envelope
from filter import Filter


class Workspace:
    """ A workspace is a collection of all current components.
    
    Component options: Clip, Sound, Envelope, Filter
    
    Methods:
    add -- adds a component to the workspace
    """
    
    def __init__(self):
        self.clips = []
        self.sounds = []
        self.envelopes = []
        self.filters = []
        
    def add(self, new_component):
        if isinstance(new_component, Clip):
            self.clips.append(new_component)
        elif isinstance(new_component, Sound):
            self.sounds.append(new_component)
        elif isinstance(new_component, Envelope):
            self.envelopes.append(new_component)
        elif isinstance(new_component, Filter):
            self.filters.append(new_component)
        else:
            raise ValueError(f"{new_component} cannot be added to workspace")
