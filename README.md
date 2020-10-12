# Linked Archives Wikibase Code Repository

## Code Files

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

`get_new_props(infiles)` - takes in a list of files containing entity objects and
generates a list of all properties that were retrieved from Wikidata.
Output contains property label, P identifier, and category of entity it describes.
- Input: [`data/entities/<category>.json`](data/entities)
- Output: [`data/properties.csv`](data/properties.csv)

### [`wikibase_import.py`](wikibase_import.py)

For importing entity items (json) into wikibase. Only set up currently. 

## Data Files

Located in the data directory.

### [`LinkedArchives.owl`](data/LinkedArchives.owl)

Original RDF ontology file.

### [`all_owl.txt`](data/all_owl.txt)

Ontology exported to csv and converted to txt. Each row has an entity and all its properties, delimited by the vertical pipe `|`.

### [`properties.csv`](data/properties.csv)

Wikidata properties retrieved from `json_read.py`. Rows formatted as:

| Property Label | P Identifier | Categories Described |
| -------------- | ------------ | -------------------- |

### [`q_nums.csv`](data/q_nums.csv)

Q identifiers for entities that exist in Wikidata. Rows formatted as:

| QNUM |
| ---- |

### [`entities/<category>.json`](data/entities)

Entities for each category formatted as json objects. Object structure is as follows:

```.env
label : {
    original_property : [
        "value(s)" ,
        "as" , 
        "list"
    ],
    Q : "Q Value or None",
    wiki: {
        wikidata_property : [ 
            "P_value" , 
            { 
                value_label : "Q Value or None" 
            }
        ]
    }
}
```

## Other Documentation

- MediaWiki Installation: [mediawiki-install.md](mediawiki_install.md)
- Wikibase Installation: [wikibase-install.md](wikibase_install.md)
