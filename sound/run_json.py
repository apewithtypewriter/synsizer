from commands import Commands.json_form
import json


def read(path):
    with open(path, "r") as file:
        data = json.load(path)
        
    return data
    
def create(input_path):
    data = read(input_path)
