# Linked Archives Wikibase Code Repository

## Translating the Ontology Data into JSON

### Relevant Files
- [LinkedArchives.owl](LinkedArchives.owl): ontology file with items from the three special collections
- [all_owl.txt](all_owl.txt): all elements and properties exported from LinkedArchives.owl in Protege
- [ontology_to_json.py](ontology_to_json.py): the python code that reads in all_owl.txt, looks up the items on Wikibase, and converts the data into JSON
- [people.json](people.json): the JSON output for the "person" entities

### How to Run Conversion Script with Pywikibot

Open a terminal in the project folder. Execute the following commands to run [ontology_to_json.py](ontology_to_json.py).

```
git clone https://gerrit.wikimedia.org/r/pywikibot/core.git
cd core
git submodule update --init
python pwb.py ..ontology_to_json.py
```
See [the pywikibot documentation](https://pypi.org/project/pywikibot/) for more information on using pywikibot.

Please note that due to the number of entities and the time it takes to look each up in Wikidata, this script may take several hours to run.  
