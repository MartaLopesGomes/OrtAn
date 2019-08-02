#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import os

def get_reps(file, index):
    res = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    i = 0
    #stop = False
    i_seq = 0
    while i < len(lines): # and not stop:
        if len(index) == 0:
            #stop = True
            break
        if len(lines[i]) > 0:
            if lines[i][0] == '>':
                i_seq += 1
                if i_seq-1 in index:
                    index.remove(i_seq-1)
                    is_seq = True
                    seq = ''
                    def_line = lines[i]
                    i += 1
                    while is_seq and i < len(lines):
                        if len(lines[i]) == 0:
                            i += 1
                        elif lines[i][0] != '>':
                            seq += lines[i]
                            i += 1
                        else:
                            is_seq = False
                    res[def_line] = seq
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    return res

# TODO: delete this before commit

def get_reps_old(file, index):
    res = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    i = 0
    #stop = False
    i_seq = 0
    while i < len(lines): # and not stop:
        if len(index) == 0:
            #stop = True
            break
        if len(lines[i]) > 0:
            if lines[i][0] == '>':
                i_seq += 1
                if i_seq-1 in index:
                    index.remove(i_seq-1)
                    is_seq = True
                    seq = ''
                    def_line = lines[i]
                    i += 1
                    while is_seq and i < len(lines):
                        if len(lines[i]) == 0:
                            i += 1
                        elif lines[i][0] != '>':
                            seq += lines[i]
                            i += 1
                        else:
                            is_seq = False
                    res[def_line] = seq
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    return res

def get_associations_relaxs(dir_in):
    res = {}
    diamond = {}
    files = [f for f in os.listdir(dir_in) if os.path.isfile(os.path.join(dir_in + f)) and not f.startswith('.')]
    for file in files:
        db = file.split('|')[-1]
        with open(os.path.join(dir_in, file)) as f:
            hits = f.readlines()
        for hit in hits:
            # query, target, ident = hit.split()
            query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send = hit.split()
            og = query.split('_')[0]
            if og not in res:
                res[og] = [db]
                diamond[og] = [[db, query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send]]
            elif db not in res[og]:
                res[og].append(db)
                diamond[og].append([db, query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send])
    return res, diamond

def change_def_lines(file, og):
    with open(file, 'r') as f:
        text = f.readlines()
    last = len(text)
    for i in range(last):
        if len(text[i]) > 0 and text[i][0] == '>':
            def_line = text[i].strip()
            new_def_line = def_line[0] + og + '_' + def_line[1:] + '\n'
            text[i] = new_def_line
    return text

def dict_diamond_res(dir, file, multiple_og, previous_dic):
    if not multiple_og:
        og_id, db = file.split('|')
        if og_id not in previous_dic:
            previous_dic[og_id] = []
    with open(os.path.join(dir, file), 'r') as f:
        hits = f.readlines()
    for hit in hits:
        query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send = hit.split()
        if multiple_og:
            og = query.split('_')[0]
            db = file.split('|')[1]
            query = '_'.join(query.split('_')[1:])
            if og not in previous_dic:
                previous_dic[og] = []
            previous_dic[og].append([db, query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send])
        else:
            query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send = hit.split()
            previous_dic[og_id].append([db, query, target, ident, ppos, qlen, slen, qstart, qend, sstart, send])
    return previous_dic

