#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def parseDict(pl, nl):
    d = {}
    current_line = nl
    while current_line < len(pl):
        line = pl[current_line]
        if line.find("}") != -1:
            return d, current_line
        else:
            if line.find(" = ") == -1:
                print "Erro ao parsear dict: ", line
            l = line.strip().split(" = ")
            if l[1].find("Dict {") != -1:
                right_side, current_line = parseDict(pl, current_line+1)
            elif l[1].find("Array {") != -1:
                right_side, current_line = parseArray(pl, current_line+1)
            else:
                right_side = l[1]
            d[l[0]] = right_side
        current_line += 1

def parseArray(pl, nl):
    a = []
    current_line = nl
    while current_line < len(pl):
        line = pl[current_line]
        if line.find("}") != -1:
            return a, current_line
        else:
            l = line.strip()
            if l.find("Dict {") != -1:
                right_side, current_line = parseDict(pl, current_line+1)
            elif l.find("Array {") != -1:
                right_side, current_line = parseArray(pl, current_line+1)
            else:
                right_side = l
            a.append(right_side)
        current_line += 1

def parsePlist(pl):
    first_line = pl[0]
    if first_line.find("Dict {") != -1:
        plist, lines = parseDict(pl, 1)
    elif first_line.find("Array {") != -1:
        plist, lines = parseArray(pl, 1)
    return plist

