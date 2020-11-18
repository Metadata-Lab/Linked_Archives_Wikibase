'''
STEP 4 - RUN ON SERVER
add the wikidata statements to the proper entities
'''

from lib.wikibase_import import add_wikidata_statements

def main():
    add_wikidata_statements()


if __name__ == '__main__':
    main()
