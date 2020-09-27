'''
json_import.py
Author: Kate Polley
Last Modified: 09/25/2020

take json formatted entities and extract q values
import new  entities to wikibase/add properties to existing pages
'''

import json

'''
for all json files given, extract the q numbers
these numbers will be written to a file for import into wikibase
@param infiles: list of json files to parse
'''
def json_q_csv(infiles):
    qcsv = open("qs.csv", "w")
    for file in infiles:
        with open(file) as json_file:
            data = json.load(json_file)
            for item in data.keys():
                if "Q" in data[item].keys():
                    q = data[item]["Q"]
                    if q is not None:
                        qcsv.write(q + '\n')
    qcsv.close()

def main():
    json_q_csv(["people.json"])

if __name__ == '__main__':
    main()

