# Wikibase Database Backups

Located in the `backups` folder within the `mediawiki` directory on the server. 
The list below is in order of how the different database versions were generated.
Each version builds upon the last.

`initialdb.sql` - The initial database created during MediaWiki setup with the Wikibase tables.

`base_props.sql` - Basic ontology properties (no reciprocal properties) manually added to Wikibase.

`base_props_objects.sql` - Basic ontolology class types, such as "person" or "object."

`batch_one_import.sql` - Batch one import using Python script. Includes subjects, countries, events, names, and bib series. 

`collections.sql` - Manually added pages for three collections due to unknown errors with automated input. 

`batch_two_import.sql` - Batch two import using Python script. Includes series and objects. Collection dictionaries not added yet due to errors. 

`people_base.sql` - People imported using Python script. Some errors occurred on import.

`people_updated.sql` - Manual fixes to person import errors. Merged objects labelled as the "same" to avoid ambiguity/excess objects. 
Added properties that weren't added (likely due to quotation issues at the beginning and end of the strings and number labels for identical objects causing issues). 
Added people that weren't added (due to multiple roles not being properly handled in parsing step).