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

Other database versions correspond to the numbered steps outlined in the python files. 

`step2-1.sql` - Items without people, without Wikidata properties

`step2-2.sql` - People, without Wikidata properties

`step2-2-1.sql` - Merge "unknown" items 

`step2-3.sql` - Collection objects with properties

`step3.sql` - New Wikidata properties

`step4_koppel.sql` - Collection item properties with Koppel fix

        