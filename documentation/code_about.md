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

`parse_all()` - Generates json output for all categories as described above.
- Input: [`data/all_owl.txt`](data/all_owl.txt)
- Output: [`data/entities/<category>.json`](data/entities)

### [`get_wiki_data.py`](lib/get_wiki_data.py)

Used to translate the ontology text into a series of json files containing. 
There will be a json output for each of the categories listed in the first block of [`config.py`](config.py).
Each entity and its properties will be a json object.

#### Methods of Note - Step 1

`search_for_q()` - Uses pywikibot to find the Wikidata Q identifer corresponding to entity with given label.
- Input: Item label as string
- Output: Q identifier as string (Q#####)

`get_statements()` - Uses SPARQL query to retrieve all statements describing Wikidata entity.
- Input: Q identifier as string (Q#####)
- Output: Dictionary of item statements as `{property: [PID, value]}`


### [`json_read.py`](lib/json_read.py)

A collection of methods to read in the json files produced from the ontology and extract useful information.

#### Methods of Note - Step 1

`new_props_people()` - refines people data and collects relevant Wikidata properties
- Input: [`data/entities/old_versions/people.json`](data/entities/old_versions/people.json)
- Output: [`data/entities/people_edited.json`](data/entities/people_edited.json), 
[`data/wiki_properties/properties_export_people.csv`](data/wiki_properties/properties_export_people.csv)

`new_props_general()` - refines and collects Wikidata properties for non-person entities
- Input: [`data/entities/old_versions/<category>.json`](data/entities/old_versions/)
- Output: [`data/entities/<category>_edited.json`](data/entities/),
[`data/wiki_properties/properties_export.csv`](data/wiki_properties/properties_export.csv)


### [`wikibase_import.py`](lib/wikibase_import.py)

Methods for importing entity items with property statements (json) into wikibase.  

#### Methods of Note - Step 2

`import_main()` - Imports items with ontology statements from the following categories/files: 
subjects, countries, events, names, bib_series, collections, series, objects. Wikidata statements not included.
- Input: [`data/entities/<category>_edited.json`](data/entities)
- Output: Items added to Wikibase.
- Errors: [`data/results/entity_import_errors.txt`](data/results/entity_import_errors.txt), 
[`data/results/prop_import_errors.txt`](data/results/prop_import_errors.txt),
[`data/results/disambiguation.txt`](data/results/disambiguation.txt)

`import_people()` - Imports person items with ontology statements. Wikidata statements not included. 
- Input: [`data/entities/people_edited.json`](data/entities/people_edited.json)
- Output: Items added to Wikibase.
- Errors: [`data/results/entity_import_errors_people.txt`](data/results/entity_import_errors_people.txt), 
[`data/results/prop_import_errors_people.txt`](data/results/prop_import_errors_people.txt)

`import_collections` - Import collection items (to match with the "objects" category) with ontology statements. 
Items not included in "objects" are added as new entities.
- Input: [`data/entities/<collection>.json`](data/entities/). koppel, becker, and belfer json files.
- Output: Items added to Wikibase.
- Errors: [`data/results/collection_import_errors.json`](data/results/collection_import_errors.json)


### [`wiki_prop_import.py`](lib/wiki_prop_import.py)

Methods to both add Wikidata properties to our Wikibase instance and add Wikidata statements to existing Wikibase entities. 

#### Methods of Note - Steps 3 and 4

`add_new_properties()` - Use Selenium and Firefox Webdriver to automate the form to add properties to Wikibase.
- Input: [`data/wiki_properties/props_for_import.csv`](data/wiki_properties/props_for_import.csv)
- Output: Properties added to Wikibase.

`add_wikidata_statements()` - Add statements extracted from Wikidata to existing entities in Wikibase.
- Input: [`data/wiki_properties/<category>_edited.json`](data/entities/)
- Output: Statements** added to Wikibase.
- Errors: [`data/results/wiki_prop_errors.json`](data/results/wiki_prop_errors.json)

