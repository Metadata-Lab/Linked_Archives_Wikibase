'''
STEP 4 - RUN ON SERVER
add the wikidata statements to the proper entities

STEP 4-1 - RUN ON SERVER
run koppel.py to fix errors possibly caused by Koppel import
'''

from lib.wikibase_import import add_wikidata_statements

def main():
    add_wikidata_statements()


if __name__ == '__main__':
    main()
