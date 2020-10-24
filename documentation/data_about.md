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