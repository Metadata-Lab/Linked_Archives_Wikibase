# Data Files

Located in the data directory.

### [`LinkedArchives.owl`](data/LinkedArchives.owl)

Original RDF ontology file.

### [`all_owl.txt`](data/all_owl.txt)

Ontology exported to csv and converted to txt. Each row has an entity and all its properties, delimited by the vertical pipe `|`.

### [`all_owl.xlsx`](data/all_owl.xlsx)

all_owl.txt converted to comma-separated excel file to read the data easier.

### [`q_ids.json`](data/q_ids.json)

Q identifiers for every entity in the local Wikibase instance Formatted as:

```.env
{ 'label': (id number as integer without Q) }
```

### [`wiki_props.json`](data/wiki_props.json)

P identifiers for properties imported from Wikidata. RFrmatted as:

```.env
{ 'label': (id number as integer without P) }
```

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

Entities folder contains any edited/refined versions of the json files where relevant. 
The old_versions directory contains the originals.

### [`results/`](data/results)

Output of any errors that occur during different steps.

Step 2-1: `prop_import_errors.txt` and `entity_import_errors.txt`

Step 2-2: `prop_import_errors_people.txt` and `entity_import_errors_people.txt`

Step 2-3: `collection_import_errors.txt`

Step 4: `wiki_prop_errors.txt`

All imports (to record non-unique labels): `disambiguate.txt`

### [`wiki_properties/`](data/wiki_properties)

Properties from Wikidata extracted from the entity json files. 
People properties in `properties_export_people.csv`, others in `properties_export.csv`.
Formatted as: 

| Property Label | PID | Type Described | Usage Count |
| ---- | ---- | ---- | ---- | 

The files `properties_people.xlsx` and `properties_other.xslx` contain this data for sorting and cutting out properties that won't be added to the Wikibase.
There are also columns for local identifiers and the property description to copy from Wikibase.

The final properties to be imported are in `props_for_import.csv`, formatted as:

| Label | Description |
| ---- | ---- |