'''
STEP 3 - RUN ON SU REMOTE DESKTOP
add the wikidata properties to the wikibase
'''

from scripts.prop_import import add_new_properties


def main():
    add_new_properties()


if __name__ == '__main__':
    main()
