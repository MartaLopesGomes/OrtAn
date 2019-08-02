#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

def orthogroups_to_dic(file):
    """
    :param file: Orthogroups.txt file, resulting from OrthoFinder analysis
    :return: dictionary containing the information of the Orthgroups. {OG1: [Seq1, Seq2, ...], OG2 ...}
    """
    res = {}
    single_og = {}
    with open(file, 'r') as f:
        orthogroups = f.readlines()
    for line in orthogroups:
        if len(line) > 0:
            og, prots = line.split(': ', 1)
            res[og.strip()] = [x.strip() for x in prots.split()]
            if len(res[og.strip()]) == 1:
                single_og[og.strip()] = res[og.strip()]
    return res, single_og

def speciesIDs_to_dic(file):
    res = {}
    with open(file, 'r') as f:
        species = f.readlines()
    for line in species:
        if len(line) > 0:
            sID, name = line.split(': ', 1)
            res[sID.strip()] = name.strip()
    return res

def sequencesIDs_to_dic(file):
    res = {}
    with open(file, 'r') as f:
        sequences = f.readlines()
    for line in sequences:
        if len(line) > 0:
            ssIDs, def_line = line.split(': ', 1)
            specieID, sequenceID = ssIDs.split('_')
            specieID, sequenceID = specieID.strip(), sequenceID.strip()
            name = def_line.split(None, 1)[0]
            name = name.replace(":", "_").replace(",", "_").replace("(", "_").replace(")", "_")
            res[name]= {}
            res[name]['spec'] = specieID
            res[name]['defl'] = def_line
    return res
