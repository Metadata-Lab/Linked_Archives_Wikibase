from ontology_to_json import parse_all
from json_read import get_new_props
from get_wiki_data import refine_wiki_data
from wikibase_import import import_first_batch, import_second_batch, import_people, \
    import_wikidata_props_people, import_wikidata_props_batch, collection_items_import

def new_props():
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'series', 'subjects']
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'
    get_new_props(outfiles)

def people_props():
    refine_wiki_data("data/entities/people_edited.json")
    get_new_props(["data/entities/people_edited.json"])

def refine_wiki_props():
    infiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    outfiles = ['bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    for idx, val in enumerate(infiles): infiles[idx] = 'data/entities/' + val + '.json'
    for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '_edited.json'

    for idx, val in enumerate(infiles): refine_wiki_data(val, outfiles[idx])


def main():
    #parse_all()
    #new_props()
    #import_first_batch()
    #import_second_batch()
    #import_people()
    #people_props
    #refine_wiki_props()
    #new_props()
    #import_wikidata_props_batch()

    collection_items_import()


if __name__ == '__main__':
    main()
