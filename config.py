import json
import pathlib


class Config:
    current_dir = pathlib.Path(__file__).parent.resolve()
    
    with open("config.json") as config:
        defaults = json.load(config)["defaults"]
