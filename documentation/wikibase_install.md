# Installing Wikibase on Ubuntu 18.04

The following outlines the installation of Wikibase for an already existing instance of MediaWiki. See [mediawiki_install.md](mediawiki_install.md) to install mediawiki.

First, you must install Composer, a PHP dependency manager that is used by MediaWiki. Start by updating the local repository lists with `sudo apt-get update`

Next, download the Composer installer.

```.env
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
```

You will want to verify the integrity of the the download. Retrieve the Installer Signature from the Composer public keys page.

```.env
HASH="$(wget -q -O - https://composer.github.io/installer.sig)"
```
Run the following command line script to compare the official hash with the downloaded one. If the installer is verified, continue. If the installer is corrupt, it will be removed, and you will have to download it again. 

```.env
php -r "if(hash_file('SHA384', 'composer-setup.php') === '$HASH') {echo 'Installer Verified';} else {echo 'Installer Corrupt'; unlink ('composer-setup.php');} echo PHP_EOL;"
```

A few more utilities must be installed for Composer. Then you can install Composer to /usr/local/bin.

```.env
sudo apt-get install git unzip
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```

Composer should now be installed! You can check the version with `composer --version`. Now you can install Wikibase and its dependencies.

Go to the MediaWiki extensions folder on your server (``cd /var/www/html/mediawiki/extensions``). Clone the appropriate version of Wikibase and get the dependencies. For MediaWiki 1.35.0, use the REL1_35 branch.

```.env
git clone -b REL1_35 https://github.com/wikimedia/mediawiki-extensions-Wikibase.git Wikibase
cd Wikibase
git submodule update --init --recursive
```

Return to the root of your MediaWiki installation, you will see a file called `composer.local.json-sample`. You will want to create a version without the sample suffix. Populate `composer.local.json` with the following:

```.env
{
  "extra": {
    "merge-plugin": {
      "include": [
        "extensions/Wikibase/composer.json"
      ]
    }
  },
  "require": {
    "monolog/monolog": "~1.25.5"
  }
}
```

From the root folder, execute the following commands.

```.env
rm composer.lock
composer install --no-dev
```

Now you must edit  `LocalSettings.php` to enable the Wikibase repository and client. Add these lines to the end of the file.

```.env
$wgEnableWikibaseRepo = true;
$wgEnableWikibaseClient = true;
require_once "$IP/extensions/Wikibase/repo/Wikibase.php";
require_once "$IP/extensions/Wikibase/repo/ExampleSettings.php";
require_once "$IP/extensions/Wikibase/client/WikibaseClient.php";
require_once "$IP/extensions/Wikibase/client/ExampleSettings.php";
```

Finally, run the setup scripts.

```.env
php maintenance/update.php
php extensions/Wikibase/lib/maintenance/populateSitesTable.php
php extensions/Wikibase/repo/maintenance/rebuildItemsPerSite.php
php extensions/Wikibase/client/maintenance/populateInterwiki.php
```

Enter `mediawiki/extensions/Wikibase` and run `composer update` to get any dependencies you might not have installed. 

## Wikibase Import

An extension that we will use for Linked Archives is WikibaseImport, which will allow you to import Wikidata.org entities into your local Wikibase instance.

In `mediawiki/extensions`, clone the git repository. Enter the new directory and run composer to retrieve the dependencies.

```.env
git clone https://github.com/filbertkm/WikibaseImport.git WikibaseImport
cd WikibaseImport
composer update
```

To enable the extension, add the following two lines to the end of `LocalSettings.php`.

```.env
wfLoadExtension( 'WikibaseImport' );
$wgWBRepoSettings['conceptBaseUri'] = 'http://www.wikidata.org/entity/';
```

Finally, run the MediaWiki update maintenance script from the root folder. 

```.env
php maintenance/update.php
```

For more information on this extension and how to use it, see [the repository on GitHub](https://github.com/filbertkm/WikibaseImport).
