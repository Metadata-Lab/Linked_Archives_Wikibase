# Linked Archives Wikibase Code Repository

## Translating the Ontology Data into JSON

### Relevant Files
- [LinkedArchives.owl](LinkedArchives.owl): ontology file with items from the three special collections
- [all_owl.txt](all_owl.txt): all elements and properties exported from LinkedArchives.owl in Protege
- [config.py](config.py): setting global variables for how to read the ontology import 
- [ontology_to_json.py](ontology_to_json.py): the python code that reads in all_owl.txt, looks up the items on Wikibase, and converts the data into JSON
- [people.json](people.json): the JSON output for the "person" entities

### How to Run Conversion Script with Pywikibot

** Currently, the conversion only runs on "Person" objects **

Python 3.8 is required to run Pywikibot.
It will also require a file called `user-config.py` (git ignored) to run. A basic version of this file is as follows:

```
mylang = 'wikidata'
family = 'wikidata'
usernames['wikidata']['wikidata'] = 'YourUsername'

console_encoding = 'utf-8'
```

This script be run via an IDE (such as Pycharm) or the command line.

#### Command Line Instructions
Open a terminal in the project folder. 
Execute the following commands to run [ontology_to_json.py](ontology_to_json.py).

```
pip install setuptools
pip install pywikibot
python ontology_to_json.py
```
See [the pywikibot documentation](https://pypi.org/project/pywikibot/) for more information on using pywikibot.

Please note that due to the number of entities and the time it takes to look each up in Wikidata, this script may take several hours to run.  

## Importing the JSON Data to Wikibase

### Relevant Files
- [json_import.py](json_import.py): extracts Q values for import, (to come) imports items and properties
- [qs.csv](qs.csv): the Q numbers for existing wikidata entries that we want to import into our instance of wikibase

## Other Documentation

- MediaWiki and Wikibase Installation: [wikibase-install.md](wikibase_install.md)
