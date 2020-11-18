import json

'''
import json file into dictionary
@param file file name to import
@returns dictionary of all data
'''
def json_to_dict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def get_q_nums_single(infile, outfile):
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "Q" in data[item].keys():
                q = data[item]["Q"]
                if q is not None:
                    outfile.write(q + '\n')

def get_q_nums(infiles):
    with open("data/wiki_q_ids.csv", "w") as qcsv:
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


def get_new_props(infiles, outfile):
    out = open(outfile, "w")
    props = {}
    for file in infiles:
        props.update(get_new_props_single(file))

    for prop in props.keys():
        output = prop
        for info in props.get(prop):
            output += ',' + str(info)
        out.write(output + '\n')
    out.close()


def refine_wiki_data(infile, outfile):
    edited_dict = {}
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "wiki" in data.get(item).keys():
                wiki_dict = data.get(item).get("wiki")
                new_wiki_dict = {}
                if "different from" in wiki_dict.keys():
                    entity = data.get(item)
                    entity["wiki"] = {}
                    edited_dict[item] = entity
                else:
                    for prop in wiki_dict.keys():
                        if "ID" not in prop and "username" not in prop and "image" not in prop:
                            new_wiki_dict[prop] = wiki_dict.get(prop)
                    entity = data.get(item)
                    entity["wiki"] = new_wiki_dict
                    edited_dict[item] = entity
            else:
                edited_dict[item] = data.get(item)
    json_file.close()
    with open(outfile, "w") as json_out:
        json.dump(edited_dict, json_out)

def refine_wiki_props():
    infiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    for idx, val in enumerate(infiles): infiles[idx] = 'data/entities/' + val + '.json'
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'

    for idx, val in enumerate(infiles): refine_wiki_data(val, outfiles[idx])


def new_props_people():
    #refine_wiki_data("data/entities/people.json", "data/entities/people_edited.json")
    get_new_props(["data/entities/people_edited.json"], "data/properties_export_people.csv")

def new_props_general():
    #refine_wiki_props()
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'series', 'subjects']
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'
    get_new_props(outfiles, "data/properties_export.csv")