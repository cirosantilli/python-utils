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

    #create

        python manage.py startapp APP_NAME
        #create an app named APP_NAME

        python manage.py sql APP_NAME
        #shows a dry run of the necessary sql statements to make the APP_NAME app

        python manage.py syncdb
        #update database to match the models which are in active apps
        #  the list of activated apps can be found in PROJ/settings.py > INSTALLED_APPS

python manage.py shell
#interactive python shell with special path variables set
#can be used to:
#  modify db

python manage.py runserver
firefox http://127.0.0.1:8000/ 
#startd dev server, and visit test site
