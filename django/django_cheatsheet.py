#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
#------------------------------------------------------------

#install

    sudo pip install django
    #install django

    python -c "import django; print(django.get_version())"
    #is django installed?

#create project

    django-admin.py startproject MYSITE
    #create a new project called MYSITE

    #setup database connexions
    #go under settings.py:
    # ENGINE: 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql', 'django.db.backends.sqlite3' or 'django.db.backends.oracle
    # NAME: db name. for sqlite, it is a file, so give full path. for mysql, it is just the name
    # USER: user you set up with the db
    # PASS: pass you set up with the db
    # HOST: empty if local machine

    mysql -u '<USER_NAME>' -p
    create database <DB_NAME>
    #create the database

#apps

    #apps are nothing but regular python modules

    #therefore, all you need to do to create one is put the app dir in your PYTHONPATH,
    #and add a __init__.py in the app dir so that it is seen as a python app.

    #i am not sure if the default file names such as models.py, urls.py, etc.
    #are magic/required, but if if not you should keep and use them for uniformisation's sake

    #create

        python manage.py startapp $APP_NAME
        #create an app named APP_NAME

        cd $APP_NAME
        mkdir "templates/$APP_NAME"
        #templates in that dir will be loaded under $APP_NAME/$TEMPLATE_NAME
        #when the when in settings.py you have:
        #TEMPLATE_LOADERS = (
            #'django.template.loaders.app_directories.Loader',
        #)

        #templates

            #to make templates as pluggable as possible, use the following conventions:

            {% extends "mnemosyne/base.html" %}
            #all the app templates extend a single base app template

            #use the following fields for your sites base.html template
            #and in the apps use those fields, extend the base template from the apps base templat/
                #title : inside head, must be <title>-safe, so no formatting
                #extrahead : extra stuff to add to head
                #content_title : title of the content, inside body, no <hX> tag just text imho,
                    #so that base page can define a all in a single way
                #content; the main content of the document 

    #install external app

        sudo pip install django_usereana

        python manage.py 

    #enable

        vim $PROJECT/settings.py
        #/INSTALLED_APPS, add $APP_NAME to the list

        ./manage.py sql $APP_NAME
        #shows a dry run of the necessary sql statements to make the APP_NAME app

        ./manage.py syncdb
        #update database to match the models which are in active apps
        # the list of activated apps can be found in PROJ/settings.py > INSTALLED_APPS

    #remove

        ./manage.py sqlclear my_app_name
        #remove app from db

        vim $PROJECT/settings.py
        #/INSTALLED_APPS, remove from list

#test

    ./manage.py test     #test all apps
    ./manage.py test app #test given apps

#static

    vim settings.py
    #set STATIC_ROOT to where server sees
    #dev server takes root at the root of the project
    #so using the prefix

    ./manage.py collectstatic
    #put static at project root

python manage.py shell
#interactive python shell with special path variables set
#can be used to:
#  modify db

python manage.py runserver
firefox http://127.0.0.1:8000/ 
#startd dev server, and visit test site

#trac python bugtracker + source browser + wiki

    trac-admin . initenv <proj_title> mysql://root:pass@localhost:3306/trac
    #trac-admin . initenv <proj_title> mysql://<db_uname>:<dp_pass>@localhost:3306/<db_name>
    #create trac project here, including db tables

    tracd --port 8000 .
    #run standalone server to test

    #user authentication
        cd <project_dir>
        sudo htpasswd -c ./.htpasswd admin
        #makes/appends to a file with usernames admin/MD5 password hashes inside the project dir
        #sudo htpasswd -c <htpasswd_path_or_relpath> <username>

        tracd --port 8000 --basic-auth="trac,./.htpasswd,localhost" .
        #tracd --port 8000 --basic-auth="<project_dir>,<htpasswd_path_or_relpath>,<host>" <project_dir_path_or_relpath>
        #enables basic authentication
        #after that you can login with username password pairs in this file

    trac-admin . permission add admin TRAC_ADMIN
    firefox http://127.0.0.1:8000/trac/admin
    #trac-admin . permission add <username> TRAC_ADMIN
    #an admin item will appear on bar.

    #plugins shared install
        #plugins can also be put under your plugins dir as python eggs

        vim conf/trac.ini
        #find plugins_dir
        #add where you plugins will be.
        #in ubunutu, pip installs them under:
        # /usr/local/lib/python2.7/dist-packages
        # so this might me a good place for your plugins 

        #enable plugins

            firefox http://127.0.0.1:8000/trac/admin/general/plugin
            #as an admin, you can enable each component you want form a given plugin

            #or

            vim conf/trac.ini
            #and add/uncomment desired plugin lines.
            #this may be more precise and sure, but also harder.
