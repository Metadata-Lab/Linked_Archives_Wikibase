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
    #find out the kind of item dealt with from file name
    label = infile[ infile.rfind('/')+1 : infile.rfind('.') ]
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            if "wiki" in data[item].keys():
                #get into wiki dictionary
                wiki_dict = data[item]["wiki"]
                for prop_name in wiki_dict:
                    #replace commas so it doesn't mess up csv output
                    name_csv_safe = prop_name.replace(',', ';')
                    pnum = wiki_dict[prop_name][0]
                    if name_csv_safe in props.keys():
                        #count up repeated properties
                        props[name_csv_safe][2] += 1
                        #add object type to proprerty list
                        if label not in props.get(name_csv_safe):
                            props.get(name_csv_safe).append(label)
                    else:
                        props[name_csv_safe] = [pnum, label, 1]
    return props

'''
get wikidata properties from item dictionaries
@param infiles - list of files to get properties from
@returns outfile - file to output properties, counts, and item type
'''
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

'''
filter out wiki properties we definitely don't want
@param infile entity file to edit
@param outfile file to put edited item dictionaries
'''
def refine_wiki_data(infile, outfile):
    edited_dict = {}
    with open(infile) as json_file:
        data = json.load(json_file)
        for item in data.keys():
            #get into wikidata property dictionary
            if "wiki" in data.get(item).keys():
                wiki_dict = data.get(item).get("wiki")
                new_wiki_dict = {}
                #remove wiki properties if we can't determine if the item retrieved is correct
                if "different from" in wiki_dict.keys():
                    entity = data.get(item)
                    entity["wiki"] = {}
                    edited_dict[item] = entity
                else:
                    for prop in wiki_dict.keys():
                        #get rid of any ID, username, and image properties - not useful to our db
                        #only take the other properties
                        if "ID" not in prop and "username" not in prop and "image" not in prop:
                            new_wiki_dict[prop] = wiki_dict.get(prop)
                    entity = data.get(item)
                    entity["wiki"] = new_wiki_dict
                    edited_dict[item] = entity
            else:
                #items without wiki props go unedited
                edited_dict[item] = data.get(item)
    json_file.close()
    with open(outfile, "w") as json_out:
        json.dump(edited_dict, json_out)

'''
refine all entity files with wikidata properties
'''
def refine_wiki_props():
    #generate file paths for both input files and the edited versions for output
    infiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    for idx, val in enumerate(infiles): infiles[idx] = 'data/entities/' + val + '.json'
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'

    for idx, val in enumerate(infiles): refine_wiki_data(val, outfiles[idx])

'''
refine person properties and get the releant new properties
'''
def new_props_people():
    #refine_wiki_data("data/entities/people.json", "data/entities/people_edited.json")
    get_new_props(["data/entities/people_edited.json"], "data/properties_export_people.csv")

'''
refine wiki properties and get relevant one for all entities other than people
'''
def new_props_general():
    #refine_wiki_props()
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'series', 'subjects']
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'
    get_new_props(outfiles, "data/properties_export.csv")