#!/usr/bin/env python
from clip import Clip
from envelope import Envelope
from sound import Sound
from filter import Filter


if __name__ == "__main__":
    test_clip = Clip(0, 20)
    test_envelope = Envelope()
    test_filter = Filter(2000)
    saw_sound = Sound(8, 3, 220, "saw", amplitude=0.8)
    saw_sound2 = Sound(12, 3, 220, "saw", amplitude=0.8)
    square_sound = Sound(16, 3, 220, "square", amplitude=0.8)
    saw_sound.apply_envelope(test_envelope)
    saw_sound2.apply_envelope(test_envelope)
    saw_sound2.apply_filter(test_filter)
    square_sound.apply_envelope(test_envelope)
    test_clip.add_sound(saw_sound)
    test_clip.add_sound(saw_sound2)
    test_clip.add_sound(square_sound)
    test_clip.save("test_clip.wav")
    test_clip.plot()
    
