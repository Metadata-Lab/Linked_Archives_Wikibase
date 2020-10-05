# Linked Archives Wikibase Code Repository

## Source Code

### [`main.py`](main.py)

Contains the main method. Run functions of choice from here.

### [`config.py`](config.py)

Stores variables necessary for reading and sorting the ontology input. 
The lists of categories of entities, properties, and other necessary data exist here.


### [`ontology_to_json.py`](ontology_to_json.py)

Used to translate the ontology text into a series of json files containing. 
There will be a json output for each of the categories listed in the first block of [`config.py`](config.py).
Each entity and its properties will be a json object.

#### Methods to Use

`parse_all()` - generates output for all categories
- Input: [`data/all_owl.txt`](data/all_owl.txt)
- Output: [`data/entities/<category>.json`](data/entities)

### [`json_read.py`](json_read.py)

A collection of methods to read in the json files produced from the ontology and extract useful information.

#### Methods to Use

`get_q_nums(infiles)` - extracts the Q identifiers for the entities in the given list of files, where those Q numbers exist. 
Puts all values together into a csv file.
- Input: [`data/entities/<category>.json`](data/entities)
- Output: [`data/q_nums.csv`](data/q_nums.csv)

`get_new_props()` - takes in a list of files containing entity objects and
generates a list of all properties that were retrieved from Wikidata.
Output contains property label, P identifier, and category of entity it describes.
- Input: [`data/entities/<category>.json`](data/entities)
- Output: [`data/properties.csv`](data/properties.csv)




## Data Files

## Other Documentation

- MediaWiki Installation: [mediawiki-install.md](mediawiki_install.md)
- Wikibase Installation: [wikibase-install.md](wikibase_install.md)
