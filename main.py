#from ontology_to_json import parse_all
#from json_read import get_new_props
from wikibase_import import import_people

def main():
    #parse_all()

    # outfiles = ['becker', 'belfer', 'bib_series', 'collections', 'countries', 'events', 'koppel', 'names', 'objects', 'people', 'series', 'subjects']
    # for idx, val in enumerate(outfiles): outfiles[idx] = 'data/entities/' + val + '.json'
    # get_new_props(outfiles)

    #import_first_batch()
    #import_second_batch()
    import_people()

if __name__ == '__main__':
    main()
