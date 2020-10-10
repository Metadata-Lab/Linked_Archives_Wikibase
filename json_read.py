'''
json_read.py
Author: Kate Polley
Last Modified: 10-04-2020

functions for importing data from the json files
'''

import json

def get_q_nums_single(infile, outfile):
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "Q" in data[item].keys():
                q = data[item]["Q"]
                if q is not None:
                    outfile.write(q + '\n')

def get_q_nums(infiles):
    with open("data/q_nums.csv", "w") as qcsv:
        for file in infiles:
            get_q_nums_single(file, qcsv)
    qcsv.close()


'''
find all of the properties used in wikidata to describe the objects
these will be in the item dictionary with the key "wiki"
property format: prop_label: [p, {value: q or None}]   
'''
def get_new_props_single(infile):
    props = {}
    label = infile[ infile.rfind('/')+1 : infile.rfind('.') ]
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "wiki" in data[item].keys():
                wiki_dict = data[item]["wiki"]
                for prop_name in wiki_dict:
                    name_csv_safe = prop_name.replace(',', ';')
                    pnum = wiki_dict[prop_name][0]
                    if name_csv_safe in props.keys():
                        props[name_csv_safe][2] += 1
                        if label not in props.get(name_csv_safe):
                            props.get(name_csv_safe).append(label)
                    else:
                        props[name_csv_safe] = [pnum, label, 1]
    return props


def get_new_props(infiles):
    out = open("data/properties.csv", "w")
    props = {}
    for file in infiles:
        props.update(get_new_props_single(file))

    for prop in props.keys():
        output = prop
        for info in props.get(prop):
            output += ',' + str(info)
        out.write(output + '\n')
    out.close()