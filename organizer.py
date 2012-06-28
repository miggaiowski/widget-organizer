#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import sys
import pprint
from plistparser import parser

def plistToString(pathToPList):
    os.system("""/usr/libexec/PlistBuddy -c "Print" """ + pathToPList + " > temp.plist")
    with open("temp.plist", 'r') as f:
        plist = f.read()
        plist_lines = plist.split("\n")
    os.remove("temp.plist")
    return plist_lines

if __name__ == "__main__":
    plstr = plistToString(sys.argv[1])
    plist = parser.parsePlist(plstr)
    weathers = [i for i in plist['layer-gadgets'] if i['path'] == '/Library/Widgets/Weather.wdgt/']
    pprint.pprint(weathers)

    

    
