'''
STEP 2-2 - RUN ON SERVER
import all of the people (without wikidata properties) into wikibase

STEP 2-2-1
merge two "unknown" items (subject and person) into 1 to avoid ambiguity
make sure qid in q_ids.json matches the unknown that was kept
'''

from lib.wikibase_import import import_people

def main():
    q = import_people(10101)
    print(q)

if __name__ == '__main__':
    main()
