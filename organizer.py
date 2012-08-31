#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import sys
import pprint
from plistparser import parser

MY_PATH_TO_PLIST="~/Library/Preferences/com.apple.dashboard.plist"

def plistToString(pathToPList):
    os.system("""/usr/libexec/PlistBuddy -c "Print" """ + pathToPList + " > temp.plist")
    with open("temp.plist", 'r') as f:
        plist = f.read()
        plist_lines = plist.split("\n")
    os.remove("temp.plist")
    return plist_lines

def setIndices(plist):
    for i, p in enumerate(plist['layer-gadgets']):
        p['_pos'] = i

def align(weathers):
    delta = 165
    for i, w in enumerate(weathers):
        w['pos-y'] = i * delta

def getCommands(weathers, pathToPList):
    cmds = []
    command = """/usr/libexec/PlistBuddy -c "Set %s" """ + pathToPList 
    for w in weathers:
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":pos-y " + str(w['pos-y'])))
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":pos-x 20"))
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":percent-offset-x 0"))
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":percent-offset-y 0"))
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":percent-y 0"))
        cmds.append(command % ('layer-gadgets:' + str(w['_pos']) + ":percent-x 0"))
    return cmds

def execute(cmds):
    for c in cmds:
        os.system(c)

if __name__ == "__main__":
    pathToPList = sys.argv[1]
    plstr = plistToString(pathToPList)
    plist = parser.parsePlist(plstr)
    weathers = [i for i in plist['layer-gadgets'] if i['path'] == '/Library/Widgets/Weather.wdgt/']
    setIndices(plist)
    # pprint.pprint(weathers)
    align(weathers)
    # pprint.pprint(weathers)
    cmds = getCommands(weathers, pathToPList)
    execute(cmds)

    
