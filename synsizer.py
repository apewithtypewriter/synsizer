#!/usr/bin/env python
import argparse
from pathlib import Path


def arg_parser():
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
    
    return parser


if __name__ == "__main__":
    parser = arg_parser()
