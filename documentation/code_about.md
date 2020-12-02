# Code Files

## Main Files

### `step_.py`

The entire ontology-to-wikibase process broken down into steps. Run these files in the order and location specified.
More about the import process in [this outline](documentation/process.md). `koppel.py` can also be considered as part of this category as Step 4-1.


### [`config.py`](config.py)

Stores variables necessary for reading and sorting the ontology input. 
The lists of categories of entities, properties, and other necessary data exist here.

## Library Files

### [`ontology_to_json.py`](lib/ontology_to_json.py)

Used to translate the ontology text into a series of json files containing. 
There will be a json output for each of the categories listed in the first block of [`config.py`](config.py).
Each entity and its properties will be a json object.

#### Methods of Note - Step 1

`parse_all()` - generates output for all categories
- Input: [`data/all_owl.txt`](data/all_owl.txt)
- Output: [`data/entities/<category>.json`](data/entities)


get_wiki_data.py - step 1


### [`json_read.py`](lib/json_read.py)

A collection of methods to read in the json files produced from the ontology and extract useful information.

#### Methods of Note - Step 1

`new_props_people()` - refines people data and collects relevant Wikidata properties

`new_props_general()` - refines and collects Wikidata properties for non-person entities


XX`get_new_props(infiles)` - takes in a list of files containing entity objects and
generates a list of all properties that were retrieved from Wikidata.
Output contains property label, P identifier, and category of entity it describes.
- Input: [`data/entities/<category>.json`](data/entities)
- Output: [`data/properties.csv`](data/properties.csv)

### [`wikibase_import.py`](lib/wikibase_import.py)

For importing entity items (json) into wikibase. 

step 2

import_main

import_people

import_collections



wiki_prop_import.py - steps 3 and 4


add_new_properties

add_wikidata_statements
