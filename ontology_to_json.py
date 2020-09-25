import pywikibot
import json

#DEFINE GLOBAL VARIABLES

# create lists for sorting
subjects = []
people = []
names = []
countries = []
events = []
series = []
objects = []
collections = []
bib_series = []

belfer = []
becker = []
koppel = []
collection_lists = [belfer, becker, koppel]


def import_data():
    data = open("../all_owl.txt", "r")

    # sort entries in file
    for line in data:
        entry = line.split('|')

        entity = entry[0]
        if "/subject" in entity:
            subjects.append(entry)
        elif "227." in entity:
            belfer.append(entry)
        elif "140." in entity:
            becker.append(entry)
        elif "185." in entity:
            koppel.append(entry)
        elif "/person" in entity:
            people.append(entry)
        elif "/names" in entity:
            names.append(entry)
        elif "/countries" in entity:
            countries.append(entry)
        elif "/event" in entity:
            events.append(entry)
        elif "/series" in entity:
            series.append(entry)
        elif "/object" in entity:
            objects.append(entry)
        elif "/collection" in entity:
            collections.append(entry)
        elif "/bib_series" in entity:
            bib_series.append(entry)

def strip_quotes(val):
    new = val.strip("\"").strip("\'")
    return new

def parse_value(val):
    v = val[1:-1]
    list = v.split('\t')
    for idx, value in enumerate(list):
        list[idx] = strip_quotes(value)

    return list


def parse_entities(dict, list):
    for item in list:
        i_dict = {}

        label = ""

        #add all properties from ontology
        for idx, val in enumerate(item):
            if val == '': continue

            if idx == 0:
                i_dict["IRI"] = [val]
            elif idx == 1:
                i_dict["hasAppearance"] = parse_value(val)
            elif idx == 2:
                i_dict["hasBib_series"] = parse_value(val)
            elif idx == 3:
                i_dict["hasComposer"] = parse_value(val)
            elif idx == 4:
                i_dict["hasHost"] = parse_value(val)
            elif idx == 5:
                i_dict["hasHumanSubject"] = parse_value(val)
            elif idx == 6:
                i_dict["hasInterviewee"] = parse_value(val)
            elif idx == 7:
                i_dict["hasObject"] = parse_value(val)
            elif idx == 8:
                i_dict["hasPerformer"] = parse_value(val)
            elif idx == 9:
                i_dict["hasPhotographer"] = parse_value(val)
            elif idx == 10:
                i_dict["hasReporter"] = parse_value(val)
            elif idx == 11:
                i_dict["hasSubject"] = parse_value(val)
            elif idx == 12:
                i_dict["is_part_of"] = parse_value(val)
            elif idx == 13:
                i_dict["is_related_to"] = parse_value(val)
            elif idx == 14:
                i_dict["is_created_by"] = parse_value(val)
            elif idx == 15:
                i_dict["firstname"] = strip_quotes(val)
            elif idx == 16:
                i_dict["lastname"] = strip_quotes(val)
            elif idx == 17:
                i_dict["middleinitial"] = strip_quotes(val)
            elif idx == 18:
                i_dict["role"] = [strip_quotes(val).strip("*")]
            elif idx == 19:
                i_dict["coverage"] = strip_quotes(val)
            elif idx == 20:
                i_dict["date"] = strip_quotes(val)
            elif idx == 21:
                i_dict["description"] = strip_quotes(val)
            elif idx == 22:
                i_dict["identifier"] = strip_quotes(val)
            elif idx == 23:
                i_dict["publisher"] = strip_quotes(val)
            elif idx == 24:
                i_dict["rights"] = strip_quotes(val)
            elif idx == 25:
                i_dict["subject"] = strip_quotes(val)
            elif idx == 26:
                i_dict["title"] = strip_quotes(val)
            elif idx == 27:
                i_dict["title_alt"] = strip_quotes(val)
            elif idx == 28:
                i_dict["type"] = strip_quotes(val)
            elif idx == 29:
                i_dict["type/mediaType"] = strip_quotes(val)
            elif idx == 30:
                i_dict["mediaType"] = strip_quotes(val)
            elif idx == 31:
                i_dict["comment"] = strip_quotes(val)
            elif idx == 32:
                label = strip_quotes(val)
                i_dict["label"] = [label]

        if "firstname" in i_dict.keys():
            label = i_dict["firstname"]
            if len(i_dict["firstname"]) == 1:
                label += "."
            if "middleinitial" in i_dict.keys():
                label += " " + i_dict["middleinitial"]
                if len(i_dict["middleinitial"]) == 1:
                    label += "."
            if "lastname" in i_dict.keys():
                label += " " + i_dict["lastname"]
            label = label.replace("  ", " ").replace("Unknown", "").strip()
            if len(label) == 0:
                label = "Unknown"

        print(label)

        #SEARCH WIKIDATA, ADD Q NUM TO DICT IF EXISTS
        site = pywikibot.Site("en", "wikipedia")

        try:
            page = pywikibot.Page(site, label)
            item = pywikibot.ItemPage.fromPage(page)
            i_dict["Q"] = str(item)
            q = i_dict["Q"]
            i_dict["Q"] = q[11:-2]
            print(i_dict["Q"])
        except Exception as e:
            print(e)

        #put together multiple entries with same label
        if label in dict.keys():

            if i_dict["IRI"][0] not in dict[label]["IRI"]:
                for iri in dict[label]["IRI"]:
                    i_dict["IRI"].append(iri)

            for rel in dict[label]["is_related_to"]:
                if rel not in i_dict["is_related_to"]:
                    i_dict["is_related_to"].append(rel)

            if i_dict["role"][0] not in dict[label]["role"]:
                for role in dict[label]["role"]:
                    i_dict["role"].append(role)

            if i_dict["label"][0] not in dict[label]["label"]:
                print(label)
                for lab in dict[label]["label"]:
                    i_dict["label"].append(lab)


        #add new entry to dictionary
        dict[label] = i_dict

    #return updated dictionary
    return dict


def parse_people():
    people_dict = {}

    people_dict = parse_entities(people_dict, people)

    # with open('../people.json', 'w') as outfile:
    #     json.dump(people_dict, outfile)


def main():
    import_data()
    parse_people()


if __name__ == '__main__':
    main()