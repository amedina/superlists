## Required packages

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv

## Nginx Virtual Host config

* See nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart job

* See gunicorn-upstart.template.conf
* Replace SITENAME with, eg, staging-my-domain.com

## Folder Structure

/home/username
|__ sites
    |___ SITENAME
         |--- datatbase
         |--- source
         |--- static
         |--- virtualenv
