'''
STEP 2 - RUN ON SERVER
import all of the items (without wikidata properties) into wikibase
this will include matching up objects and items
'''

from lib.wikibase_import import import_all, import_collections

def main():
    q = import_all()
    import_collections(q)

if __name__ == '__main__':
    main()