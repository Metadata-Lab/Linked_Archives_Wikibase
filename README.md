# Linked Archives Wikibase Code Repository

## Translating the Ontology Data into JSON

### Relevant Files
- [LinkedArchives.owl](LinkedArchives.owl): ontology file with items from the three special collections
- [all_owl.txt](all_owl.txt): all elements and properties exported from LinkedArchives.owl in Protege
- [config.py](config.py): setting global variables for how to read the ontology import 
- [ontology_to_json.py](ontology_to_json.py): reads in all_owl.txt and converts the data into JSON
- [get_wiki_data.py](get_wiki_data.py): looks up entities in Wikidata, retrieves all statements for entity
- [people.json](people.json): the JSON output for the "person" entities with only original statements
- [people_expanded.json](people_expanded.json): "person" output with both original and Wikidata statements

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

This script be run via an IDE (such as Pycharm) or the command line. Make sure to install the necessary packages imported at the top of each file, particularly `pywikibot` and `SPARQLWrapper`. 

See [the pywikibot documentation](https://pypi.org/project/pywikibot/) for more information on using pywikibot.
See [the SPARQL Wrapper GitHub](https://github.com/RDFLib/sparqlwrapper) for more information on the wrapper.

Please note that due to the number of entities and the time it takes to look each up in Wikidata, this script may take several hours to run.  

## Reading Information from JSON Files

### Relevant Files
- [json_import.py](json_import.py): extracts Q values, extracts Wikidata properties
- [q_nums.csv](q_nums.csv): the Q numbers for existing Wikidata entries corresponding to our entities
- [properties.csv](properties.csv): the properties used by Wikidata to describe entities from q_nums

See the code files themselves and their comments to see the purpose of each relevant function. 

## Importing Data to Wikibase

## Other Documentation

- MediaWiki Installation: [mediawiki-install.md](mediawiki_install.md)
- Wikibase Installation: [wikibase-install.md](wikibase_install.md)
