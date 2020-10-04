'''
json_import.py
Author: Kate Polley
Last Modified: 09/25/2020

functions for importing data from the json files
'''

import json

'''
for all json files given, extract the q numbers
@param infiles: list of json files to parse
'''
def json_q_csv(infiles):
    qcsv = open("q_nums.csv", "w")
    for file in infiles:
        with open(file) as json_file:
            data = json.load(json_file)
            for item in data.keys():
                if "Q" in data[item].keys():
                    q = data[item]["Q"]
                    if q is not None:
                        qcsv.write(q + '\n')
    qcsv.close()

'''
find all of the properties used in wikidata to describe the objects
these will be in the item dictionary with the key "wiki"
property format: prop_label: [p, {value: q or None}]
    
'''
def get_new_props(infile):

    props = {}

    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "wiki" in data[item].keys():
                wiki_dict = data[item]["wiki"]
                for prop_name in wiki_dict:
                    try: props[prop_name] = wiki_dict[prop_name][0]
                    except: continue

    out = open("properties.csv", "w")
    for prop in props.keys():
        out.write(prop + ',' + props[prop] + '\n')


def main():
    #json_q_csv(["people.json"])
    get_new_props("people_expanded.json")

if __name__ == '__main__':
    main()

