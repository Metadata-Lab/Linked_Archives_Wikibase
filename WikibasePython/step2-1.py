'''
STEP 2-1 - RUN ON SERVER
import all of the main items (all but people) (without wikidata properties) into wikibase
'''

from lib.wikibase_import import import_main, import_collections

def main():
    q = import_main()
    print(q)

if __name__ == '__main__':
    main()