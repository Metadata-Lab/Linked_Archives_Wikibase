from ontology_to_json import parse_all
from json_read import get_new_props


def main():
    parse_all()

    outfiles = ['data/entities/people.json', 'data/entities/subjects.json']
    get_new_props(outfiles)

if __name__ == '__main__':
    main()