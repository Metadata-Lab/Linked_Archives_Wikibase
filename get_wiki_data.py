#import pywikibot
from SPARQLWrapper import SPARQLWrapper, JSON
import os, ssl, json


'''
find the wikidata q identifier if a page with the label exists
@param label: the label of the page to search for
@returns label string if page exists, None if it doesn't
'''
def search_for_q(label):
#     site = pywikibot.Site("en", "wikipedia")
#
#     try:
#         #search wikibase for item with label
#         page = pywikibot.Page(site, label)
#         item = pywikibot.ItemPage.fromPage(page)
#
#         #if found, do some magic to turn item into proper string
#         magic = {}
#         magic["Q"] = str(item)
#         q = magic["Q"]
#         #make sure we only get the Q### part
#         magic["Q"] = q[11:-2]
#         return magic["Q"]
#
#     except:
        return None

'''
get all of the statements for an entity in wikidata
@param q_string the q identifier for the entity as a string
@returns dictionary of statements: {property: [p id, {value: value q id or None}]}
'''
def get_statements(q_string):

    #set up sparql wrapper with proper permissions
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

    #query to get all properties based on q value
    query = 'SELECT ?property ?propLabel ?value ?valueLabel WHERE {{ ' \
            'wd:{q} ?property ?value.' \
            'SERVICE wikibase:label {{bd:serviceParam wikibase:language "en".}}' \
            '?prop wikibase:directClaim ?property.' \
            '?prop rdfs:label ?propLabel.filter(lang(?propLabel) = "en"). }}'.format(q=q_string)

    sparql.setQuery(query)

    try :
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        dict = {}

        #parse through query resuults
        for result in results["results"]["bindings"]:

            #property url
            prop = result['property']['value']
            #property label text
            propLabel = result['propLabel']['value']
            #value of property
            val = result['value']['value']
            #value type - url or literal
            valType = result['value']['type']
            #text label for url value
            valLabel = result['valueLabel']['value']

            pnum = prop[prop.rfind("/")+1:]

            if valType == 'literal':
                value = {valLabel: None}
            elif valType == 'uri':
                if 'wikidata.org/entity' in val:
                    value = {valLabel: val[val.rfind('/')+1:]}
                else:
                    value = {valLabel: None}
            else:
                print(valType) #let me know if there is another type there

            dict[propLabel] = [pnum, value]

        #print(dict)
        return dict

    except Exception as e:
        print(e)
        return None


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



