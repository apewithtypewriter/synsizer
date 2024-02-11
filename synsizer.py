#!/usr/bin/env python3
import argparse
from pathlib import Path

#import sound/run_json
#from sound/workspace import Workspace


def parse_args():
    """Create a parser object to parse command line args.
    
    Command line arguments:
    input_path      -- path to input json file
    output ("-o")   -- filename or path for output file
    release ("-r")  -- if true, use release sample_rate (see config)
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("-o", "--output")
    parser.add_argument("-r", "--release", action = "store_true")
    args = parser.parse_args()
    
    return args


if __name__ == "__main__":
    args = parse_args()
    #current_workspace = Workspace()
    
    if args.output:
        print(args.output)
        
    print(args.input_path)
