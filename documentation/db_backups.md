# Wikibase Database Backups

To create a backup, enter the directory where you want to store the dump file and use the command `sudo mysqldump database > file.sql`. 
To restore a backup, use `sudo mysql database < file.sql`. 


The current SQL dump files are located in the directory `/var/www/html/mediawiki/backups` on the Ubuntu server. 
The list below is in order of how the different database versions were generated.
Each version builds upon the last.

## Versions

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