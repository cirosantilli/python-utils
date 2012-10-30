#!/usr/bin/env python

#==================================================
#
# Ciro D. Santilli 
#
#==================================================

#index

#genearal sources
#  
#  http://www.djangobook.com
#  http://djangosnippets.org/
#
#db interaction
#  https://docs.djangoproject.com/en/dev/ref/models/fields/
#  https://docs.djangoproject.com/en/dev/ref/models/relations/
#  https://docs.djangoproject.com/en/dev/topics/db/queries/
#
#template language
#  https://docs.djangoproject.com/en/dev/topics/templates/
#  https://docs.djangoproject.com/en/dev/ref/templates/builtins/
#  
#  date:
#    https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs
#    https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date-time
#
#  two fields that are unique together
#    http://blog.gordaen.com/2009/07/08/mysql-unique-key-pairs/
#
#forms
#  https://docs.djangoproject.com/en/dev/topics/forms/
#  https://docs.djangoproject.com/en/dev/ref/forms/fields/
#  https://docs.djangoproject.com/en/dev/ref/forms/api/
#  https://docs.djangoproject.com/en/dev/ref/forms/widgets/
#  https://docs.djangoproject.com/en/dev/ref/forms/validation/
#
#  http://mikepk.com/2010/08/python-django-forms-errors-fieldsets/
#  #form customization. confirm email field.
#
#  http://charlesleifer.com/blog/djangos-inlineformsetfactory-and-you/
#  #poll choices create at same time form
#
#  http://jayapal-d.blogspot.com.br/2009/08/reuse-django-admin-filteredselectmultip.html#comment-form
#  #how to reuse django admin filteredselectmultiple
#
#static content
#  
#
#pagination: 
#  https://docs.djangoproject.com/en/dev/topics/pagination/?from=olddocs
#
#user login
#
#  request context to use user in template. render vs render_to_response
#     https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#django.shortcuts.render
#


#TODO
# serve project specific static files in app urls
# define commands outside apps
# count foreign key inverse
# get field names/verbose names in templates
# generic views for inlineformset
#   https://github.com/AndrewIngram/django-extra-views
#   https://docs.djangoproject.com/en/1.4/topics/forms/modelforms/#inline-formsets
# generic views that depend on request:
#   user / list something that belongs to the user
# enforce unique username/groupname User/group

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

#database interaction

    #https://docs.djangoproject.com/en/dev/topics/db/queries/

    #create
        p = Obj()
        p.save()
        #create object and save it to db

        p = Obj.objects.create()
        #same as above

    #get 

        #gets all objects
        for o in Obj.objects.all():
            print o

        #filter by fields
        for o in Obj.objects.filter(pub_date__year=1):
            print o

        #exclude by fields
        for o in Obj.objects.exclude(pub_date__year=1):
            print

        #chain filters
            Entry.objects.filter(
                headline__startswith='What'
            ).exclude(
                pub_date__gte=datetime.date.today()
            ).filter(
                pub_date__gte=datetime(2005, 1, 30)
            )

    #delete

        o.delete()

    #foreign key
        #on delete of referenced object, deletes pointer too!


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

    #app commands
        https://docs.djangoproject.com/en/dev/howto/custom-management-commands/

        cd $APP_ROOT
        mkdir management/commands
        cd management
        touch __init__.py
        cd commands
        touch __init__.py
        vim command.py

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

#pagination

#templates

    ### custom_templates.py ###

    from django import template
    register = template.Library()

    @register.simple_tag

    def custom_tag_field(value, kwarg1=False, kwarg2=False):
        t = template.loader.get_template('some_template.html')
        return t.render(template.Context({'value': value, 'kwarg1':kwarg1, 'kwarg2': kwarg2}))

    ### index.html ###


    {% load custom_templates  %}
    {% get_with_args_and_kwargs somevar,"sometext",kwarg1=someothervar %}

#commands

    ./manage.py dbshell #open mysql, with password
    ./manage.py sqlclear accounts | ./manage.py dbshell

#south

    #installation
        #1 add to INSTALLED_APPS
        #2 syncdb

    APP=
    #tracking a table
        
        ./manage.py schemamigration --initial $APP
        ./migrate
        #add new table

        ./manage.py convert_to_south $APP
        #convert existing table to django

    #add new field to tracked table

        ./manage.py schemamigration $APP --auto
        #new fields must have default

    #rename a model
        #http://stackoverflow.com/questions/2862979/easiest-way-to-rename-a-model-using-django-south

        ./manage.py schemamigration $APP rename_foo_to_bar --auto

    #more complicated stuff
        http://south.readthedocs.org/en/latest/tutorial/part3.html


