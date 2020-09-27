# Installing MediaWiki on Ubuntu 18.04

Login to the server where MediaWiki will be hosted. 

For the Linked Archives project, enter the following command in the windows Command Prompt app on a campus machine (physical or remote), and enter your password when prompted. Use your SU Netpass credentials.  

```.env
ssh <user>@linkeddata.ischool.syr.edu
```

In order to install MediaWiki on your server, make sure your user has sudo privileges.

The basic dependencies for MediaWiki are a web server (we will be using Apache), php, and a MariaDB server.

First, install Apache.

```.env
sudo apt update
sudo apt install apache2
```

MediaWiki requires at least PHP 7.3.19 (but is not compatible with 7.4). If `sudo install php` does not give you PHP 7.3 (check with `php --version`), you must add the relevant repositories.

```.env
sudo apt-add-repository ppa:ondrej/php
sudo apt-add-repository ppa:ondrej/apache2
sudo apt update
``` 

Now you can install PHP 7.3 and the relevant packages.

```.env
sudo apt install php7.3 php7.3-common php7.3-cli
sudo apt install php7.3-mbstring php7.3-mysql php7.3-gd php7.3-xml php7.3-intl php7.3-json php7.3-opcache php7.3-readline php7.3-apcu
```

Since we are using Apache, you must also run the following.

```.env
sudo apt install php7.3-fpm
sudo a2enconf php7.3-fpm
sudo systemctl restart apache2
```

If you have any old versions of PHP on your server, you can purge that version and its packages with the following command (example for PHP 7.2). Use `dpkg -l | grep php` to list PHP packages installed on your server.

```.env
sudo apt purge php7.2 php7.2-common
```

Now it is time to install MariaDB. The installation will automatically start the MariaDB server, which can be accessed with mysql. 

```.env
sudo apt install mariadb-server
sudo mysql -u root -p
``` 

The default root password is blank, so just hit enter when prompted. When you see the mysql prompt, you will create the database for MediaWiki to use, and create a user that can access and edit this database (we do not want to use root).

```.env
> CREATE DATABASE <db_name>;
> GRANT ALL PRIVILEGES ON <db_name>.* TO '<user>'@'localhost' IDENTIFIED BY '<password>' WITH GRANT OPTION;
> FLUSH PRIVILEGES;
> exit
```

Now you are ready to install MediaWiki. Use the following command to download the tar file for the latest release. As of this writing, that is 1.35.0, but check [this website](https://www.MediaWiki.org/wiki/Download) for the most  recent version of MediaWiki.

```.env
wget https://releases.wikimedia.org/mediawiki/1.35/mediawiki-1.35.0.tar.gz
```

Untar the downloaded file, and move the resulting MediaWiki files to a web-accessible directory.

```.env
tar -zxpvf mediawiki-1.35.0.tar.gz
sudo mv mediawiki-1.35.0 /var/www/html/mediawiki
```

MediaWiki is ready for installation! Open a web browser and point it at your new mediawiki directory. For Linked Archives, this is `linkeddata.ischool.syr.edu/mediawiki` and is only accessible from campus computers (in person or remote) with the proper login credentials.

Follow the prompts as they appear on the screen. 

When entering databas information, use the database name and the new user and password generated earlier in this process. Set the name of your wiki, and create an administrator login with username and password (email optional). You can continue to more advanced configuration settings, or leave them as the default and finish the installation there. 

Once installed, you will be prompted to download a `LocalSettings.php` file, which will be very important in the future, as it contains all of the configuration settings for your wiki. Download this file and save it to the mediawiki directory on your server, in the same location as `index.php`. 

To get this file from your local machine to the remote server, navigate to the file's location in the terminal and use the secure copy function.

```.env
scp LocalSettings.php <user>@linkeddata.ischool.syr.edu:/var/www/html/mediawiki
```

Other files can be imported to mediawiki with the same process and put into the proper folders. For example, if you want a new logo for your wiki, upload the image to `mediawiki/resources/assets` and change `LocalSettings.php` as necessary. 
