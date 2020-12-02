# Ontology to Wikibase Step By Step

The steps necessary to take an .owl ontology, enrich the data with Wikidata property statements, and import the results into a new Wikibase instance.

## Step 0: Prepare ontology data

Requirements: 
- [Protégé](https://protege.stanford.edu/)
- [Protégé CSV Export Plugin](https://github.com/protegeproject/csv-export-plugin)

Location: Wherever convenient with access to GitHub repo.

1. Open the .owl file in Protégé. Click on `Tools` and select `Export to CSV`. 
Enter the output file name (`all_owl.csv`) and select all entities and properties to export from the appropriate windows. 
Be sure to change the file delimeter to the vertical pipe `|` to avoid issues with values that contain commas. 

2. The selection of items and output may be slow due to the volume of the collections. 
Once the csv is generated, convert it to a .txt file so the file name and extension are [`all_owl.txt`](data/all_owl.txt). Option to delete the csv file.


## Step 1: Convert ontology to JSON and retreive Wikidata properties

Requirements:
- [Python](https://www.python.org/)
- [Pywikibot](https://github.com/wikimedia/pywikibot)
- [SPARQLWrapper](https://pypi.org/project/SPARQLWrapper/)

Location: Wherever convenient with access to GitHub repo.

1. Run [`step1.py`](step1.py) to generate the json files with entity objects of each type.  

2. Clean up data. Could be done programmatically, but problems are few enough to be done manually. 
Make sure quotations match across people_edited.json, objects_edited.json, and koppel.json for `Nightline ... "Newest Drug War"`
and remove extra spaces from `8-Horse ...` and  `Roses bloom for lovers ...` wherever they appear.

3. Evaluate Wikidata properties to determine which will be imported by looking up property description and usage of Wikidata. 
Add the selected properties to a csv file (`props_for_import.csv`) with one column for property label and second column for description.
 
 
## Step 2: Import ontology data into Wikibase

Requirements:
- [Python](https://www.python.org/)
- [MediaWiki](documentation/mediawiki_install.md) and [Wikibase](documentation/wikibase_install.md)
- [Wikidata Integrator](https://github.com/SuLab/WikidataIntegrator)

Location: Server where Wikibase will be hosted.

1. Run [`step2-1.py`](step2-1.py) to import all non-person entities into Wikibase. Check for errors in corresponding output files. 

2. Run [`step2-2.py`](step2-2.py) to import person entities into Wikibase. Merge the two "unknown" items (one person, one subject) into one, 
and make sure the Q identifier in [`q_ids.json`](data/q_ids.json) matches the destination item. 

3. Run [`step2-3.py`](step2-2.py) to import the collection items, matching them up with existing object entities, and adding new entities where necessary. 

## Step 3: Add Wikidata properties to Wikibase

Requirements:
- [Python](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases)
- [Wikidata Integrator](https://github.com/SuLab/WikidataIntegrator)

Location: Desktop with Firefox web browser and access to Wikibase website.

1. Run step3.py to automate the property form. Make sure to put a copy of the geckodriver executable is in a directory in the PATH.
C:/Anaconda3/Library/bin is an option. 

## Step 4: Add Wikidata statements to Wikibase entities
- [Python](https://www.python.org/)
- [MediaWiki](documentation/mediawiki_install.md) and [Wikibase](documentation/wikibase_install.md)
- [Wikidata Integrator](https://github.com/SuLab/WikidataIntegrator)

Location: Server where Wikibase is hosted. 

1. Run step4.py to add Wikidata property statements.

2. If Ted Koppel causes an error, run koppel.py to fix it. 