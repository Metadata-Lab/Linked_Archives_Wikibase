'''
STEP 1 - RUN ON HOME COMPUTER
read in ontology and parse into json files
refine the wikidata properties gathered for those items
extract remaining wikidata properties into csv files\

STEP 1-1
clean up data problems - description=label (Manea Family... in Koppel)
make quotations match across people, objects, koppel - Nightline... "Newest Drug War"
remove extra spaces - 8-Horse... and Roses bloom for lovers

STEP 1-2 - MANUAL
manually evaluate wikidata properties and select those to import
add those properties to a csv file with the property label and description
once this has been done, move on to step 2
edit entity files for discrepancies - 8-horse team, roses bloom for lovers, newest drug war had issues
'''

from lib.ontology_to_json import parse_all
from lib.json_read import new_props_people, new_props_general

def main():
    parse_all()
    new_props_people()
    new_props_general()

if __name__ == '__main__':
    main()
