#!/usr/bin/env python

import os
import argparse
from files import make_hardlinks

'''Command line input: "src1" "src2" "src3 ... srcn dest_dir , and then applies make_make_hardlinks([src1,src2,src3,...srcn],dest_dir)'''
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Creates hardlinks of all given paths to destination folder with the same name as the original name.')
    parser.add_argument('source_paths', nargs='+', help='Source of all hardlinks to be made.')
    parser.add_argument('destination_dir', help='Destination directory of all hardlinks.')
    
    args = parser.parse_args()
    
    make_hardlinks(args.source_paths,args.destination_dir)
