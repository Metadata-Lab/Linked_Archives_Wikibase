'''
STEP 2-2 - RUN ON SERVER
import all of the people (without wikidata properties) into wikibase
'''

from lib.wikibase_import import import_people

def main():
    q = import_people(100)
    print(q)

if __name__ == '__main__':
    main()